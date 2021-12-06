######################################### 
# Funciones auxiliares para el 
# pre-procesamiento de texto de Wikipedia
#
# autor: Jorge Hermosillo
# Fecha: 01-dic-2021
# cursos: IA y Minería de Texto
##########################################
import sys
import string
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter, OrderedDict

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

####################################
#        cargado de Cuentos        #
####################################
def carga_cuentos(archivos,encoding='utf-8',tam='KB'): #"ISO-8859-1", MB
    file=[]
    nombres=[]
    suma = 0
    print("leyendo...")
    for i,filename in enumerate(archivos):
        with open(filename,encoding=encoding) as f:
            content = f.readlines()
        #quitamos los espacios en blanco extras
        content = [x.lower() for x in content] 
        if tam == 'MB':
            size=sys.getsizeof(content)//1048576 #tamaño en MB
        else:
            size=sys.getsizeof(content)//1024 #tamaño en KB            
        suma += size
        file.append(content)
        nombres.append(filename)
        # print(filename)

    print(f'tamaño del contenido de archivos cargados: \
            {suma} {tam}')
    return file, nombres

####################################
#      lectura de documentos       #
#            Cuentos               #
####################################
def lee_cuentos(cuentos,test=False):
    #palabras demasiado frecuentes
    stop_words = set(stopwords.words('spanish'))
    #conjunto de palabras únicas --vocabulario
    vocabulario = set()

    Cuentos = []
    docs = []
    Fin = False
    Tit = False
    Tip = False
    Aut = False
    suma = 0
    if not test:
        columnas = ['titulo','tipo','autor','texto']
    else:
        columnas = ['titulo','texto']        
    for h in cuentos:
        if not test:
            titulo = ' '.join(h[0].split())
            tipo = h[1].split()[0][1:]
            autor = ' '.join(h[2].split())
            texto = h[3:]
        else:
            titulo = ' '.join(h[0].split())
            texto = h[1:]            
        r=pd.DataFrame(texto,columns=['cadena'])
        r=r[r.cadena != '\n'].reset_index()
        r=r.cadena.str.translate(\
        str.maketrans('','',string.digits))\
        .str.translate(\
        str.maketrans('','',string.punctuation))\
        .str.replace('«','')\
        .str.replace('»','')\
        .str.replace('(','')\
        .str.replace(')','')\
        .str.replace('—','')\
        .str.replace('…','')\
        .str.replace('¿','')\
        .str.replace('¡','')\
        .str.replace('“','')\
        .str.replace('”','')\
        .str.strip()
        r=r.to_frame()
        r=r[r.cadena != ''].reset_index()
        r=r.T
        r=r.loc['cadena']
        palabras = r.tolist()[:-1]
        #elimino las stopwords
        text = [w for t in palabras for w in t.split() \
         if not w in stop_words and len(w)>2]
        #se genera el texto del documento
        doc = ' '.join(text)  
        if not test:
            Cuentos.append([titulo,tipo,autor,doc])
        else:
            Cuentos.append([titulo,doc])            
    df = pd.DataFrame(Cuentos,columns=columnas)
    return df

####################################
#        cargado de Wiki-docs      #
####################################
def carga_datos_wiki(archivos,encoding='utf-8',tam='KB'): #"ISO-8859-1", MB
    file=[]
    nombres=[]
    suma = 0
    print("leyendo...")
    for i,filename in enumerate(archivos):
        with open(filename,encoding=encoding) as f:
            content = f.read().split()
        #quitamos los espacios en blanco extras
        content = [x.strip().lower() for x in content] 
        if tam == 'MB':
            size=sys.getsizeof(content)//1048576 #tamaño en MB
        else:
            size=sys.getsizeof(content)//1024 #tamaño en KB            
        suma += size
        file.append(content)
        nombres.append(filename)
        # print(filename)

    print(f'tamaño del contenido de archivos cargados: \
            {suma} {tam}')
    return file, nombres

####################################
#      lectura de documentos       #
#            Wikipedia             #
####################################
def lee_docs_wiki(file, nombres):
    #palabras demasiado frecuentes
    stop_words = set(stopwords.words('spanish'))

    #conjunto de palabras únicas --vocabulario
    vocabulario = set()

    registros = []
    docs = []
    completo = False
    suma = 0
    for i,archivo in enumerate(file):
        for j,cadena in enumerate(archivo):
            if 'id=' in cadena and completo == False:
                id_ = cadena[4:-1]
            elif 'dbindex=' in cadena and completo == False:
                inicio = j+1
            elif 'doc>' in cadena and completo == False:
                fin = j-1
                completo = True
            if completo:
                x = archivo[inicio:fin]
                r=pd.DataFrame(x,columns=['cadena'])
                r=r.cadena.str.translate(\
                        str.maketrans('','',string.digits))\
                        .str.translate(\
                       str.maketrans('','',string.punctuation))\
                .str.replace('«','')\
                .str.replace('»','').str.replace('(','')\
                .str.replace(')','').str.strip()
                palabras = r.tolist()
                #elimino las stopwords
                texto = [w for w in palabras \
                         if not w in stop_words and len(w)>2]
                #genero el texto del documento
                doc = ' '.join(texto)  
                registros.append([id_,doc,i])
                completo = False
                suma += 1
        print('archivo {0} contiene {1}\
        documentos \n'.format(nombres[i],suma) )
        suma=0
        docs.append(registros)
        registros=[]
    return docs

#####################################
#  graficación de palabras por doc  #
#Generamos los vectores que vamos a # 
# usar en los gráficos de barras:   #
# * x: contiene la enumeración      #
#      de los documentos            #
# * y: contiene sus respectivos     #
#       totales de palabras         #
#####################################
def grafica_palabras_porDoc(datos,nombre='barras',ancho=0.8):
    #ordena los datos en orden descendente y saca el promedio.
    promedio = datos['Total'].mean()
    print('Promedio de palabras por documento en el corpus: {}'.format(promedio))
    
    #obtiene los valores de x y y
    x=np.arange(len(datos.index.values))
    etiquetas=[]
    
    for e in datos.index.values:
        etiquetas.append(str(e))
    
    y=datos['Total'].values
    print(y[:10])
    
    #define el área de dibujo
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_facecolor('white')
    plt.grid(False)
    ax.tick_params(axis='x', labelsize=6)

    #graficación
    #ancho = 0.8 #ancho de las barras
    ax.bar(x - ancho/2, y, ancho, label='Totales')
    ax.axhline(y=promedio, \
               color='r', \
               linestyle='--', \
               label='Promedio')

    # Etiquetas, títulos, etc.
    ax.set_ylabel('Palabras')
    ax.set_title('Número de palabras por documento')
    ax.set_xticks(x)
    plt.xticks(rotation=90)
    ax.set_xticklabels(etiquetas)
    ax.legend()
    #plt.savefig('img/'+nombre+'.pdf')
    plt.show()
    return

def grafica_docs(df,titulo='Documentos'):
    #""" Obtención de valores"""
    docs_0=df[df.clase==0]
    docs_1=df[df.clase==1]

    #"""Areas de Graficacion y visualizacion de los datos"""
    fig,ax = plt.subplots(figsize=(5,5))

    #"""Documentos en clase 0"""
    ax.scatter(docs_0.c0, docs_0.c1,
               facecolor='royalblue', 
               marker='o', 
               edgecolor='blue',
               s=20,
               alpha=0.5,
               label='Docs_0')

    #"""Documentos en clase 1"""
    ax.scatter(docs_1.c0, docs_1.c1,
               facecolor='orangered', 
               marker='o', 
               edgecolor='red',
               s=20,
               alpha=0.5,
               label='Docs_1')
    plt.title(titulo)
    plt.xlabel('c0')
    plt.ylabel('c1')
    ax.legend()
    return ax

def anota_docs(ax,df):
    docs_0=df[df.clase==0]
    d0 = docs_0[['c0','c1']].values.tolist()
    e0 = df[df['clase']==0]['doc_id'].tolist()

    docs_1=df[df.clase==1]
    d1 = docs_1[['c0','c1']].values.tolist()
    e1 = df[df['clase']==1]['doc_id'].tolist()

    #""" Anotación de algunos puntos """
    azules=[]
    rojos=[]
    for i, txt in enumerate(e0[:40]):
        if txt == '1023628' or  txt=='1035967'\
        or txt == '1024447':
            azules.append([d0[i][0], d0[i][1]])
            ax.annotate(txt, (d0[i][0], d0[i][1]))
    for i, txt in zip(range(80),e1[:80]):
        if txt == '1891029' or txt == '1894599':
            rojos.append([d1[i][0], d1[i][1]])
            ax.annotate(txt, (d1[i][0], d1[i][1]), color='red')
    azules=np.array(azules)
    ax.scatter(azules[:,0],azules[:,1],
               marker='^',
               facecolor='blue', 
               edgecolor='black',s=80)
    rojos=np.array(rojos)
    ax.scatter(rojos[:,0],rojos[:,1],
               marker='H',
               facecolor='red', 
               edgecolor='black',s=80)
    return

def grafica_palabras(voc,titulo,color='red'):  
    if isinstance(voc,pd.DataFrame):
        try:
            X=voc.c0
            Y=voc.c1
        except:
            raise ValueError('Tipo de data frame invalido')
            return
    elif isinstance(voc,np.ndarray):
        try:
            X=voc[:,0]
            Y=voc[:,1]
        except:
            raise ValueError('Tipo de numpy array invalido')
            return
    else:
        print('tipo de datos invalido')
        return
    
    """Areas de Graficacion y visualizacion de los datos"""
    fig,ax = plt.subplots(figsize=(5,5))
    
    if color =='red':
        c='orange'+color
    elif color == 'blue':
        c='royal'+color
    else:
        c=color

    """Vocabulario"""
    ax.scatter(X, Y,
               facecolor=c, 
               marker='o', 
               edgecolor=color,
               s=20,
               alpha=0.5,
               label='Palabras únicas')

    plt.title(titulo)
    plt.xlabel('c0')
    plt.ylabel('c1')
    ax.legend()
    return ax
    
def dist_pts(pts,id_):
    dist=[]
    if len(id_) != len(pts):
        print('error!: el número de etiquetas \
                debe corresponder con el de puntos')
        return dist
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            for x in range(len(pts[i])):
                s=np.square(pts[i][x]-pts[j][x])
            d = np.sqrt(s)
            dist.append((id_[i],id_[j],d))
    dist=sorted(dist,key=lambda x: x[2])
    return dist

def palabras_comunes(df):
    Palabras=df['Palabras'].values.tolist()
    docs = df.doc_id.values
    lista=[]
    for i in range(len(Palabras)):
        lista.append((docs[i],Palabras[i]))
    palco=[]
    nopalco=[]
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            palco.append(((lista[i][0],lista[j][0]),\
                          lista[i][1] & lista[j][1]))
            nopalco.append(((lista[i][0],lista[j][0]),\
                            lista[i][1] | lista[j][1] - \
                            lista[i][1] & lista[j][1]))

    palco=sorted(palco,key=lambda x: len(x[1]),reverse=True)
    nopalco=sorted(nopalco,key=lambda x: len(x[1]),reverse=True)
    npd = pd.DataFrame(nopalco).drop(columns=[0])
    paldoc=pd.DataFrame(palco)
    paldoc=pd.concat([paldoc,npd],ignore_index=True, sort=False,axis=1)
    paldoc.columns=['_ids','PalCom','PalNoCom']
    return paldoc

def get_pts(df,vocabulario,metodo):
    if not isinstance(metodo,pd.core.frame.DataFrame):
        print('Error: el metodo {}\
        no es de tipo <pandas.core.frame.DataFrame>'.format(metodo))
        return
    if not isinstance(vocabulario,OrderedDict):
        print('Error: el vocabulario no es de tipo <collections.OrderedDict>')
        return
    try:
        lp=df.Texto.apply(lambda x: x.split()).values
    except ValueError:
            print('Error en el data frame de documentos')
            return
    pts={}
    lista_=[]
    for i,l in enumerate(lp):
        for p in l:
            i = vocabulario[p]
            pts[p]=metodo.loc[i].values
        lista_.append(pts)
        pts={}
    ptsMETODO=pd.DataFrame(df['doc_id'],columns=['doc_id'])
    ptsMETODO['Puntos']=pd.Series(lista_)
    return ptsMETODO

def geometria_pts(pts):
    dist_df=[]
    dicos=pts['Puntos'].values.tolist()
    dist=[]
    m_pts=[]
    m_df=[]
    centroides=[]
    #matriz de puntos
    for d in dicos:
        palabras=[*d.keys()]
        for i,p in enumerate(palabras):
            p1=d[palabras[i]]
            m_pts.append(p1)
        m_pts=np.array(m_pts)
        m_df.append(m_pts)        
        #calcula el centroide
        centroide=m_pts.sum(axis=0)/len(m_pts)
        centroides.append([centroide])
        #distancias al centroide
        for p in m_pts:            
            dis = np.sqrt(np.square(p[0]-centroide[0])\
                         +np.square(p[1]-centroide[1]))
            dist.append(dis)
        distancias=np.array(sorted(dist))
        dist_df.append([distancias])
        m_pts=[]
        dist=[]

    return m_df,centroides,dist_df

def extrae_datos(df,voc,metodo):
    pts = get_pts(df,voc,metodo)
    #print(pts.head())
    matrices,centroides,distancias= geometria_pts(pts)
    df1=pd.DataFrame(matrices,columns=['puntos'])
    df2=pd.DataFrame(centroides,columns=['centroides'])
    df3=pd.DataFrame(distancias,columns=['distancias'])
    data=pd.concat([df1,df2,df3],axis=1)
    data['doc_id']=pts['doc_id']
    data=data[['doc_id','puntos','centroides','distancias']]
    return data

def grafica_puntos(df,centroides='',ds=['1023628', '1024447', '1035967', '1891029', '1894599'],titulo='Palabras de documentos'):
    col=set(df.columns.tolist())
    if not set(['puntos','centroides','distancias']).issubset(col):
        print('error en el data frame')
        return
    docs=df.doc_id.values
    X=df.puntos.values
    C=df.centroides.values
    lista=[]
    for i in range(len(docs)):
        lista.append((docs[i],(X[i],C[i])))
    lista=sorted(lista,key=lambda x: x[0])
    dico=OrderedDict(lista)

    docs=[]
    X=[]
    C=[]
    for k in ds:
        docs.append(k)
        X.append(dico[k][0])
        C.append(dico[k][1])
        
    docus=['1023628', '1024447', '1035967', '1891029', '1894599']
    colors=['blue','royalblue','cyan','red','orangered']

    dicolor = {k: v for k, v in zip(docus,colors)}
    colores = list(map(dicolor.__getitem__, docs))

    marcadores=['o','D','s','^','*']

    """Areas de Graficacion y visualizacion de los datos"""
    fig,ax = plt.subplots(figsize=(5,5))

    """Palabras"""
    if centroides == '':
        for i,x in enumerate(X):
            ax.scatter(x[:,0], x[:,1],
                       facecolor=colores[i], 
                       marker=marcadores[i], 
                       edgecolor=colores[i],
                       s=20,
                       alpha=0.5,
                       label=docs[i])
            ax.scatter(C[i][0], C[i][1],
                       facecolor=colores[i], 
                       marker='$\\bigoplus$', 
                       edgecolor=colores[i],
                       s=50,
                       alpha=0.9)
            ax.annotate(docs[i], (C[i][0], C[i][1]))
    else:
        for i,x in enumerate(X):
            ax.scatter(C[i][0], C[i][1],
                       facecolor=colores[i], 
                       marker='$\\bigoplus$', 
                       edgecolor=colores[i],
                       s=50,
                       alpha=0.9)
            ax.annotate(docs[i], (C[i][0], C[i][1]))
    plt.title(titulo)
    plt.xlabel('c0')
    plt.ylabel('c1')
    plt.grid(True)
    ax.legend()

    return ax

def distribucion_dist(df,ds=['1023628', '1024447', '1035967', '1891029', '1894599'],titulo='Distribucion de distancias'):
    col=set(df.columns.tolist())
    if not set(['puntos','centroides','distancias']).issubset(col):
        print('error en el data frame')
        return
    docs=df.doc_id.values
    D=df.distancias.values
    
    lista=[]
    for i in range(len(docs)):
        lista.append((docs[i],D[i]))
    lista=sorted(lista,key=lambda x: x[0])
    dico=OrderedDict(lista)

    docs=[]
    dist=[]
    for k in ds:
        docs.append(k)
        dist.append(np.round(dico[k],2))
    
    docus=['1023628', '1024447', '1035967', '1891029', '1894599']
    colors=['blue','royalblue','cyan','red','orangered']

    dicolor = {k: v for k, v in zip(docus,colors)}
    colores = list(map(dicolor.__getitem__, docs))
    
    """Areas de Graficacion y visualizacion de los datos"""
    fig,ax = plt.subplots(figsize=(8,5))
    
    for i,l in enumerate(dist):
        n=len(l)
        pasos=np.array(range(n))/n
        datos=np.array(list(map(lambda x,y:[x,y],l,pasos)))
        ax.plot(datos[:,0],datos[:,1],
                ls='--',
                color=colores[i],
                linewidth=1,
                label=docs[i])
    plt.title(titulo)
    plt.xlabel('distancia de cada palabra al centroide')
    plt.ylabel('proporción')
    plt.grid(True)
    ax.xaxis.grid(True, which='minor')
    ax.yaxis.grid(True, which='minor')
    ax.grid(which='major', color='gray', linestyle='-')
    ax.grid(which='minor', color='grey', linestyle='--')
    ax.legend()

    return ax

def get_dataFrame(D,df):    
    dp = pd.DataFrame(data = D)
    dp['doc_id']=df['doc_id']

    cols = dp.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    dp=dp[cols]
    return dp

def get_dataFrame_WiDocs(docs):
    docs_0 = pd.DataFrame(docs[0],\
                          columns = ['doc_id','Texto','Clase'])
    docs_1 = pd.DataFrame(docs[1],\
                          columns = ['doc_id','Texto','Clase'])
    df = pd.concat([docs_0, docs_1],\
                   ignore_index=True, sort=False)
    df=df.drop(columns=['Clase'])
    
    types=df['Texto'].str.split(' ',\
                                expand=True).stack().unique()

    Textos=df.Texto.values

    #Creamos las oraciones, este será la entrada del modelo W2V
    frases = [s.split() for s in Textos]

    documentos= []

    #Concatenamos todas las oraciones en una sola lista
    for f in frases:
        documentos.append(f)

    print('Hay {} documentos y {} palabras únicas'.\
          format(len(documentos),len(types)))
    return df,documentos

def grafica_vr(datos,nombre='Explained Variance Ration',ancho=0.8):
    #ordena los datos en orden descendente y saca el promedio.
    
    #obtiene los valores de x y y
    x=np.arange(len(datos))
    etiquetas=x
    
    y=datos
    
    #define el área de dibujo
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_facecolor('white')
    plt.grid(False)
    ax.tick_params(axis='x', labelsize=6)

    #graficación
    #ancho = 0.8 #ancho de las barras
    ax.bar(x - ancho/2, y, ancho, label='Variance Ratio')

    # Etiquetas, títulos, etc.
    ax.set_ylabel('VR')
    ax.set_xlabel('Componente')
    ax.set_title(nombre)
    ax.set_xticks(x)
    plt.xticks(rotation=90)
    ax.set_xticklabels(etiquetas)
    ax.legend()
    #plt.savefig('img/'+nombre+'.pdf')
    plt.show()
    return ax

def distribucion_vr(D,titulo='Distribucion de Varianzas'):
    
    d=[]
    y=0
    for x in D:
        y+=x
        d.append(y)
    
    """Areas de Graficacion y visualizacion de los datos"""
    fig,ax = plt.subplots(figsize=(8,5))
    
    pasos=range(len(D))
    datos=np.array(list(map(lambda x,y:[x,y],pasos,d)))
    ax.plot(datos[:,0],datos[:,1],
            ls='--',
            color='green',
            linewidth=1,
            label='Contribucion acumulada')
    plt.title(titulo)
    plt.xlabel('Componente')
    plt.ylabel('Proporción')
    plt.grid(True)
    ax.xaxis.grid(True, which='minor')
    ax.yaxis.grid(True, which='minor')
    ax.grid(which='major', color='gray', linestyle='-')
    ax.grid(which='minor', color='grey', linestyle='--')
    ax.legend()

    return ax

def get_representativos(df,numero=100):
    cols = [col for col in df.columns[:numero+1]]
    rep = df.loc[:, cols]
    return rep

def dist_docs(df):
    dist=[]
    id_=df.doc_id.values
    datos=df.drop(columns=['doc_id'])
    pts=datos.values
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            d = np.sqrt(np.sum(np.square(pts[i]-pts[j])))
            dist.append((id_[i],id_[j],d))
    dist=sorted(dist,key=lambda x: x[2])
    return np.array(dist)

def dist_docs_w2v(df):
    dist=[]
    id_=df.doc_id.values
    pts=df.W2V.values
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            d = np.sqrt(np.sum(np.square(pts[i]-pts[j])))
            dist.append((id_[i],id_[j],d))
    dist=sorted(dist,key=lambda x: x[2])
    return np.array(dist)

def dist_vecinos(id_docu,df):
    dist=[]
    candidato = df[df['doc_id']==id_docu]
    candidato = candidato.iloc[:,1].values[0]
    fila=df.index[df['doc_id'] == id_docu].tolist()
    pts=df.drop(df.index[fila])
    id_=pts.doc_id.values
    pts=pts.iloc[:,1].values

    for i in range(len(pts)):
        d = np.sqrt(np.sum(np.square(candidato-pts[i])))
        dist.append((id_docu,id_[i],d))
    dist=sorted(dist,key=lambda x: x[2])
    return dist

def k_vecinos_mas_cercanos(docus,df,k=1):
    l=docus.doc_id.values
    vec=OrderedDict()
    for id_ in l:
        d=dist_vecinos(id_,df)
        for i in range(k):
            if i==0:
                vec[id_]=[[d[i][1],d[i][2]]]
            else:
                vec[id_].append([d[i][1],d[i][2]])
    return vec

def vecinos_mas_cercanos(df,distancias):
    l=df.doc_id.values
    vec=OrderedDict()
    for id_ in l:
        for i,d in enumerate(distancias):
            if id_ == d[0]:
                vecino=d[1]
                if id_ not in vec.keys():
                    vec[id_]=[(vecino,d[2])]
                else:
                    vec[id_].append((vecino,d[2]))
            elif id_== d[1]:
                vecino=d[0]
                if id_ not in vec.keys():
                    vec[id_]=[(vecino,d[2])]
                else:
                    vec[id_].append((vecino,d[2]))
    return vec

def lee_data_frame(nombre='datos/data_frame_curso.pkl'):
    df=pd.read_pickle(nombre)
    df=df.drop(columns=['Palabras','Total','Conteos'])
    df.index = range(len(df.index))
    
    types=df['Texto'].str.split(' ', \
                                expand=True).stack().unique()

    Textos=df.Texto.values

    #Creamos las oraciones, este será la entrada del modelo W2V
    frases = [s.split() for s in Textos]

    documentos= []

    #Concatenamos todas las oraciones en una sola lista
    for f in frases:
        documentos.append(f)

    print('Hay {} documentos y {} palabras\
    únicas'.format(len(documentos),len(types)))
    return df,documentos

def modela_documentos_rep(df):
    id_=df.doc_id.values
    datos=df.drop(columns=['doc_id'])
    datos=datos.values
    dx=[]
    for i,doc_id in enumerate(id_):
        dx.append((doc_id,datos[i]))
    do=pd.DataFrame(dx,columns=['doc_id','Vectores'])
    return do


def modela_documentos(df,w2v):
    docs=df.doc_id.values
    textos=df.Texto.str.split(' ').values.tolist()
    d=[]
    Dx=[]
    for i,texto in enumerate(textos):
        for w in texto:
            e=w2v[w]
            d.append(e)
        d=np.array(d)
        dx=np.sum(d,axis=0)/len(d)
        Dx.append([docs[i],dx])
        d=[]
    do=pd.DataFrame(Dx,columns=['doc_id','W2V'])
    return do

def modela_documentos_w(vm,df,voc):
    df_t=df.drop(columns=['Total','Conteos','Palabras','clase'])
    id_=df_t.doc_id.values
    textos=df_t.Texto.apply(lambda x: x.split()).values.tolist()
    datos=vm.values
    dx=[]
    ex=[]
    for i,doc_id in enumerate(id_):
        for palabra in textos[i]:
            j=voc[palabra]
            e=datos[j]
            ex.append(e)
        ex=np.array(ex)
        ex=np.sum(ex,axis=0)/len(ex)
        dx.append((doc_id,ex))
        ex=[]
    do=pd.DataFrame(dx,columns=['doc_id','Vectores'])
    return do

def mas_RAM_porfavor():
    from sklearn.feature_extraction import DictVectorizer
    from collections import Counter, OrderedDict
    from sklearn.decomposition import PCA
    
    df=pd.read_pickle('datos/data_frame_8K.pkl')
    df.index = range(len(df.index))
    df['Palabras']=df['Texto'].apply(lambda x: x.split())
    df['Total']=df['Palabras'].apply(lambda x: len(x))
    df['Conteos']=df['Palabras'].apply(lambda x: Counter(x))

    docs = df.Conteos.tolist()
    v = DictVectorizer(sparse=False)
    X = v.fit_transform(docs)
    pca = PCA(svd_solver='auto')
    Y_pca = pca.fit_transform(X)
    return
