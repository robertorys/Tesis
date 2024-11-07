import random
from itertools import product
from mib_v2_3_3.var import Var

class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    Atributos:
        table (dict): Dicciónario de las probabilidades (tuple: float).
        vars (tuple): Tupla con el orden de las variables del diccionario.
        indep (tuple (optional)): Tupla con el orden de las variables independientes del diccionario.
        
    Distrib(tuple,tuple,dict) -> nuevo objeto Distrib
    
    Distrib(tuple,dict) -> nuevo objeto Distrib
    """

    def __init__(self, name, table:dict, vars:tuple, indep:tuple = None) -> None:
        self.name = name
        self.table = table
        self.vars = vars
        self.indep = indep

    def P(self) -> float:
        if not self.indep:
            return self._jointP()
        else:
            return self._condP()
    
    def _jointP(self) -> float:
        key = [v.event for v in self.vars]
        return self.table[tuple(key)]
    
    def _condP(self) -> float:
        vars_key = [v.event for v in self.vars]
        indep_key = [v.event for v in self.indep]
        return self.table[tuple(indep_key)][tuple(vars_key)]
    
    def check(self, knwon:set) -> bool:
        vars = set(self.vars)
        if self.indep:
            vars = vars.union(set(self.indep))
        
        if len(vars.difference(knwon)) == 0:
            return True
        
        return False
    
    def getVars(self) -> set:
        vars = set(self.vars)
        if self.indep:
            vars = vars.union(set(self.indep))
        return vars
    
    def setSample(self) -> None:
        if self.indep:
            indep_key = tuple([v.event for v in self.indep])
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

