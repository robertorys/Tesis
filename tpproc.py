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
from nltk.stem import WordNetLemmatizer

####################################
#        cargado de Cuentos        #
####################################

def  load_sms(file: str) -> tuple:
    df = pd.read_csv(file)
    
    # Mezclar aleatoriamente los datos
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    # Calcular el índice de separación
    split_idx = int(0.8 * len(df))
    
    # Dividir los datos
    df_train = df[:split_idx]
    df_test = df[split_idx+1:-1]
    
    return df_train, df_test

def brigramspos(tokens) -> list:
    # Etiquetar las palabras con sus POS
    etiquetas_pos = nltk.pos_tag(tokens)
        
    pos = [epos[1] for epos in etiquetas_pos]
    return list(bigrams(pos))

def dfpp(df_train:pd.DataFrame, df_test:pd.DataFrame) -> tuple:
    stopWords = set(stopwords.words('english'))
    puntacion_extra = "¡¿“”``’'..."
    
    df_train_T = df_train.copy()
    
    df_train_T['Tokens'] = df_train_T.Message .\
        apply(lambda message: nltk.word_tokenize(message))
        
    df_train_T['Bigrams'] = df_train_T.Tokens .\
        apply(lambda tokens: brigramspos(tokens))
    
    df_train_T['Tokens'] = df_train_T.Tokens .\
        apply(lambda tokens: [
            palabra.lower() for palabra in tokens
            if palabra.lower() not in stopWords and palabra not in string.punctuation + puntacion_extra
        ])
    
    # Crear el lematizador
    lemmatizer = WordNetLemmatizer()
    df_train_T['Tokens'] = df_train_T.Tokens .\
        apply(lambda tokens: [lemmatizer.lemmatize(palabra) for palabra in tokens])
    
    df_test_T = df_test.copy()
    
    df_test_T['Tokens'] = df_test_T.Message .\
        apply(lambda message: nltk.word_tokenize(message))
        
    df_test_T['Bigrams'] = df_test_T.Tokens .\
        apply(lambda tokens: brigramspos(tokens))
    
    df_test_T['Tokens'] = df_test_T.Tokens .\
        apply(lambda tokens: [
            palabra.lower() for palabra in tokens
            if palabra.lower() not in stopWords and palabra not in string.punctuation + puntacion_extra
        ])
    
    df_test_T['Tokens'] = df_test_T.Tokens .\
        apply(lambda tokens: [lemmatizer.lemmatize(palabra) for palabra in tokens])
    
    return df_train_T, df_test_T
    
    
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
        puntacion_extra = '¡¿“”'
        tokens_limpios = nltk.pos_tag(tokens)
        tokens_limpios = [
            palabra.lower() for palabra in tokens
            if palabra.lower() not in stopWords and palabra not in string.punctuation + puntacion_extra
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