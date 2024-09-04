#==============================================================================
#title          : mib_v2_3.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.1
#python_version : 3.10.12
#==============================================================================
from itertools import product

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
        vars (set): Conjunto de varibales para la distribución (tipo vars).
        table (dict): Dicciónario de las probabilidades (tuple: float).
        columns (list): Lista con el orden de los nombres de las variables del diccionario.
    
    Distrib(set,dict,list) -> nuevo objeto Distrib
    """
    def __init__(self, vars: set, table: dict, columns:tuple) -> None:
        self._vars = vars
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
        vars (set): Conjunto de las variables (tipo var) dependiente (hipotesis).
        indep (set): Conjunto de las variables (tipo var) independientes (observaciones).
        table (dict): Dicciónario de las probabilidades ((tuple,tuple): float),
        donde la primera tupla representa la llave para los valores de indep y la segunda para vars.
        columns_vars (tuple): Lista con el orden de los nombres de las variables vars para el diccionario.
        columns_indep (tuple): Lista con el orden de los nombres de las variables indep para el diccionario.
    
    Distrib(set,set,dict,tuple,tuple) -> nuevo objeto Distrib
    """
    def __init__(self, vars: set, indep: set, table: dict, columns_vars: tuple, columns_indep: tuple) -> None:
        self._vars = vars
        self._indep = indep
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
        
    def GetVars(self) -> list:
        """ Método para obtener una lista del conjunto de los valores de las variables.

        Returns:
            list: Lista de los valores de cada variable.
        """
        vars = []
        for e in self._vars:
            vars.append(e.getValues())
        return vars

class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            model (Model): Modelo del problema con su distribución conjunta y su descomposción.
    """
    def __init__(self, model: Specification) -> None:
        self._model = model
        self._nameToVar = {}
        
        for v in self._model.getVars():
            self._nameToVar[v.getName()] = v
            
    def _ResetAllVars(self) -> None:
        for v in self._model.getVars():
            v.clear()
    
    def marginal(self, names:tuple, events: list) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            names (tuple): Conjunto del nombre de las variables para la marginal.
            events (tuple): Lista de los valores para las variables de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        sum = 0
        
        for i,name in enumerate(names):
            self._nameToVar[name].setMarginal(events[i])
        
        for k in product(*self._model.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for v in self._model.getVars():
                v.setEvent(k[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self._model.getDescomp():
                p *= d.P(self._nameToVar)
            
            sum += p
        
        self._ResetAllVars()
        return sum

    def cond(self, vars_names:tuple, vars_values:tuple, indep_names:tuple, indep_values:tuple) -> float:
        """ Método para hacer la consulta de una distribución conjunta.

        Args:
            vars_names (tuple): Conjunto del nombre de las variables de vars.
            vars_values (tuple): Lista de los valores para las variables de vars.
            indep_names (tuple): Conjunto del nombre de las variables de indep.
            indep_values (tuple): Lista de los valores para las variables de indep.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        # Calcular el numerados
        vars_u = tuple(list(vars_names) + list(indep_names))
        vals_u = list(vars_values) + list(indep_values)
        num =  self.marginal(vars_u, vals_u)
        
        
        # Calcular el denominador
        den = self.marginal(indep_names, list(indep_values))
        
        return num/den
    
    def marginalDistrib(self, vars:set) -> Distrib:
        """ Método para hacer la consulta de una distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.

        Returns:
            Distrib: Dsitribución marginal calculada.
        """
        table = {}
        columns = tuple([v.getName() for v in vars])
        values = [v.getValues() for v in vars]
        
        for value in product(*values):
            table[value] = self.marginal(columns, list(value))
            
        return Distrib(vars, table, columns)

    def condDistrib(self, vars:set, indep:set) -> CondDistrib:
        """ Método para hacer la consulta de una distribución condicional.

        Args:
            vars (set): Conjunto de variables de las hipótesis.
            indep (set): Conjunto de varibales de las observaciones.
            
        Returns:
            CondDistrib: Distribución condicional.
        """
        columns_vars = tuple([v.getName() for v in vars])
        columns_indep = tuple([v.getName() for v in indep])
        
        values_var = [v.getValues() for v in vars]
        values_indep = [v.getValues() for v in indep]
        
        table = {}
        for vi in product(*values_indep):
            table[vi] = {}
            for vv in product(*values_var):
                table[vi][vv] = self.cond(columns_vars, vv, columns_indep, vi)
                
        return CondDistrib(vars, indep, table, columns_vars, columns_indep)
    
    def marginal_inference(self, vars:set) -> tuple:
        """ Método para inferir el valor más probable de una distribución marginal o conjunta.

        Args:
            vars (set): Conjunto de variables de la distribución.

        Returns:
            tuple ((tuple, tuple, float)): El primer valor es la tupla de nombres, la segunda tupla representa sus valores
            y el último elemento es la probabilidad.
        """
        columns = tuple([v.getName() for v in vars])
        vars_values = [v.getValues() for v in vars]
        
        p = 0
        value = None
        for vv in product(*vars_values):
            p_vv = self.marginal(columns, list(vv))

            if p_vv > p:
                p = p_vv
                value = vv
        
        return columns, value, p
    
    def condObs(self, vars:tuple, vars_values:tuple, indep:tuple) -> tuple:
        """ Método para inferir el valor más probable de una obersvación de una distribución condicional
        dado los valores de las hipótesis

        Args:
            vars (tuple): Tupla de las variables de la distribución condicional.
            vars_values (tuple): Tupla con los valores de las variables de la distribución.
            indep (tuple): Tupla de las variables independientes de la distribución condicional.
        Returns:
            tuple ((tuple, tuple, tuple, tuple, float)): El primer elemento es la tupla de nombres de vars, el segundo elemento es la tupla que representa sus valores, 
            el tercer elemento es la tupla de nombres de indep, el cuarto elemento tupla representa sus valores y el último elemento es la probabilidad.
        """
        
        columns_vars = tuple([v.getName() for v in vars])
        columns_indep = tuple([v.getName() for v in indep])
        
        values_indep = [v.getValues() for v in indep]
        
        p = 0
        value_indep = None
        for vi in product(*values_indep):
            p_vi = self.cond(columns_vars, vars_values, columns_indep, vi)
            
            if p_vi > p:
                p = p_vi
                value_indep = vi
                
        return columns_vars, vars_values, columns_indep, value_indep, p
    
    def condHyp(self, vars:tuple, indep:tuple, indep_values:tuple) -> tuple:
        """ Método para inferir el valor más probable de una hipótesis de una distribución condicional
        dado los valores de las observaciones.

        Args:
            vars (tuple): Tupla de las variables de la distribución condicional.
            indep (tuple): Tupla de las variables independientes de la distribución condicional.
            indep_values (tuple): Tupla con los valores de las variables de indep de la distribución.
        Returns:
            tuple ((tuple, tuple, tuple, tuple, float)): El primer elemento es la tupla de nombres de vars, el segundo elemento es la tupla que representa sus valores, 
            el tercer elemento es la tupla de nombres de indep, el cuarto elemento tupla representa sus valores y el último elemento es la probabilidad.
        """
        columns_vars = tuple([v.getName() for v in list(vars)])
        columns_indep = tuple([v.getName() for v in list(indep)])
        
        values_vars = [v.getValues() for v in vars]
        p = 0
        value_vars = None
        for vv in product(*values_vars):
            p_vi = self.cond(columns_vars, vv, columns_indep, indep_values)
            
            if p_vi > p:
                p = p_vi
                value_vars = vv
                
        return (columns_vars, value_vars, p)

class Question:
    def __init__(self, sp: Specification) -> None:
        self._sp = sp
    
    def DistributionQuery(self, vars:set, indep:set = None):
        mib = Mib(self._sp)
        if not indep:
            return mib.marginalDistrib(vars)
        else:
            return mib.condDistrib(vars, indep)
        
    def Query(self, vars:tuple, indep:tuple = None, values_var:tuple = None, values_indep:tuple = None):
        mib = Mib(self._sp)
        if not indep:
            if values_var:
                return mib.marginal(tuple([v.getName() for v in vars]), list(values_var))
            else:
                return mib.marginal_inference(set(vars))
        else:
            if values_var and values_indep:
                return mib.cond(tuple([v.getName() for v in vars]), values_var, tuple([v.getName() for v in indep]), values_indep)
            elif values_var and not values_indep:
                return mib.condObs(vars, values_var, indep)
            elif not values_var and values_indep:
                return mib.condHyp(vars, indep, values_indep)
            
        print("Consulta no valida")