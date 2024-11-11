from mib_v2_3_3.var import Var

class Specification:
    """ Clase el manejo de la especificación de un pragrama Bayesiano.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (tuple): Tupla de las distribuciones que generan el modelo. 
            
        Specification(set,tuple) -> nuevo objeto Distrib
    """
    
    def __init__(self, vars:set, descomp:tuple) -> None:
        self.vars = vars
        self.descomp = descomp
        self.varsDict = {}
        for v in self.vars:
            self.varsDict[v.name] = v
    
    def getVar(self, name) -> Var:
        if name in self.varsDict.keys():
            return self.varsDict[name]
        return None

    def getValues(self, hidden_vars:tuple) -> list:
        """ Método para obtener una lista de los valores de las variables.

        Returns:
            list: Lista de los valores de cada variable.
        """
        return [var.getValues() for var in hidden_vars]

    def resetVars(self) -> None:
        for v in self.vars:
            v.reset()   
        