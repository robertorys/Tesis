Temas:
1.  Capitulo 1 (Razonamiento plausible):
	1. Razonamiento deductivo y plausible
2. Capitulo 2 (Reglas cuantitativas):
	1. Regla del producto - 21
	2. Regla de la suma - 26

#Introducción
La escritura real comenzó como notas para una serie de conferencias dadas en la Universidad de Stanford en 1956. Expuesto en el entonces nuevo y apasionante trabajo de George Pólya sobre “Matemáticas y razonamiento plausible”. Diseccionó nuestro “sentido común” intuitivo en un conjunto de desiderata cualitativos elementales y demostró que los matemáticos los habían estado utilizando todo el tiempo para guiar las primeras etapas del descubrimiento, que necesariamente preceden al hallazgo de una prueba rigurosa. Los resultados fueron muy parecidos a los del “Arte de conjetura” de James Bernoulli (1713), desarrollado analíticamente por Laplace a finales del siglo XVIII; pero Pólya pensaba que el parecido era sólo cualitativo.

Sin embargo, Pólya demostró este acuerdo cualitativo con un detalle tan completo y exhaustivo que sugiere que debe haber más. Afortunadamente, los teoremas de consistencia de R. T. Cox fueron suficientes para resolver las cosas; cuando se les añadían las condiciones cualitativas de Pólya, el resultado era una prueba de que, si los grados de plausibilidad se representan mediante números reales, entonces existe un conjunto único de reglas cuantitativas para realizar la inferencia. Es decir, cualquier otra regla cuyos resultados entren en conflicto con ellas violará necesariamente un deseado (desiderátum) elemental (y casi ineludible) de racionalidad o coherencia.

Pero el resultado final fue justo el inicio de la reglas de la teoría de la probabilidad, dadas ya por Bernoulli y Laplace. La nueva característica importante fue que estas reglas ahora se consideraban principios excepcionalmente válidos de la lógica en general, sin hacer ninguna referencia al "azar" o a las "variables aleatorias"; por lo que su ámbito de aplicación es mucho mayor de lo que se suponía en la teoría de probabilidad convencional desarrollada a principios del siglo XX. Como resultado, la distinción imaginaria entre “teoría de la probabilidad” e “inferencia estadística” desaparece, y el campo logra no sólo unidad lógica y simplicidad, sino mucho mayor poder técnico y flexibilidad en las aplicaciones. 
Por lo tanto, en las conferencias del escritor, el énfasis estuvo en la formulación cuantitativa del punto de vista de Pólya, de modo que pudiera usarse para problemas generales de inferencia científica, casi todos los cuales surgen de información incompleta y no de “aleatoriedad”.

Por "inferencia" nos referimos simplemente: razonamiento deductivo siempre que se dispone de suficiente información para permitirlo; razonamiento inductivo o plausible cuando (como ocurre casi invariablemente en problemas reales) la información necesaria no está disponible. Pero si un problema puede resolverse mediante razonamiento deductivo, la teoría de la probabilidad no es necesaria para ello; por tanto, nuestro tema es el procesamiento óptimo de información incompleta.

Pero antes de que se puedan utilizar los métodos bayesianos, se debe desarrollar un problema más allá de la “fase exploratoria” hasta el punto en que tenga suficiente estructura para determinar todos los aparatos necesarios (un modelo, espacio muestral, espacio de hipótesis, probabilidades previas, distribución muestral). Casi todos los problemas científicos pasan por una fase exploratoria inicial en la que necesitamos hacer inferencias, pero los supuestos frecuentistas no son válidos y el aparato bayesiano aún no está disponible. De hecho, algunos de ellos nunca salen de la fase exploratoria. Los problemas a este nivel exigen medios más primitivos para asignar probabilidades directamente a partir de nuestra información incompleta.

Para ello, el Principio de Máxima Entropía tiene actualmente la justificación teórica más clara y el más desarrollado computacionalmente, con un aparato analítico tan potente y versátil como el bayesiano. Para aplicarlo debemos definir un espacio muestral, pero no necesitamos ningún modelo ni distribución muestral. En efecto, ¿la maximización de la entropía crea un modelo para nosotros a partir de nuestros datos, que resulta óptimo según tantos criterios diferentes? que es difícil imaginar circunstancias en las que no se quiera utilizarlo en un problema en el que tenemos un espacio muestral pero no un modelo.
Los métodos bayesianos y de máxima entropía difieren en otro aspecto. Ambos procedimientos producen inferencias óptimas a partir de la información contenida en ellos, pero podemos elegir un modelo para el análisis bayesiano; esto equivale a expresar algún conocimiento previo (o alguna hipótesis de trabajo) sobre el fenómeno que se observa. Por lo general, tales hipótesis se extienden más allá de lo que es directamente observable en los datos y, en ese sentido, podríamos decir que los métodos bayesianos son (o al menos pueden ser) especulativos. Si las hipótesis adicionales son ciertas, entonces esperamos que los resultados bayesianos mejoren con la entropía máxima; si son falsas, las inferencias bayesianas probablemente serán peores.

Por otro lado, la Máxima Entropía es un procedimiento no especulativo, en el sentido de que no invoca hipótesis más allá del espacio muestral y la evidencia que se encuentra en los datos disponibles. Por lo tanto, predice sólo hechos observables (funciones de observaciones pasadas o futuras) en lugar de valores de parámetros que pueden existir sólo en nuestra imaginación. Es justamente por esa razón que Maximum Entropy es la herramienta apropiada (más segura) cuando tenemos muy poco conocimiento más allá de los datos sin procesar; nos protege contra sacar conclusiones no respaldadas por los datos. Pero cuando la información es extremadamente vaga, puede resultar difícil definir un espacio muestral apropiado y uno puede preguntarse si se pueden encontrar principios aún más primitivos que la máxima entropía. 
## Capitulo 1 (Razonamiento plausible)
### Razonamiento deductivo y plausible
Supongamos que en una noche oscura un policía camina por una calle aparentemente desierta; pero de repente escucha una alarma antirrobo, mira al otro lado de la calle y ve una joyería con una ventana rota. Entonces, un caballero con una máscara sale arrastrándose por la ventana rota, llevando una bolsa que resulta estar llena de joyas caras. El policía no duda en decidir que este señor es deshonesto. Pero ¿mediante qué proceso de razonamiento llega a esta conclusión? Primero echemos un vistazo pausado a la naturaleza general de tales problemas.

Un momento de reflexión deja claro que la conclusión de nuestro policía no fue una deducción lógica de la evidencia; porque puede haber habido una explicación perfectamente inocente para todo. Podría ser, por ejemplo, que este señor fuera el dueño de la joyería y regresara a casa de una fiesta de disfraces y no tuviera la llave consigo. Pero justo cuando pasaba por su tienda, un camión que pasaba arrojó una piedra por la ventana; y él sólo estaba protegiendo su propia propiedad.

Ahora bien, si bien el proceso de razonamiento del policía no fue una deducción lógica, concederemos que tuvo cierto grado de validez. Las pruebas no demostraban con certeza la deshonestidad del caballero, pero sí la hacían extremadamente plausible. Este es un ejemplo de un tipo de razonamiento en el que todos nos hemos vuelto más o menos competentes, necesariamente, mucho antes de estudiar teorías matemáticas. Difícilmente podemos pasar una hora de vigilia sin enfrentarnos a alguna situación (por ejemplo, ¿lloverá o no?) en la que no tenemos suficiente información para permitir el razonamiento deductivo; pero aun así debemos decidir inmediatamente qué hacer.

Pero a pesar de su familiaridad, la formación de conclusiones plausibles es un proceso muy sutil, probablemente nadie ha realizado nunca un análisis del proceso que otros encuentren completamente satisfactorio. Todas las discusiones sobre estas cuestiones comienzan dando ejemplos del contraste entre el razonamiento deductivo y el razonamiento plausible. Como generalmente se atribuye al Organon de Aristóteles (siglo IV a. C.)†, el razonamiento deductivo (apodeixis) puede analizarse en última instancia mediante la aplicación repetida de dos fuertes silogismos: 

If A is true, then B is true
A is true 
Therefore, B is true

(Modus Ponens)
p -> q
p
therefore q

y su inverso:

If A is true, then B is true
B is false 
Therefore, A is false

(Modus Tollens)
p -> q
~q
therefore ~p

Éste es el tipo de razonamiento que nos gustaría utilizar todo el tiempo; pero como se señaló, en casi todas las situaciones que enfrentamos no tenemos el tipo de información adecuado para permitir este tipo de razonamiento. Recurrimos a silogismos más débiles (epagoge):

If A is true, then B is true
B is true
Therefore, A becomes more plausible

La evidencia no prueba que A sea verdadera, pero la verificación de una de sus consecuencias sí nos da más confianza en A. Por ejemplo, dado

A ≡ "Empezará a llover a más tardar a las 10 de la mañana."
B ≡ "El cielo se nublará antes de las 10 de la mañana."

Observar las nubes a las 9:45 a. m. no nos da una certeza lógica de que seguirá la lluvia; sin embargo, nuestro sentido común, obedeciendo al débil silogismo, puede inducirnos a cambiar nuestros planes y comportarnos como si creyéramos que así será, si esas nubes son lo suficientemente oscuras.

Este ejemplo muestra también que la premisa mayor, “Si A, entonces B”, expresa B sólo como una consecuencia lógica de A; y no necesariamente una consecuencia física causal, que sólo podría ser efectiva en un momento posterior. La lluvia a las 10 a.m. no es la causa física de las nubes a las 9:45 a.m. Sin embargo, la conexión lógica adecuada no está en la dirección causal incierta (nubes ⇒ lluvia), sino más bien (lluvia ⇒ nubes), que es cierta, aunque no causal.

Destacamos desde el principio que lo que nos interesa aquí son las conexiones lógicas, porque algunas discusiones y aplicaciones de la inferencia han caído en errores graves al no ver la distinción entre implicación lógica y causalidad física. La distinción es analizada con cierta profundidad por H. A. Simon y N. Rescher (1966), quienes señalan que todos los intentos de interpretar la implicación como expresión de la causalidad física fracasan por la falta de contraposición expresada por el segundo silogismo. Es decir, si intentáramos interpretar la premisa mayor como "A es la causa física de B", entonces difícilmente podríamos aceptar que "no-B es la causa física de no-A". 

Otro silogismo débil, que todavía utiliza la misma premisa mayor, es:

If A is true, then B is true
A is false
Therefore, B becomes less plausible

En este caso, la evidencia no prueba que B sea falsa; pero se ha eliminado una de las posibles razones por las que esto es cierto, por lo que nos sentimos menos seguros acerca de B. El razonamiento de un científico, mediante el cual acepta o rechaza sus teorías, consiste casi enteramente en silogismos del segundo y tercer tipo. 

Ahora bien, el razonamiento de nuestro policía ni siquiera era del tipo mencionado anteriormente. Se describe mejor mediante un silogismo aún más débil:

If A is true, then B becomes more plausible
B is true
Therefore, A becomes more plausible

Pero a pesar de la aparente debilidad de este argumento, cuando se plantea de manera abstracta en términos de A y B, reconocemos que la conclusión del policía tiene un poder convincente muy fuerte. Hay algo que nos hace creer que en este caso particular su argumento tenía casi el poder de un razonamiento deductivo.

Estos ejemplos muestran que el cerebro, al realizar un razonamiento plausible, no sólo decide si algo se vuelve más o menos plausible, sino que evalúa el grado de plausibilidad de alguna manera. La probabilidad de que llueva a las 10 a.m. depende en gran medida de la oscuridad de esas nubes. Y el cerebro también hace uso de información antigua así como de datos nuevos específicos del problema; Al decidir qué hacer, intentamos recordar nuestra experiencia pasada con las nubes y la lluvia, y lo que predijo el meteorólogo anoche.

