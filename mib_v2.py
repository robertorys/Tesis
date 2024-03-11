#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2
#python_version : 3.10.12
#==============================================================================

from itertools import product

class Event:
    def __init__(self, values: list) -> None:
        self.values = values
        self.value = None
        self.infer = None
    
    def SetValue(self, value: int) -> None:
        self.value = value
    
    def SetInfer(self, value: int) -> None:
        self.infer = self.values
        self.values = [value]
    
    def Reset(self) -> None:
        self.values = self.infer
        self.infer = None
        
class Distrib:
    def __init__(self, event: Event, table: dict) -> None:
        self.event = event
        self.table = table
        
    def _GetP(self) -> float:
        return self.table[self.event.value]
        
class CondDistrib:
    def __init__(self, event: Event, indep: list, table: dict) -> None:
        self.event = event
        self.indep = indep
        self.table = table

    def _GetP(self) -> float:
        indep_key = [e.value for e in self.indep]
        return self.table[tuple(indep_key)][self.event.value]
        
class JointDistrib:
    def __init__(self, events: list, descomp: list) -> None:
        self.events = events
        self.descomp = descomp
        
    def GetVars(self) -> list:
        vars = []
        for e in self.events:
            vars.append(e.values)
        return vars
    
class Mib:
    def __init__(self, model: JointDistrib) -> None:
        self.jointDistrib = model
    
    def MarginalInference(self, event: Event) -> Distrib:
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

def ejemplo_prueba():
    A = Event([0,1])
    B = Event([0,1])
    C = Event([0,1,2])
    
    dA = {0:0.3,1:0.7}
    PA = Distrib(A, dA)

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
    PB = mib.MarginalInference(B)
    
    print(PB.table)
    
    
ejemplo_prueba()