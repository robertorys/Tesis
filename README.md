# Proyecto-IA
Archivos del proyecto de fin de curso

## Contenido de este repositorio
En este repositorio encontrarán:
* Notebook del proyecto, donde se han agregado algunas celdas para reducir el vocabulario de 4763 a 1142 palabras.
* scripts de trabajo:
  - mib.py (motor de inferencia)
  - tpproc.py (lectura y pre-procesamiento de archivos de texto)
* vocabulario original
* Las carpetas con los archivos de texto de entrenamiento y prueba
* Los archivos de entrenamiento (carpeta Train) sirven para calcular estadísiticas (tablas de probabilidad) de las distribuciones de sus variables, en función del modelo que elijan proponer.
* Los archivos de prueba (carpeta Test) son los que deben de utilizar para responder a las preguntas planteadas como parte del proyecto.

## Notas importantes:
* La notebook se puede ejecutar directamente dando click en el archivo aquí arriba y luego click en la liga: "Open in Colab".
* Deben subir los scripts de trabajo y el archivo del vocabulario original directamente a colab.
* *Las carpetas Train y Test se subirán automáticamente al correr las celdas de la notebook*
* El vocabulario original (voc_pry.txt) fue construido a partir de los archivos conjuntos (Train y Test).
* La reducción del vocabulario tal y como se propone en la notebook de este repositorio, asume que sólo las palabras que se conservan deben de utilizarse tanto para el entrenamiento como para la prueba (respuestas a preguntas).
* A partir de la notebook proporcionada, se sugiere seguir la metodología vista en clase, utilizando como enfoque de solución algo similar al modelo de filtrado de Spam.
* Deben de ser capaces de calcular las distribuciones de su modelo (descomposición de la distribución conjunta). 
* Donde puede haber dificultades es a la hora de la inferencia, debido a la alta dimensionalidad del espacio de variables. 

## Entregables del proyecto:
* Un PDF con su propuesta de modelo, incluyendo la fase de Descripción.
* La notebook hasta donde hayan podido realizar.
