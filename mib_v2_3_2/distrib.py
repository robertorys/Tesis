import random
from itertools import product
from mib_v2_3_2.var import Var

class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    Atributos:
        table (dict): Dicciónario de las probabilidades (tuple: float).
        vars (tuple): Tupla con el orden de las variables del diccionario.
        parents (tuple (optional)): Tupla con el orden de las variables padres del diccionario.
        
    Distrib(tuple,tuple,dict) -> nuevo objeto Distrib
    
    Distrib(tuple,dict) -> nuevo objeto Distrib
    """

    def __init__(self, table:dict, vars:tuple, parents:tuple = None) -> None:
        self.table = table
        self.vars = vars
        self.parents = parents
    
    def P(self) -> float:
        if not self.parents:
            return self._jointP()
        else:
            return self._condP()
    
    def _jointP(self) -> float:
        key = [v.event for v in self.vars]
        return self.table[tuple(key)]
    
    def _condP(self) -> float:
        vars_key = [v.event for v in self.vars]
        indep_key = [v.event for v in self.parents]
        return self.table[tuple(indep_key)][tuple(vars_key)]
    
    def setSample(self) -> None:
        if self.parents:
            indep_key = tuple([v.event for v in self.parents])
            values = list(product(*[v.values for v in self.vars]))
            probabilitys = []
            for key in product(*[v.values for v in self.vars]):
                probabilitys.append(self.table[indep_key][key])
            
            value = random.choices(values, probabilitys, k=1)[0]
        else:
            values = list(product(*[v.values for v in self.vars]))
            probabilitys = []
            for key in values:
                probabilitys.append(self.table[key])
            
            value = random.choices(values, probabilitys, k=1)[0]
            
        for i,v in enumerate(self.vars):
                v.event = value[i]

