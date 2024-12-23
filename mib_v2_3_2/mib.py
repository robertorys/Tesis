#==============================================================================
#title          : Mib.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.3.2
#python_version : 3.10.12
#==============================================================================
from itertools import product
import multiprocessing as mp
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
    
    def probability(self, known:set, hidden_vars:set) -> float:
        """ Método para hacer el calculo de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        descompK = set()
        
        for d in self.ds.descomp:
            if d.check(known):
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

        
        
            
            