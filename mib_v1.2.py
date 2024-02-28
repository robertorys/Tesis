#==============================================================================
#title          :mib_v1.2.py
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

# Funciones de entrada/salida de datos
def genera_espacio(entrada: list)->list:
    """Función para generar el espacio de valores posibles mediante el producto 
    cartesiano de los valores de las variables (entrada).

    Args:
        entrada (list): valores posibles por cada variable de entrada.

    Returns:
        list: n-tuplas con todas las combinaciones posibles de los valores de las variables.
    """
    L=[]
    for element in product(*entrada):
        L.append(element)
    return L

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

def genera_llaves_cond(var: list, entrada, indep) -> tuple: 
    """Genera las llaves de entrada al diccionario de una distribución condicional.
    Si son varias variables de entrada, genera las combinaciones posibles

    Args:
        var (list): Variables dependiente de salida.
        entrada (list): Combinación de valores de la entrada a la tabla.
        indep (list): Variables independientes (entradas de la tabla).

    Returns:
        tuple (list, list): 
            - Lista de n-tuplas con las combinaciones de salida.
            - Llaves: lista de n-tuplas con las combinaciones de entrada.
    """
    salida=[]
    llaves=[]
    
    try:
        if isinstance(var,list):
            listVar=True
        else:
            listVar=False
    except:
        listVar=False
    
    if not listVar:
        nombre = var.name
        for i in range(len(var.values)):
            salida.append((nombre,var.values[i]))
    else:
        salida = genera_llaves(var)
        
    l = []
    
    for v in indep:
        l.append(v.name)
        
    l = tuple(list(chain(*product(l))))
    
    for i in range(len(entrada)):
        x = list(chain(*(l,entrada[i])))
        llaves.append(tuple(x))
    
    return salida, llaves

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

def genera_vars_llaves(variables: list) -> tuple:
    """Función para generar el espacio de valores posibles mediante el producto
    cartesiano de los valores de las variables (entrada)

    Args:
        variables (list): variables de entrada.

    Returns:
        tuple: lista de n-tuplas con todas las combinaciones posibles de los valores de las variables y
        lista de combinaciones por cada variable.
    """
    #==============================================================================
    # ejemplo:
    # A=[0,1], B=[0,1]
    # llaves= [('A', 'B', 0, 0), ('A', 'B', 0, 1), ('A', 'B', 1, 0), ('A', 'B', 1, 1)]
    # var_list=[('A', 0), ('A', 1), ('B', 0), ('B', 1)]
    #==============================================================================
    var_list = []
    llaves = genera_llaves(variables)
    
    for v in variables:
        var_list.append(genera_llaves([v]))    
    var_list=list(chain.from_iterable(var_list)) #flat list of lists
    
    return llaves, var_list

def look_up_table(variables: list, espacio: list) -> list:
    """Función para recuperar la intersección entre las variables y el espacio 
    cartesiano de entrada

    Args:
        variables (list): Lista de variables de búsqueda.
        espacio (list): lista de n-tuplas con todas las combinaciones posibles del espacio de búsqueda.

    Returns:
        list: lista de las variables con sus valores que tienen intersección con
        el espacio de búsqueda.
    """
    #==============================================================================
    #ejemplo:
    # A=[0,1], C=[0,1,2]
    # variables = [A,C]
    # espacio = ([A,C,0,0],[A,C,0,1],[A,C,0,2],[A,C,1,0],[A,C,1,1],[A,C,1,2])
    # lkt = [('A', 1), ('C', 1), ('A', 0), ('C', 0), ('C', 2)]
    #==============================================================================
    
    def genera_mascaras(va):
        L = []
        n = len(va)
        cadena='1'*2*n
        
        for i in range(n):
            mascara = []
            a = cadena[:i]+'0'+'1'*(n-(i+1))
            a = a*2
            mascara.extend(a)
            mascara = np.array(mascara, dtype=int)
            L.append(mascara)
            
        return L

    def get_masked_array(key, mask):
        y = list(key)
        z = []
        
        for i in range(len(mask)):
            if mask[i] == 0:
                z.append(y[i])
        
        return z
    
    lkt = []
    v = []
    
    for va in variables:
        v.append(va.name)
        
    mascaras = genera_mascaras(variables)
    
    for k in espacio:
        for m in mascaras:
            if set(v).issubset(list(k)):
                z = get_masked_array(k, m)
                if all(z) not in lkt:
                    lkt.append(tuple(z))
    
    lkt = list(set(lkt))
    
    return lkt

def filter(keys: list, v: list, thevars: list) -> list:
    """Función para buscar una coencidencia entre las claves de entrada (dico_Y) y
    el par variable-valor a su vez (llave de dico_X).

    Args:
        keys (list): _description_
        v (list): _description_
        thecars (list): _description_
    """
    m = []
    n = len(keys[0])
    in_v = []
    foundMatch = False
    
    for x in v: # x contiene el par (variable,value)
        for i in range(n):
            if keys[0][i] == x[0]:
                foundMatch = True
                i_v = i
            
            if foundMatch:
                if keys[0][i] not in thevars:
                    in_v.append(i+i_v)
                    break
                
    if foundMatch:
        foundMatch = False
        for j,x in enumerate(v):
            for k in keys:
                if k[in_v[j]] == x[1]:
                    foundMatch = True
                    
                    if k not in m:
                        m.append(k)
        
        if foundMatch:
            return m 
    return None

def filter_rec(candidates: list, variables: list, v: tuple) -> list:
    """_summary_

    Args:
        candidates (list): Espacio de búsqueda.
        variables (list): Las variables son términos de filtrado.
        v (_type_): Llave de una variable.
    """
    n = len(v)
    
    i_v = 0
    i_n = 0
    terms = []
    foundVar = False
    match = False
    Idx = True
    
    try:
        x = variables.pop()
    except IndexError:
        x = []
    
    if x != []:
        for i in range(n):
            if v[i] == x[0]:
                foundVar = True
                i_v = 1
            
            if isinstance(v[i], int) and Idx == True:
                i_n = iIdx = False 
            
            if foundVar and i == i_v + i_n:
                if v[i] == x[1]:
                    match = True
                    break
        
        if match:
            match = False
            foundVar = False
            foundIdx = False
            
            for k in candidates:
                for i in range(len(k)):
                    if k[i] == x[0]:
                        i_v = i
                        foundVar = True
                    
                    if foundVar:
                        if isinstance(k[i], int) and not foundIdx:
                            i_n = i = i_v
                            foundIdx = True
                        
                        if foundIdx and k[i_n] == x[1]:
                            match = True
                            
                            if k not in terms:
                                terms.append(k)
                                break
            
            candidates = filter_rec(terms, variables, v)
        else:
            candidates = filter_rec(candidates, variables, v)
        
        return candidates
    
def checkMatch(kand: tuple, sand: list, v: list, variables: list) -> tuple:
    n = len(v)
    i_v = 0
    i_n = 0
    foundVar = False
    match = False
    Idx = True
    
    for x in variables:
        for i in range(n):
            if v[i] == x[0]:
                foundVar = True
                i_v = i
            
            if isinstance(v[i], int) and Idx == True:
                i_n = i
                Idx = False
                
            if foundVar and i == i_v + i_n:
                if v[i] == x[1]:
                    match = True
                    break
        
        if match:
            match = False
            foundVar = False
            foundIdx = False
            
            for k in kand:
                for i in range(len(k)):
                    if k[i] == x[0]:
                        i_v = i
                        foundVar = True
                        
                    if foundVar:
                        if isinstance(k[i], int) and not foundIdx:
                            i_n = i + i_v
                            foundIdx = True
                            
                        if foundIdx and k[i_n] == x[1]:
                            match = True
                            return match, 'K'
            
            match=False
            foundVar=False
            foundIdx=False
            
            for s in sand:
                for i in range(len(s)):
                    if s[i] == x[0]:
                        i_v = i
                        foundVar = True
                    
                    if foundVar:
                        if isinstance(s[i], int) and not foundIdx:
                            i_n = i + i_v
                            foundIdx = True
                        
                        if foundIdx and s[i_n] == x[1]:
                            return True, 'S' 
    
    return match, 'U'

def checkLines(S_llaves: list, K_llaves: list, KS: list, KSvars: list, lineas: list):
    """_summary_

    Args:
        S_llaves (list): _description_
        K_llaves (list): _description_
        KS (list): _description_
        KSvars (list): _description_
        lineas (list): _description_

    Returns:
        _type_: _description_
    """
    
    L = []
    
    for e in KS:
        for K,S in zip(K_llaves, S_llaves):
            for l in lineas:
                k = K[l]
                s = S[l]
                found = False
                
                found, C = checkMatch([k], s, e, KSvars)
                
                if found:
                    L.append([e, l, C])
    
    return L

def compute_conditional_probs(dico_Y: dict, dico_X: dict, searched: list, known: list, r=0) -> dict:
    """

    Args:
        dico_Y (dict): _description_
        dico_X (dict): _description_
        searched (list): _description_
        known (list): _description_
        r (int, optional): _description_. Defaults to 0.

    Returns:
        dict: _description_
    """
    #######################################################################
    # The problem is to compute the division dico_Y/dico_X
    # dico_X has less variables than dico_Y
    # So, keys in dico_X (llaves) are used as patterns to be found in
    # dico_Y (keys_Y).
    # However, if dico_X's keys has more than one variable
    # the patterns of combination pairs (variables,values)
    # have to be detected, so they can be found in dico_Y
    # The names of the variables are passed, so as to differentiate
    # the values from the names of the variables, as values 
    # may be other thing than integers (e.g. real numbers or categorical).
    #######################################################################
    
    Sn = [i.name for i in searched]
    Kn = [i.name for i in known]
    
    entrada = [i.values for i in known]
    entrada = genera_espacio(entrada)
    
    salida, llaves = genera_llaves_cond(searched, entrada, known)
    
    dico = {}
    
    for k in llaves:
        Srd_vars = look_up_table(searched+known,dico_Y.keys())
        km = filter_rec(dico_Y.keys(),Srd_vars,k)
        dO={}
        
        for i,o in enumerate(salida):
            if r!=0:
                dO[o]=round(dico_Y[km[i]]/dico_X[k],r)
            else:
                dO[o]=dico_Y[km[i]]/dico_X[k]
        
        dico[k] = dO
    
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
    
    def get_all_P(self) -> list:
        """ Obtener todas los prabilidades.

        Returns:
            list: lista de las probabilidades.
        """
        return [self.tabla[key] for key in self.tabla.keys()]
    
    def to_Frame(self) -> pd.DataFrame:
        print('Creating DataFrame for: ', self.name)
        columnas=[self.name]
        indice=list(self.tabla.keys())
        registros=list(self.tabla.values())
        df=pd.DataFrame(registros, columns = columnas, index = indice)
        return df

    def _print(self) -> None:
        print('Printing: ',self.name)
        for k in self.tabla.keys():
            print('{0}:{1} '.format(k,self.tabla[k]),end=' ')
        print('\n')

class DistribCond():
    """Distribución Condicional; Tabla de valores de probabilidad condicional.

    Atributos:
        name (str): Nombre de la distribución (string); p.e. "P(A|B)".
        indep (list): variables independientes (tipo Var) (entrada).
        var (Var): apuntador a objeto de tipo Var (salida).
        tabla (dict): valores de probabilidad de la salida.
    """
    def __init__(self, name: str, var: Var, indep: list, tabla: dict = None) -> None:
        self.name = name
        self.indep = indep
        self.var = var
        entrada = [i.values for i in indep]
        
        self.entry = genera_espacio(entrada)
        
        if tabla is not None:
            self.tabla = carga_tabla_cond(self.var,self.entry,self.indep,tabla)
        
    def set_name(self, name: str) -> None:
        self.name = name
        
    def load_tabla(self, tabla: dict) -> None:
        self.tabla = carga_tabla_cond(self.var,self.entry,self.indep,tabla) 
    
    def get_P(self, conditions='all', values='all') -> list:
        L = []
        if not isinstance(conditions,str) and not isinstance(conditions,list):
            print("Las condiciones deben ser una lista de tuplas")
            return L
        else:
            if conditions=='all' and values == 'all':
                return self.tabla
            else:
                if conditions=='all':
                    entries = itemgetter(*self.tabla.keys())(self.tabla)
                else:
                    entries = itemgetter(*conditions)(self.tabla)
                if values == 'all':
                    L.append(entries)
                else:
                    if len(values) == len(conditions):
                        for v,d in zip(values,entries):
                            data = itemgetter(*v)(d)
                            L.append(data)
                    elif len(values) <= len(conditions):
                        val = values[:]
                        for i in range(len(conditions)-len(values)-1):
                            val.extend(val)
                        val.extend(val)
                        for v,d in zip(val,entries):
                            data = itemgetter(*v)(d)
                            L.append(data)
                    else:
                        print("Combinación de condiciones y valores incompatible!")    
        return L

    def to_Frame(self, formateo=False) -> pd.DataFrame:
        
        def format_numbers(data):
            base10 = np.log10(abs(data))
            base10 = abs(floor(base10))
            if base10 >= 4:
                return data
            else:
                return f'{data:.6f}'

        dico = self.get_P()
        indice = list(dico.keys())
        vals = list(dico.values())
        
        columnas = []
        registros = []
        
        if type(vals[0]) == dict:
            for d in vals:
                if list(d.keys()) not in columnas:
                    columnas.append(list(d.keys()))
                registros.append(list(d.values()))
        else:
            columnas = list(dico[list(dico.keys())[0]].keys())
            registros = []
            
            for i,d in enumerate(vals): 
                reg = []
                
                for c in columnas:
                    reg.append(d[c])
                    
                registros.append(reg)
                
        if type(self.var) == list:
            searched = [v.name for v in self.var]
        else:
            searched = [self.var.name]
        if type(self.indep) == list:
            known = [v.name for v in self.indep]
        else:
            known = [self.indep.name]
            
        df = pd.DataFrame(registros, columns=columnas, index=indice)
        
        if formateo:
            for col in df.columns:
                df[col]=df[col].map(lambda x:f'{format_numbers(x)}')
    
        return df    

class JoinDistrb():
    """ Distribución Conjunta; Tabla de probabilidad de una descomposición
    condicional siguiendo la regla del producto.
    
    Atributos:
        name (str): Nombre de la distribución.
        vars (list): Lista de variables, objetos de tipo Var, (entrada).
        descomp (list): lista de distribuciones marginales y condicionales. La lista se ordena por orden ascendente de la longitud del nombre de cada distribución.
        lable_to_var (dict): Diccionario donde la llave es el nombre de los objetos Var, que se encuentran en la lista vars, y su valor es el objeto.
    """
    #=================================================================================
    # *No se calculan las posibilidades de valores de entrada, solo sirve para
    #  estructurar el cálculo a partir de distribuciones marginales y condicionales.
    #=================================================================================
    def __init__(self, name: str, variables: list, descomp: list) -> None:
        self.name = name
        self.vars = variables
        self.label_to_var = {}
        self.ID = self
        
        for v in self.vars:
            self.label_to_var[v.name] = v

        descomp.sort(key = lambda x: len(x.name), reverse = True)
        self.descomp = descomp
    
    # ------ ** Dependencia con clase Question ** ------- #
    def get_P(self):
        Q = None
    
    def _print(self):
        for distrib in self.descomp:
            print('{0} : {1}'.format(distrib.name, distrib.tabla))
    
    def to_Frame(slef):
        slef.ID = None
            
class Question():
    """Inferencia probabilista mediante una pregunta a la Conjunta.
    
    Atributos:
        joint: Distribución conjunta (objeto); p.e. P_AB
    """
    #=================================================================================
    # NOTA: las variables se dividen en los siguientes sub-conjuntos:
    # - KNOWN: variables cuyos valores de probabilidad son conocidos.
    # - UNKNOWN: variables cuyos valores son deconocidos.
    # - SEARCHED: variables cuyos valores nos interesa conocer (query)
    #=================================================================================
    def __init__(self, joint: JoinDistrb) -> None:
        self.joint = joint
        
    def compute_marginal(self, searched: list, unknown: list, r = 0) -> dict:
        """Método de inferencia probabilista de una distribución marginal.

        Args:
            searched (list): variables cuyos valores nos interesa conocer (query).
            unknown (list): variables cuyos valores son deconocidos.
            r (int, optional): ... Defaults to 0.

        Returns:
            dict: Diccionario de las probabilidades buscadas (P(searched)).
        """
        
        # Generación de llaves
        if len(searched) > 1:
            skeys,var_list = genera_vars_llaves(searched)
        else:
            skeys = genera_llaves(searched) 
        ukeys = genera_llaves(unknown)
        
        # valores de las variales que tienen intersección con el espacio de búsqueda.
        Unk_vars = look_up_table(unknown,ukeys)
        Unk_vars.sort()
        
        dico = {} 
        
        for v in skeys:
            # Working data structures to compute marginal dist.
            K_llaves=[]
            S_llaves=[]
            lineas=[]
            a_Lps=[]
            
            #############################################################
            # COMPUTING P(v=searched) from JOINT distribution.
            # JOINT is assumed to be a product of Distributions.
            # Distributions are assumed to be of the form P(Y|X) or P(Y)
            # where X or Y may be a list of variables.
            ############################################################
            
            for n,distrib in enumerate(self.joint.descomp):
                ################################################################
                # Creating new array alignments K=X; S=Y.
                # Array alignmnents Li are assumed to correspond
                # to Known (K) searched keys in the first distribution.
                # P points to the current distribution.
                # We adopt the convention: K(known)=X; S(searched)=Y.
                # Knd stands for KNOWN_dist vars and Srd for SEARCHED_dist vars.
                # Combinatorial spaces are created from this variables and then
                # filtered out in function of the searched variable 'v'.
                ################################################################
                LK = {}
                LS = {}
                
                L_ps = defaultdict(dict)
                
                if n != 0:
                    LK=defaultdict(list)
                    LS=defaultdict(list)
                
                P = distrib
                Knd = distrib.indep
                Srd = distrib.var
                
                if Knd == []:
                    Skeys = genera_llaves(Srd) # Llaves de las variables a buscar
                    Srd_vars = look_up_table(Srd, Skeys) # Intersección de las variables a buscar con las llaves de las variables a buscar
                    S_U = list(set(Srd_vars) & set(Unk_vars))
                    thevars = [i.name for i in Srd]
                    Srd_space = Skeys
                    
                    if S_U != []:
                        Srd_space = filter(Srd_space, S_U, thevars)
                    Srd_space = filter_rec(Srd_space, Srd_vars, v)
                    
                    for i,k in enumerate(lineas):
                        LK[k] = []
                    
                    n_Svars = look_up_table(Srd, Srd_space)
                    L_s = checkLines(S_llaves, K_llaves, Srd_space, n_Svars, lineas)
                    
                    if L_s == []:
                        for i,k in enumerate(lineas): 
                            LS[k] = Srd_space
                    else:
                        for e in L_s:
                            LS[e[1]].append(e[0])
                    
                    
                    for s in LS.keys():
                        y = LS[s]
                        L_ps = defaultdict(list)
                        
                        for j in y:
                            p = P.tabla[j]
                            L_ps[s][j].append(p)
                    
                    a_Lps.append(L_ps)
                    K_llaves.append(LK)
                    S_llaves.append(LS)
                
                else:
                    #################################################
                    # Filtrar el KNOWN SPACE: X para calcular P(Y|X)
                    #################################################
                    Kkeys=genera_llaves(Knd)
                    Skeys=genera_llaves([Srd])
                    
                    Knd_vars = look_up_table(Knd,Kkeys)
                    Srd_vars = look_up_table([Srd],Skeys)
                    
                    K_U = list(set(Knd_vars) & set(Unk_vars))
                    S_U = list(set(Srd_vars) & set(Unk_vars))
                    
                    thevars = list(set([i.name for i in [Srd]] + [i.name for i in Knd]))
                    
                    Knd_space = Kkeys
                    
                    if K_U != []:
                        Knd_space = filter(Knd_space, K_U, thevars)
                    Knd_space = filter_rec(Knd_space,Knd_vars,v) 
                    Knd_space.sort()
                    
                    ##############################################################
                    # Inicialice las etiquetas de alineación de la matriz: 'LINES'
                    # y crear nuevas alineaciones de matriz K<->X; S<->Y.
                    # Se supone que las alineaciones de matriz Li corresponden
                    # a claves buscadas conocidas (K) en la primera distribución.
                    ##############################################################
                    
                    if n == 0:
                        linea = 'L'
                        for i in range(len(Knd_space)):
                            lineas.append(linea+str(i))
                            
                        LK=defaultdict(list)
                        LS=defaultdict(list)

                    #################################################
                    # Filtrar ele RETRIEVED SPACE: Y.
                    #################################################
                    
                    Srd_space = Skeys
                    
                    if S_U != []:
                        Srd_space = filter(Srd_space, S_U, thevars)
                        
                    Srd_space=filter_rec(Srd_space,Srd_vars,v)
                    Srd_space.sort()
                        
                    #################################################
                    # Alinear los cálculos de probabilidad en K y S.
                    #################################################

                    n_Kvars = look_up_table(Knd,Knd_space)
                    n_Svars = look_up_table([Srd],Srd_space)
                    L_k=checkLines(S_llaves, K_llaves, Knd_space, n_Kvars, lineas)
                    L_s=checkLines(S_llaves, K_llaves, Srd_space, n_Svars, lineas)
                    
                    if L_k == []:
                        for i,k in enumerate(lineas):
                            LK[k] = Knd_space[i]
                    else:
                        for e in L_k:
                            LK[e[1]].append(e[0])
                        
                    if L_s == []:
                        for i,k in enumerate(lineas):
                            LS[k] = Srd_space
                    else:
                        for e in L_s:
                            LS[e[1]].append(e[0])
                    
                    #########################################################
                    # Recuperar probabilidades basadas en alineaciones K y S.
                    #########################################################
                    LK_llaves=list(LK.keys())
                    LK_llaves.sort()
                    LS_llaves=list(LS.keys())
                    LS_llaves.sort()
                    
                    for k,s in zip(LK_llaves, LS_llaves):
                        x = LK[k]
                        L_ps[k] = defaultdict(dict)
                        y = LS[s]
                        
                        if isinstance(x, list):
                            for i in x:
                                L_ps[k][i] = defaultdict(list)

                                for j in y:
                                    p = P.tabla[i][j]
                                    L_ps[k][i][j].append(p)

                        else:
                            L_ps[k][x] = defaultdict(list)
                            
                            for j in y:
                                p = P.tabla[x][j]
                                L_ps[k][x][j].append(p)
                                
                    a_Lps.append(L_ps)
                    K_llaves.append(LK)
                    S_llaves.append(LS)
            
            #######################################################
            # Calcular probabilidades basadas en alineaciones K y S
            #######################################################

            llaves = a_Lps[0].keys()
            s = []
            
            for linea in llaves:
                dd = []
                
                for d in a_Lps:
                    dd.append(d[linea])
                    
                dd.reverse()
                d = dd.pop()
                dd.reverse()
                
                summation = 0.0
                keys=list(d.keys())
                
                for k in keys:
                    for dk in d[k].keys():
                        pr = np.array(d[k][dk])
                        
                        for j in range(len(dd)):
                            todas_las_llaves=[]
                            
                            for kllave in dd[j].keys():
                                todas_las_llaves.append(kllave)
                                
                            if dk in todas_las_llaves:
                                kllave=dk
                                
                                if isinstance(dd[j][kllave],dict):
                                    el = 0
                                    
                                    for kkllave in dd[j][kllave].keys():
                                        el+=np.array(dd[j][kllave][kkllave])
                                        
                                    pr *= np.array(el)
                                else:
                                    pr *= np.array(dd[j][kllave])
                                    
                            else:
                                for kllave in dd[j].keys():
                                    if isinstance(dd[j][kllave],dict):
                                        el=0
                                        for kkllave in dd[j][kllave].keys():
                                            el += np.array(dd[j][kllave][kkllave])
                                        pr *= np.array(el)
                                    else:
                                        pr*=np.array(dd[j][kllave])
                                        
                        summation+=pr
                s.append(summation)
                
            fp = np.sum(np.array(s))
            if r != 0:
                dico[v]=np.round(fp,r)
            else:
                dico[v]=fp
                
        return dico
                
    def compute_conditional(self, searched: list, known: list, unknown: list) -> dict:
        """Método para calculas los marginales de searched.

        Args:
            searched (list): Variables cuyos valores nos interesa conocer (query).
            known (list): Variables cuyos valores de probabilidad son conocidos.
            unknown (list): Variables cuyos valores son deconocidos.

        Returns:
            dict: Probabilidades marginales de searched.
        """
        ###################################################################
        # El objetivo es calcular los marginales involucrados en el numerador
        # y en el denominador.
        # Entonces la función que realiza la división alineando las variables
        # y los valores correspondientes se llama.
        ####################################################################  
        nS = [s.name for s in searched]
        nK = [s.name for s in known]
        nU = [s.name for s in unknown]
        name = 'P('+','.join(nS) +'|'+','.join(nK) +')'
        
        searchedJoint = searched + known
        unknownJoint = searched + unknown
        dico_Y = self.compute_marginal(searchedJoint, unknown)
        dico_X = self.compute_marginal(known, unknownJoint)
        
        dico = compute_conditional_probs(dico_Y,dico_X,searched,known)

        return dico

    def query(self, searched, known = []):
        """_summary_

        Args:
            searched (_type_): _description_
            known (list, optional): _description_. Defaults to [].
        """
        if len(searched) > 1:
            if known != []:
                nS = [s.name for s in searched]
                nK = [s.name for s in known]
                
                name='P('+','.join(nS) +'|'+','.join(nK) +')'
                print('computing conditional of joint: {}'.format(name))
                
                All = [a.name for a in self.joint.vars]
                Uk = list(set(All)-set(nS).union(set(nK)))
                
                unknown = []
                
                for nombre in Uk:
                    unknown.append(self.joint.label_to_var[nombre])

                dico = self.compute_conditional(searched, known, unknown)                                            
                distribution = DistribCond(name, searched, known)            
                distribution.tabla=dico
                return distribution
            
            
def carga_tabla_cond(var: Var, entrada: list, indep: list, tabla: dict) -> dict:
    """Función para cargar valores de probabilidad condicional en un diccionario.

    Args:
        var (Var): Apuntador a la variable de salida (objeto tipo Var).
        entrada (list): n-tuplas con combinaciones de los valores de entrada.
        indep (list): Variables (tipo Var) independientes (entrada)
        tabla (dict): Valores de probabilidad de la salida.
    
    Returns:
        dict: Valores de probabilidad para var.
    """
    dico = {}
    
    salidas,keys = genera_llaves_cond(var,entrada,indep)
    
    for k,v in zip(keys,list(tabla.values())):
        tab = {}
        for i,s in enumerate(salidas):
            tab[s] = v[i]
        dico[k] = tab
    
    return dico
    