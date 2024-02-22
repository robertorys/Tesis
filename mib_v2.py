#==============================================================================
#title          :mib_v2.py
#description    :Motor de inferencia bayesiano para variables discretas.
#version        : 1.2
#python_version :3.10.12
#==============================================================================

#Librerías estándar
import numpy as np
from itertools import product,chain
from operator import itemgetter
from collections import defaultdict
import pandas as pd
from math import floor

def genera_llaves(variables: list) -> list:
    """Función para generar las llaves de entrada a un diccionario de probabilidades.

    Args:
        variables (list): lista de variables (objetos tipo Var).

    Returns:
        list: lista de n-tuplas con todas las combinaciones posibles de los valores de las variables de entrada.
    """
    #===============================================================================
    # ejemplo:
    # variables = [A,B] ; con A=[0,1], B=[0,1]
    # llaves = [(['A'], ['B'], 0, 0)
    #           (['A'], ['B'], 0, 1),
    #           (['A'], ['B'], 1, 0),
    #           (['A'], ['B'], 1, 1)]
    #===============================================================================
    llaves = []
    nombre = []
    valores = []
    
    for v in variables:
        nombre.append(v.name)
        valores.append(v.values)
    
    for element in product(*valores):
        x = chain(*(nombre,element))
        llaves.append(tuple(x))
        
    return llaves   

def carga_tabla(var: list, tabla: dict):
    """ Función para cargar valores de probabilidad en un diccionario.

    Args:
        var (Lista): Eventos de la probabilidad.
        tabla (dict): Diccionario de valores de probabilidad.

    Returns:
        dict: diccionario de valores de probabilidad para Var.
    """
    dico={}
    keys = genera_llaves(var) 
    
    for k,v in zip(keys,list(tabla.values())):
        print(k, v)
        dico[k] = v
    
    return dico

#----------- Estructuras de datos del motor de inferencia ----------#

class Var():
    """Clase para las variables.
    
    Atributos:
        name (str): Nombre de la variable, p.e. 'A'.
        values (list): Lista de los posibles valores. Cada evento se representa con un número entero.
        card (int): Cardinalidad de los eventos.
    """
    def __init__(self, name:str, values = None): 
        self.name = name
        if values is not None:
            self.values = list(values)
            self.card = len(values)
        else:
            self.values = None
            self.card = 0
            
    def set_values(self, values:list):
        self.values = list(values)
        self.card = len(values)
        
    def get_var_data(self):
        return (self.name, self.card, self.values)

class Distrib():
    """Distribución Marginal - Tabla de probabilidad de una variable.

    Atributos:
        name (str): Nombre de la destribución; p.e. "P(A)".
        var (Var): Variable independiente.
        tabla (dict): Diccionario de valores de probabilidad.
    """
    def __init__(self, name, variable:Var = None, tabla:dict = None):
        self.name = name
        if variable is not None:
            self.var = variable
        if tabla is not None:
            self.tabla = carga_tabla(self.var, tabla)
            
    def set_name(self, name:str):
        self.name = name

    def set_variable(self, variable: Var):
        self.var = variable
        
    def load_tabla(self,var,tabla):
        self.tabla=carga_tabla(var,tabla)
    
    def get_P(self, key) -> float:
        """Obtener una probabilidad.

        Args:
            key : Llave de la probabilidad.

        Returns:
            float : Valor de la probabilidad.
        """
        if key in self.tabla.keys():
            return self.tabla[key]
        else:
            print("Llave no valida")
    
    def get_all_P(self):
        """ Obtener todas los prabilidades,

        Returns:
            list : lista de las probabilidades.
        """
        return [self.tabla[key] for key in self.tabla.keys()]
    
    def to_Frame(self):
        print('Creating DataFrame for: ', self.name)
        columnas=[self.name]
        indice=list(self.tabla.keys())
        registros=list(self.tabla.values())
        df=pd.DataFrame(registros, columns = columnas, index = indice)
        return df

    def _print(self):
        print('Printing: ',self.name)
        for k in self.tabla.keys():
            print('{0}:{1} '.format(k,self.tabla[k]),end=' ')
        print('\n')

