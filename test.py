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
archivos = glob.glob('./Test/El Caballo y el Lobo.txt')
archivos,nombres = tp.carga_cuentos(archivos)
df_test = tp.lee_cuentos(archivos,test=True)

def df_autores(autores:list = None) -> pd.DataFrame:
    conds = []
    
    if not autores:
        return df_train
    
    for a in autores:
        conds.append(df_train['autor'] == a)
    
    filt = conds[0]
    for cond in conds[1:]:
            filt |= cond
    
    return df_train[filt]

def vocab(df:pd.DataFrame) -> set:
    s = df.texto.str.cat(sep=' ').split()
    vocabSet = set([palabra for palabra in s])
    return vocabSet

def new_dfs(autorVocab) -> tuple:
    df_train_T = df_train.copy()
    df_train_T['nuevo_texto'] = df_train_T.texto.str.split().\
        apply(lambda texto: [w for w in texto if w in autorVocab]).\
        apply(lambda x : ' '.join(x))
    df_train_T['Conteos'] = df_train_T.nuevo_texto.str.split().apply(Counter)
    
    df_test_T = df_test.copy()
    df_test_T['nuevo_texto' ]= df_test_T.texto.str.split().\
        apply(lambda texto: [w for w in texto if w in autorVocab]).\
        apply(lambda x : ' '.join(x))
    df_test_T['Conteos'] = df_test_T.nuevo_texto.str.split().apply(Counter)
    
    return df_train_T, df_test_T

# Corrección de Laplace en el caso general
# Se corrige la misma tabla que se senvía como argumento; no se crea una nueva.
def Laplace_gral(tabla):
    n = len(tabla[list(tabla.keys())[0]]) 
    for k in tabla.keys():
        registro = tabla[k]
        n_j = np.sum(list(registro.values()))
        for i in registro.keys():
            pb = (registro[i] + 1)/(n_j+n)
            tabla[k][i]=pb

def check(palabra, pares_ta, W, conteo_w):
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
       
def test(autores:list, nT:int):
    df_train_T = df_autores(autores)
    vocabTrain = vocab(df_train_T)
    
    df_train_T, df_test_T = new_dfs(vocabTrain)
    vocabTest =  vocab(df_test_T)
    
    # Vraible para autor
    # Ocurrencias de cada autor y conteos de ocurrencias y de número de autores
    oc_autor = Counter(df_train_T.autor)
    tot_oc_aut = np.sum(list(oc_autor.values()))
    tot_autores = len(oc_autor)
    A = mb.Var('A', set([autor for autor in oc_autor]))
    
    # Distribución P(A)
    n_= []
    for autor in oc_autor:
        n_.append(((autor,),oc_autor[autor]/tot_oc_aut))
    # Distribución de probabilidad
    dA = dict(n_)
    PA = mb.Distrib(table = dA, columns=('A',))
    
    # Variable para tipos
    # Ocurrencias de cada tipo y conteos de ocurrencias y de número de tipos
    oc_tipo = Counter(df_train_T.tipo)
    tot_oc_tipo = np.sum(list(oc_tipo.values()))
    tot_tipos = len(oc_tipo)
    T = mb.Var('T', set([tipo for tipo in oc_tipo]))
    
    # Distribución P(T|A)
    # Ocurrencias (conteos) de cada combinación (tipo,autor)
    conteo_pares = Counter(zip(df_train_T.autor, df_train_T.tipo))
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
    
    Laplace_gral(dT_A)
    
    PT_A = mb.CondDistrib(dT_A, (T.getName(),), (A.getName(),))
    
    vocabInter = vocabTest & vocabTrain
    vocabDif = vocabTrain - vocabTest 

    nuevoVocab = vocabInter.copy()
    r = len(nuevoVocab)
    qn = []
    xn = []
    
    for i in range(nT):
        df_train_T['nuevo_texto'] = df_train_T.texto.str.split().\
            apply(lambda texto: [w for w in texto if w in nuevoVocab]).\
            apply(lambda x : ' '.join(x))
        df_train_T['Conteos']=df_train_T.nuevo_texto.str.split().apply(Counter)

        # Palabras
        W = {}
        for w in nuevoVocab:    # vocabulario reducido
            W[w] = mb.Var(w,set([0,1]))

        # Combinaciones (tipo,autor)
        autores = list(set(df_train_T.autor))
        tipos = list(set(df_train_T.tipo))
        pares_ta = list(product(autores,tipos))
        
        # Conteos de palabras en nuevo_texto por pares (a,t) en el data frame de train
        conteo_w = dict(df_train_T.Conteos)
        pares_train = list(zip(df_train_T.autor,df_train_T.tipo))
        
        PW_AT = {}
        for w in nuevoVocab:    # vocabulario reducido
            t = check(w,pares_ta,W,conteo_w)
            PW_AT[w] = mb.CondDistrib(dict(t), (W[w].getName(),), (A.getName(), T.getName()))
            
        vars_set = set([A,T] + [W[w] for w in W]) 
        descomp_set = set([PA, PT_A] + [PW_AT[w] for w in W])
        PATW = mb.Specification(vars_set, descomp_set)
        
        Q_PATW = mb.Question(PATW)
    
        values_wi = []
        Wl = [W[w] for w in W]
        for w in Wl:
            if w in vocabInter:
                values_wi.append(1)
            else:
                values_wi.append(0)
                
        q = Q_PATW.Query(vars=tuple([A]), indep=tuple(Wl), indep_values=values_wi)
        print("i_{}: n-r = {}".format(i, len(nuevoVocab) - r))
        qn.append(q)
        xn.append(len(nuevoVocab))  
        
        if len(vocabDif) > 0:
            nuevoVocab.add(vocabDif.pop())
        else: 
            return xn, qn
    
    return xn, qn

def save(xn, qn, psn, jsonName:str):
    print(jsonName)
    data = {
        'xn': xn,
        'qn': qn,
        'psn': psn
    }
    
    with open(jsonName+'.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def presicion(qn) -> list:
    psn = []
    e_ps_n = 0
    for i in range(len(qn)):
        if qn[i][1][0] == 'jean de la fontaine':
            e_ps_n += 1 
            psn.append(e_ps_n / (i + 1))
        else:
            psn.append(e_ps_n / (i + 1))
    
    return psn
    
def tests():
    autoresS = set(df_train.autor)
    autoresS.remove('jean de la fontaine')

    autor1 = autoresS.pop()
    autor2 = autoresS.pop()
    testAutores = [
        ['jean de la fontaine'], 
        ['jean de la fontaine', autor1],
        ['jean de la fontaine', autor1, autor2]
    ]

    i = 1
    for autores in testAutores:
        xn, qn = test(autores, 20)
        print(qn[0])
        psn = presicion(qn)
        save(xn, qn, psn, 'test_'+str(i))
        i += 1


tests()
    