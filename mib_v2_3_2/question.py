from mib_v2_3_2.specification import Specification
from mib_v2_3_2.mib import Mib

class Question:
    """ Clase para generar preguntas y generar consultas para responder.

        Atributos:
            sp (Specification): Espesificación del problema con su distribución conjunta y su descomposción.
    """

    def __init__(self, description: Specification) -> None:
        self.ds = description
    
    def _DQ(self, mib:Mib, vars:set, indep:set = None):
        if not indep:
            return mib.Distrib_inference(vars)
        else:
            return mib.Distrib_inference(vars, indep)
        
    def DistributionQuery(self, vars:set, indep:set = None):
        """ Método para generar una consulta que generar una distribución.

        Args:
            vars (set): Conjunto de variables.
            indep (set (optional)): Conjunto de variables independientes. Defaults to None.

        Returns:
            Distrib | CondDistrib: Distribución consultada.
        """
        mib = Mib(self.ds)
        return self._DQ(mib, vars, indep)
    
    def _Q(self, mib:Mib, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None):
        if not indep:
            if vars_values:
                return mib.marginal(vars, vars_values)
            else:
                return mib.marginal_inference(vars)
        else:
            if vars_values and indep_values:
                return mib.cond(vars, vars_values, indep, indep_values)
            elif vars_values and not indep_values:
                return mib.obs_inference(vars, vars_values, indep)
            elif not vars_values and indep_values:
                return mib.hyps_inference(vars, indep, indep_values)
            
        print("Consulta no valida")
    
    def Query(self, vars:tuple, indep:tuple = None, vars_values:tuple = None, indep_values:tuple = None):
        """ Método para generar una consulta sobre los valores más probables o consulta de probabilidades.
        
        Args:
            vars (tuple): Tupla de variables (vars).
            indep (tuple, optional): Tupla de variables independientes. Defaults to None.
            vars_values (tuple, optional): Tupla para los valores de las variables (vars). Defaults to None.
            indep_values (tuple, optional): Tupla para los valores de las variables independientes. Defaults to None.

        Returns:
            tuple : Tupla con los datos de la consulta.
        """
        mib = Mib(self.ds)
        return self._Q(mib, vars, indep, vars_values, indep_values)
    