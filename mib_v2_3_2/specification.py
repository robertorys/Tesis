from mib_v2_3_2.var import Var

class Specification:
    """ Clase el manejo de la especificación de un pragrama Bayesiano.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (set): Conjunto de las distribuciones que generan el modelo. 
            
        Specification(set,tuple) -> nuevo objeto Distrib
    """
    
    def __init__(self, vars:set, descomp:set) -> None:
        self.vars = vars
        self.descomp = descomp
        
        t_descompo = []
        
        for d in self.descomp:
            t_descompo.append((d.level,d))
        
        self.Bn = sorted(t_descompo, key=lambda x: x[0])
    
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