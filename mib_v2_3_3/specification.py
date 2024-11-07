from mib_v2_3_3.var import Var
from mib_v2_3_3.bayesian_network import nodo

class Specification:
    """ Clase el manejo de la especificación de un pragrama Bayesiano.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (set): Conjunto de las distribuciones que generan el modelo. 
            
        Specification(set,tuple) -> nuevo objeto Distrib
    """
    
    def __init__(self, vars:set, bn:set) -> None:
        self.vars = vars
        self.bn = bn
        
    def getVar(self, name) -> Var:
        for v in self.vars:
            if name == v.name:
                return v
        
    def getValues(self, hidden_vars:tuple) -> list:
        """ Método para obtener una lista de los valores de las variables.

        Returns:
            list: Lista de los valores de cada variable.
        """
        return [var.getValues() for var in hidden_vars]

    def resetVars(self) -> None:
        for v in self.vars:
            v.reset()