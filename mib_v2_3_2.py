#==============================================================================
#title          : mib_v2_3_2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.3.2
#python_version : 3.10.12
#==============================================================================
from itertools import product
import math
import multiprocessing as mp
import copy

class Var:
    """Clase para el manejo de las variables (establecer y manejar los eventos).
    Atributos:
        name (any): Nombre de la varibale.
        values (set): Conjunto, de enteros, que contiene los valores que representan un evento.
        event (any): Valor que representa un evento.   
        
    Var(any,set) -> Nuevo objeto Var.
    """
    def __init__(self, name, values:set) -> None:
        self.name = name
        self.values = values
        self.event = None
    
    def getValues(self) -> list:
        """ Método obtner los valores de la variable para calcular la marginal.

        Return:
            list: lista con los valores de la variable.
        """  
        if self.event:
            return [self.event]
        else:
            return list(self.values)
            
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
        key = [v.name for v in self.vars]
        return self.table[tuple(key)]
    
    def _condP(self) -> float:
        vars_key = [v.name for v in self.vars]
        indep_key = [v.name for v in self.parents]
        return self.table[tuple(indep_key)][tuple(vars_key)]
    
class Specification:
    """ Clase el manejo de la especificación de un pragrama Bayesiano.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (set): Conjunto de las distribuciones que generan el modelo. 
            
        Specification(set,tuple) -> nuevo objeto Distrib
    """
    
    def __init__(self, vars:set, descomp:tuple) -> None:
        self.vars = vars
        self.descomp = descomp
        
    def getValues(hidden_vars:tuple) -> list:
        """ Método para obtener una lista de los valores de las variables.

        Returns:
            list: Lista de los valores de cada variable.
        """
        return [var.getValues() for var in hidden_vars]
    
class mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            description (Specification): Descripción de un modelo.
    """
    
    def __init__(self, description: Specification) -> None:
        self.description = description
    
    def _ResetAllVars(self) -> None:
        for v in self.description.vars:
            v.event = None
    
    def probability(self, hidden_vars:tuple) -> float:
        """ Método para hacer el calculo de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        for key in product(self.description.getValues(hidden_vars)):
            # Establecer los valores de los eventos.
            i = 0
            for v in hidden_vars:
                v.event = key[i]
                i += 1
        
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.description.descomp:
                p *= d.P()
            
            sum += p
    
        self._ResetAllVars()
        return sum

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
        
        return self.probability(self.description.vars - set(vars))
    
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
        
        union = set(vars1).union(set(vars2))
        return self.probability(self.descriparents_columnsption.vars - union)
    
    def cond(self, vars:tuple, vars_values:tuple, indep_vars:tuple, indep_values:tuple) -> float:
        """ Método para hacer la consulta de una distribución conjunta.

        Args:
            vars (tuple): Tupla de las variables de vars.
            vars_values (tuple): Tupla de los valores para las variables de vars.
            indep_vars (tuple): Tupla de los nombres de las variables de indep.
            indep_values (tuple): Tupla de los valores para las variables de indep.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        # Calcular el numerados
        num = self.joint_marginal(vars, vars_values, indep_vars, indep_values)
        
        # Calcular el denominador
        den = self.marginal(indep_vars, indep_values)
        
        return num / den
    
    def Distrib_inference(self, vars:set) -> Distrib:
        """ Método para hacer la consulta de una distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.

        Returns:
            Distrib: Dsitribución marginal calculada.
        """
        table = {}
        columns = tuple(vars)
        values = [v.values for v in vars]
        
        for event in product(*values):
            table[event] = self.marginal(columns, event)
            
        return Distrib(table, columns)  
    
    def condDistrib_inference(self, vars:set, indep:set) -> Distrib:
        """ Método para hacer la consulta de una distribución condicional.

        Args:
            vars (set): Conjunto de variables de las hipótesis.
            indep (set): Conjunto de varibales de las observaciones.
            
        Returns:
            CondDistrib: Distribución condicional.
        """
        columns_vars = tuple(vars)
        columns_indep = tuple(indep)
        
        values_var = [v.values for v in vars]
        values_indep = [v.values for v in indep]
        
        table = {}
        for vi in product(*values_indep):
            table[vi] = {}
            for vv in product(*values_var):
                table[vi][vv] = self.cond(columns_vars, vv, columns_indep, vi)
                
        return Distrib(table, columns_vars, columns_indep)