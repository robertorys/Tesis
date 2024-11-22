from mib_v2_3_3.mib import Mib
from mib_v2_3_3.var import Var
from mib_v2_3_3.distrib import Distrib
from mib_v2_3_3.specification import Specification
from itertools import product
import numpy as np
import random

class MibAp(Mib):
    """ Clase para el motor de inferencia bayesiana usando aproximación.

        Atributos:
            ds (Specification): Modelo del problema con su distribución conjunta y su descomposción.
            N (int): Número de muestreo.
    """
    def __init__(self, ds:Specification, N:int) -> None:
        super().__init__(ds)
        self.N = N
        
    def __setValueDs(self, dist:Distrib) -> None:
        """ Establece los valores de las variables (o hipótesis), de forma aleatoria según su probabilidades,
        dado los evetos establecidos de los padres.
        
        Args:
            dist (Distrib): Distribución para establecer los valores de las variables.
        """
        if dist.parents:
            parents_key = tuple([v.event for v in dist.parents])
            values = list(product(*[v.values for v in dist.vars]))
            probabilities = []
            
            for key in values:
                probabilities.append(dist.table[parents_key][key])

            value = random.choices(values, probabilities)[0]
        else:
            values = list(product(*[v.values for v in dist.vars]))
            probabilities = []
            
            for key in values:
                probabilities.append(dist.table[key])

            value = random.choices(values, probabilities)[0]
        
        for i,v in enumerate(dist.vars):
                v.event = value[i]
    
    def __setValueGs(self, dist:Distrib) -> None:
        """ Establece los valores de las variables (o hipótesis), de forma aleatoria según su probabilidades,
        dado los evetos establecidos de los padres y las observaciones.

        Args:
            dist (Distrib): Distribución para establecer los valores de las variables.
        """
        v = dist.vars[0]
        probabilities = []
        values = []
        
        for value in v.values:
            values.append(value)
            p = dist.P()
            
            if len(dist.Children) > 0:         
                for d in dist.Children:
                    p *= d.P()
            probabilities.append(p)
                
        alpha = 1 / np.sum(probabilities)
            
        for i in range(len(probabilities)):
            probabilities[i] = alpha * probabilities[i]
                
        v.event = random.choices(values, probabilities)[0]
         
    def direct_sampling(self, vars:tuple, values:tuple) -> int:
        """ Método para realizar un muestreo directo.

        Args:
            vars (tuple): Variables para hacer el muestreo.
            values (tuple): Valores para las variables a buscar.

        Returns:
            int: Número de veces que se genero la muestra buscada.
        """
        iteration = 0
        count = 0
        vars_set = set(vars)
        
        while iteration < self.N:
            vs = vars_set.copy()
            i = 0
            
            while len(vs) > 0:
                self.__setValueDs(self.ds.descomp[i])
                
                vs = vs - set(self.ds.descomp[i].vars)
                i += 1
            
            indv = []
            for v in vars:
                indv.append(v.event)
            
            if tuple(indv) == values:
                count += 1
                
            self.ds.resetVars()
            iteration += 1
            
        return count

    def marginal(self, vars:tuple, values:tuple) -> float:
        return self.direct_sampling(vars, values) / self.N
    
    def gibss_sampling(self, vars:tuple, values:tuple, indep:tuple, indep_values:tuple) -> int:
        """ Método para realizar un muestreo de Gibss.

        Args:
            vars (tuple): Variables para hacer el muestreo.
            values (tuple): Valores para las variables a buscar.
            indep (_type_): Variables independientes (observaciones) para hacer el muestreo.
            indep_values (_type_): Valores para las variables independientes.

        Returns:
            int: Número de veces que se genero la muestra buscada.
        """
        for i,v in enumerate(indep):
            v.event = indep_values[i]
        
        unkwon_vars = self.ds.vars - set(indep)
        
        iteration = 0
        count = 0
        vars_set = set(vars)
        
        while iteration < self.N:
            vs = vars_set.copy()
            
            for v in unkwon_vars:
                v.event = random.choices(v.getValues())[0]
            
            i = 0
            while len(vs) > 0:
                self.__setValueGs(self.ds.descomp[i])
                
                vs = vs - set(self.ds.descomp[i].vars)
                i += 1
            
            indv = []
            for v in vars:
                indv.append(v.event)
            
            if tuple(indv) == values:
                count += 1
            
            for v in unkwon_vars:   
                v.reset()
            iteration += 1
            
        return count
    
    def cond(self, vars:tuple, values:tuple, indep:tuple, indep_values:tuple) -> float:
        return self.gibss_sampling(vars, values, indep, indep_values) / self.N

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
        
        values_values = [v.values for v in vars]
        
        p = 0
        value_vars = None
        for hyp in product(*values_values):
            
            p_hyp = self.cond(vars, hyp, indep, indep_values)
            
            if p_hyp > p:
                p = p_hyp
                value_vars = hyp
                      
        return vars_column, value_vars, p

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
            p_obs = self.cond(vars, vars_values, indep, obs)
            
            if p / p_obs < 1:
                p = p_obs
                indep_value = obs
                
        return indep_column, indep_value, p