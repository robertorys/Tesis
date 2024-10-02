from .Specification import *
from .Mibs import *

class Question:
    """ Clase para generar preguntas y generar consultas para responder.

        Atributos:
            sp (Specification): Espesificación del problema con su distribución conjunta y su descomposción.
    """

    def __init__(self, sp: Specification) -> None:
        self._sp = sp
    
    def _DQ(self, mib:Mib | MibMp | MibLg, vars:set, indep:set = None):
        if not indep:
            return mib.Distrib_inference(vars)
        else:
            return mib.condDistrib_inference(vars, indep)
    
    def DistributionQuery(self, vars:set, indep:set = None):
        """ Método para generar una consulta que generar una distribución.

        Args:
            vars (set): Conjunto de variables.
            indep (set (optional)): Conjunto de variables independientes. Defaults to None.

        Returns:
            Distrib | CondDistrib: Distribución consultada.
        """
        mib = Mib(self._sp)
        return self._DQ(mib, vars, indep)

    def DistributionQuery_mp(self, vars:set, indep:set = None, lote_n=1000, process_n=8):
        """ Método para generar una consulta que generar una distribución.

        Args:
            vars (set): Conjunto de variables.
            indep (set (optional)): Conjunto de variables independientes. Defaults to None.
            lote_n (int):
            process_n (int) :
        Returns:
            Distrib | CondDistrib: Distribución consultada.
        """
        mib = MibMp(self._sp, lote_n, process_n)
        return self._DQ(mib, vars, indep)
    
    def _Q(self, mib:Mib | MibMp | MibLg, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None, vars_:tuple = None):
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
    
    def Query(self, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None, vars_:tuple = None):
        """ Método para generar una consulta sobre los valores más probables o consulta de probabilidades.
        
        Args:
            vars (tuple): Tupla de variables (vars).
            indep (tuple, optional): Tupla de variables independientes. Defaults to None.
            vars_values (tuple, optional): Tupla para los valores de las variables (vars). Defaults to None.
            indep_values (tuple, optional): Tupla para los valores de las variables independientes. Defaults to None.

        Returns:
            tuple : Tupla con los datos de la consulta.
        """
        mib = Mib(self._sp)
        return self._Q(mib, vars, indep, vars_values, indep_values, vars_)
    
    def Query_mp(self, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None, vars_:tuple = None, lote_n=1000, procces_n=8):
        """ Método para generar una consulta sobre los valores más probables o consulta de probabilidades usando paralelismo.
        
        Args:
            vars (tuple): Tupla de variables (vars).
            indep (tuple, optional): Tupla de variables independientes. Defaults to None.
            vars_values (tuple, optional): Tupla para los valores de las variables (vars). Defaults to None.
            indep_values (tuple, optional): Tupla para los valores de las variables independientes. Defaults to None.
            lote_n (int): 
            process_n(int): 
        Returns:
            tuple : Tupla con los dato de las consulta.
        """
        
        mib = MibMp(self._sp, lote_n, procces_n)
        return self._Q(mib, vars, indep, vars_values, indep_values, vars_)
        
    def Query_lg(self, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None, vars_:tuple = None):
        """ Método para generar una consulta sobre los valores más probables o consulta de probabilidades usando logaritmos.
        
        Args:
            vars (tuple): Tupla de variables (vars).
            indep (tuple, optional): Tupla de variables independientes. Defaults to None.
            vars_values (tuple, optional): Tupla para los valores de las variables (vars). Defaults to None.
            indep_values (tuple, optional): Tupla para los valores de las variables independientes. Defaults to None.

        Returns:
            tuple : Tupla con los datos de la consulta.
        """
        mib = MibLg(self._sp)
        return self._Q(mib, vars, indep, vars_values, indep_values, vars_)
