#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.1
#python_version : 3.10.12
#==============================================================================
from itertools import product
import json

class Var:
    """
    Clase para el manejo de las variables.
    Var(set) -> Nuevo objeto var
    """
    def __init__(self, values: set) -> None:
        self.values = values
        self.Omega = None
        self.event = None
        
    def setEvent(self, event) -> None:
        self.event = event
        self.Omega = self.values.copy().remove(event)
    
    def getValues(self) -> list:
        if self.Omega:
            return list(self.Omega)
        else:
            return [self.event]
    
    def clear(self) -> None:
        self.event = None
        self.Omega = None
       

class Distrib:
    """ 
    Clase para el manejo de las distribuciones de probabilidad de una sola varible.
    
    Distrib(Var) -> nuevo objeto Distrib sin especificación de sus probabilidades.
    
    Distrib(Var,str) -> nuevo objeto Distrib donde la tabla de probabilidades es un archivo JSON.
    
    Distrib(Var,dict) -> nuevo objeto Distrib donde la tabla de probabilidades es un diccionario.
    """
    def __init__(self, var: Var, dirJson: str = None, table: dict = None) -> None:
        self.var = var
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
        return self.table[self.var.event]
          
class CondDistrib:
    """
    Clase para el manejo de las distribuciones de probabilidad condicionales.
    
    CondDistrib(Var) -> nuevo objeto CondDistrib sin especificación de sus probabilidades.
    
    CondDistrib(Var,str) -> nuevo objeto CondDistrib donde la tabla de probabilidades es un archivo JSON.
    
    CondDistrib(Var,dict) -> nuevo objeto CondDistrib donde la tabla de probabilidades es un diccionario.
    """
    def __init__(self, vars: set, indep: set, dirJson: str = None, table: dict = None) -> None:
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
        indep_key = [v.event for v in self.indep]
        events_key = [v.event for v in self.vars]
        return self.p[tuple(indep_key)][tuple(events_key)]

class JointDistrib:
    """ 
    Clase para el manejo de las distribuciones de probabilidad de una sola varible.
    
    Distrib(Vars) -> nuevo objeto Distrib sin especificación de sus probabilidades.
    """
    def __init__(self, vars: set) -> None:
        self.vars = vars
            
    def setTable(self, table: dict) -> None:
        self.table = table
    
class Model:
    """
    Clase el manejo del modelo probabilístico de un problema basado en una especificación de una rede de Bayes.
    
    Model(set (Var),set (Distrib y CondDistrib)) -> nuevo objeto Model.
    """
    def __init__(self, vars: set, descomp: set) -> None:
        self.vars = vars
        self.descomp = descomp
    
    def P(self, values: list) -> float:
        if len(values) == len(self.vars):
            i = 0
            for var in self.vars:
                var.event = values[i]
                i += 1

            p = 1
            for d in self.descomp:
                p *= d.P()
            
            return p
        else:
            print('Error')
    
    def clearVars(self):
        for v in self.vars:
            v.clear()
    
    def getValues(self) -> list:
        """ Método para obtener todos los eventos de las variables de la conjunta.

        Returns:
            list: Lista de los valores de cada variable.
        """
        vars = []
        for e in self.vars:
            vars.append(e.getValues())
        return vars

class Question:  
    def __init__(self, distrib, iDistrib = False) -> None:
        self.__dstrib = distrib
        self.__iDistrib = iDistrib
        self.data = None
        self.__obs = None
        self.__hyps = None
    
    def setValue(self, value):
        if type(self.dstrib) is Distrib:
            self.value = value
    
    def setObs(self, vules: list):
        if type(self.__dstrib) is CondDistrib:
            self.obs = vules
    
    def setHyps(self, vules: list):
        if type(self.__dstrib) is CondDistrib:
            self.hyps = vules
            
class Mib:
    """
    Clase que cumple la función de un motor de inferencia
    
    Mib(Model) -> nuevo objeto Mib.
    """
    def __init__(self, model: Model) -> None:
        self.model = model
    
    def query(self, question: Question):
        if type(question.dstrib) is Distrib:
            if not question.iDistrib:
                mp = 0
                for event in question.distrib.var.values:
                    p = self.__marginal_event(question.distrib.var, event)
                    if p > mp:
                        mp = p
                        se = event
                question.data = (se, mp)
            else:
                self.__marginal_distrib(question.dstrib)
        
        elif type(question.dstrib) is CondDistrib:
            if not question.iDistrib:
                if question.obs:
                    mp = 0
                    sv = None
                    
                    obs = [v.values for v in question.dstrib.vars]
                    for values in product(*obs):
                        p = self.__cond_event(question.dstrib.vars, values, question.dstrib.indep, question.obs)
                        if p > mp:
                            mp = p
                            sv = values
                    
                    question.data = (sv, mp)
                
                elif question.hyps:
                    pass
                
                else:
                    print("Error: falta establecer las obervaciones o hipotesis")
            else:
                pass
            
        
        elif type(question.dstrib) is JointDistrib:
            pass
    
    #---------- Métodos para la inferencia --------------#
    
    def __marginal_event(self, var: Var, event: int) -> float:
        """ Método para hacer la consulta de inferencia de un evento.

        Args:
            var (Var): Vriable con los eventos de la distribución.
            value (int): Valor del evento para inferir.
            
        Returns:
            float: Valor de probabilidad del evento.
        """
        sum = 0
        var.setEvent(event)
        for k in product(*self.model.getValues()):
            # Establecer los valores de los eventos.
            i = 0
            for e in self.model.vars:
                e.event = k[i]
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.model.descomp:
                p *= d.P()
            
            sum += p
            
        self.model.clearVars()
        return sum
        
    def __marginal_distrib(self, distrib: Distrib) -> None:
        """ Método para hacer la consulta de inferencia de una distribución marginal.

        Args:
            distrib (Distrib): Distribución para inferir las probabiliodades.
        """
        probDict = {}
        
        for event in distrib.var.values:
            probDict[event] = self.__marginal_event(distrib.var, event)
        
        distrib.table = probDict
    
    def __cond_event(self, hypotesis: set, events: list, observations: set, values: list) -> float:
        """Método para hacer la consulta de inferencia de un evento condicional dada las observaciones.

            Args:
                hypotesis (set): COnjunto de hipótesis.
                events (list): Lista de los valores de las hipótesis.
                observations (set): Conjunto de varibales observadas.
                values (list): Valores de las observaciones, 
                    el orden debe de ser el mismo que el del argumento observations.
        """
        
        # Calcular el denominador
        den = 0
        # Establecer las observaciones
        i = 0
        for o in observations:
            o.event(values[i])
            i += 1
        
        # Calcular las combinaciones.
        for k in product(*self.model.getValues()):
            # Establecer los eventos.
            i = 0
            for v in self.model.vars:
                v.event(k[i])
                i += 1
            
            p = 1
            for d in self.model.descomp:
                p *= d.P()
            den += p
        
        # Calcular el numerador
        num = 0
        # Establecer la hipótesis
        i = 0
        for v in hypotesis:
            v.setEvent(events[i])
            i += 1
        
        # Calcular las combinaciones.
        for k in product(*self.model.getValues()):
            # Establecer los eventos.
            i = 0
            for v in self.model.vars:
                v.SetEvent(k[i])
                i += 1
            
            p = 1
            for d in self.model.descomp:
                p *= d._GetP()
            num += p
            
        self.model.clearVars()
        return num / den