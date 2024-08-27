import string
import sys
import pandas as pd
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
    # palabras demasiado frecuentes
    stop_words = set(stopwords.words('spanish'))
    # conjunto de palabras únicas --vocabulario
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
        # elimino las stopwords
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