#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2
#python_version : 3.10.12
#==============================================================================
from itertools import product

class Var:
    """Clase para el manejo de eventos.
        Atributos:
            values (set): Lista que contiene los valores que representan un suceso.
            value: Vlaor que representa un suceso.
            infer (set): Auxiliar para guardar temporalmente los valores del evento
            durante la inferencia.
    """
    def __init__(self, values: set) -> None:
        self.values = values
        self.event = None
        self.infer = None
    
    def SetValue(self, value) -> None:
        """ Método para establecer un suceso.

        Args:
            value: Valor que representa un suceso. 
        """
        self.event = value
    
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
    def __init__(self, event: Var, table: dict) -> None:
        self.event = event
        self.table = table
        
    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer el suceso de event.

        Returns:
            float: Probabilidad del suceso establecido.
        """
        return self.table[self.event.event]
        
class CondDistrib:
    """ Clase para el manejo de distibuciones condicionales.

        Atributos:
            event (Event): Objeto que guarda el evento dependiente.
            indep (list): Lista de objetos tipo Event que guarda los eventos independientes. 
                La llave priemro es la tupla de los valores de los eventos independiante
                y luego la llave para el evento dependiente, ej.: {(0,1):{0:.5,1:.5}}.
    """
    def __init__(self, var: Var, indep: set, table: dict) -> None:
        self.event = var
        self.indep = indep
        self.table = table

    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer 
        los sucesos de event y de indep.

        Returns:
            float: Probabilidad de los sucesos establecido.
        """
        indep_key = [e.value for e in self.indep]
        return self.table[tuple(indep_key)][self.var.event]
        
class JointDistrib:
    """ Clase para manejar la probabilidad conjunta y también
        el manejo del modelado de un problema de inferencia.
        
        Atributos:
            events (set): Lista de eventos de la conjunta.
            descomp (set): Lista que guarda las distribuciones 
            que generan el modelo de un problema.
    """
    def __init__(self, events: set, descomp: set) -> None:
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
    
    def MarginalInference_Distrib(self, var: Var) -> Distrib:
        """ Método para hacer la consulta de inferencia de una distribución marginal.

        Args:
            var (Var): Variable para inferir la probabiliodad de los eventos de la distribución.

        Returns:
            Distrib: Dsitribución marginal de la inferencia de event.
        """
        probDict = {}
        events = var.values.copy()
        
        for value in events:
            sum = 0
            var.SetInfer(value)
            
            for k in product(*self.jointDistrib.GetVars()):
                i = 0
                for e in self.jointDistrib.events:
                    e.SetValue(k[i])
                    i += 1
                
                p = 1
                for d in self.jointDistrib.descomp:
                    p *= d._GetP()

                sum += p
                
            probDict[value] = sum
        
        var.Reset()
        return Distrib(var, probDict)
    
    def MarginalInference_Event(self, var: Var, event: int) -> float:
        """ Método para hacer la consulta de inferencia de un evento.

        Args:
            var (Var): Vriable con los eventos de la distribución.
            value : Valor del evento para inferir.
            
        Returns:
            Distrib: Dsitribución marginal de la inferencia de event.
        """
        sum = 0
        var.SetInfer(event)
        
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

    def CondInference_Distrib(self, hypothesis: Var, observations: set, obsValues: list) -> CondDistrib:
        """_summary_

        Args: 
            hypothesis (Var): Varibale para los eventos de la hipotesis.
            observations (set): Conjubto de varibales para las observaicones.
            
        Returns:
            CondDistrib: Distribución de la probabilidad condicional consultada.
        """
        probDict = {}
        events = hypothesis.values.copy()
        
        # Establecer los eventos a las obsevaciones.
        for obs in observations:
                obs.SetInfer(obsValues[i])
                i += 1
        
        for value in events:
            # Calcular denominador
            
            # Establecer los eventos a la hipótesis.
            hypothesis.SetInfer(value)
            i = 0
            
            den = 0
            for k in product(*self.jointDistrib.GetVars()):
                j = 0
                for e in self.jointDistrib.events:
                    e.SetValue(k[i])
                    j += 1
                
                p = 1
                for d in self.jointDistrib.descomp:
                    p *= d._GetP()
                den += p
                
            hypothesis.Reset()  
            
            # Calcular numerador
            num = 0
            for k in product(*self.jointDistrib.GetVars()):
                j = 0
                for e in self.jointDistrib.events:
                    e.SetValue(k[i])
                    j += 1
                
                p = 1
                for d in self.jointDistrib.descomp:
                    p *= d._GetP()
                num += p
                
            probDict()
            
        # Establecer los eventos a las obsevaciones.
        for obs in observations:
                obs.Reset()
                
        return CondDistrib(hypothesis, )
            
    
    def CondInference_Event(self, hypothesis: int, observations: set) -> CondDistrib:
        """_summary_

        Returns:
            CondDistrib: _description_
        """
        
def ejemplo_prueba():
    A = Var(set([0,1]))
    B = Var(set([0,1]))
    C = Var(set([0,1,2]))
    
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