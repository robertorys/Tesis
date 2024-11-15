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
        """ Establece los valores de las variables (o hipótesis) dada una distribución conjunta o condicional (hipótesis).

        Args:
            dist (Distrib): Distribución.
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

    def marginal(self, vars, values):
        return self.direct_sampling(vars, values) / self.N
    
    def gibss_sampling(self, vars, values, indep, indep_values):
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
    
    def cond(self, vars, values, indep, indep_values):
        return self.gibss_sampling(vars, values, indep, indep_values) / self.N

