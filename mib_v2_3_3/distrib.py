from mib_v2_3_3.var import Var
import random
from itertools import product

class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    Atributos:
        table (dict): Dicciónario de las probabilidades (tuple: float).
        vars (tuple): Tupla con el orden de las variables del diccionario.
        indep (tuple (optional)): Tupla con el orden de las variables independientes del diccionario.
        
    Distrib(tuple,tuple,dict) -> nuevo objeto Distrib
    
    Distrib(tuple,dict) -> nuevo objeto Distrib
    """
    
    def __init__(self, table:dict, vars:tuple, parents:tuple=None):
        self.table = table
        self.vars = vars
        self.parents = parents
        self.Parents = set()
        self.Children = set()
        
        if self.parents:
            self.name = f"P({self.vars}|{self.parents})"
        else:
            self.name = f"P({self.vars})"
    
    def setChildren(self, dists_children:set) -> None:
        self.Children = dists_children
    
    def getVars(self) -> set:
        vars = set(self.vars)
        if self.parents:
            vars = vars.union(set(self.parents))
        return vars
    
    def P(self) -> float:
        if not self.parents:
            return self.__jointP()
        else:
            return self.__condP()
    
    def __jointP(self) -> float:
        key = [v.event for v in self.vars]
        return self.table[tuple(key)]
    
    def __condP(self) -> float:
        vars_key = [v.event for v in self.vars]
        parents_key = [v.event for v in self.parents]
        return self.table[tuple(parents_key)][tuple(vars_key)]
    
    def check(self, knwon:set) -> bool:
        vars = set(self.vars)
        if self.parents:
            vars = vars.union(set(self.parents))
        
        if len(vars.difference(knwon)) == 0:
            return True
        
        return False