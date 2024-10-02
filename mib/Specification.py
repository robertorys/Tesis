class Var:
    """Clase para el manejo de las variables (establecer y manejar los eventos).
    Atributos:
        name (any): Nombre de la varibale.
        values (set): Conjunto, de enteros, que contiene los valores que representan un evento.
        event (any): Valor que representa un evento.   
        
    Var(any,set) -> Nuevo objeto Var.
    """
    def __init__(self, name, values:set) -> None:
        self._name = name
        self._values = values
        self._know = False
        self._event = None
    
    def getName(self):
        return self._name
    
    def getEvent(self):
        return self._event
    
    def setEvent(self, event):
        self._event = event
    
    def getCard(self) -> int:
        if self._know:
            return len([self._event])
        else:
            return len(self._values)
        
    def setMarginal(self, event) -> None:
        """ Método para establecer un evento para el calculo de la marginal.
        Args:
            value (any): Valor que representa un evento. 
        """
        self._event = event
        self._know = True
    
    def getValues(self) -> list:
        """ Método obtner los valores de la variable para calcular la marginal.

        Return:
            list: lista con los valores de la variable.
        """  
        if self._know:
            return [self._event]
        else:
            return list(self._values)
    
    def clear(self) -> None:
        self._event = None
        self._know = False

class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    Atributos:
        table (dict): Dicciónario de las probabilidades (tuple: float).
        columns (tuple): Tupla con el orden de los nombres de las variables del diccionario.
    
    Distrib(dict,tuple) -> nuevo objeto Distrib
    """
    def __init__(self, table: dict, columns:tuple) -> None:
        self._table = table
        self._columns = columns
    
    def print_table(self) -> None:
        print(self._table)
    
    def P(self, nameToVar: dict) -> float:
        """ Método para regresar el valor de probabilidad de los valores establecidos a los 
        eventos de las variables.

        Returns:
            float: Valor de probabilidad.
        """
        key = [nameToVar[name].getEvent() for name in self._columns]
        return self._table[tuple(key)]

class CondDistrib:
    """ Clase para el manejo de distibuciones condicionales.

    Atributos:
        table (dict): Dicciónario de las probabilidades ((tuple,tuple): float),
            donde la primera tupla representa la llave para los valores de indep y la segunda para vars.
        columns_vars (tuple): Lista con el orden de los nombres de las variables dependientes para el diccionario.
        columns_indep (tuple): Lista con el orden de los nombres de las variables independientes para el diccionario.
    
    Distrib(dict,tuple,tuple) -> nuevo objeto Distrib
    """
    def __init__(self, table: dict, columns_vars: tuple, columns_indep: tuple) -> None:
        self._table = table
        self._columns_vars = columns_vars
        self._columns_indep = columns_indep
    
    def print_table(self) -> None:
        print(self._table)
    
    def P(self, nameToVar:dict) -> float:
        """ Método para regresar el valor de probabilidad de los valores establecidos a los 
        eventos de las variables.

        Returns:
            float: Valor de probabilidad.
        """
        vars_key = [nameToVar[name].getEvent() for name in self._columns_vars]
        indep_key = [nameToVar[name].getEvent() for name in self._columns_indep]
        return self._table[tuple(indep_key)][tuple(vars_key)]
    
class Specification:
    """ Clase el manejo de la especificación de un pragrama Bayesiano.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (set): Conjunto de las distribuciones que generan el modelo. 
    """
    
    def __init__(self, vars: set, descomp: set) -> None:
        self._vars = vars
        self._descomp = descomp
        
    def getVars(self) -> set:
        """ Método para obtener el conjunto de las variables

        Returns:
            set: Conjunto de las variables.
        """
        return self._vars
    
    def getDescomp(self) -> set:
        """ Método para obtener el conjunto de las distribuciones de la descomposición.

        Returns:
            set: Conjunto de las distribuciones
        """
        return self._descomp
        
    def getValues(self) -> list:
        """ Método para obtener una lista del conjunto de los valores de las variables.

        Returns:
            list: Lista de los valores de cada variable.
        """
        vars = []
        for e in self._vars:
            vars.append(e.getValues())
        return vars
