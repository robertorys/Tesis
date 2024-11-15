from mib_v2_3_3.var import Var
from mib_v2_3_3 import Distrib

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

    def getValues(self, unkonw:tuple) -> list:
        """ Método para obtener una lista de los valores de las variables.
        Args:
            unkonw (tuple (optional)): Tupla de las variables desconocidas.
        Returns:
            list: Lista de los valores de cada variable.
        """
        return [var.getValues() for var in unkonw]

    def resetVars(self) -> None:
        for v in self.vars:
            v.reset()   
    
def Copy(ds:Specification) -> tuple:
    """ Crea la copia de una especificación.

    Args:
        ds (Specification): Descripción con la espesificación a copiar.
    Returns:
        tuple (Specification, dict): Especificación y diccionario de nombres a variables.
    """
    vars_copy = set()
    for v in ds.vars:
        v_aux = Var(v.name, v.values)
        if v.event:
            v_aux.event = v.event
        vars_copy.add(v_aux) 
        
    name2var = {}
    
    for v in vars_copy:
        name2var[v.name] = v  
    
    descomp_copy = []
    for d in ds.descomp:
        d_vars = tuple([name2var[v.name] for v in d.vars]) 
        if d.parents:
            d_parents = tuple([name2var[v.name] for v in d.parents])   
            descomp_copy.append(Distrib(d.table, d_vars, d_parents))
        else:
            descomp_copy.append(Distrib(d.table, d_vars))
                    
    ds_copy = Specification(vars_copy, tuple(descomp_copy)) 
    
    return ds_copy, name2var