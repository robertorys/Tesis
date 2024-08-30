#==============================================================================
#title          : mib_v2.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.1
#python_version : 3.10.12
#==============================================================================
from itertools import product
import pandas as pd
import time

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
        self.namesToVar = self._namesToVar()
        
    def _namesToVar(self) -> dict:
        ntv = {}
        for v in self.vars:
            ntv[v.name] = v
    
        
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
        n_vars = [v for v in self.vars] + [v for v in self.indep]
        for v in n_vars:
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
    
    def marginal(self, vars: set, values: list) -> float:
        self.times = []
        """ Método para hacer la consulta de una marginal.

        Args:
            vars (zip): Conjunto de variables para la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        
        i = 0
        for v in vars:
            v.setMarginal(values[i])
            i += 1 
            
        for k in product(*self.model.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for v in self.model.vars:
                v.event = k[i]
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self.model.descomp:
                inicio = time.time()
                p *= d.P()
                fin = time.time()
                self.times.append(fin - inicio)
            sum += p
        
        self._ResetAllVars()
        return sum
    
    def cond(self, vars:set, vars_values:list, indep:set, indep_values:list) -> float:
        """ Método para hacer la consulta de una distribución conjunta.

        Args:
            varsn (zip): Conjunto de variables.
            varsd (zip): Conjunto de variables para la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        # Calcular el denominador
        den = self.marginal(indep, indep_values)
        
        # Calcular el numerados
        num = 0
        
        for i,v in enumerate(vars):
            v.setMarginal(vars_values[i])
        for i,v in enumerate(indep):
            v.setMarginal(indep_values[i])
            
        for k in product(*self.model.GetVars()):
            # Establecer los valores de los eventos.
            i = 0
            for v in self.model.vars:
                v.event = k[i]
                i += 1
            
            # Calcutimes[-1]lar la probabilidad con los valores de k.
            p = 1
            for d in self.model.descomp:
                p *= d.P()
            
            num += p
        
        self._ResetAllVars()
        
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
            p = self.marginal(vars, list(events))
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
        vars_v = [v.values for v in vars]
        indep_i = [v.values for v in indep]
        
        rows = []
        for vv in product(*vars_v):
            for vi in product(*indep_i):
                lvv = list(vv)
                lvi = list(vi)
                p = self.cond(vars, lvv, indep, lvi)
                values = lvv + lvi
                values.append(p)
                rows.append(values)
        
        return CondDistrib(vars, indep, pd.DataFrame(rows, columns=cols))
    
    def marginal_inference(self, vars:set) -> pd.DataFrame:
        """ Método para consultar el mayor valor de la distribución de la conjunta de vars.

        Args:
            vars (set): Conjunto de variables para la distribución.

        Returns:
            DataFrame: DataFrame con el valor más probable.
        """
        cols = [v.name for v in vars]  + ['probability']
        pValues = [v.values for v in vars]
        
        p = 0
        values = None
        for value in product(*pValues):
            pv = self.marginal(vars, list(value))
            
            if pv > p:
                p = pv
                values = list(value)
        
        values.append(p)
        return pd.DataFrame([values], columns=cols)

    def cond_inference_obs(self, vars:set, indep:set, obs:list) -> pd.DataFrame:
        """  Método para consultar el mayor valor de distribución condicional dada las observaciones.

        Args:
            vars (set): Conjunto de variables para la distribución.
            indep (set): Conjunto de variables independientes para la distribución.

        Returns:
            CondDistrib: Dsitribución condicional calculada.
        """
        cols = [v.name for v in vars] + [v.name for v in indep] + ['probability']
        vars_v = [v.values for v in vars]
        
        p = 0
        values = None
        for vv in product(*vars_v):
            lvv = list(vv)  
            pv = self.cond(vars, lvv, indep, obs)
            
            if pv > p:
                p = pv
                values = lvv + obs
                
        values.append(p)
        return pd.DataFrame([values], columns=cols)
    
    def cond_inference_hyp(self, vars:set, hyp:list, indep:set) -> pd.DataFrame:
        """  Método para consultar el mayor valor de distribución condicional dada las hipótesis.

        Args:
            vars (set): Conjunto de variables para la distribución.
            indep (set): Conjunto de variables independientes para la distribución.

        Returns:
            CondDistrib: Dsitribución condicional calculada.
        """
        cols = [v.name for v in vars] + [v.name for v in indep] + ['probability']
        vars_v = [v.values for v in vars]
        indep_i = [v.values for v in indep]
        
        p = 0
        values = None
        for vi in product(*indep_i):
            lvi = list(vi)
            pv = self.cond(vars, hyp, indep, lvi)
            
            if pv > p:
                p = pv
                values = hyp + lvi
            
        values.append(p)
        
        return pd.DataFrame([values], columns=cols)

class Question:
    def __init__(self, sp: Specification) -> None:
        self.mib = Mib(sp)
    
    def DistributionQuery(self, vars:set, indep:set = None):
        if not indep:
            return self.mib.marginalDistrib(vars)
        else:
            return self.mib.condDistrib(vars, indep)
        
    def Query(self, vars:set, indep:set = None, values:list = None, obs:list = None):
        if not indep:
            if values:
                return self.mib.marginal(vars, values)
            else:
                return self.mib.marginal_inference(vars)
        else:
            if obs and not values:
                return self.mib.cond_inference_obs(vars, indep, obs)
            elif not obs and values:
                return self.mib.cond_inference_hyp(vars, values, indep)
            
        print("Consulta no valida")

        