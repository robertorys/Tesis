import string
import sys
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import bigrams

####################################
#        cargado de Cuentos        #
####################################
    
def carga_cuentos_(files, encoding='utf-8'):
    stories = []    
    
    for fileName in files:
        with open(fileName, encoding=encoding) as f:
            content = f.readlines()
            content = [line.strip() for line in content]
        stories.append(content)
    
    return stories

def lee_cuentos_(stories, test=False):
    stopWords = set(stopwords.words('spanish'))
    
    storyInfo = []
    
    if not test:
        columnas = ['titulo','tipo','autor','tokens','bigramas']
    else:
        columnas = ['titulo','tokens','bigramas'] 
    
    for content in stories:
        if not test:
            title = ''
            title = content[0].lower()
            type = content[1].strip("[]").split()[0].lower()
            autor = content[2].lower()
            text = ''
            for line in content[3:-1]:
                text += line
        else:
            title = content[0].lower()
            text = ''
            for line in content[1:-1]:
                text += line
        
        tokens = nltk.word_tokenize(text)
        # Etiquetar las palabras con sus POS
        etiquetas_pos = nltk.pos_tag(tokens)
        
        pos = [epos[1] for epos in etiquetas_pos]
        bigramas = list(bigrams(pos))

        # Quitar stop words y signos de puntuación
        tokens_limpios = [
            palabra.lower() for palabra in tokens
            if palabra.lower() not in stopWords and palabra not in string.punctuation
        ]
        
        if not test:
            storyInfo.append([title,type,autor,tokens_limpios,bigramas])
        else:
            storyInfo.append([title,tokens_limpios,bigramas])  
        
        df = pd.DataFrame(storyInfo,columns=columnas)
    return df
            
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
        r = pd.DataFrame(texto,columns=['cadena'])
        r = r[r.cadena != '\n'].reset_index()
        r = r.cadena.str.translate(\
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
        r = r.to_frame()
        r = r[r.cadena != ''].reset_index()
        r = r.T
        r = r.loc['cadena']
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