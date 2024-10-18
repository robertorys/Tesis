#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2
#python_version : 3.10.12
#==============================================================================
from itertools import product

class Var:
    """Clase para el manejo de las variables de probabilidad (establecer y manejar los eventos).
    Atributos:
        values (set): Conjunto, de enteros, que contiene los valores que representan un evento.
        value (int): Valor que representa un evento.   
    """
    
    def __init__(self, values: set) -> None:
        self.values = values
        self.event = None
        '''infer (int): Auxiliar para guardar temporalmente los valores de los eventos.
            durante la inferencia.'''
        self.infer = False
        
    def SetEvent(self, value: int) -> None:
        """ Método para establecer un evento.
        Args:
            value (int): Valor que representa un evento. 
        """
        self.event = value
    
    def SetInfer(self, event: int) -> None:
        """ Método para establecer un evento para hacer inferencia,
        Args:
            event (int): Valor del evento
        """
        self.infer = True
        self.event = event
    
    def GetInfer(self) -> list:
        """ Método obtner los eventos para calcular.

        Return:
            list: lista con los eventos para hacer el calculo.
        """  
        if self.infer:
            return [self.event]
        else:
            return list(self.values)
    
    def Reset(self) -> None:
        """ Reestablecer el valor del atributo infer.
        """
        self.infer = False
        self.event = None
    
class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    
    Atributos:
        var (Var): Objeto de los eventos de la distribución.
        table (dict): Dicciónario de las probabilidades (key (int): probability).
    """
    def __init__(self, var: Var, table: dict) -> None:
        self.var = var
        self.table = table
        
    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer el un evento.

        Returns:
            float: Probabilidad del evento establecido.
        """
        return self.table[self.var.event]

class CondDistrib:
    """ Clase para el manejo de distibuciones condicionales.

    Atributos:
        var (Var): Objeto que guarda los eventos dependiente.
        indep (set): Conjunto de objetos tipo Var, son las variables de probabilidad independientes (probabilidades dadas). 
            La llave priemro es la tupla de los valores de los eventos independiante,
            y luego la llave para el evento dependiente, ej.: {(0,1):{0:.5,1:.5}}.
    """
    def __init__(self, var: Var, indep: set, table: dict) -> None:
        self.var = var
        self.indep = indep
        self.table = table

    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer el evento de la variable, 
            y los eventos de las variables independientes.

        Returns:
            float: Probabilidad de los eventos establecido.
        """
        indep_key = [e.event for e in self.indep]
        return self.table[tuple(indep_key)][self.var.event]

class JointDistrib:
    """ Clase para el manejo de las distribuciones conjuntas.

    Atributos:
        var (set): Conjunto de objeto de los eventos de la distribución.
        table (dict): Dicciónario de las probabilidades (key (tuple): probability).
    """
    
    def __init__(self, vars: set, table: dict) -> None:
        self.vars = vars
        self.table = table
    
    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer el evento de las variables.

        Returns:
            float: Probabilidad de los eventos establecido.
        """
        key = [e.event for e in self.vars]
        return self.table[tuple(key)]

class Model:
    """ Clase el manejo del modelado de un problema para inferir alguna distribución de probabilidad.
        
        Atributos:
            vars (set): Conjunto de variables de la distribución conjunta.
            descomp (set): Conjunto de las distribuciones que generan el modelo. 
            que generan el modelo de un problema.
    """
    def __init__(self, vars: set, descomp: set) -> None:
        self.vars = vars
        self.descomp = descomp
        
    def GetVars(self) -> list:
        """ Método para obtener todas los eventos de las variables de la conjunta.

        Returns:
            list: Lista de los valores de cada evento.
        """
        vars = []
        for e in self.vars:
            vars.append(e.GetInfer())
        return vars

class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            jointDistrib (Model): Distribución conjunta con el modelo del problema.
    """
    def __init__(self, model: Model) -> None:
        self.jointDistrib = model
    
    def _ResetAllVars(self) -> None:
        for v in self.jointDistrib.vars:
            v.Reset()
    
    def MarginalInference_Event(self, var: Var, event: int) -> float:
        """ Método para hacer la consulta de inferencia de un evento.

        Args:
            var (Var): Vriable con los eventos de la distribución.
            value (int): Valor del evento para inferir.
            
        Returns:
            float: Valor de probabilidad del evento.
        """
        sum = 0
        var.SetInfer(event)
        for k in product(*self.jointDistrib.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for e in self.jointDistrib.vars:
                e.SetEvent(k[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            
            sum += p
            
        self._ResetAllVars()
        return sum

    def Marginal_Distrib(self, var: Var) -> Distrib:
        """ Método para hacer la consulta de inferencia de una distribución marginal.

        Args:
            var (Var): Variable para inferir la probabiliodad de los eventos de la distribución.

        Returns:
            Distrib: Dsitribución marginal inferida.
        """
        probDict = {}
        events = var.values.copy()
        
        for event in events:
            probDict[event] = self.MarginalInference_Event(var, event)
        
        return Distrib(var, probDict)
    
    def Marginal_inference(self, var: Var) -> tuple:
        """ Método para inferir el valor del evento más probable de una distribución marginal.

        Args:
            var (Var): Variable para inferir la probabiliodad de los eventos de la distribución.

        Returns:
            tuple (int, float): Valor del evento y su probabilidad.
        """
        prob = 0
        v = 0
        for value in var.values:
            vp = self.MarginalInference_Event(var, value)
            
            if prob < vp:
                prob = vp
                v = value
                
        return (v, prob)
    
    def CondInference_Event(self, hypotesis: Var, event: int, observations: set, values: list) -> float:
        """Método para hacer la consulta de inferencia de un evento condicional dada las observaciones.

        Args:
            hypotesis (Var): Variable de hipótesis.
            event (int): Valor de la hipótesis.
            observations (set): Conjunto de varibales observadas.
            values (list): Valores de las observaciones, 
                el orden debe de ser el mismo que el del argumento observations.

        Returns:
            float: Valor de probabilidad.
        """
        # Calcular el denominador
        den = 0
        # Establecer las observaciones
        i = 0
        for o in observations:
            o.SetInfer(values[i])
            i += 1
        
        # Calcular las combinaciones.
        for k in product(*self.jointDistrib.GetVars()):
            # Establecer los eventos.
            i = 0
            for e in self.jointDistrib.vars:
                e.SetEvent(k[i])
                i += 1
            
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            den += p
        
        # Calcular el numerador
        num = 0
        # Establecer la hipótesis
        hypotesis.SetInfer(event)
        
        # Calcular las combinaciones.
        for k in product(*self.jointDistrib.GetVars()):
            # Establecer los eventos.
            i = 0
            for e in self.jointDistrib.vars:
                e.SetEvent(k[i])
                i += 1
            
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            num += p
            
        self._ResetAllVars()
        return num / den
    
    def Cond_Obs(self, hypotesis: Var, observations: set, values: int) -> dict:
        """Método para hacer la consulta de inferencia de un evento condicional, 
            con todos los valores posibles de la hipótesis.

        Args:
            hypotesis (Var): Variable de hipótesis.
            observations (set): Conjunto de varibales observadas.
            values (list): Valores de las observaciones, 
                el orden debe de ser el mismo que el del argumento observations.
            
        Returns:
            dict: Diccionario de la probabilidades de las hipótesis.
        """
        dH_O = {}
        for e in hypotesis.values:
            dH_O[e] = self.CondInference_Event(hypotesis, e, observations, values)
        return dH_O

    def Cond_Dist(self, hypotesis: Var, observations: set) -> CondDistrib:
        """Método para hacer la consulta de inferencia de los eventos, 
            con todos los valores posibles de las observaciones.

        Args:
            hypotesis (Var): Variable de hipótesis.
            observations (set): Conjunto de varibales observadas.
            
        Returns:
            CondDistrib: Distribución condicional inferida.
        """
        dH_O = {}
        obs = [e.values for e in observations]
        for values in product(*obs):
            dH_O[values] = self.Cond_Obs(hypotesis, observations, values)
        
        return CondDistrib(hypotesis, observations, dH_O)
    
    def Cond_inference(self, hypotesis: Var, observations: set, values: list):
        """ Método para hacer la consulta de inferencia de la hipótesis.

        Args:
            hypotesis (Var): Variable de hipótesis.
            observations (set): Conjunto de varibales observadas.
            values (list): Valores de las observaciones, 
                el orden debe de ser el mismo que el del argumento observations.
            
        Returns:
            dict: Diccionario de la probabilidades de las hipótesis.
        """
        
        prob = 0
        for value in hypotesis.values:
            vp = self.CondInference_Event(hypotesis, value, observations, values)
            
            if prob < vp:
                prob = vp
                v = value
                
        return (v, prob)
    
    def JointInference_Evets(self, vars: set, values: list) -> float:
        """ Método para hacer la consulta de inferencia de un evento.

        Args:
            vars (set): Variebles de los evento para inferir.
            value (int): Valores de los evento para inferir.
            
        Returns:
            float: Valor de probabilidad de los evento.
        """
        
        # Estables los eventos
        i = 0
        for var in vars:
            var.SetInfer(values[i])
            i += 1
            
        sum = 0
        for k in product(*self.jointDistrib.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for e in self.jointDistrib.vars:
                e.SetEvent(k[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            
            sum += p
            
        self._ResetAllVars()
        return sum
    
    def Joint_Distrib(self, vars: set) -> Distrib:
        """ Método para hacer la consulta de inferencia de una distribución conjunta.

        Args:
            var (Var): Variable para inferir la probabiliodad de los eventos de la distribución.

        Returns:
            Distrib: Dsitribución conjunta inferida.
        """
        probDict = {}
        values = [var.values for var in vars]
        
        for events in product(*values):
            probDict[events] = self.JointInference_Evets(vars, list(events))
        
        return Distrib(vars, probDict)

    def Joint_inference(self, vars: set) -> tuple:
        """ Método para inferir los valores de los eventos más probable de una distribución conjunta.

        Args:
            vars (set): Variables para inferir la probabiliodad de los eventos de la distribución.

        Returns:
            tuple (list, float): Valores de los eventos y su probabilidad.
        """
        
        prob = 0
        v = ()
        values = [var.values for var in vars]
        for value in product(*values):
            vp = self.JointInference_Evets(vars, value)
            
            if prob < vp:
                prob = vp
                v = value
                
        return (v, prob) 