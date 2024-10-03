import tpproc as tp
from collections import Counter  #regresa un diccionario con conteos
import glob
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import OrderedDict #diccionarios ordenados
import numpy as np
import pandas as pd
from itertools import product
import mib_v2_3_1 as mb
import json

# Leer cuentos y cargar dataframe
# Train
archivos = glob.glob('./Train/*/*')
archivos,nombres = tp.carga_cuentos(archivos)
df_train = tp.lee_cuentos(archivos)

# Tests
archivos = glob.glob('./Test/*')
archivos,nombres = tp.carga_cuentos(archivos)
df_test = tp.lee_cuentos(archivos,test=True)

def new_df_train(autores:list) -> pd.DataFrame:
    df_train_a = df_train.copy()
    conds = []
    for autor in autores:
        conds.append(df_train_a['autor'] == autor)
        
    filt = conds[0]
    for cond in conds[1:]:
        filt |= cond
    
    return df_train_a[filt]

def reduc_vocab(df_tr:pd.DataFrame, df_ts:pd.DataFrame) -> tuple:
    s = df_tr.texto.str.cat(sep=' ').split()
    conteos = Counter(s)
    train_vocabulario = set([palabra for palabra in s if conteos[palabra] > 1])
    
    s = df_ts.texto.str.cat(sep=' ').split()
    conteos = Counter(s)
    test_vocabulario = set([palabra for palabra in s if conteos[palabra] > 1])
    
    return train_vocabulario,test_vocabulario

def new_dfs(df_tr:pd.DataFrame, vc_tr:set, df_ts:pd.DataFrame, vc_ts:set) -> tuple:
    df_train_T = df_tr.copy()
    df_train_T['nuevo_texto'] = df_train_T.texto.str.split().\
        apply(lambda texto: [w for w in texto if w in vc_tr]).\
        apply(lambda x : ' '.join(x))
    df_train_T['Conteos']=df_train_T.nuevo_texto.str.split().apply(Counter)
    
    df_test_T = df_ts.copy()
    df_test_T['nuevo_texto']=df_test_T.texto.str.split().\
        apply(lambda texto: [w for w in texto if w in vc_ts]).\
        apply(lambda x : ' '.join(x))
    df_test_T['Conteos'] = df_test_T.nuevo_texto.str.split().apply(Counter)
    
    return df_train_T, df_test_T

def Laplace_gral(tabla):
    n = len(tabla[list(tabla.keys())[0]]) 
    for k in tabla.keys():
        registro = tabla[k]
        n_j = np.sum(list(registro.values()))
        for i in registro.keys():
            pb = (registro[i] + 1)/(n_j+n)
            tabla[k][i]=pb

def test(autores: list) -> tuple:
    df_train_T = new_df_train(autores)
    train_vocabulario,test_vocabulario = reduc_vocab(df_train_T, df_test)
    vocabulario = train_vocabulario.union(test_vocabulario)
    df_train_T, df_test_T = new_dfs(df_train_T, train_vocabulario, df_test, test_vocabulario)
    
    # Creación de variables

    # Vraible para autor
    # Ocurrencias de cada autor y conteos de ocurrencias y de número de autores
    oc_autor = Counter(df_train_T.autor)
    tot_oc_aut = np.sum(list(oc_autor.values()))
    A = mb.Var('A', set([autor for autor in oc_autor]))
    # Distribución P(A)
    n_= []
    for autor in oc_autor:
        n_.append(((autor,), oc_autor[autor] / tot_oc_aut))

    # Dicionario de valores de probabilidad
    dA = dict(n_)
    # Distribución de probabilidad
    PA = mb.Distrib(table = dA, columns=('A',))

    # Variable para tipos
    # Ocurrencias de cada tipo y conteos de ocurrencias y de número de tipos
    oc_tipo = Counter(df_train_T.tipo)
    tot_oc_tipo = np.sum(list(oc_tipo.values()))
    tot_tipos = len(oc_tipo)
    T = mb.Var('T', set([tipo for tipo in oc_tipo]))

    # Distribución P(T|A)
    # Ocurrencias (conteos) de cada combinación (tipo,autor)
    conteo_pares = Counter(zip(df_train_T.autor,df_train_T.tipo))
    # Combinaciones (tipo,autor)
    autores = list(set(df_train_T.autor))
    tipos = list(set(df_train_T.tipo))

    dT_A = {}

    for autor, tipo in product(*[autores,tipos]):
        par = (autor, tipo)
        ak = (autor,)
        
        if ak in dT_A.keys():
            if par in conteo_pares.keys():
                dT_A[ak][(tipo,)] = conteo_pares[par]
            else:
                dT_A[ak][(tipo,)] = 0 
        else:
            if par in conteo_pares.keys():
                dT_A[ak] = {(tipo,): conteo_pares[par]}
            else:
                dT_A[ak] = {(tipo,): 0}
                
    # Corrección de Laplace en el caso general
    # Se corrige la misma tabla que se senvía como argumento; no se crea una nueva.
    Laplace_gral(dT_A)

    PT_A = mb.CondDistrib(dT_A, (T.getName(),), (A.getName(),))
    
     # Palabras
    W = {}
    for w in vocabulario:    # vocabulario reducido
        W[w] = mb.Var(w,set([0,1]))
    
    # Combinaciones (tipo,autor)
    autores = list(set(df_train_T.autor))
    tipos = list(set(df_train_T.tipo))
    pares_ta = list(product(autores,tipos))
    
    # Conteos de palabras en nuevo_texto por pares (a,t) en el data frame de train
    conteo_w = dict(df_train_T.Conteos)
    pares_train = list(zip(df_train_T.autor,df_train_T.tipo))
    
    for j,k in enumerate(conteo_w.keys()):
        conteo_w[k] = {pares_train[j] : dict(conteo_w[k])}
        
    def check(palabra,pares_ta):
        pw_ = {}
        var = W[palabra]
        
        for par in pares_ta:
            cw_1 = 0   # conteos de presencia 
            cw_0 = 0   # y ausencia en 0
            it = 0     # total de pares (a,t) contabilizados
            
            for item in list(conteo_w.values()):  # checamos cada par (a,t) en el conjunto de train
                # print(i,list(item.keys())[0], end=' ')
                it += 1
                if par in item: # checamos si el par (a,t) de entrada tiene correspondencia en Train
                    if palabra in list(item.values())[0]: #checamos si la palabra existe en el par (a,t) de Train
                        cw_1 += 1
                    else:
                        cw_0 += 1  #debemos contar también la no existencia por si hay igualdad
            
            if cw_0 == cw_1: # la palabra aparece por igual en todos los pares Train, o bien, no hay pares Train
                pw_1 = 0.5   #corrección de Laplace que indica que la palabra puede o no estar por igual
                pw_0 = 0.5
                
            else:
                pw_1=(1+cw_1)/(len(var.getValues())+it) #corrección de Laplace en caso de que la palabra exista
                pw_0 = 1-pw_1
            
            pw_[par] = {(0,): pw_0, (1,): pw_1}
        pw_ = OrderedDict(sorted(pw_.items()))
        return pw_
            
        
    PW_AT = {}
    for w in W:    
        t = check(w,pares_ta)
        PW_AT[w] = mb.CondDistrib(dict(t), (W[w].getName(),), (A.getName(), T.getName()))
        
    vars_set = set([A,T] + [W[w] for w in W]) 
    descomp_set = set([PA, PT_A] + [PW_AT[w] for w in W])
    PATW = mb.Specification(vars_set, descomp_set)
    Q_PATW = mb.Question(PATW)
    
    dcont = df_test_T.loc[df_test['titulo'] == 'el caballo y el lobo', 'Conteos'].iloc[0]
    vocab_test = set(dcont)
    
    wit = []
    for w in W:
        if w in vocab_test:
            wit.append(1)
        else:
            wit.append(0)
    
    qn = Q_PATW.Query(vars=(A,), indep=tuple([W[w] for w in W]), indep_values=tuple(wit))       
    
    for autor in set(df_train_T.autor):
        conteos_autor = df_train_T[df_train_T['autor'] == autor].Conteos
        vocab_autor = set()
        for ca in conteos_autor:
            vocab_autor = vocab_autor.union(set(ca))
        print(f"Autor: {autor} \n\tVocabulario: {len(vocab_autor)} \n\tInterseccion: {len(vocab_test & vocab_autor)}\n\t p: {Q_PATW.Query(vars=(A,), indep=tuple([W[w] for w in W]), vars_values=(autor,),indep_values=tuple(wit))}")
    
    return qn
    
def tests():
    lista_autores = [
        ['jean de la fontaine','carlos fuentes'], 
        ['jean de la fontaine','alfonso reyes','esopo'],
        ['jean de la fontaine','alfonso reyes','esopo','carlos fuentes'],
        ['jean de la fontaine','alfonso reyes','esopo','carlos fuentes', 'gibrán jalil gibrán']
    ]
    
    for autores in lista_autores:  
        print(f"{test(autores)}\n")

tests()