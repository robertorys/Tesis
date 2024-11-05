#==============================================================================
#title          : Mib.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.3.2
#python_version : 3.10.12
#==============================================================================
from itertools import product
import multiprocessing as mp
import copy
import math
from mib_v2_3_2.var import Var
from mib_v2_3_2.distrib import Distrib
from mib_v2_3_2.specification import Specification

class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            description (Specification): Descripción de un modelo.
    """
    
    def __init__(self, description: Specification) -> None:
        self.ds = description
    
    def probability(self, knwon:set, hidden_vars:set) -> float:
        """ Método para hacer el calculo de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        descompK = set()
        
        for d in self.ds.descomp:
            if d.check(knwon):
                descompK.add(d)
        
        sum = 0
        p = 1
        if len(descompK) > 0:
            for d in descompK:
                p *= d.P()
            
        descomp = set(self.ds.descomp) - descompK
        
        for key in product(*self.ds.getValues(hidden_vars)):
            # Establecer los valores de los eventos.
            i = 0
            for v in hidden_vars:
                v.event = key[i]
                i += 1
        
            # Calcular la probabilidad con los valores de k.
            p_i = 1
            for d in descomp:
                p_i *= d.P()
            
            sum += p_i
    
        self.ds.resetVars()
        return p * sum
 
    def marginal(self, vars:tuple, values:tuple) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            vars (tuple): Tupla con las varibales para la marginal.
            values (tuple): Tupla con los valores de las varibales para la marginal.

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        i = 0
        for var in vars:
            var.event = values[i]
            i += 1
        knwon = set(vars)
        hidden = self.ds.vars - knwon
        return self.probability(knwon, hidden)
    
    def joint_marginal(self, vars1:tuple, values1:tuple, vars2:tuple, values2:tuple) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1 (tuple): Tupla con las varibales del primer conjunto.
            values1 (tuple): Tupla con los valores del primer conjunto.
            vars1 (tuple): Tupla con las varibales del segundo conjunto.
            values1 (tuple): Tupla con los valores del segundo conjunto.

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        i = 0
        for var in vars1:
            var.event = values1[i]
            i += 1
            
        i = 0
        for var in vars2:
            var.event = values2[i]
            i += 1
            
        knwon = set(vars1).union(vars2)
        hidden = self.ds.vars - knwon
        return self.probability(knwon, hidden)
    
    def cond(self, vars:tuple, values:tuple, indep:tuple, indep_values:tuple) -> float:
        p_var_indep = self.joint_marginal(vars, values, indep, indep_values)
        p_indep = self.marginal(indep, indep_values)
        return p_var_indep / p_indep
    
    def distrib_inference(self, vars:set, indep:set = None) -> Distrib:
        """ Método para hacer la consulta de una distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.
            indep (set (optional)): Conjunto de variables para la condicional.
        Returns:
            Distrib: Dsitribución marginal calculada.
        """
        table = {}
        vars_column = tuple(vars)
        vars_values = [v.values for v in vars]
        
        if not indep:
            for event in product(*vars_values):
                table[event] = self.marginal(vars_column, event)
            return Distrib(table, vars_column)  
        else:
            indep_column = tuple(indep)
            indep_values = [v.values for v in indep]
            for ei in product(*indep_values):
                table[ei] = {}
                num = self.marginal(indep_column, ei)
                for ev in product(*vars_values):
                    table[ei][ev] = self.joint_marginal(vars_column, ev, indep_column, ei) / num
                    
            return Distrib(table, vars_column, indep_column)
            
    def marginal_inference(self, vars:tuple) -> tuple:
        """ Método para inferir el valor más probable de una distribución marginal o conjunta.

        Args:
            vars (tuple): Tupla de las variables de la distribución.

        Returns:
            tuple ((tuple, tuple, float)): El primer valor es la tupla de nombres, la segunda tupla representa sus valores
            y el último elemento es la probabilidad.
        """
        vars_column = tuple([v.name for v in vars])
        values = [v.values for v in vars]
        
        p = 0
        value = None
        for event in product(*values):
            p_event = self.marginal(vars, event)

            if p_event > p:
                p = p_event
                value = event
        
        return vars_column, value, p
    
    def hyps_inference(self, vars:tuple, indep:tuple, indep_values:tuple) -> tuple:
        """ Método para inferir el valor más probable de una hipótesis de una distribución condicional
        dado los valores de las observaciones.

        Args:
            vars (tuple): Tupla de las variables de la distribución condicional.
            indep (tuple): Tupla de las variables independientes de la distribución condicional.
            indep_values (tuple): Tupla con los valores de las variables de indep de la distribución.
        Returns:
            tuple ((tuple, tuple, float)): El primer elemento es la tupla de nombres de vars, el segundo elemento es la tupla que representa sus valores, 
            y el último elemento es la probabilidad.
        """
        vars_column = tuple([v.name for v in vars])
        
        vars_values = [v.values for v in vars]
        
        p = 0
        value_vars = None
        for hyp in product(*vars_values):
            
            p_hyp = self.joint_marginal(vars, hyp, indep, indep_values)
            
            if p > 0:
                if p_hyp > p:
                    p = p_hyp
                    value_vars = hyp
            else: 
                p = p_hyp
                value_vars = hyp
                
        den = self.marginal(indep, indep_values)
        if den == 0:
            return vars_column, value_vars, p
                               
        return vars_column, value_vars, p / den
    
    def obs_inference(self, vars:tuple, vars_values:tuple, indep:tuple) -> tuple:
        """ Método para inferir el valor más probable de una obersvación de una distribución condicional
        dado los valores de las hipótesis.

        Args:
            vars (tuple): Tupla de las variables de la distribución condicional.
            vars_values (tuple): Tupla con los valores de las variables de la distribución.
            indep (tuple): Tupla de las variables independientes de la distribución condicional.
        Returns:
            tuple ((tuple, tuple, float)): El primer elemento es la tupla de nombres de indep, el segundo elemento es la tupla que representa sus valores, 
            y el último elemento es la probabilidad.
        """
        
        indep_column = tuple([v.name for v in indep])
        
        indep_values = [v.values for v in indep]
        
        p = 0
        indep_value = None
        for obs in product(*indep_values):
            p_obs = self.joint_marginal(vars, vars_values, indep, obs)

            if p > 0:
                if p_obs / p > 1:
                    p = p_obs
                    indep_value = obs
            else:
                p = p_obs
                indep_value = obs
                
        return indep_column, indep_value, p / self.marginal(indep, indep_value)

class MibAp(Mib):
    """ Clase para el motor de inferencia bayesiana usando aproximación.

        Atributos:
            ds (Specification): Modelo del problema con su distribución conjunta y su descomposción.
    """
    def __init__(self, ds: Specification, N:int) -> None:
        super().__init__(ds)
        self.N = N
    
    def sample_marginal(self, vars:tuple, values:tuple) -> int:
        iteration = 0
        count_p = 0
        vars_set = set(vars)
        
        while iteration < self.N:
            vs = vars_set.copy()
            i = 0
            
            while len(vs) > 0 and i < len(self.ds.descomp):
                self.ds.descomp[i].setSample()
                
                vs = vs - self.ds.descomp[i].getVars()
                i += 1
            
            indv = []
            for v in vars:
                indv.append(v.event) 
                    
            if tuple(indv) == values:
                count_p += 1
            
            self.ds.resetVars()
            iteration += 1
            
        return count_p
    
    def margianl(self, vars, values) -> float:
        return self.sample_marginal(vars, values) / self.N
    
    def sample_cond(self, vars:tuple, values:tuple, indep_vars:tuple, indep_values:tuple) -> tuple:
        iteration = 0
        count = 0
        count_N = 0
        vars_set = set(vars).union(set(indep_vars))
        
        while iteration < self.N:
            vs = vars_set.copy()
            i = 0
            
            while len(vs) > 0 and i < len(self.ds.descomp):
                self.ds.descomp[i].setSample()
                
                vs = vs - self.ds.descomp[i].getVars()
                i += 1
                
            indv_indep = []
            for v in indep_vars:
                indv_indep.append(v.event)
                
            if tuple(indv_indep) == indep_values:
                count_N += 1
                
                indv = []
                
                for v in vars:
                    indv.append(v.event)
                        
                if tuple(indv) == values:
                    count += 1
            
            self.ds.resetVars()
            iteration += 1
        
        return count, count_N

    def cond(self, vars, values, indep, indep_values):
        i,n = self.sample_cond(vars, values, indep, indep_values)
        if n == 0 or i == 0 :
            return 1/self.N
        return i / n

    def joint_marginal(self, vars1, values1, vars2, values2):
        vars = tuple(list(vars1) + list(vars2))
        values = tuple(list(values1) + list(values2))
            
        return self.marginal(vars, values)
    
    def distrib_inference(self, vars:set, indep:set = None) -> Distrib:
        """ Método para hacer la consulta de una distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.
            indep (set (optional)): Conjunto de variables para la condicional.
        Returns:
            Distrib: Dsitribución marginal calculada.
        """
        table = {}
        vars_column = tuple(vars)
        vars_values = [v.values for v in vars]
        
        if not indep:
            for event in product(*vars_values):
                table[event] = self.marginal(vars_column, event)
            return Distrib(table, vars_column)  
        else:
            indep_column = tuple(indep)
            indep_values = [v.values for v in indep]
            for ei in product(*indep_values):
                table[ei] = {}
                for ev in product(*vars_values):
                    table[ei][ev] = self.cond(vars_column, ev, indep_column, ei)
                    
            return Distrib(table, vars_column, indep_column)

class MibMpap(MibAp):
    def __init__(self, ds, process_n, N):
        self.process_n = process_n
        super().__init__(ds, N)
        
    def sample_margianl_p(self, ds:Specification, vars:tuple, values:tuple, count_q:mp.Queue, N:int) -> None:
        mib = MibAp(ds,N)
        
        count = mib.sample_marginal(vars, values)
        
        count_q.put(count)
    
    def sample_cond_p(self, ds:Specification, vars, values, i_vars, i_values, count_q:mp.Queue, countN_q:mp.Queue,N) -> None:
        mib = MibAp(ds, N)
        
        count, countN = mib.sample_cond(vars, values, i_vars, i_values)
        
        count_q.put(count)
        countN_q.put(countN)
    
    def margianl(self, vars:tuple, values:tuple) -> float:
        N = math.ceil(self.N / self.process_n)

        processes = []
        count_q = mp.Queue()
        for i in range(self.process_n):
            vars_copy = set([Var(v.name, v.values) for v in self.ds.vars])
            
            name2var = {}
            for v in vars_copy:
                name2var[v.name] = v
            
            vars_mc = tuple([name2var[v.name] for v in vars])    
            descomp_copy = []
           
            for d in self.ds.descomp:
                d_vars = tuple([name2var[v.name] for v in d.vars]) 
                if d.parents:
                    d_parents = tuple([name2var[v.name] for v in d.parents])   
                    descomp_copy.append(Distrib(d.table, d_vars, d_parents))
                else:
                    descomp_copy.append(Distrib(d.table, d_vars))
            ds_copy = Specification(vars_copy, tuple(descomp_copy))   
               
            process = mp.Process(
                target=self.sample_margianl_p,
                args=(
                    ds_copy,
                    vars_mc, 
                    values, 
                    count_q,
                    N
                )
            )
            processes.append(process)
        
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        
        count = 0
        while not count_q.empty():
            count+=count_q.get()
        if count == 0:
            return 1 / self.N
        return count / (self.process_n * N)
    
    def cond(self, vars:tuple, values:tuple, indep_vars, indep_values) -> float:
        N = math.ceil(self.N / self.process_n)

        processes = []
        count_q = mp.Queue()
        countN_q = mp.Queue()
        
        for i in range(self.process_n):
            vars_copy = set([Var(v.name, v.values) for v in self.ds.vars])
            
            name2var = {}
            for v in vars_copy:
                name2var[v.name] = v
            
            vars_mc = tuple([name2var[v.name] for v in vars])    
            vars_ic = tuple([name2var[v.name] for v in indep_vars])  
            descomp_copy = []
           
            for d in self.ds.descomp:
                d_vars = tuple([name2var[v.name] for v in d.vars]) 
                if d.parents: 
                    d_parents = tuple([name2var[v.name] for v in d.parents])    
                    descomp_copy.append(Distrib(d.table, d_vars, d_parents))
                else:
                    descomp_copy.append(Distrib(d.table, d_vars))
            ds_copy = Specification(vars_copy, tuple(descomp_copy))   
               
            process = mp.Process(
                target=self.sample_cond_p,
                args=(
                    ds_copy,
                    vars_mc, 
                    values,
                    vars_ic,
                    indep_values,
                    count_q,
                    countN_q,
                    N
                )
            )
            processes.append(process)
        
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        
        countN = 0
        while not countN_q.empty():
            countN+=countN_q.get()
        if countN == 0:
            return 1/self.N
        
        count = 0
        while not count_q.empty():
            count+=count_q.get()
        if count == 0:
            return 1/self.N
        
        return count / countN
    
    