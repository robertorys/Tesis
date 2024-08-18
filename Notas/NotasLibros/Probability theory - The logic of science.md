[[Jaynes_book.pdf]]
## Introducción

### History

La escritura real comenzó como notas para una serie de conferencias dadas en la Universidad de Stanford en 1956. Expuesto en el entonces nuevo y apasionante trabajo de George Pólya sobre “Matemáticas y razonamiento plausible”. Diseccionó nuestro “sentido común” intuitivo en un conjunto de desiderata cualitativos elementales y demostró que los matemáticos los habían estado utilizando todo el tiempo para guiar las primeras etapas del descubrimiento, que necesariamente preceden al hallazgo de una prueba rigurosa. Los resultados fueron muy parecidos a los del “Arte de conjetura” de James Bernoulli (1713), desarrollado analíticamente por Laplace a finales del siglo XVIII; pero Pólya pensaba que el parecido era sólo cualitativo.

Sin embargo, Pólya demostró este acuerdo cualitativo con un detalle tan completo y exhaustivo que sugiere que debe haber más. Afortunadamente, los teoremas de consistencia de R. T. Cox fueron suficientes para resolver las cosas; cuando se les añadían las condiciones cualitativas de Pólya, el resultado era una prueba de que, si los grados de plausibilidad se representan mediante números reales, entonces existe un conjunto único de reglas cuantitativas para realizar la inferencia. Es decir, cualquier otra regla cuyos resultados entren en conflicto con ellas violará necesariamente un deseado (desiderátum) elemental (y casi ineludible) de racionalidad o coherencia.

Pero el resultado final fue justo el inicio de la reglas de la teoría de la probabilidad, dadas ya por Bernoulli y Laplace. La nueva característica importante fue que estas reglas ahora se consideraban principios excepcional-mente válidos de la lógica en general, sin hacer ninguna referencia al "azar" o a las "variables aleatorias"; por lo que su ámbito de aplicación es mucho mayor de lo que se suponía en la teoría de probabilidad convencional desarrollada a principios del siglo XX. Como resultado, la distinción imaginaria entre “teoría de la probabilidad” e “inferencia estadística” desaparece, y el campo logra no sólo unidad lógica y simplicidad, sino mucho mayor poder técnico y flexibilidad en las aplicaciones. 

Por lo tanto, en las conferencias del escritor, el énfasis estuvo en la formulación cuantitativa del punto de vista de Pólya, de modo que pudiera usarse para problemas generales de inferencia científica, casi todos los cuales surgen de información incompleta y no de “aleatoriedad”.

Una vez que comenzó el desarrollo de las aplicaciones, el trabajo de Harold Jeffreys, que había visto mucho de ello intuituvamente y parecía anticipar cada problema de encontraría, volvió a ser el foco central de atención. \

Entre 1957 y 1970, las clases repitieron, con contenido cada vez mayor, en muchas otras universidades y laboratorios de investigación. En este crecimiento, se hizo evidente poco a poco que las dificultades pendientes de la 'inferencia estadística' convencional se comprenden y se superan fácilmente. Pero las reglas que ahora tomaron su ligar eran bastantes sutiles conteptualmente, y se requería una reflexión profunda para ver cómo aplicarse correctamente. Las dificultades del pasado, que habían llevado al rechazo del trabajo de Laplace, fueron vistas finalmente como meras aplicaciones erróneas, que surgían generalmente de la falta de una definición inequívoca del problema o de una apreciación de la coherencia de información secundaria aparentemente trivial, y que eran fáciles de corregir una vez que se reconocía esto. Las diversas relaciones entre nuestro enfoque de 'lógica extendida' y el enfoque habitual de 'variable aleatoria' aparecen en casi todos los capítulos en muchas formas diferentes. 

Con el tiempo, el material creció hasta alcanzar una extensión mucho mayor de la que se podía presentar en una serie corta de conferencias y el trabajo evolucionó más allá de la fase pedagógica; una vez superadas las viejas dificultades, nos encontramos en posesión de una herramienta poderosa para abordar nuevos problemas. Desde aproximadamente 1970, la acumulación ha continuado al mismo ritmo, pero alimentada por la actividad investigadora del autor y sus colegas. Esperamos que el resultado final haya conservado lo suficiente de sus orígenes híbridos para que pueda utilizarse como libro de texto o como obra de referencia; de hecho, varias generaciones de estudiantes han llevado consigo versiones anteriores de nuestros apuntes y, a su vez, se los han enseñado a sus alumnos.

### Foundations

A partir de muchos años de experiencia con sus aplicaciones en cientos de problemas reales, nuestra opinion sobre los fundamentos de la teoría de la probabilidad han evolucionado hasta convertirse en algo bastante complejo, que no se puede describir en términos tan simplistas como 'a favor de esto' o  'en contra de aquello'. Por ejemplo nuestro sistema de probabilidad difícilmente podría ser más diferente del de Kolmogorov en estilo, filosofía y propósito tal como se necesita en las aplicaciones actuales -los principios para asignar probabilidades mediante el análisis lógico de información incompleta- no está presente en absoluto en el sistema de Kolmogorov. 

Sin embargo, cuando toso está dicho y hecho, nos encontramos, para nuestra propia sorpresa, de acuerdo con Kolmogorov y en desacuerdo con sus críticos en casi todas las cuestiones técnicas. Como se señala en el Apéndice A, cada  uno de sis axiomas resulta, para todos los efectos prácticos, derivable de los desiderata de racionalidad y consistencia de Póyla-Cox. En resumen, consideramos que nuestro sistema de probabilidad no contradice al de Kolmogorov, sino que en busca de una base lógica más profunda que permita su extensión en lsa direcciones que se necesitan para las aplicaciones modernas. En este esfuerzo, se han resuelto muchos problemas, y los que aún no se han resuelto aparecen donde naturalmente deberíamos esperarlos: al abrir nuevos caminos.

Como otro ejemplo, a primera vista parece que estamos muy de acuerdo con el sistema de probabilidad de De Finetti. De hecho, el autor creyó en esto durante algún tiempo. Sin embargo cuando toso está dicho y hecho, descubrimos, para nuestra propia sorpresa, que quedo poco más que un acuerdo filosófico vago; en muchas cuestiones técnicas estamos en total desacuerdo con De Finitti. Nos parece que su forma de tratar conjuntos infinitos ha abierto una caja de Pandora de paradojas inútiles e innecesarias.

### Comparisons 

Durante muchos años ha existido una controversia entre los métodos de inferencia 'frecuentistas' y 'bayesianos', en la que el autor ha sido un abierto partido del lado bayesiano. EL registro de esto hasta 1981 se encuentra en un libro anterior (Jaynes, 1983). En estos trabajos antiguos había una fuerte tendencia, por ambas partes, a argumentar en el plano filosófico e ideológico. Ahora podemos mantenernos un poco al margen de esto, porque, gracias a los trabajos recientes, ya no es necesario recurrir a tales argumentos. Ahora disponemos de teoremas probados y de una gran cantidad de ejemplos numéricos resueltos. Como resultado, la superioridad de los métodos Bayesianos es ahora un hecho plenamente demostrado en cien áreas diferentes. Se puede discutir con una filosofía, pero no es tan fácil discutir con una hoja impresa en una computadora que nos dice: "Independientemente de toda su filosofía, aquí están los hehcos del desempeño real". Los señalamos con cierto detalle siempre que hay una diferencia sustancial en los resultados finales. Por lo tanto, seguimoos defendiendo vigorosamente los métodos bayesianos, pero pedimos al lector que tenga en cuenta que nuestros argumentos ahora se basan en citar hechos en lugar de proclamar una posición filosófica o ideológica. 

Sin embargo, ni el enfoque bayesiano ni el frecuentistas son de aplicación universal, por lo que en el presente trabajo, más general, adoptamos una visión más amplia de las cosas. Nuestro tema es simplemente: la teoría de la probabilidad como lógica extendida. La 'nueva' percepción equivale al reconocimiento de que las reglas matemáticas de la teoría de la probabilidad no son simplemente reglas para calcular frecuencias de 'variables aleatorias' son también las únicas reglas consistentes para realizar inferencias (es decir, razonamiento plausible) de cualquier tipo, y las aplicaciones con total generalidad para ese fin.

Es cierto que todos los cálculos 'bayesianos´ se incluyen automáticamente como casos particulares de nuestras reglas, pero también lo son todos los cálculos 'frecuentistas'. Sin embargo, nuestras reglas básicas son más amplias que cualquiera de ellas y, en muchas aplicaciones, nuestros cálculos no encajan en ninguna de las dos categorías. 

Para explicar la situación tal como la vemos actualmente: los métodos 'frecuentistas' tradicionales que utilizan sólo distribuciones de muestreo sin utilizables y útiles en muchos problemas particularmente simples e idealizados; sin embargo, representas los casos especiales más proscritos de la teoría de la probabilidad, porque presuponen condiciones (repeticiones independientes de un 'experimento aleatorio',  pero ninguna información precia relevante) que casi nunca se cumplen en los problemas reales. Este enfoque es completamente inadecuado para las necesidades actuales de la ciencia.

Todos los defectos se corrigen mediante el uso de métodos bayesianos, que son adecuados para lo que podríamos llamar problemas de inferencia 'bien desarrollados'.  Como demostró Harold Jeffreys, cuentan como un magnífico aparato analítico, capaz de resolver sin esfuerzo los problemas técnicos en los que los métodos frecuentistas fracasan. Determinan automáticamente los estimadores y algoritmos óptimos, teniendo en cuenta la información previa y teniendo en cuenta los parámetros molestos y, al ser exactos, no fallan, sino que siguen produciendo resultados razonables, en casos extremos. Por lo tanto, nos permite resolver problemas de una complejidad mucho mayor que la que se puede analizar en términos frecuentistas. Uno de nuestros principales objetivos es mostrar cómo toda estas capacidades ya estaba contenida en las sencillas reglas de producto y suma de la teoría de la probabilidad interpretada como lógica extendida.

Antes de poder utilizar los métodos bayesianos, es necesario desarrollar un problema más allá de la 'fase exploratoria' hasta el punto en que tenga suficiente estructura para determinar todos los aparatos necesarios (un modelo, un espacio muestra, un espacio de hipótesis, probabilidades precias, distribución de muestreo). Casi todos los problemas científicos pasan por una fase de exploratoria inicial en la que necesitamos hacer inferencias, pero los supuestos frecuentistas son inválidos y el aparato bayesiano aún no está disponible. De hecho, algunos de ellos nunca superaran la fase exploratoria. Los problemas de este nivel requieren medios más premitivos de asignar probabilidades directamente a partir de nuestra información.

Los métodos bayesianos y de máxima entropía difieren en otro aspecto. Ambos procedimientos producen las inferencias óptimas a partir de información que se utilizó para su elaboración, pero podemos elegir un modelo para el análisis bayesiano; esto equivale a expresar algún conocimiento previo -o alguna hipótesis de trabajo- sobre el fenómeno que se observa. Por lo general, esta hipótesis van más allá de lo que se observa directamente en los datos y, en ese sentido, podríamos decir que los métodos bayasianos mejoren la entropía máxima; si son falsas, las inferencias bayesianas probablemente serán peores. 

Para este propósito, el Principio de la máxima entropía tiene en la actualidad la justificación teórica más clara y es el más desarrollado computacionalmente, con un aparato analítico tan potente y versátil como el bayesiano. Para aplicarla debemos definir un espacio muestral, pero no necesitamos ningún modelo ni distribución de muestreo. En efecto, la maximización de la entropía crea un modelo para nosotros a partir de nuestros datos, que resulta óptimo según tantos criterios diferentes que es difícil imaginar circunstancias en las que no querríamos utilizarla en un problema en el que tenemos espacio muestral pero no un modelo. 

Pero antes de que se puedan utilizar los métodos bayesianos, se debe desarrollar un problema más allá de la “fase exploratoria” hasta el punto en que tenga suficiente estructura para determinar todos los aparatos necesarios (un modelo, espacio muestral, espacio de hipótesis, probabilidades previas, distribución muestral). Casi todos los problemas científicos pasan por una fase exploratoria inicial en la que necesitamos hacer inferencias, pero los supuestos frecuentistas no son válidos y el aparato bayesiano aún no está disponible. De hecho, algunos de ellos nunca salen de la fase exploratoria. Los problemas a este nivel exigen medios más primitivos para asignar probabilidades directamente a partir de nuestra información incompleta.

Para ello, el Principio de Máxima Entropía tiene actualmente la justificación teórica más clara y el más desarrollado computacionalmente, con un aparato analítico tan potente y versátil como el bayesiano. Para aplicarlo debemos definir un espacio muestral, pero no necesitamos ningún modelo ni distribución muestral. En efecto, ¿la maximización de la entropía crea un modelo para nosotros a partir de nuestros datos, que resulta óptimo según tantos criterios diferentes? que es difícil imaginar circunstancias en las que no se quiera utilizarlo en un problema en el que tenemos un espacio muestral pero no un modelo.

Los métodos bayesianos y de máxima entropía difieren en otro aspecto. Ambos procedimientos producen inferencias óptimas a partir de la información contenida en ellos, pero podemos elegir un modelo para el análisis bayesiano; esto equivale a expresar algún conocimiento previo (o alguna hipótesis de trabajo) sobre el fenómeno que se observa. Por lo general, tales hipótesis se extienden más allá de lo que es directamente observable en los datos y, en ese sentido, podríamos decir que los métodos bayesianos son (o al menos pueden ser) especulativos. Si las hipótesis adicionales son ciertas, entonces esperamos que los resultados bayesianos mejoren con la entropía máxima; si son falsas, las inferencias bayesianas probablemente serán peores.

Por otro lado, la Máxima Entropía es un procedimiento no especulativo, en el sentido de que no invoca hipótesis más allá del espacio muestral y la evidencia que se encuentra en los datos disponibles. Por lo tanto, predice sólo hechos observables (funciones de observaciones pasadas o futuras) en lugar de valores de parámetros que pueden existir sólo en nuestra imaginación. Es justamente por esa razón que Maximum Entropy es la herramienta apropiada (más segura) cuando tenemos muy poco conocimiento más allá de los datos sin procesar; nos protege contra sacar conclusiones no respaldadas por los datos. Pero cuando la información es extremadamente vaga, puede resultar difícil definir un espacio muestral apropiado y uno puede preguntarse si se pueden encontrar principios aún más primitivos que la máxima entropía. 

Por "inferencia" nos referimos simplemente: razonamiento deductivo siempre que se dispone de suficiente información para permitirlo; razonamiento inductivo o plausible cuando (como ocurre casi invariablemente en problemas reales) la información necesaria no está disponible. Pero si un problema puede resolverse mediante razonamiento deductivo, la teoría de la probabilidad no es necesaria para ello; por tanto, nuestro tema es el procesamiento óptimo de información incompleta.
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

Para demostrar que el policía también estaba haciendo uso de la experiencia pasada de los policías en general, sólo tenemos que cambiar esa experiencia. Supongamos que hechos como estos ocurrieran varias veces cada noche a todos los policías, y que en todos los casos el caballero resultara ser completamente inocente. Muy pronto, los policías aprenderían a ignorar esas cosas triviales.

Así, en nuestro razonamiento dependemos en gran medida de información previa que nos ayude a evaluar el grado de verosimilitud de un nuevo problema. Este proceso de razonamiento se lleva a cabo de manera inconsciente, casi instantánea, y ocultamos lo complicado que es en realidad llamándolo sentido común.

El matemático George Pólya (1945, 1954) escribió tres libros sobre razonamiento plausible, señalando una gran cantidad de ejemplos interesantes y demostrando que existen reglas definidas mediante las cuales podemos realizar razonamientos plausibles (aunque en su obra permanecen en forma cualitativa). Los silogismos débiles anteriores aparecen en su tercer volumen. Se recomienda encarecidamente al lector que consulte la exposición de Pólya, que fue la fuente original de muchas de las ideas que sustentan el presente trabajo. Mostramos a continuación cómo los principios de Pólya pueden hacerse cuantitativos, con las consiguientes aplicaciones útiles.

Evidentemente, el razonamiento deductivo descrito anteriormente tiene la propiedad de que podemos recorrer largas cadenas de razonamiento del tipo (1–1) y (1–2) y las conclusiones tienen tanta certeza como las premisas. En los otros tipos de razonamiento (1-3)-(1-5), la fiabilidad de la conclusión cambia a medida que pasamos por varias etapas, pero en su forma cuantitativa veremos que en muchos casos nuestras conclusiones pueden acercarse a la certeza del razonamiento deductivo (como nos lleva a esperar el ejemplo del policía). Pólya demostró que incluso un matemático puro utiliza en realidad estas formas más débiles de razonamiento la mayor parte del tiempo. Por supuesto, cuando publica un nuevo teorema, se esforzará mucho en inventar un argumento que utilice sólo el primer tipo; pero el proceso de razonamiento que lo llevó al teorema en primer lugar casi siempre implica una de las formas más débiles (basándose, por ejemplo, en conjeturas sugeridas por analogías). La misma idea se expresa en una observación de S. Banach (citada por S. Ulam, 1957): “Los buenos matemáticos ven analogías entre teoremas; los grandes matemáticos ven analogías entre analogías”.

Los modelos tienen usos prácticos de un tipo muy diferente. A mucha gente le gusta decir: “Nunca fabricarán una máquina que sustituya a la mente humana, pues ésta hace muchas cosas que ninguna máquina podría hacer jamás”. J. von Neumann dio una hermosa respuesta a esta pregunta en una charla sobre ordenadores que dio en Princeton en 1948, a la que el autor tuvo el privilegio de asistir. En respuesta a la pregunta canónica del público \[“Pero, por supuesto, una simple máquina no puede pensar realmente, ¿verdad?”], dijo: “Usted insiste en que hay algo que una máquina no puede hacer. Si me dice exactamente qué es lo que una máquina no puede hacer, entonces siempre puedo fabricar una máquina que haga precisamente eso”.

En principio, las únicas operaciones que una máquina no puede realizar por nosotros son aquellas que no podemos describir en detalle o que no se pueden completar en un número finito de pasos. Por supuesto, algunos evocarán imágenes de la incompletitud de Gödel, la indecidibilidad, las máquinas de Turing que nunca se detienen, etc. Pero para responder a todas esas dudas sólo necesitamos señalar la existencia del cerebro humano, que lo hace. Tal como indicó von Neumann, las únicas limitaciones reales para fabricar “máquinas que piensen” son nuestras propias limitaciones al no saber exactamente en qué consiste “pensar”.

Pero en nuestro estudio del sentido común llegaremos a algunas ideas muy explícitas sobre el mecanismo del pensamiento. Cada vez que podemos construir un modelo matemático que reproduce una parte del sentido común prescribiendo un conjunto definido de operaciones, esto nos muestra cómo “construir una máquina” (es decir, escribir un programa de computadora) que opera con información incompleta y, al aplicar versiones cuantitativas de los silogismos débiles antes mencionados, realiza un razonamiento plausible en lugar de un razonamiento deductivo.

De hecho, el desarrollo de este tipo de software informático para determinados problemas especializados de inferencia es una de las tendencias actuales más activas y útiles en este campo. Un tipo de problema abordado de esta manera podría ser el siguiente: dada una masa de datos, que comprende 10.000 observaciones separadas, determinar, a la luz de estos datos y de cualquier información previa disponible, las plausibilidades relativas de 100 hipótesis posibles diferentes sobre las causas en juego.

Nuestro sentido común, por sí solo, podría ser suficiente para decidir entre dos hipótesis cuyas consecuencias son muy diferentes; pero para tratar con 100 hipótesis que no son muy diferentes, no podríamos hacer nada sin un ordenador y una teoría matemática bien desarrollada que nos muestre cómo programarlo. Es decir, ¿qué determina, en el silogismo del policía (1-5), si la plausibilidad de A aumenta en una cantidad grande, elevándola casi hasta la certeza, o sólo en una cantidad insignificante, haciendo que los datos B sean casi irrelevantes? El objeto del presente trabajo es desarrollar la teoría matemática que responda a tales preguntas, con la mayor profundidad y generalidad posible en la actualidad.

Si bien esperamos que una teoría matemática sea útil para programar computadoras, la idea de una computadora pensante también es psicológicamente útil para desarrollar la teoría matemática. La cuestión del proceso de razonamiento que utilizan los cerebros humanos reales está cargada de emoción y de malentendidos grotescos. Es casi imposible decir algo al respecto sin involucrarse en debates sobre cuestiones que no sólo son indecidibles en nuestro estado actual de conocimiento, sino que son irrelevantes para nuestro propósito aquí.

Obviamente, el funcionamiento del cerebro humano real es tan complicado que no podemos pretender explicar sus misterios; y en cualquier caso, no estamos tratando de explicar, y mucho menos de reproducir, todas las aberraciones e inconsistencias del cerebro humano. Se trata de un tema interesante e importante, pero no es el que estamos estudiando aquí. Nuestro tema son los principios normativos de la lógica, y no los principios de la psicología o la neurofisiología.

Para enfatizar esto, en lugar de preguntarnos “¿Cómo podemos construir un modelo matemático del sentido común humano?”, preguntémonos “¿Cómo podríamos construir una máquina que pudiera llevar a cabo un razonamiento plausible y útil, siguiendo principios claramente definidos que expresen un sentido común idealizado?”.

#### Introducing the Robot
Para dirigir la atención hacia cosas constructivas y alejarla de irrelevancias controvertidas, inventaremos un ser imaginario. Su cerebro será diseñado por nosotros, de modo que razone de acuerdo con ciertas reglas definidas. Estas reglas se deducirán de desiderata simples que, nos parece, serían deseables en cerebros humanos; es decir, pensamos que una persona racional, debería.

En principio, somos libres de adoptar las reglas que queramos; esa es nuestra manera de definir qué robot estudiaremos. Si comparamos su razonamiento con el suyo, si no encuentra ninguna semejanza, a su vez somos libres de rechazar nuestro robot y diseñar uno diferente, más a su gusto. Pero si encuentra una semejanza muy fuerte y decide que quiere y confía en este robot para que le ayude en sus propios problemas de inferencia, entonces eso será un logro de la teoría, no una premisa.

Nuestro robot va a razonar sobre proposiciones. Como ya se ha indicado anteriormente, denotaremos las distintas proposiciones con letras mayúsculas en cursiva {A, B, C, etc.} y, por el momento, debemos exigir que cualquier proposición utilizada tenga, para el robot, un significado inequívoco y sea del tipo lógico simple y definido que debe ser verdadera o falsa. Es decir, hasta que se indique lo contrario, nos ocuparemos únicamente de la lógica de dos valores, o lógica aristotélica. No exigimos que la verdad o falsedad de una “proposición aristotélica” de ese tipo sea determinable mediante una investigación factible; de ​​hecho, nuestra incapacidad para hacerlo suele ser la razón por la que necesitamos la ayuda del robot. Por ejemplo, el autor personalmente considera que las dos proposiciones siguientes son verdaderas:

$$ 
A \equiv \quad\text{"Bethoven and Berlioz never met."} 
$$
$$
B \equiv \quad\text{"Beethoven’s music has a better sustained quality than that ofBerlioz, although Berlioz at his best is the equal of anybody."}
$$
Pero la proposición B no es una proposición admisible para que nuestro robot piense en ella en este momento, mientras que la proposición A sí lo es, aunque es poco probable que su verdad o falsedad pueda establecerse definitivamente hoy. Una vez que nuestra teoría esté desarrollada, será interesante ver si la restricción actual a proposiciones aristotélicas como la A puede relajarse, de modo que el robot pueda ayudarnos también con proposiciones más vagas como la B.

#### The Basic Desiderata
Nuestro robot debe asignar a cada proposición sobre la que razona un cierto grado de plausibilidad, basándose en las pruebas que le hemos proporcionado; y siempre que recibe nuevas pruebas debe revisar estas asignaciones para tenerlas en cuenta. Para que estas asignaciones de plausibilidad puedan almacenarse y modificarse en los circuitos de su cerebro, deben estar asociadas a alguna cantidad física definida, como un voltaje o una duración de pulso o un número codificado en binario, etc., de cualquier forma que nuestros ingenieros quieran diseñar los detalles. Para los propósitos actuales, esto significa que tendrá que haber algún tipo de asociación entre los grados de plausibilidad y los números reales:

1. *Degrees of Plausibility are represented by real numbers.*

El Desideratum (I) se nos impone prácticamente por el requisito de que el cerebro del robot debe funcionar mediante la ejecución de algún proceso físico definido. Sin embargo, parecerá (Apéndice A) que también se requiere teóricamente; no vemos la posibilidad de ninguna teoría consistente sin una propiedad que sea funcionalmente equivalente al Desideratum (I).

Adoptamos una convención natural pero no esencial: a un número mayor corresponderá una mayor verosimilitud. Será conveniente suponer también una propiedad de continuidad, que es difícil de enunciar con precisión en esta etapa; pero para decirlo intuitivamente: una verosimilitud infinitesimalmente mayor debe corresponder sólo a un número infinitesimalmente mayor.

La plausibilidad que el robot asigna a alguna proposición A dependerá, en general, de si le dijimos que alguna otra proposición B es verdadera. Siguiendo la notación de Keynes (1921) y Cox (1961), lo indicamos con el símbolo

$$ A|B $$
que podemos llamar “la plausibilidad condicional de que A sea verdadero, dado que B es verdadero” o simplemente, “A dado B”. Representa algún número real. Así, por ejemplo,

$$ A|BC$$
(que podemos leer: “Un BC dado”) representa la plausibilidad de que A sea verdadero, dado que tanto B como C son verdaderos. O bien,\
$$ A+B|CD $$

representa la plausibilidad de que al menos una de las proposiciones A y B sea verdadera, dado que tanto C como D son verdaderas; y así sucesivamente. Hemos decidido representar una mayor plausibilidad con un mayor
número, por lo que

$$ (A|B) \gt (C|B) $$

dice que, dado B, A es más plausible que C. En esta notación, si bien el símbolo de plausibilidad tiene la forma A|B sin paréntesis, a menudo añadimos paréntesis para mayor claridad de expresión. Por tanto, (1–32) dice lo mismo que

$$  A|B \gt C|B $$
pero su significado es más claro a la vista.

Con el fin de evitar problemas imposibles, no vamos a pedirle a nuestro robot que se someta a la agonía de razonar a partir de premisas imposibles o mutuamente contradictorias; no podría haber una respuesta “correcta”. Por lo tanto, no intentamos definir A|BC cuando B y C son mutuamente contradictorias. Siempre que aparece un símbolo de este tipo, se entiende que B y C son proposiciones compatibles.

Además, no queremos que este robot piense de una manera que sea directamente opuesta a la manera en que pensamos tú y yo. Por lo tanto, lo diseñaremos para que razone de una manera que sea al menos cualitativamente similar a la forma en que los humanos intentan razonar, como se describe en los silogismos débiles anteriores y en varios otros similares.

Así, si tiene información antigua $C$ que se actualiza a $C'$ de tal manera que aumenta la plausibilidad de $A$: 
$$ (A|C') \gt (A|C) $$
pero la plausibilidad de B dado A no cambia:
$$ (B|AC') = (B|AC) $$
Por supuesto, esto sólo puede producir un aumento, nunca una disminución, en la plausibilidad de que tanto $A$ como $B$ sean verdaderas:
$$ (AB|C') \geq (AB|C) $$
y debe producir una disminución en la plausibilidad de que A sea falso:

$$ (A\neg | C') \lt (A\neg | C) $$
Este requisito cualitativo simplemente da el “sentido de dirección” en el que debe ir el razonamiento del robot; no dice nada acerca de cuánto cambian las plausibilidades, excepto que nuestro supuesto de continuidad (que también es una condición para la correspondencia cualitativa con el sentido común) ahora requiere que si A|C cambia solo infinitesimalmente, puede inducir solo un cambio infinitesimal en AB|C y A|C.

En el próximo capítulo se explicarán las formas específicas en que utilizamos estos requisitos cualitativos, en el punto en que se ve por qué los necesitamos. Por ahora los resumiremos de manera sencilla:

2. *Qualitative Correspondence with common sense.*

Por último, queremos darle a nuestro robot otra propiedad deseable por la que la gente honesta se esfuerza sin conseguirla siempre: que siempre razone de manera coherente. Con esto nos referimos simplemente a los tres significados coloquiales comunes de la palabra “coherente”:

3. coherente:
	1. Si una conclusión puede razonarse de más de una manera, entonces todas las formas posibles deben conducir al mismo resultado.
	2. El robot siempre tiene en cuenta todas las pruebas que tiene en relación con una cuestión. No ignora arbitrariamente parte de la información, basando sus conclusiones únicamente en lo que queda. En otras palabras, el robot es completamente aideológico.
	3. El robot siempre representa estados de conocimiento equivalentes mediante asignaciones de plausibilidad equivalentes. Es decir, si en dos problemas el estado de conocimiento del robot es el mismo (excepto quizás por el etiquetado de las proposiciones), entonces debe asignar las mismas plausibilidades en ambos.

Los desiderata (I), (II), (IIIa) son los requisitos “estructurales” básicos del funcionamiento interno del cerebro de nuestro robot, mientras que (IIIb), (IIIc) son condiciones de “interfaz” que muestran cómo el comportamiento del robot debe relacionarse con el mundo exterior. 
## 'Subjective’ vs. ‘objective’
Estas palabras se utilizaron tanto en la teoría de la probabilidad que tratamos de aclarar nuestro uso de ellas. En la teoría que estamos desarrollando, cualquier asignación de probabilidad es necesariamente 'subjetivista' en el sentido de que describe sólo un estado de conocimiento, y no algo que pueda medirse en un experimento físico. Inevitablemente, alguien preguntará: '¿De quién es el estado de conocimiento?' La respuesta siempre es: "la del robot, o la de cualquier otra persona a quien se le dé la misma información y las mismas razones de acuerdo con los desiderata (conjunto de las cosas que se echan de menos y se desean) utilizados en nuestras deducciones en este capitulo". 

Cualquiera que tenga la misma información, pero que llegue a una conclusión diferente a la de nuestro robot, necesariamente está violando uno de esos desiderata. En cista de tales violaciones, nos parece que una persona racional, si descubriera que está violando una de ellas, desearía revisar su pensamiento (en cualquier caso, seguramente tendría dificultades para persuadir a cualquier otra persona, que fuera consciente de esa violación, a que aceptara sus conclusiones). Ahora bien, era simplemente función de nuestros desiderata de interfaz (IIIb), (IIIc) hacer que estas asignaciones de probabilidad fueran completamente 'objetivas' en el sentido e son independientes de la personalidad del usuario. Son un medio para describir (o, lo que es lo mismo, para codificar) la información dada en el enunciado de un problema, independientemente de cualquier sentimiento personal (esperanza, temores, juicios de valor, etc.) que usted o yo podemos tener sobre las proposiciones implicadas. Es la 'objetividad 'en este sentido lo que se necesita para una teoría de la inferencia cintíficamente respetable.

## Chapter 2 THE QUANTITATIVE RULES
Hemos formulado ahora nuestro problema, y ​​es una cuestión de matemáticas sencillas calcular las consecuencias de nuestros desiderata: expresados ​​en términos generales,
1. Representación de grados de plausibilidad mediante números reales.
2. Correspondencia cualitativa con el sentido común.
3. Consistencia.
El presente capítulo está dedicado por completo a la deducción de las reglas cuantitativas para la inferencia que se desprenden de estos desiderata. Las reglas resultantes tienen una historia larga, complicada y asombrosa, llena de lecciones para la metodología científica en general (véanse los comentarios al final de varios capítulos).

### La regla del producto 
En primer lugar, buscamos una regla consistente que relacione la plausibilidad del producto lógico AB con las plausibilidades de A y B por separado. En particular, hallemos AB|C. Como el razonamiento es algo sutil, lo examinamos desde varios puntos de vista diferentes.

## 12. Ignorance priors and transformation groups
### 12.1 What are we trying to do?

Es curioso que, incluso cuando distintos trabajadores están prácticamente de acuerdo sobre que cálculos deben realizarse, pueden tener puntos de vista radicalmente diferentes sobre lo que realmente estamos haciendo y por qué lo hacemos. Por ejemplo, existe una gran comunidad bayesiana cuyos miembros se autodenominan 'bayesianos subjetivos' y se han establecido en una posición intermedia entre las estadísticas 'ortodoxas' y la teoría aquí expuesta. Sus mienbros han recibido, en su mayor parte, una información ortodoxa estándar, pero luego vieron lo absurdo que había en ella y se alejaron de la filosofía ortodoxa, aunque conservaron los hábitos de las terminología y la notación ortodoxas.

Estos hábitos de expresión ponen a los bayesianos subjetivos bajo una severa desventaja. Si bien perciben que las probabilidad no pueden representar solo frecuencias, aún considerando que las probabilidades de muestreo representan frecuencias de 'variables aleatorias'. Para ello las probabilidades previas y posteriores representan sólo opiniones privadas, que deben de actualizarse, de acuerdo con el principio de coherencia de De Finetti. Afortunadamente, esto conduce al algoritmo bayesiano, por lo que hacemos los mismos cálculos.

Los bayesianos subjetivistas se enfrentaron a una ambigüedad incómoda al comienzo de un problema, cuando se asigna probabilidades previas. Si éstas representan meras opiniones previas, entonces son básicamente arbitrarias e indefinidas; parece que sólo la introspección previa podría asignarlas, y diferentes personas harán asignaciones diferentes. Sin embargo, la mayoría de los bayesiano subjetivos siguen utilizando un lenguaje que implica que existe una distribución de probabilidad previa 'verdadera' desconocida en un problema real. En nuestra opinión, los problemas de inferencia están mal planteados hasta que reconocemos tres cosas esenciales. 


1. Las probabilidades previas representan nuestra *información*  previa y deben de determinarse, no mediante introspección, sino mediante el *análisis lógico* de esa información. 
2. Dado que las conclusiones finales dependen necesariamente tanto de la información previa como de los datos, se deduce que, al formular un problema, uno debe especificar la información previa que se utilizará con tanta exactitud como se especifican los datos. 
3. Nuestro objetivo es que las inferencias sean completamente 'objetivas' en el sentido de que dos personas con la misma información previa deben de asignar las mismas probabilidades previas. 
