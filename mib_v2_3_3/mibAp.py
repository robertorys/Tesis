#==============================================================================
#title          : Mib.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.3.2
#python_version : 3.10.12
#==============================================================================
from itertools import product
import multiprocessing as mp
import math
from mib_v2_3_3.mib import Mib
from mib_v2_3_3.var import Var
from mib_v2_3_3.distrib import Distrib
from mib_v2_3_3.specification import Specification

class MibAP(Mib):
    """ Clase para el motor de inferencia bayesiana usando aproximación.

        Atributos:
            ds (Specification): Modelo del problema con su distribución conjunta y su descomposción.
    """
    def __init__(self, ds: Specification, N:int) -> None:
        super().__init__(ds)
        self.N = N
    
    def direct_sampling(self, vars:tuple, values:tuple) -> int:
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
    
    def margianl(self, vars:tuple, values:tuple) -> float:
        
        return self.direct_sampling(vars, values) / self.N
    
    def gibbs_sampling(self, vars:tuple, values:tuple, indep_vars:tuple, indep_values:tuple) -> tuple:
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
        i,n = self.gibbs_sampling(vars, values, indep, indep_values)
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

class MibApMp(MibAP):
    
    def __init__(self, ds, process_n, N):
        self.process_n = process_n
        super().__init__(ds, N)
        
    def sample_margianl_p(self, ds:Specification, vars:tuple, values:tuple, count_q:mp.Queue, N:int) -> None:
        mib = MibAP(ds,N)
        
        count = mib.sample_marginal(vars, values)
        
        count_q.put(count)
    
    def sample_cond_p(self, ds:Specification, vars, values, i_vars, i_values, count_q:mp.Queue, countN_q:mp.Queue,N) -> None:
        mib = MibAP(ds, N)
        
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
                if d.indep:
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
 