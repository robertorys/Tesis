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
        value: Vlaor que representa un evento.
    """
    
    def __init__(self, values: set) -> None:
        self.values = values
        self.event = None
        
        '''infer (set): Auxiliar para guardar temporalmente los valores de los eventos.
            durante la inferencia.'''
        self.infer = None
        
    def SetValue(self, value: int) -> None:
        """ Método para establecer un evento.

        Args:
            value (int): Valor que representa un suceso. 
        """
        self.event = value
    
    def SetEvent(self, value: int) -> None:
        """ Método para establecer un evento a inferir.

        Args:
            value (int): Valor que representa un suceso. 
        """
        
        self.infer = self.values.copy()
        self.values = set([value])
    
    def Reset(self) -> None:
        """ Método para restablecer los atributos del objeto después de la inferencia.
        """
        if self.infer:
            self.values = self.infer
            self.infer = None
        self.event = None
    
class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    
    Atributos:
        var (Var): Objeto de los eventos de la distribución.
        table (dict): Dicciónario de las probabilidades (key (int): probability).
    """
    def __init__(self, var: Var, table: dict) -> None:
        self.event = var
        self.table = table
        
    def _GetP(self) -> float:
        """ Método para obtener la probabilidad después de establecer el un evento.

        Returns:
            float: Probabilidad del evento establecido.
        """
        return self.table[self.event.event]

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
            float: Probabilidad de los sucesos establecido.
        """
        indep_key = [e.event for e in self.indep]
        return self.table[tuple(indep_key)][self.var.event]

class JointDistrib:
    """ Clase para manejar la probabilidad conjunta y 
        el manejo del modelado de un problema para inferir alguna distribución de probabilidad.
        
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
            vars.append(list(e.values))
        return vars

class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            jointDistrib (JointDistrib): Distribución conjunta con el modelo del problema.
    """
    def __init__(self, model: JointDistrib) -> None:
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
        var.SetEvent(event)
        for k in product(*self.jointDistrib.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for e in self.jointDistrib.vars:
                e.SetValue(k[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            
            sum += p
            
        
        return sum

    def MarginalInference_Distrib(self, var: Var) -> Distrib:
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
    
    def CondInference_Event(self, hypothesis: Var, event: int, observations: set, observationValues: list, iterable: bool = False) -> float:
        """ Método para hacer la consulta de inferencia de un evento (hipótesis) dada las observaciones.
            Inferir probabilidad condicional de un evento.
        
        Args:
            hypothesis (Var): Variable de la hipótesis.
            event (int): Valor de la hipótesis.
            observations (set): Conjunto de varibales observadas.
            observationValues (list): Liste de enteros de los valores de las observaciones (mismo orden que las observaciones).

        Returns:
            float: Valor de probabilidad del evento dada las observaciones.
        """
        
        # Establecer los eventos de las observaciones.
        i = 0
        for o in observations:
            o.SetEvent(observationValues[i])
            i += 1
        
        # Calcular el denominador
        den = 0
        
        for k in product(*self.jointDistrib.GetVars()):
            
            # Establecer los valores de los eventos.
            j = 0
            for e in self.jointDistrib.vars:
                e.SetValue(k[j])
                j += 1
            
            # Calcular la probailidad con los valores de k.
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            
            den += p
        
        # Calcular el numerador
        num = 0
        # Establecer el evento de la hipótesis.
        hypothesis.SetEvent(event)
    
        for k in product(*self.jointDistrib.GetVars()):
            # Establecer los valores de los eventos.
            j = 0
            for e in self.jointDistrib.vars:
                e.SetValue(k[j])
                j += 1
            
            # Calcular la probailidad con los valores de k.
            p = 1
            for d in self.jointDistrib.descomp:
                p *= d._GetP()
            
            num += p  
            
        if iterable:
            self._ResetAllVars()
        
        return num / den

    def CondInference(self, hypothesis: Var, observations: set, observationValues: list) -> dict:
        """ Método para hacer la consulta de inferencia de una distribución condicional dada observaciones.

        Args:
            hypothesis (Var): Variable para inferir la probabiliodad de los eventos de la distribución.
            observations (set): Conjunto de variables observadas.
            observationValues (list): Lista de los eventos dados de las variables.

        Returns:
            dict: Diccionario con las probabilidades de las diferentes hipótesis.
        """
        probDict = {}
        events = hypothesis.values.copy()
        for event in events:
            probDict[event] = self.CondInference_Event(hypothesis, event, observations, observationValues, True)
        self._ResetAllVars()
        return probDict
    
    def CondInference_Distrb(self, hypothesis: Var, observations: set) -> CondDistrib:
        """ Método para hacer la consulta de inferencia de una distribución condicional.

        Args:
            hypothesis (Var): Variable para inferir la probabiliodad de los eventos de la distribución.
            observations (set): Conjunto de variables observadas.

        Returns:
            dict: Diccionario con las probabilidades de las diferentes hipótesis.
        """
        probDict = {}
        oList = [o.values for o in observations]
        
        for oValues in product(*oList):
            probDict[oValues] = self.CondInference(hypothesis, observations, oValues)
            
        return CondDistrib(hypothesis, observations, probDict)
    
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
    
    ''' 
    PB = mib.MarginalInference_Distrib(B)
    print(PB.table)
    
    print(mib.MarginalInference_Event(B, 0))
    '''
    
    PA_BC = mib.CondInference_Distrb(A, set([B,C]))
    print(PA_BC.table)
    
    
ejemplo_prueba()