#==============================================================================
#title          : mib_v2_3.py
#description    : Motor de inferencia bayesiano para variables discretas.
#version        : 2.1
#python_version : 3.10.12
#==============================================================================
from itertools import product
import math
import multiprocessing as mp
import copy
import math

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
    
    def getCard(self) -> int:
        if self._know:
            return len([self._event])
        else:
            return len(self._values)
        
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
        table (dict): Dicciónario de las probabilidades (tuple: float).
        columns (tuple): Tupla con el orden de los nombres de las variables del diccionario.
    
    Distrib(dict,tuple) -> nuevo objeto Distrib
    """
    def __init__(self, table: dict, columns:tuple) -> None:
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
        table (dict): Dicciónario de las probabilidades ((tuple,tuple): float),
            donde la primera tupla representa la llave para los valores de indep y la segunda para vars.
        columns_vars (tuple): Lista con el orden de los nombres de las variables dependientes para el diccionario.
        columns_indep (tuple): Lista con el orden de los nombres de las variables independientes para el diccionario.
    
    Distrib(dict,tuple,tuple) -> nuevo objeto Distrib
    """
    def __init__(self, table: dict, columns_vars: tuple, columns_indep: tuple) -> None:
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
        
    def getValues(self) -> list:
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
        
        for k in product(*self._model.getValues()):
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
    
    def joint_marginal(self, vars1_columns:tuple, vars1_values:list, vars2_columns:tuple, vars2_values:list) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1_columns (tuple): Tupla de los nombres de las variables del primer conjunto de variables.
            vars1_values (list): _description_
            vars2_columns (tuple): Tupla de los nombres de las variables del segundo conjunto de variables.
            vars2_values (list): _description_

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        
        for i,name in enumerate(vars1_columns):
            self._nameToVar[name].setMarginal(vars1_values[i])
        for i,name in enumerate(vars2_columns):
            self._nameToVar[name].setMarginal(vars2_values[i])
        
        for k in product(*self._model.getValues()):
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

    def cond(self, vars_names:tuple, vars_values:list, indep_names:tuple, indep_values:list) -> float:
        """ Método para hacer la consulta de una distribución conjunta.

        Args:
            vars_names (tuple): Tupla de los nombres de las variables de vars.
            vars_values (list): Lista de los valores para las variables de vars.
            indep_names (tuple): Tupla de los nombres de las variables de indep.
            indep_values (list): Lista de los valores para las variables de indep.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        # Calcular el numerados
        num = self.joint_marginal(vars_names, vars_values, indep_names, indep_values)
        
        # Calcular el denominador
        den = self.marginal(indep_names, list(indep_values))
        
        return num / den
    
    def Distrib_inference(self, vars:set) -> Distrib:
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
            
        return Distrib(table, columns)

    def condDistrib_inference(self, vars:set, indep:set) -> CondDistrib:
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
                
        return CondDistrib(table, columns_vars, columns_indep)
    
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

    def condObs_inference(self, vars:tuple, vars_values:tuple, indep:tuple) -> tuple:
        """ Método para inferir el valor más probable de una obersvación de una distribución condicional
        dado los valores de las hipótesis.

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
            p_vv = self.joint_marginal(columns_vars, vars_values, columns_indep, vi)
        
            if p == 0:
                p = p_vv
                value_indep = vi
            else: 
                if p_vv / p > 1:
                    p = p_vv
                    value_indep = vi
                
        return columns_indep, value_indep, p
    
    def condHyp_inference(self, vars:tuple, indep:tuple, indep_values:tuple) -> tuple:
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
        columns_vars = tuple([v.getName() for v in vars])
        columns_indep = tuple([v.getName() for v in indep])
        
        values_vars = [v.getValues() for v in vars]
        
        p = 0
        value_vars = None
        for vv in product(*values_vars):
            
            p_vi = self.joint_marginal(columns_vars, vv, columns_indep, indep_values)
            
            if p == 0:
                p = p_vi
                value_vars = vv
            else: 
                if p_vi / p > 1:
                    p = p_vi
                    value_vars = vv
                               
        return columns_vars, value_vars, p
    
    def joint_inference(self, vars:tuple, vars_values:tuple, vars_:tuple) -> tuple:
        """ Método para inferir el valor más probable de distribución conjunta dado los valores de algunas variables.

        Args:
            vars (tuple): Tupla de las variables de la distribución conjunta sin las variables a buscas.
            vars_values (tuple):Tupla con los valores de las variables de la distribución condicconjuntaional.
            vars_ (tuple): Tupla de las variables a buscar.
        Returns:
            tuple ((tuple, tuple, tuple, tuple, float)): El primer elemento es la tupla de nombres de vars, el segundo elemento es la tupla que representa sus valores, 
            y el último elemento es la probabilidad.
        """
        columns_vars = tuple([v.getName() for v in vars] + [v.getName() for v in vars_])
        
        values_vars = [v.getValues() for v in vars_]
        
        p = 0
        value_vars = None
        for vv in product(*values_vars):
            
            p_vi = self.marginal(columns_vars, tuple(list(vars_values) + list(vv)))
            
            if p == 0:
                p = p_vi
                value_vars = vv
            else: 
                if p_vi / p > 1:
                    p = p_vi
                    value_vars = vv
                               
        return columns_vars, vars_values+value_vars, p

class Mib_mp:
    """ Clase para el motor de inferencia bayesiana usando paralelismo.

        Atributos:
            model (Model): Modelo del problema con su distribución conjunta y su descomposción.
    """
    def __init__(self, sp: Specification) -> None:
        self._model = sp
        self._nameToVar = {}
        
        for v in self._model.getVars():
            self._nameToVar[v.getName()] = v
    
    def _ResetAllVars(self) -> None:
        for v in self._model.getVars():
            v.clear()
    
    def multip_m(self, keys:list, vars:list, descomp:set , nameToVar, _:mp.Queue):
        sum = 0
        for key in keys:
            i = 0
            for v in vars:
                v.setEvent(key[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in descomp:
                p *= d.P(nameToVar)
                
            sum += p
        _.put(sum)
        
    def inference_mp(self, lote_n:int, thread_n:int) -> float:
        # Crear una cola para comunicar los hilos
        resultado_cola = mp.Queue()
        
        sum = 0
            
        keys = []
        count_lote = 0
        
        product_cc = 1
        for v in self._model.getVars():
            product_cc *= v.getCard()
        
        hilos = []
        
        for k in product(*self._model.getValues()):
            
            if count_lote < lote_n:
                keys.append(k)
                product_cc -= 1
                count_lote += 1
                
            if product_cc == 0 or count_lote == lote_n:
                if len(hilos) < thread_n:
                    count_lote = 0
                    
                    vars_copy = [copy.deepcopy(v) for v in self._model.getVars()]
                    nameToVar = {}
                    for v in vars_copy:
                        nameToVar[v.getName()] = v
                        
                    hilo =  mp.Process(
                        target = self.multip_m,
                        args = (
                            keys.copy(), 
                            vars_copy.copy(), 
                            self._model.getDescomp(), 
                            nameToVar.copy(),
                            resultado_cola
                            )
                    )
                    
                    hilos.append(hilo)
                    keys.clear()
                    nameToVar.clear()
                
                if len(hilos) == thread_n or product_cc == 0:
                    for hilo in hilos:
                        hilo.start()
                        
                    for hilo in hilos:
                        hilo.join()
                    
                    hilos.clear()
                    
        # Obtener los resultados desde la cola
        while not resultado_cola.empty():
            sum += resultado_cola.get()
                
        return sum
    
    def marginal_mp(self, vars_names:tuple, vars_values:tuple, lote_n:int, thread_n:int) -> float:
        """ Método para hacer la consulta de una distribución.

        Args:
            vars_names (tuple): Conjunto del nombre de las variables de vars.
            vars_values (tuple): Lista de los valores para las variables de vars.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        for i,name in enumerate(vars_names):
            self._nameToVar[name].setMarginal(vars_values[i])
            
        p = self.inference_mp(lote_n, thread_n)
        self._ResetAllVars()
        
        return p
        
    
    def joint_mp(self, vars1_names:tuple, vars1_values:tuple, vars2_names:tuple, vars2_values:tuple, lote_n:int, thread_n:int) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1_names (tuple): Tupla de los nombres de las variables del primer conjunto de variables.
            vars1_values (list): _description_
            vars2_names (tuple): Tupla de los nombres de las variables del segundo conjunto de variables.
            vars2_values (list): _description_

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        for i,name in enumerate(vars1_names):
            self._nameToVar[name].setMarginal(vars1_values[i])
        for i,name in enumerate(vars2_names):
            self._nameToVar[name].setMarginal(vars2_values[i])
    
        p = self.inference_mp(lote_n, thread_n)
        self._ResetAllVars()
        return p
    
    def cond_mp(self, vars_names:tuple, vars_values:tuple, indep_names:tuple, indep_values:tuple, lote_n, thread_n) -> float:
        """ Método para hacer la consulta de una distribución condicional.

        Args:
            vars_names (tuple): Conjunto del nombre de las variables de vars.
            vars_values (tuple): Lista de los valores para las variables de vars.
            indep_names (tuple): Conjunto del nombre de las variables de indep.
            indep_values (tuple): Lista de los valores para las variables de indep.
            
        Returns:
            float: Valor de la probabilidad de la condicional.
        """
        num = mp.Queue()
        den = mp.Queue()
        
        # Calcular el numerados
        def joint_mp_aux(vars_names, vars_values, indep_names, indep_values, lote_n, thread_n, queue):
            queue.put(self.joint_mp(vars_names, vars_values, indep_names, indep_values, lote_n, thread_n))
            
        processNum = mp.Process(
            target = joint_mp_aux, 
            args = (vars_names, vars_values, indep_names, indep_values, lote_n, thread_n, num)
        )
        
        # Calcular el denominador
        def marginal_mp_aux(indep_names, indep_values, lote_n, thread_n, queue):
            queue.put(self.marginal_mp(indep_names, indep_values, lote_n, thread_n))
        
        processDen = mp.Process(
            target = marginal_mp_aux, 
            args = (indep_names, indep_values, lote_n, thread_n, den)
        )
        
        processNum.start()
        processDen.start()
        
        processNum.join()
        processDen.join()
        
        return num.get() / den.get()
    
    def Distrib_inference_mp(self, vars:set, lote_n:int, thread_n:int) -> Distrib:
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
            table[value] = self.marginal_mp(columns, list(value), lote_n, thread_n)
            
        return Distrib(table, columns)
    
    def condDistrib_inference_mp(self, vars:set, indep:set, lote_n:int, thread_n:int) -> CondDistrib:
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
                table[vi][vv] = self.cond_mp(columns_vars, vv, columns_indep, vi, lote_n, thread_n)
                
        return CondDistrib(table, columns_vars, columns_indep)
    
    def marginal_inference_mp(self, vars:set, lote_n:int, thread_n:int) -> tuple:
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
            p_vv = self.marginal_mp(columns, list(vv), lote_n, thread_n)

            if p_vv > p:
                p = p_vv
                value = vv
        
        return columns, value, p
    
    def condObs_inference_mp(self, vars:tuple, vars_values:tuple, indep:tuple, lote_n, thread_n) -> tuple:
        """ Método para inferir el valor más probable de una obersvación de una distribución condicional
        dado los valores de las hipótesis.

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
            p_vv = self.joint_mp(columns_vars, vars_values, columns_indep, vi, lote_n, thread_n)
        
            if p == 0:
                p = p_vv
                value_indep = vi
            else: 
                if p_vv / p > 1:
                    p = p_vv
                    value_indep = vi
                
        return columns_indep, value_indep, p
    
    def condHyp_inference_mp(self, vars:tuple, indep:tuple, indep_values:tuple, lote_n, thread_n) -> tuple:
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
        columns_vars = tuple([v.getName() for v in vars])
        columns_indep = tuple([v.getNvars_namesame() for v in indep])
        
        values_vars = [v.getValues() for v in vars]
        
        p = 0
        value_vars = None
        for vv in product(*values_vars):
            
            p_vi = self.joint_mp(columns_vars, vv, columns_indep, indep_values, lote_n, thread_n)
            
            if p == 0:
                p = p_vi
                value_vars = vv
            else: 
                if p_vi / p > 1:
                    p = p_vi
                    value_vars = vv
                               
        return columns_vars, value_vars, p
    
    def joint_inference_mp(self, vars:tuple, vars_values:tuple, vars_:tuple) -> tuple:
        """ Método para inferir el valor más probable de distribución conjunta dado los valores de algunas variables.

        Args:
            vars (tuple): Tupla de las variables de la distribución conjunta sin las variables a buscas.
            vars_values (tuple):Tupla con los valores de las variables de la distribución condicconjuntaional.
            vars_ (tuple): Tupla de las variables a buscar.
        Returns:
            tuple ((tuple, tuple, tuple, tuple, float)): El primer elemento es la tupla de nombres de vars, el segundo elemento es la tupla que representa sus valores, 
            y el último elemento es la probabilidad.
        """
        columns_vars = tuple([v.getName() for v in vars] + [v.getName() for v in vars_])
        
        values_vars = [v.getValues() for v in vars_]
        
        p = 0
        value_vars = None
        for vv in product(*values_vars):
            
            p_vi = self.marginal_mp(columns_vars, tuple(list(vars_values) + list(vv)))
            
            if p == 0:
                p = p_vi
                value_vars = vv
            else: 
                if p_vi / p > 1:
                    p = p_vi
                    value_vars = vv
                               
        return columns_vars, vars_values+value_vars, p

class Mib_lg:
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
        
        for k in product(*self._model.getValues()):
            # Establecer los valores de los eventos.
            i = 0
            for v in self._model.getVars():
                v.setEvent(k[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self._model.getDescomp():
                p += math.log(d.P(self._nameToVar))
            
            sum += p
        
        self._ResetAllVars()
        return sum
    
    def joint_marginal(self, vars1_columns:tuple, vars1_values:list, vars2_columns:tuple, vars2_values:list) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1_columns (tuple): Tupla de los nombres de las variables del primer conjunto de variables.
            vars1_values (list): _description_
            vars2_columns (tuple): Tupla de los nombres de las variables del segundo conjunto de variables.
            vars2_values (list): _description_

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        sum = 0
        
        for i,name in enumerate(vars1_columns):
            self._nameToVar[name].setMarginal(vars1_values[i])
        for i,name in enumerate(vars2_columns):
            self._nameToVar[name].setMarginal(vars2_values[i])
        
        for k in product(*self._model.getValues()):
            # Establecer los valores de los eventos.
            i = 0
            for v in self._model.getVars():
                v.setEvent(k[i])
                i += 1
            
            # Calcular la probabilidad con los valores de k.
            p = 1
            for d in self._model.getDescomp():
                p += math.log(d.P(self._nameToVar))
            
            sum += p
        
        self._ResetAllVars()
        return sum
    
class Question:
    """ Clase para generar preguntas y generar consultas para responder.

        Atributos:
            sp (Specification): Espesificación del problema con su distribución conjunta y su descomposción.
    """

    def __init__(self, sp: Specification) -> None:
        self._sp = sp
    
    def DistributionQuery(self, vars:set, indep:set = None):
        """ Método para generar una consulta que generar una distribución.

        Args:
            vars (set): Conjunto de variables.
            indep (set (optional)): Conjunto de variables independientes. Defaults to None.

        Returns:
            Distrib | CondDistrib: Distribución consultada.
        """
        mib = Mib(self._sp)
        if not indep:
            return mib.Distrib_inference(vars)
        else:
            return mib.condDistrib_inference(vars, indep)
        
    def DistributionQuery_mp(self, vars:set, indep:set = None, lote_n=1000, thread_n=8):
        """ Método para generar una consulta que generar una distribución.

        Args:
            vars (set): Conjunto de variables.
            indep (set (optional)): Conjunto de variables independientes. Defaults to None.

        Returns:
            Distrib | CondDistrib: Distribución consultada.
        """
        mib = Mib_mp(self._sp)
        if not indep:
            return mib.Distrib_inference_mp(vars, lote_n, thread_n)
        else:
            return mib.condDistrib_inference_mp(vars, indep, lote_n, thread_n)
        
    def Query(self, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None, vars_:tuple = None):
        """ Método para generar una consulta sobre los valores más probables o.
        
        Args:
            vars (tuple): Tupla de variables (vars).
            indep (tuple, optional): Tupla de variables independientes. Defaults to None.
            vars_values (tuple, optional): Tupla para los valores de las variables (vars). Defaults to None.
            indep_values (tuple, optional): Tupla para los valores de las variables independientes. Defaults to None.

        Returns:
            tuple : Tupla con los datos de la consulta.
        """
        mib = Mib(self._sp)
        if not indep and not vars_:
            if vars_values:
                return mib.marginal(tuple([v.getName() for v in vars]), list(vars_values))
            else:
                return mib.marginal_inference(set(vars))
        elif indep and not vars_:
            if vars_values and indep_values:
                return mib.cond(tuple([v.getName() for v in vars]), vars_values, tuple([v.getName() for v in indep]), indep_values)
            elif vars_values and not indep_values:
                return mib.condObs_inference(vars, vars_values, indep)
            elif not vars_values and indep_values:
                return mib.condHyp_inference(vars, indep, indep_values)
        elif not indep and vars_:
            return mib.joint_inference(vars, vars_values, vars_)
            
        print("Consulta no valida")
    
    def Query_mp(self, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None, vars_:tuple = None, lote_n=1000, thread_n=8):
        """ Método para generar una consulta sobre los valores más probables o.
        
        Args:
            vars (tuple): Tupla de variables (vars).
            indep (tuple, optional): Tupla de variables independientes. Defaults to None.
            vars_values (tuple, optional): Tupla para los valores de las variables (vars). Defaults to None.
            indep_values (tuple, optional): Tupla para los valores de las variables independientes. Defaults to None.
            lote_n
        Returns:
            tuple : Tupla con los dato de las consulta.
        """
        
        mib = Mib_mp(self._sp)
        if not indep and not vars_:
            if vars_values:
                return mib.marginal_mp(tuple([v.getName() for v in vars]), list(vars_values), lote_n, thread_n)
            else:
                return mib.marginal_inference_mp(set(vars), lote_n, thread_n)
        elif indep and not vars_:
            if vars_values and indep_values:
                return mib.cond_mp(tuple([v.getName() for v in vars]), vars_values, tuple([v.getName() for v in indep]), indep_values, lote_n, thread_n)
            elif vars_values and not indep_values:
                return mib.condObs_inference_mp(vars, vars_values, indep, lote_n, thread_n)
            elif not vars_values and indep_values:
                return mib.condHyp_inference_mp(vars, indep, indep_values, lote_n, thread_n)
        elif not indep and vars_:
            return mib.joint_inference(vars, vars_values, vars_)
            
        print("Consulta no valida")