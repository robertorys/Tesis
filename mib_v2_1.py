#==============================================================================
#title          : mib_v2_1.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.1
#python_version : 3.10.12
#==============================================================================
from itertools import product
import json

class Var:
    """Clase para el manejo de las variables (establecer y manejar los eventos).
    Atributos:
        values (set): Conjunto, de enteros, que contiene los valores que representan un evento.
        value (int): Valor que representa un evento.   
        
    Var(set) -> Nuevo objeto var
    """
    def __init__(self, values: set) -> None:
        self.values = values
        self.know = False
        self.event = None
        
    def setMarginal(self, event) -> None:
        """ Método para establecer un evento para el calculo de la marginal.
        Args:
            value (any): Valor que representa un evento. 
        """
        self.event = event
        self.know = True
    
    def getValues(self) -> list:
        """ Método obtner los valores de la variable para calcular la marginal.

        Return:
            list: lista con los valores de la variable.
        """  
        if self.know:
            return [self.event]
        else:
            return list(self.values)
    
    def clear(self) -> None:
        self.event = None
        self.know = False
       

class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    Atributos:
        vars (set): Conjunto de varibales para la distribución (tipo vars).
        dirJson (str): Dirreción de un archivo JSON con el diccionario de probabilidad.
        table (dict): Dicciónario de las probabilidades (tuple: float).
    
    Distrib(list,str) -> nuevo objeto Distrib donde la tabla de probabilidades es un archivo JSON.
    Distrib(list,dict) -> nuevo objeto Distrib donde la tabla de probabilidades es un diccionario.
    """
    def __init__(self, vars: set, table: dict = None, dirJson: str = None) -> None:
        self.vars = vars
        if dirJson:
            try:
                with open(dirJson, 'r') as archivo:
                    self.table = json.load(archivo)
            except FileNotFoundError:
                print(f"Error: El archivo '{dirJson}' no se encontró.")
            except json.JSONDecodeError:
                print(f"Error: El archivo '{dirJson}' no es un JSON válido.")
            except Exception as e:
                print(f"Se produjo un error: {e}")
        elif table:
            self.table = table
        else:
            self.table = None
            
    def P(self) -> float:
        key = [v.event for v in self.vars]
        return self.table[tuple(key)]

class CondDistrib:
    """ Clase para el manejo de distibuciones condicionales.

    Atributos:
        vars (set): Conjunto de las variables (tipo var) dependiente (hipotesis).
        indep (set): Conjunto de las variables (tipo var) independientes (observaciones).
        dirJson (str): Dirreción de un archivo JSON con el diccionario de probabilidad.
        table (dict): Dicciónario de las probabilidades ((tuple,tuple): float),
        donde la primera tupla representa la llave para los valores de indep y la segunda para vars.
    """
    
    def __init__(self, vars: set, indep: set, table: dict = None, dirJson: str = None) -> None:
        self.vars = vars
        self.indep = indep
        if dirJson:
            try:
                with open(dirJson, 'r') as archivo:
                    self.table = json.load(archivo)
            except FileNotFoundError:
                print(f"Error: El archivo '{dirJson}' no se encontró.")
            except json.JSONDecodeError:
                print(f"Error: El archivo '{dirJson}' no es un JSON válido.")
            except Exception as e:
                print(f"Se produjo un error: {e}")
        elif table:
            self.table = table
        else:
            self.table = None
    
    def P(self) -> float:
        key = [v.event for v in self.vars]
        indep_key = [e.event for e in self.indep]
        return self.table[tuple(indep_key)][tuple(key)]
    
class Specification:
    """ Clase el manejo de la especificación de un pragrama Bayesiano.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (set): Conjunto de las distribuciones que generan el modelo. 
    """
    
    def __init__(self, vars: set, descomp: set) -> None:
        self.vars = vars
        self.descomp = descomp
        
    def GetVars(self) -> list:
        """ Método para obtener una lista del conjunto de los valores de las variables.

        Returns:
            list: Lista de los valores de cada variable.
        """
        vars = []
        for e in self.vars:
            vars.append(e.getValues())
        return vars

class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            model (Model): Modelo del problema con su distribución conjunta y su descomposción.
    """
    def __init__(self, model: Specification) -> None:
        self.model = model
    
    def _ResetAllVars(self) -> None:
        for v in self.model.vars:
            v.clear()
    
    def marginalEvents(self, vars: set, events: list) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            vars (set): Conjunto de variables para la marginal.
            events (list): Lista de los valores para las variables de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        
        for i,v in enumerate(vars):
            print(i,v, events[i])
            v.setMarginal(events[i])
        
        for k in product(*self.model.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for v in self.model.vars:
                v.event = k[i]
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.model.descomp:
                p *= d.P()
            
            sum += p
        
        self._ResetAllVars()
        return sum
    
    def marginalDistrib(self, vars: set) -> Distrib:
        """ Método para hacer la consulta de una distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.

        Returns:
            Distrib: Dsitribución marginal calculada.
        """
        probDict = {}
        pEvents = [v.values for v in vars]
        
        for events in product(*pEvents):
            probDict[tuple(events)] = self.marginalEvents(vars, list(events))
        
        return Distrib(vars, probDict)
    
    def DistribInference(self, vars: set) -> tuple:
        """ Método para hacer la consulta del valor más probable de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.

        Returns:
            tuple (tuple, float): Valores de las variables y su probabilidad.
        """
        pv = 0
        ev = 0
        pEvents = [v.values for v in vars]
        
        for events in pEvents:
            prob = self.marginalEvents(vars, events)
            
            if prob > pv:
                pv = prob
                ev = events
                
        return (tuple(ev), prob)
    
    def CondEvents(self, hypotesis: set, events: list, observations: set, values: list) -> float:
        """ Método para hacer la consulta de una distribución condicional dada las hipótesis y observaciones.

        Args:
            hypotesis (set): Conjunto de variables para la hipótesi.
            event (list): Lista de los vlores de la hipótesis.
            observations (set): Conjunto de varibales para las observaciones.
            values (list): Valores de las observaciones. 

        Returns:
            float: Valor de probabilidad.
        """
        
        # Calcular el denominador
        den = self.marginalEvents(hypotesis.union(observations), events + values)
        
        # Calcular el numerados
        num = self.marginalEvents(observations, values)
        
        return num / den
    
    def CondHyp(self, hypotesis: set, observations: set, values: list) -> dict:
        """ Método para hacer la consulta de una distribución condicional dada las observaciones.
        Args:
            hypotesis (set): Conjunto de variable de la hipótesis.
            observations (set): Conjunto de varibales de las observaciones.
            values (list): Valores de las observaciones.
            
        Returns:
            dict: Diccionario de la probabilidades de las hipótesis.
        """
        
        dH_O = {}
        HypValues = [h.values for h in hypotesis]
        for hv in product(*HypValues):
            dH_O[tuple(hv)] = self.CondEvents(hypotesis, list(hv), observations, values)
        return dH_O
    
    
    def CondDistrib_Inference(self, hypotesis: set, observations: set) -> CondDistrib:
        """ Método para hacer la consulta de una distribución condicional.

        Args:
            hypotesis (Var): Conjunto de variables de las hipótesis.
            observations (set): Conjunto de varibales de las observaciones.
            
        Returns:
            CondDistrib: Distribución condicional.
        """
        dH_O = {}
        ObsValues = [o.values for o in observations]
        for ov in product(*ObsValues):
            dH_O[tuple(ov)] = self.CondHyp(hypotesis, observations, list(ov))
        return dH_O
    
    def CondInference_Hyp(self, hypotesis: set, observations: set, values: list) -> tuple:
        """ Método para hacer la consulta de una distribución condicional dada las observaciones.
        Args:
            hypotesis (set): Conjunto de variable de la hipótesis.
            observations (set): Conjunto de varibales de las observaciones.
            values (list): Valores de las observaciones.
            
        Returns:
            (hyp, p): Tupla con los valores de las variables de la hipótesis y su probabilidad.
        """
        
        pv = 0
        
        HypValues = [h.values for h in hypotesis]
        for hv in product(*HypValues):
            proba = self.CondEvents(hypotesis, list(hv), observations, values)
            
            if proba > pv:
                pv = proba
                hyp = hv
        return (hyp, pv)
    
    def CondInference_Obs(self, hypotesis: set, values: list, observations: set) -> tuple:
        """ Método para hacer la consulta de una distribución condicional dada las observaciones.
        Args:
            hypotesis (set): Conjunto de variable de la hipótesis.
            values (list): Valores de la hipótesis.
            observations (set): Conjunto de varibales de las observaciones.
              
        Returns:
            (hyp, p): Tupla con los valores de las variables de la hipótesis y su probabilidad.
        """
        
        pv = 0
        
        obsValues = [o.values for o in observations]
        for ov in product(*obsValues):
            proba = self.CondEvents(hypotesis, values, observations, list(ov))
            
            if proba > pv:
                pv = proba
                ons = ov
        return (ov, pv)

class Question:
    def __init__(self, sp: Specification) -> None:
        self.mib = Mib(sp)
    
    def DistributionQuery(self, vars:set, indep:set = None):
        if not indep:
            return self.mib.marginalDistrib(vars)
        else:
            return self.mib.CondDistrib_Inference(vars, indep)
        
    def Query(self, vars:set, indep:set = None, values:list = None, obs:list = None):
        if not indep:
            if values:
                return self.mib.marginalEvents(vars, values)
            else:
                return self.mib.DistribInference(vars)
        else:
            if obs and values:
                return self.mib.CondEvents(vars, values, indep, obs)
            elif obs and not values:
                return self.mib.CondInference_Hyp(vars, indep, obs)
            elif not obs and values:
                return self.mib.CondInference_Obs(vars, indep, obs)
            
        print("Consulta no valida")
