#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2
#python_version : 3.10.12
#==============================================================================
from itertools import product

class Event:
    """Clase para el manejo de eventos.
        Atributos:
            values (list): Lista que contiene los valores que representan un suceso.
            value: Vlaor que representa un suceso.
            infer (list): Auxiliar para guardar temporalmente los valores del evento
            durante la inferencia.
    """
    def __init__(self, values: list) -> None:
        self.values = values
        self.value = None
        self.infer = None
    
    def SetValue(self, value) -> None:
        """ Método para establecer un suceso.

        Args:
            value: Valor que representa un suceso. 
        """
        self.value = value
    
    def SetInfer(self, value) -> None:
        """ Método para establecer un seceso para inferir.

        Args:
            value: Valor que representa un suceso. 
        """
        self.infer = self.values
        self.values = [value]
    
    def Reset(self) -> None:
        """ Método para restablecer los atrubutos del objeto después de la inferencia.
        """
        self.values = self.infer
        self.infer = None
        
class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    
        Atributos:
            event (Evente): Objeto que guarda el evento de la distribución.
            table (dict): Dicciónario que guarda las probabilidades (key: probability).
    """
    def __init__(self, event: Event, table: dict) -> None:
        self.event = event
        self.table = table
        
    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer el suceso de event.

        Returns:
            float: Probabilidad del suceso establecido.
        """
        return self.table[self.event.value]
        
class CondDistrib:
    """ Clase para el manejo de distibuciones condicionales.

        Atributos:
            event (Event): Objeto que guarda el evento dependiente.
            indep (list): Lista de objetos tipo Event que guarda los eventos independientes. 
                La llave priemro es la tupla de los valores de los eventos independiante
                y luego la llave para el evento dependiente, ej.: {(0,1):{0:.5,1:.5}}.
    """
    def __init__(self, event: Event, indep: list, table: dict) -> None:
        self.event = event
        self.indep = indep
        self.table = table

    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer 
        los sucesos de event y de indep.

        Returns:
            float: Probabilidad de los sucesos establecido.
        """
        indep_key = [e.value for e in self.indep]
        return self.table[tuple(indep_key)][self.event.value]
        
class JointDistrib:
    """ Clase para manejar la probabilidad conjunta y también
        el manejo del modelado de un problema de inferencia.
        
        Atributos:
            events (list): Lista de eventos de la conjunta.
            descomp (list): Lista que guarda las distribuciones 
            que generan el modelo de un problema.
    """
    def __init__(self, events: list, descomp: list) -> None:
        self.events = events
        self.descomp = descomp
        
    def GetVars(self) -> list:
        """ Método para obtener todas los sucecsos de los eventos de la conjunta.

        Returns:
            list: Lista que gurda la lista de valores de cada evento.
        """
        vars = []
        for e in self.events:
            vars.append(e.values)
        return vars
    
class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            jointDistrib (JointDistrib): Objeto que guarda la distribución conjunta y
            su descomposición de distribuciones.
    """
    def __init__(self, model: JointDistrib) -> None:
        self.jointDistrib = model
    
    def MarginalInferenceDistrib(self, event: Event) -> Distrib:
        """ Método para hacer la consulta de inferencia de una distribución.

        Args:
            event (Event): Evento para inferir la distribución.

        Returns:
            Distrib: Dsitribución marginal de la inferencia de event.
        """
        margDict = {}
        values = event.values.copy()
        
        for value in values:
            sum = 0
            event.SetInfer(value)
            
            for k in product(*self.jointDistrib.GetVars()):
                i = 0
                p = 1
                
                for e in self.jointDistrib.events:
                    e.SetValue(k[i])
                    i += 1
                
                for d in self.jointDistrib.descomp:
                    p *= d._GetP()

                sum += p
                
            margDict[value] = sum
        
        event.Reset()
        return Distrib(event, margDict)
    
    def MarginalInferenceEvent(self, event: Event, value) -> float:
        """ Método para hacer la consulta de inferencia de un evento.

        Args:
            event (Event): Evento de la distribución.
            value : Valor del suceso para inferir.
            
        Returns:
            Distrib: Dsitribución marginal de la inferencia de event.
        """
        sum = 0
        event.SetInfer(value)
        
        for k in product(*self.jointDistrib.GetVars()):
            i = 0
            p = 1
            
            for e in self.jointDistrib.events:
                e.SetValue(k[i])
                i += 1
            
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            
            sum += p
        
        return sum
        
def ejemplo_prueba():
    A = Event([0,1])
    B = Event([0,1])
    C = Event([0,1,2])
    
    dA = {0:0.3,1:0.7}
    PA = Distrib(A,dA)

    dB_A = {(0,):{0:.2,1:.8},(1,):{0:.3,1:.7}}
    PB_A = CondDistrib(B,[A],dB_A)
    
    dC_AB = {
        (0,0): {0: 0.1, 1: 0.8, 2: 0.1},
        (0,1): {0: 0.3, 1: 0.5, 2:0.2},
        (1,0): {0: 0.4, 1: 0.5, 2: 0.1},
        (1,1): {0: 0.2, 1: 0.7, 2: 0.2}
    }
    
    PC_AB = CondDistrib(C,[A,B],dC_AB)
    
    PABC = JointDistrib([A,B,C], [PA, PB_A, PC_AB])
    
    mib = Mib(PABC)
    
    PB = mib.MarginalInferenceDistrib(B)
    print(PB.table)
    
    print(mib.MarginalInferenceEvent(B, 0))
    
    
ejemplo_prueba()