from .Specification import *
from itertools import product
import multiprocessing as mp
import copy
import math 

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
    
    def marginal(self, colum:tuple, values: list) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            colum (tuple): Conjunto del nombre de las variables para la marginal.
            values (list): Lista de los valores para las variables de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        sum = 0
        
        for i,name in enumerate(colum):
            self._nameToVar[name].setMarginal(values[i])
        
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
            vars1_values (list):  Lista de los valores para las variables del primer conjunto.
            vars2_columns (tuple): Tupla de los nombres de las variables del segundo conjunto de variables.
            vars2_values (list):  Lista de los valores para las variables del segundo conjunto.

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
                
        return columns_indep, value_indep, p / self.marginal(columns_indep, value_indep)
    
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
                               
        return columns_vars, value_vars, p / self.marginal(columns_indep, indep_values)
    
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

class MibMp(Mib):
    """ Clase para el motor de inferencia bayesiana usando paralelismo.

        Atributos:
            model (Model): Modelo del problema con su distribución conjunta y su descomposción.
    """
    def __init__(self, model: Specification, lote_n:int, procces_n:int) -> None:
        self.lote_n = lote_n
        self.process_n = procces_n
        super().__init__(model)
    
    def marginal_p(self, keys:list, vars:list, descomp:set, nameToVar: dict, _:mp.Queue):
        """ Método para los subprecesos para calcular la margial.

        Args:
            keys (list): Lista de un sub conjunto de llaves para caclcular la marginal.
            vars (list): Copia de las vairiables.
            descomp (set): Distribuciones de la descomposición.
            nameToVar (dict): Diccionario que enlaza el nombre de la varible con el objeto de la variable.
            _ (mp.Queue): Cola para guardar el resultado.
        """
        sum = 0
        for key in keys:
            i = 0
            for v in vars:
                v.setEvent(key[i])
                i += 1
            
            # Calcular la probabilidad con los valores de key.
            p = 1
            for d in descomp:
                p *= d.P(nameToVar)
                
            sum += p
        _.put(sum)
    
    def marginal_mp(self) -> float:
        """ Método para realizar la marginal con multples procesos. 

        Returns:
            float: Valor de probabilidad.
        """
        # Crear una cola para el resultado de los procesos.
        queue = mp.Queue()
        
        sum = 0
            
        keys = []
        count_lote = 0
        
        # Calcular la cantidad de llaves.
        product_cc = 1
        for v in self._model.getVars():
            product_cc *= v.getCard()
        
        processes = []
        
        for k in product(*self._model.getValues()):
            # Guardad llaves.
            if count_lote < self.lote_n:
                keys.append(k)
                product_cc -= 1
                count_lote += 1
                
            if product_cc == 0 or count_lote == self.lote_n:
                # Generar procesos.
                if len(processes) < self.process_n:
                    count_lote = 0
                    
                    vars_copy = [copy.deepcopy(v) for v in self._model.getVars()]
                    nameToVar = {}
                    for v in vars_copy:
                        nameToVar[v.getName()] = v
                        
                    process =  mp.Process(
                        target = self.marginal_p,
                        args = (
                            keys.copy(), 
                            vars_copy.copy(), 
                            self._model.getDescomp(), 
                            nameToVar.copy(),
                            queue
                            )
                    )
                    
                    processes.append(process)
                    
                    keys.clear()
                    vars_copy.clear() 
                    nameToVar.clear()
                
                # Ejecutar los procesos.
                if len(processes) == self.process_n or product_cc == 0:
                    for process in processes:
                        process.start()
                        
                    for process in processes:
                        process.join()
                        
                    # Obtener los resultados desde la cola.
                    while not queue.empty():
                        sum += queue.get()
                    
                    processes.clear()
                
        return sum

    def marginal(self, colum: tuple, values: list) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            colum (tuple): Conjunto del nombre de las variables para la marginal.
            values (list): Lista de los valores para las variables de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        for i,name in enumerate(colum):
            self._nameToVar[name].setMarginal(values[i])
            
        p = self.marginal_mp()
        
        super()._ResetAllVars()
        return p
        
    def joint_marginal(self, vars1_columns: tuple, vars1_values: list, vars2_columns: tuple, vars2_values: list) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1_columns (tuple): Tupla de los nombres de las variables del primer conjunto de variables.
            vars1_values (list):  Lista de los valores para las variables del primer conjunto.
            vars2_columns (tuple): Tupla de los nombres de las variables del segundo conjunto de variables.
            vars2_values (list):  Lista de los valores para las variables del segundo conjunto.

        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        for i,name in enumerate(vars1_columns):
            self._nameToVar[name].setMarginal(vars1_values[i])
        for i,name in enumerate(vars2_columns):
            self._nameToVar[name].setMarginal(vars2_values[i])
    
        p = self.marginal_mp()
        
        super()._ResetAllVars()
        return p
        
class MibLg(Mib):
    """ Clase para el motor de inferencia bayesiana.

        Atributos:
            model (Model): Modelo del problema con su distribución conjunta y su descomposción.
    """
    
    def __init__(self, model: Specification) -> None:
        super().__init__(model)
    
    def marginal(self, colum: tuple, values: list) -> float:
        """ Método para hacer la consulta de una marginal.

        Args:
            colum (tuple): Conjunto del nombre de las variables para la marginal.
            values (list): Lista de los valores para las variables de la marginal.
            
        Returns:
            float: Valor de la probabilidad de la marginal.
        """
        
        sum = 0
        
        for i,name in enumerate(colum):
            self._nameToVar[name].setMarginal(values[i])
        
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
    
    def joint_marginal(self, vars1_columns: tuple, vars1_values: list, vars2_columns: tuple, vars2_values: list) -> float:
        """ Método para calcular la marginal sobre dos cunjontos de variables.

        Args:
            vars1_columns (tuple): Tupla de los nombres de las variables del primer conjunto de variables.
            vars1_values (list):  Lista de los valores para las variables del primer conjunto.
            vars2_columns (tuple): Tupla de los nombres de las variables del segundo conjunto de variables.
            vars2_values (list):  Lista de los valores para las variables del segundo conjunto.

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
   
    
    #def cond(self, vars_names: tuple, vars_values: list, indep_names: tuple, indep_values: list) -> float:
    #    return self.joint_marginal(vars_names, vars_values, indep_names, indep_values)
  