import glob

simbolos = ['¿','?','-','.',',',':',';','¡','!',' ','\n']

    
def cargar_textos(dir) -> list:
    # Busca todos los archivos .txt en un directorio
    archivos = glob.glob(dir)

    # Cargar el contenido de todos los archivos
    textos = []
    for archivo in archivos:
        with open(archivo, 'r', encoding='utf-8') as f:
            textos.append(f.readlines())
    
    return textos

def cargar_cuentosTr(dir) -> dict:    
    textos = cargar_textos(dir)
    dict_textos = {}
    
    # dict_textos[nombre del cuento] = {'tipo':str, 'autor':str, 'texto':list}
    
    for texto in textos:

        nombre = ''
        for l in texto[0][0:]:
            if l != '\n':
                nombre = nombre + l
            else:
                break
            
        dict_textos[nombre] = {}
        
        tipo = ''
        for l in texto[1][1:]:
            if(l != ' '):
                tipo = tipo + l
            else:
                break
        dict_textos[nombre]['tipo'] = tipo
        
        autor = ''
        for l in texto[2][0:]:
            if l != '\n':
                autor = autor + l
            else:
                break

        dict_textos[nombre]['autor'] = autor
        
        aTexto = []
       
        for line in texto[3:]:
            w = ''
            for letter in line:
                
                if not letter in simbolos:
                    w = w + letter
                elif w != '':
                    aTexto.append(w)
                    w = ''
                
        dict_textos[nombre]['texto'] = aTexto[:len(aTexto)-1]
        
    
    return dict_textos

def cargar_palabras(textos) -> set:
    palabras = set()
    for key in textos.keys():
        palabras = palabras | set(textos[key]['texto'])
    return palabras

def conteos(textos, palabras) -> dict:
    conteo = {}
    conteo['tipo'] = {'minicuento':0, 'cuento':0, 'fábula':0}
    conteo['autor'] = {}
    conteo['palabra'] = {}
    
    for key in textos.keys():
        conteo['tipo'][]