#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.1
#python_version : 3.10.12
#==============================================================================
from itertools import product
import pandas as pd
    
class Var:
    """Clase para el manejo de las variables (establecer y manejar los eventos).
    Atributos:
        values (set): Conjunto, de enteros, que contiene los valores que representan un evento.
        value (any): Valor que representa un evento.   
        
    Var(set) -> Nuevo objeto var
    """
    def __init__(self, name, values:set) -> None:
        self.name = name
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
    
    def getEvent(self) -> tuple:
        """Método para obtener el nombre y valor del evento de la variable.

        Returns:
            tuple: Tupla donde el primer elemento corresponde al nombre de la variable y
            el segundo elemento al valor del evento establecido.
        """
        return (self.name, self.event)
    
    def clear(self) -> None:
        self.event = None
        self.know = False

class Distrib:
    """ Clase para el manejo de distibuciones marginales.
    Atributos:
        vars (set): Conjunto de varibales para la distribución (tipo vars).
        table (DataFrame): DataFrame con la tabla de probabilidad.
    
    Distrib(set,DataFrame) -> nuevo objeto Distrib.
    """
    def __init__(self, vars: set, table: pd.DataFrame) -> None:
        self.vars = vars
        self.table = table
    
    def P(self) -> float:
        """Método para regresar el valor de probabilidad de los valores establecidos a los 
        eventos de las variables.
        """
        conds = []
        for v in self.vars:
            conds.append(self.table[v.name] == v.event)
            
        filt = conds[0]
        for cond in conds[1:]:
            filt &= cond
            
        return self.table.loc[filt, 'probability'].iloc[0]

class CondDistrib(Distrib):
    def __init__(self, vars: set, indep: set, table: pd.DataFrame) -> None:
        super().__init__(vars, table)
        self.indep = indep
    
    def P(self):
        """Método para regresar el valor de probabilidad de los valores establecidos a los 
        eventos de las variables.
        """
        conds = []
        t_vars = self.vars | self.indep
        for v in t_vars:
            conds.append(self.table[v.name] == v.event)
            
        filt = conds[0]
        for cond in conds[1:]:
            filt &= cond
            
        return self.table.loc[filt, 'probability'].iloc[0]

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
        vrs = []
        for e in self.vars:
            vrs.append(e.getValues())
        return vrs
    
class Mib:
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            model (Specification): Especificación de un programa Bayesiano del problema 
            con su distribución conjunta y su descomposción.
    """
    def __init__(self, model: Specification) -> None:
        self.model = model
    
    def _ResetAllVars(self) -> None:
        for v in self.model.vars:
            v.clear()
    
    def marginal(self, vars: zip) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            vars (zip): Conjunto de variables para la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        
        for v,e in vars:
            v.setMarginal(e)
            
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
    
    def cond(self, varsn:zip, varsd:zip) -> float:
        """ Método para hacer la consulta de una distribución conjunta.

        Args:
            varsn (zip): Conjunto de variables.
            varsd (zip): Conjunto de variables para la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        # Calcular el denominador
        den = self.marginal(varsn)
        
        # Calcular el numerados
        num = self.marginal(varsd)
        
        return num / den
    
    def marginalDistrib(self, vars:set) -> Distrib:
        """ Método para hacer la consulta de una distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.

        Returns:
            Distrib: Dsitribución marginal calculada.
        """
        cols = [v.name for v in vars] + ['probability']
        pEvents = [v.values for v in vars]
        
        rows = []
        for events in product(*pEvents):
            p = self.marginal(zip(vars, events))
            values = list(events)
            values.append(p)
            rows.append(values)
        
        return Distrib(vars, pd.DataFrame(rows, columns=cols))
    
    def condDistrib(self, vars:set, indep:set) -> CondDistrib:
        """ Método para hacer la consulta de una distribución condicional.

        Args:
            vars (set): Conjunto de variables para la distribución.
            indep (set): Conjunto de variables independientes para la distribución.

        Returns:
            CondDistrib: Dsitribución condicional calculada.
        """
        cols = [v.name for v in vars] + [v.name for v in indep] + ['probability']
        vars_e = [v.values for v in vars]
        indep_e = [v.values for v in indep]
        
        rows = []
        for ve in product(*vars_e):
            for vi in product(*indep_e):
                lve = list(ve)
                lvi = list(vi)
                p = self.cond(zip(vars | indep,  lve + lvi), zip(indep, lvi))
                values = lve + lvi
                values.append(p)
                rows.append(values)
        
        return CondDistrib(vars, indep, pd.DataFrame(rows, columns=cols))







def ejemplo():
    vA = set([0,1])
    vB = set([0,1])
    A = Var('A',vA)
    B = Var('B',vB)
    C = Var('C',vB)
    
    
    col = [A.name, B.name, 'probability']
    tAB = [
        [0,0, 1 / (len(vA) * len(vB))],
        [0,1, 1 / (len(vA) * len(vB))],
        [1,0, 1 / (len(vA) * len(vB))],
        [1,1, 1 / (len(vA) * len(vB))]
    ]
    dAB = pd.DataFrame(tAB, columns=col)
    PAB = Distrib(set([A,B]),dAB)
    
    
    PA_C = CondDistrib(set([A]),set([C]),pd.DataFrame(tAB, columns=[A.name, C.name, 'probability']))
    
    PABC = Specification(set([A,B,C]), set([PAB, PA_C]))
    mib = Mib(PABC)
    
    print(mib.marginalDistrib(set([A])).table)
    print(mib.condDistrib(set([A]), set([B])).table)

ejemplo()

            
