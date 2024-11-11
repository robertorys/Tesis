from mib_v2_3_3.var import Var
from mib_v2_3_3.distrib import Distrib
from mib_v2_3_3.specification import Specification
from itertools import product
import multiprocessing as mp
import math

class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            description (Specification): Descripción de un modelo.
    """
    
    def __init__(self, description: Specification) -> None:
        self.ds = description
    
    def probability(self, hidden_vars:tuple) -> float:
        """ Método para hacer el calculo de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        
        for key in product(*self.ds.getValues(hidden_vars)):
            # Establecer los valores de los eventos.
            i = 0
            for v in hidden_vars:
                v.event = key[i]
                i += 1
        
            # Calcular la probabilidad con los valores de k.
            p_i = 1
            for d in self.ds.descomp:
                p_i *= d.P()
            
            sum += p_i
    
        self.ds.resetVars()
        return sum
 
    def marginal(self, vars:tuple, values:tuple) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            vars (tuple): Tupla con las varibales.
            values (tuple): Tupla con los valores de las varibales.

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        i = 0
        for var in vars:
            var.event = values[i]
            i += 1
        
        hidden = self.ds.vars - set(vars)
        return self.probability(tuple(hidden))
    
    def joint_marginal(self, vars1:tuple, values1:tuple, vars2:tuple, values2:tuple) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1 (tuple): Tupla con las varibales del primer conjunto.
            values1 (tuple): Tupla con los valores del primer conjunto.
            vars1 (tuple): Tupla con las varibales del segundo conjunto.
            values1 (tuple): Tupla con los valores del segundo conjunto.

        Returns:
            float: Valor de la probabilidad de la conjunta.
        """
        return self.marginal(vars1+vars2, values1+values2)
    
    def cond(self, vars:tuple, values:tuple, indep:tuple, indep_values:tuple) -> float:
        """ Método para hacer la consulta de una condicional.

        Args:
            vars (tuple): Tupla con las varibales dependientes.
            values (tuple): Tupla con los valores de las varibales dependientes.
            indep (tuple): Tupla con las varibales independientes.
            indep_values (tuple): Tupla con los valores de las varibales independientes.

        Returns:
            float: Valor de la probabilidad de la condicional.
        """
        
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
        
        values_values = [v.values for v in vars]
        
        p = 0
        value_vars = None
        den = self.marginal(indep, indep_values)
        for hyp in product(*values_values):
            
            p_hyp = self.joint_marginal(vars, hyp, indep, indep_values) / den
            
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
            p_obs = self.joint_marginal(vars, vars_values, indep, obs)
            
            if p / p_obs < 1:
                p = p_obs
                indep_value = obs
                
        return indep_column, indep_value, p / self.marginal(indep, indep_value)

    
