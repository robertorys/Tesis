[[AIMA-4th-edition.pdf]]
## 1. BASIC PROBABILITY NOTATION
### 1.1 What probabilities are about

Al igual que las afirmaciones lógicas, las afirmaciones probabilísticas se refieren a mundos posibles. Mientras que las afirmaciones lógicas dicen qué mundos posibles están estrictamente descartados (todos aquellos en los que la afirmación es falsa), las afirmaciones probabilísticas hablan de cuán probables son los distintos mundos. En teoría de la probabilidad, el conjunto de todos los mundos posibles se llama espacio muestral (sample space). Los mundos posibles son mutuamente excluyentes y exhaustivos: dos mundos posibles no pueden ser ambos, y un mundo posible debe serlo. Por ejemplo, si estamos a punto de tirar dos dados (distinguibles), hay 36 mundos posibles a considerar: (1,1), (1,2), . . ., (6,6). La letra Griega $\Omega$ (omega mayúscula) es usada para referir el espacio muestral, y $\omega$ (omega minúscula) refiere a los elementos del espacio, esto es, los "mundos" posibles particulares.

Un **modelo de probabilidad** completamente especificado asocia una probabilidad numérica $P(\omega)$ con cada "mundo" posible. El básico axioma de la teoría de la probabilidad dice que cada mundo tiene una probabilidad entre 0 y 1 y que el total de la probabilidad del conjunto de mundos posibles es 1:

$0 \leq P(\omega) \geq 1$ for every  $\Omega$ y $\sum_{\omega \in \Omega}{P(\omega) = 1}$. Ecuación 1.1
 
Las afirmaciones y consultas probabilísticas no suelen referirse a mundos posibles concretos, pero sobre conjuntos de ellos. Por ejemplo, podríamos preguntar por la probabilidad de que los dos dados sumen 11, la probabilidad de que se lancen dobles, etc. En teoría de la probabilidad, estos conjuntos se denominan **eventos**. En lógica, un conjunto de mundos corresponde a una **proposición** en un lenguaje formal; específicamente, para cada proposición, el conjunto correspondiente contiene sólo aquellos mundos posibles en los que se cumple la proposición. (Por lo tanto, “evento” y “proposición” significan más o menos lo mismo en este contexto, excepto que una proposición se expresa en un lenguaje formal). La probabilidad asociada con una proposición se define como la suma de las probabilidades de los mundos en los que se cumple:

Para cualquier proposición $\phi$, $P(\phi) = \sum_{\omega \in \phi}{P(\omega)}$. Ecuación 1.2

Por ejemplo, al tirar dados justos, tenemos $P(Total=11) = P((5,6)) + P((6,5)) = \frac{1}{36} + \frac{1}{36} = \frac{1}{18}$. Tenga en cuenta que la teoría de la probabilidad no requiere un conocimiento completo de las probabilidades de cada mundo posible. Por ejemplo, si creemos que los dados conspiran para producir el mismo número, podríamos afirmar que $P(double) = \frac{1}{4}$ sin saber si los dados prefieren el doble 6 al doble 2. Al igual que con las afirmaciones lógicas, esta afirmación restringe el modelo de probabilidad subyacente sin determinarlo por completo.

 
 Las probabilidades semejantes como $P(Total=11)$ y $P(double)$ son llamadas probabilidades **incondicionales** o probabilidades **prior** (y a veces simplemente "priors" (antecedentes) para abreviar); se refiere a grados de carencias en proposiciones *en ausencia de cualquier otra información*. Sin embargo, la mayoría de las veces tenemos cierta información, generalmente llamada **evidencia** , que ya ha sido revelado. Por ejemplo, puede que el primer dado ya tenga un 5 y estemos esperando con gran expectación a que el otro deje de girar. EN este caro, no estamos interesados en la probabilidad incondicional de obtener dobles, pero la probabilidad **condicional** o **prior** (o solo "posterior" para abreviar) de obtener dobles *dado que el primer dado es un 5*. Esta probabilidad se escribe $P(doubles | Die_1 = 5)$, donde the "$|$" es pronunciado como "dado". 

Similarmente, si to voy al dentista por un chequeo programado regularmente, entonces la probabilidad prior $P(cavity) = 0.2$ podría ser de interés; pero si yo voy al dentista porque u tengo un dolor de muelas, esto es la probabilidad condicional $P(cavity | toothache) = 0.6$ eso importa. 

Es importante entender que  $P(cavity) = 0.2$ es aún *valido* después de observas *dolor de muelas*; simplemente no es especialmente útil. Cuando hacemos decisiones, un agente necesita condicionar *todas* las evidencias que ha observado. Esto también es importante para entender la diferencia entre condicionamiento e implicación lógica.  La afirmación que $P(cavity | toothache) = 0.6$ no quiere decir "Siempre que el *dolor de muelas* sea cierto, concluya que las *caries* es verdadero con probabilidad de 0.6" más bien significa "Siempre que el *dolor de muelas* sea cierto y *no tengamos más información*, concluimos que las *caries* son verdad con probabilidad de 0.6" . La condición extra es importante; por ejemplo, si tenemos más información de que el dentista no encontró caries, nosotros definitivamente no querríamos concluir que la *caries* es verdad con probabilidad de 0.6; en cambio necesitamos usar $P(cavity | toothace \land \neg cavity) = 0$.

Matemáticamente hablando, las probabilidades condicionales son definidas en terminas de probabilidades incondicionales como sigue: para cualquier proposición $a$ y $b$, tenemos 

$P(a|b) = \frac{P(a \land b)}{P(b)}$,

 que se mantiene siempre que $P(b) > 0$. Pr ejemplo,

$P(doubles | Die_1 = 5) = \frac{P(doubles \land Die_1 = 5)}{P(Die_1 = 5)}$.

La definición hace sentido si recuerdas que observar *b* descarta todos los posibles mundos donde *b* es falso, dejando un conjunto cuyo probabilidad total es solo $P(b)$. Dentro de ese conjunto, los mundos donde *a* es verdad debed de satisfacer $a \land b$ y construir una fracción $\frac{P(a \land b)}{P(b)}$. 
La definición de probabilidad condicional, puede ser escrita en una forma deferente llamada la **regla del producto**:

$P(a \land b) = P(a|b)p(b)$. Ecuación 1.4 

La regla del producto es tal vez fácil de recordad: esto viene del hecho que para que $a$ y $b$ sean verdad, necesitamos que $b$ sea verdad, y también necesitamos que $a$ sea verdad dado $b$. 
### 1.2. The language of propositions in probability assertions

La proposiciones que describen conjuntos posibles de mundos generalmente se escriben en notación que combina elementos de proposición lógica y notación de satisfacción de restricciones. Esto es una **representación factorizada**, en el que cada mundo posible está representado por un conjunto de pares de variable/valor. 

Las variables en teoría de la probabilidad son llamadas **variables aleatorias**, y su nombre empieza con una letra mayúscula. De este modo, en el ejemplo del dado, $Tota$ y $Die_1$ son variables aleatorias. Cada variable aleatoria es una función que asigna desde el dominio de los mundos posibles $\Omega$ a algún **rango**; el conjunto de valores posibles que puede tomar. El rango $Ttoal$ para dos datos es el conjunto $\{2,...,12\}$ y el rango de $Die_1$ es $\{1,...,6\}$. Los nombres de los valores siempre están en minúsculas, entonces podríamos escribir $\sum_{x}{P(X=x)}$ para sumar los valores de $X$. 

Podemos combinar proposiciones elementales utilizando los conectivos de la lógica proposicional. Por ejemplo, podemos expresar "La probabilidad de que el paciente sin dolor de muelas, es de 0.1", como sigue:

$P(cavity | \neg toothache \land teen) = 0.1$

En notación de probabilidad, es también común usar comas para conjunciones, entonces podemos escribir $P(cavity|\neg toothache,teeen)$.
A veces querremos hablar de las probabilidad de todos los valores posibles de una variable aleatoria, Podemos escribirlo:

$P(Weather = sun) = 0.6$
$P(Weather = rain) = 0.1$
$P(Weather = cloud) = 0.29$
$P(Weather = snow) = 0.01$,

pero como una abreviación tenemos lo siguiente:

$P(Weather) = \langle 0.6,0.1,0.29,0.01 \rangle$,

donde **P** indica que el resultado es un vector de números y donde asumimos un orden predefinido $\langle sun,rain,cloud,snow \rangle$ en el rango de $Weather$. Decimos que la declaración de **P** define una **distribución de probabilidad** para una variable aleatoria $Weather$, que es una asignación de una probabilidad a cada uno de los posibles valores de la variable aleatoria. (En este caso, con un rengo discreto, la distribución es llamada una **distribución categórica**). La notación de **P** es también usado para distribuciones condicionales: **P**$(X|Y)$ dado los valores de $P(X = x_i | Y = y_j)$ para cada posible par $i,j$.  

Para variables continuas, no es posible escribir la distribución completa como un vector, porque hay infinitos valores. En cambio, podemos definir la probabilidad de que una variable aleatoria tome algún valor $x$ como una función parametrizada de $x$, generalmente llamada **función de densidad de probabilidad**.

En adición a las distribuciones en una sola variable, necesitamos una notación para distribuciones en multiple variables. La comas son usadas para esto. Por ejemplo, $P(Weather,Cavity)$ denota la probabilidad de todas las combinaciones de los valores de $Weather$ y $Cavity$.  Esto es una tabla de $4 \times 2$  de probabilidades llamada la **distribución de probabilidad conjunta (joint probability distribution)** de $Wather$ y $Cavity$. Podemos también mezclar variables y valores específicos; $P(sol, Cavidad)$ sería un vector de dos elementos dadas las probabilidades de una carié con un día soleado y ninguna carié con un día soleado.: 

La notación de **P** hace que ciertas expresiones seam mucho más concisas de lo que podrían ser de otra manera.  Por ejemplo, la regla del producto para todos los posibles valores de $Weather$ y $Cavity$ pueden escribirse como una sola ecuación:

$P(Weather,Cavity) = P(Weather|Cacity)P(Cavity)$

en lugar de estas ecuaciones $4 \times 2 = 8$ (usando las abreviaturas $W$ y $C$):

$P(W = sun \land C = true) = P(W = sun|C = true) P(C = true)$
.
.
.
$P(W = snow \land C = false) = P(W = snow|C = false) P(C = false)$

Ahora hemos definido una sintaxis para proposiciones y afirmaciones de probabilidad y tenemos una parte de la semántica: la ecuación 1.2 define la probabilidad de una proposición como la suma de las probabilidades de los mundos en los que se sostiene. Para completar la semántica, necesitamos decir como son los mundos y como se determina si una proposición se cumple en un mundo. Tomamos prestada esta parte directamente de la semántica de la lógica proposicional, como sigue. *Un mundo posible se define como una asignación de valores a todas las variables aleatorias bajo consideración.* 

Es fácil ver que esta definición satisface el requisito básico de que los mundos posibles sean mutuamente excluyentes y exhaustivos. Por ejemplo, si las variables aleatorias son $Cavity, Toothache,$ and $Weather,$ entonces serian $2 \times 2 \times 4 = 16$ mundos posibles. Además, la verdad de cualquier proposición dada puede ser determinada fácilmente en cada mundo posible por el mismo cálculo de verdad recursivo que usamos para la lógica proposicional.

Tenga en cuenta que algunas variables aleatorias pueden ser redundantes, porque sus valores pueden obtenerse en todos los casos a partir de los valores de otras variables. Por ejemplo, la variable $Double$ en el mundo de los dos dados es verdad cuando $Die_1 = Die_2$. Incluyendo $Doubles$ como una de las variables aleatorias, en adición a $Die_1$ y $Die_2$,  parece aumentar el número de mundos posibles de 36 a 72, pero, por su puesto, exactamente la mitad de los 72 será lógicamente imposible y tendrá probabilidad 0.

De la definición anterior de mundos posibles, se tiene que un modelo de probabilidad es completamente determinado por la distribución conjunta de todas las variables aleatorias, las llamadas **distribución de probabilidad conjunta completa(full joint probability distribution)**. Por ejemplo, dado $Cavity$, $Toothache$, y $Weather$, la distribución conjunta completa es $P(Cavity,Toothache,Weather)$. Esta distribución conjunta puede ser representada como una tabla $2 \times 2 \times 4$ con 16 entradas. Porque cada la probabilidad de cada proposición es una suma sobre todos los mundos posibles, una distribución conjunta completa es suficiente, en principio, por calcular la probabilidad de cada proposición. 

### 1.3. Probability axioms and their reasonableness

los axiomas básicos de la probabilidad (Ecuación 1.1 y 1.2) implica cierta relación entre los grados de creencias que puede concederse a proposiciones lógicamente relacionadas. Por ejemplo,  podemos derivar la relación familiar entre la probabilidad de una proposición y la probabilidad de su negación:

$P(\neg a) = \sum_{\omega \in \neg a}{P(\omega)}$  por la ecuación (1.2)
$= \sum_{\omega \in \neg a}{P(\omega)} + \sum_{\omega \in a}{P(\omega)} - \sum_{\omega \in a}{P(\omega)}$
$=\sum_{\omega \in \Omega}{P(\omega)} - \sum_{\omega}{p(\omega)}$                             Agrupando los dos primeros términos por (1.1) y (1.2)
$= 1 - P(a)$                                                 

También podemos derivar la conocida fórmula para la probabilidad de una disyunción, a veces llamada **principio de inclusión-exclusión (inclusion-exclusion principie)**:

$P(a \lor b) = P(a) + P(b) - P(a \land b)$. Ecuación 1.5

Esta regla es fácilmente recordada observando que los casos en los donde $a$ se mantiene, junto con el cando donde $b$ se mantiene, ciertamente cubre todos los casos en los que $a \lor b$ se mantiene, pero al sumar los dos conjuntos de casos se cuenta su intersección dos veces, por lo que debemos restar $P(a \land b)$.

Las ecuaciones (1.1 y 1.5) a menudo son llamados **axiomas de Kolmogorov (Kolmogorov’s axioms)**, Si bien la ecuación (1.2) tiene un sabor definitorio, La ecuación (1.5) revela que los axiomas realmente limitan los grados de creencia que un agente puede tener respecto de proposiciones lógicamente relacionadas. Esto es análogo al hecho de que un agente lógico no puede creer simultáneamente $A$, $B$ y $\neg(A \land B)$, porque no existe un mundo posible en el que las tres sean verdaderas. Sin embargo, en los casos de las probabilidades, los enunciados no se refieren directamente al mundo , sino al propio estado del agente. 

### 1.4. Inference using full joint distributions 

En esta sección se describe un método simple para la **inferencia probabilístico**, es decir, el cálculo de probabilidades posteriores para proposiciones de **consultas (query)** dada la evidencia observada. Usamos la distribución conjunta como la "base de conocimientos" del cual se puede derivar respuestas a todas las preguntas.

Empezaremos con un ejemplo simple: un dominio que consta solo de las tres variables booleanas $Toothache$, $Cavity$, y $Catch$. La distribucion conjunta completa es una tabla de $2 \times 2 \times 2$

|               | $toothache$ | $toothace$   | $\neg toothace$ | $\neg toothace$ |
| ------------- | ----------- | ------------ | --------------- | --------------- |
|               | $catch$     | $\neg catch$ | $catch$         | $\neg catch$    |
| $cavity$      | 0.108       | 0.012        | 0.072           | 0.008           |
| $\neg cavity$ | 0.016       | 0.064        | 0.144           | 0.576           |
**Figure 1.1** Una distribución conjunta completa para $Toothache$, $Cvity$ y $Catch$.

Observe que las probabilidades en la distribución conjunta suman 1, como lo exigen los axiomas de probabilidad. Observe también que la ecuación (1.2) nos brinda una forma directa de calcular la probabilidad de cualquier proposición, simple o compleja: simplemente identifique aquellos mundos posibles en los que la proposición es verdadera y sume sus probabilidades. Por ejemplo, hay seis mundos posibles en los que se produce $cavity \lor toothache$.

$P(cavity \lor toothache) = 0.108 + 0.012 + 0.072 + 0.008 + 0.016 + 0.064 = 0.28$.

Una tarea particularmente común es extraer la distribución de algún subconjunto de variables o de una sola variable. Por ejemplo, sumar las entradas de la primera fila da la probabilidad incondicional o **probabilidad marginal** de $cavity$:

$P(cavity) = 0.108 + 0.012 + 0.072 + 0.008 = 0.2$.

El proceso es llamado **marginalización (marginalization)**, o **"summing out"**, porque sumamos las probabilidades para cada valor posible de las otras variables, de este modo sacándolas de la ecuación. Podemos escribir la siguiente generalización de la regla de la marginalización para cualquier conjunto de variables **Y** y  **Z**:

$P(Y) = \sum_{z}{P(Y, Z = z)}$. Ecuación 1.6

Donde $\sum_{z}$ suma sobre todas las combinaciones  posibles de los valores del conjunto de la variable **Z**. Como usualmente abreviamos en la ecuación $P(Y,Z=z)$ por $P(Y,z)$. 

Usando la regla del producto (Ecuación (1.4)), podemos remplazar $P(Y, z)$ en la ecuación 1.6 por $P(Y|z)P(z)$, obteniendo una regla llamada **acondicionamiento (conditioning)**:

$P(Y) = \sum_{z}{P(Y|z)P(z)}$. Ecuación 1.7

La marginalización y acondicionamiento resultan ser reglar útiles para todo tipo de derivaciones que involucran expresiones de probabilidad.

En la mayoría de los casos, estamos interesados en calcular probabilidades condicionales de algunas variables, dada la evidencia sobre otras. Las probabilidades condicionales pueden ser encontradas por usar primero la ecuación (1.3) para obtener una expresión en términos de probabilidades incondicionales y luego evaluar la expresión  de la distribución conjunta completa. Por ejemplo, Podemos calcular la probabilidad de una caries, dada la evidencia de un dolor de muelas, de la siguiente manera:

$P(cavity|toothache) = \frac{(cavity \land toothache)}{P(toothache)}$
$= \frac{0.108 + 0.012}{ 0.108 + 0.012 + 0.016 + 0.064} = 0.6$.

Sólo para comprobarlo, también podemos calcular la probabilidad de que no haya caries, dado un dolor de muelas:

$P(\neg cavity|toothache) = \frac{(\neg cavity \land toothache)}{P(toothache)}$
$= \frac{0.0.16 + 0.064}{ 0.108 + 0.012 + 0.016 + 0.064} = 0.4$.

Los dos valores suman 1.0, como debe de ser. Note que el termino  $P(toothache)$ está en el denominador de ambos cálculos. Si la variable $Cavity$ tenía más de dos valores, estaría en el denominador para todas ellas. De hecho, puede verse como una constante de **normalización (normalization)** para la distribución $P(Cavity|toothache)$, asegurándose de que su suma sea 1. Usamos $\alpha$ para denotar tales constantes. Con esa notación, podemos escribir las dos ecuaciones anteriores en una:

$P(Cavity | toothache) = \alpha P(Cavity, toothache)$
$= α [P(Cavity, toothache, catch) + P(Cavity, toothache, \neg catch)]$
$= α [\langle 0.108, 0.016\rangle + \langle0.012, 0.064\rangle] = α \langle0.12, 0.08\rangle = \langle0.6, 0.4\rangle$.

En otras palabras, podemos calcular $P(Cavity | toothache)$ incluso si no conocemos el valor de $P(toothache)$. Nos olvidamos temporalmente del factor $1/P(toothache)$ y sumamos los valores para $cavity$ y $\neg cavity$, obteniendo 0.12 y 0.08. Esas son las proposiciones relativas correctas, pero no suman 1, entonces los normalizamos dividiendo cada uno por $0.12+0.08$, obteniendo la probabilidad de 0.6 y 0.4. La normalización resulta ser un atajo útil en muchos cálculos de probabilidad, tanto para facilitar el cálculo como para permitirnos proceder cuando alguna evaluación de probabilidad (como $P(toothache$)) no esté disponible.

Del ejemplo, podemos extraer un procedimiento general para la inferencia. Empezamos con el caso en el cual la consulta involucra una sola variable, $X$ ($Cavity$ en el ejemplo). Sea $E$ la lista de variables de evidencia (solo $Toothache$ en el ejemplo), sea $e$ la lista de valores observados para ellos, y sea $Y$ las variables restantes no observadas (solo $catch$ en el ejemplo). La consulta "query" es $P(X|e)$ y puede ser evaluado como 

$P(X|e) = \alpha P(X,e) = \alpha \sum_{y}{P(X,e,y)}$ Ecuación 1.8

donde la sumatoria sobre todos los posibles de $y$ (i.e., todos las posibles combinaciones de los valores no observados de la variable $Y$). Note que junto con las variables $X$, $E$, y $Y$ constituyen el conjunto completo de las variables para el dominio, entonces $P(X,e,t)$ es simplemente un subconjunto  de probabilidades de la distribución conjunta completa.

 Dada la distribución conjunta completa con la que trabajar, la ecuación 1.8 puede responder consultar probabilistas para variables discretas. Sin embargo, no escala bien: para un dominio descrito por $n$ variables booleanas, esto requiere una esta de una tabla de tamaño  $O(2^n)$ y toma un tiempo de $O(2^n)$ para procesar la tabla. Un un problema real puede ser fácil tener $n = 100$, haciendo que $O(2^n)$ sea poco práctico: una tabla con $2^{100} \thickapprox 10^{30}$ entradas. El problema no es sólo la memoria y la computación: el problema real es que si cada una de las $10^{30}$ probabilidades debe estimarse por separado de los ejemplos, el número de ejemplos requeridos será astronómico. Por esta razón, la distribución conjunta completa en forma tabular rara vez es una herramienta práctica para construir sistemas razonables. En cambio, debe ser la base teórica sobre la cual se puede construir enfoques más eficaces.
### 1.5 Independence 
Ampliemos la distribución conjunta completa en la figura 1.1 agregando una cuarta variable, $Weather$. La distribución conjunta completa se convierte en $P(Toothache, Catch, Cavity, Weather)$, el cual tiene $2 \times 2 \times 2\times 4 = 32$ entrada. Contiene cuatro “ediciones” de la tabla que se muestra en la Figura 1.1, uno para cada tipo de clima.¿Qué relación  tienen estas ediciones entre sí y con la tabla original de tres variables?. ¿Cómo es el valor de $P(toothache, catch, cavity, cloud)$ relacionada con el valor de $P(toothache, catch, cavity)$?. Podemos usar la regla del producto (Ecuación 1.4):

$P(toothache, catch, cavity, cloud) = P(cloud | toothache, catch, cavity)P(toothache, catch, cavity)$

Ahora, a menos que uno este en el negocio de la deidad, No debemos imaginar que nuestros problemas dentales influyen en el clima. Y para odontología de interior, parece seguro decir que el clima no influye en las variables dentales. Por lo tanto, las siguientes afirmación parece razonable:

$P(cloud | toothache, catch, cavity) = P(cloud)$. Ecuación 1.9

De esto podemos deducir

$P(toothache, catch, cavity, cloud) = P(cloud)P(toothache, catch, cavity)$

Una ecuación similar existe para *cada entrada* en $P(Toothache, Catch, Cavity, Weather)$. De hecho, podemos escribir la ecuación general 

$P(Toothache, Catch, Cavity, Weather) = P(Toothache, Catch, Cavity)P(Weather)$

De este modo, La tabla de 32 elementos para cuatro variables se puede construir a partir de una tabla de 8 elementos y una tabla de 4 elementos. Esta descomposición se ilustra esquemáticamente en la figura 12.4(a).

![[Figure12_4.png]]

La propiedad que utilizamos en la ecuación (1.9) es llamada **Independencia (independence)** (también llamado **independencia marginal (marginal independence)** y **independencia absoluta (absolute independence)**). En particular, $weather$ es independiente de un problema dental. La independencia entre las proposiciones $a$ y $b$ pueden ser escritas como 

$P(a | b) = P(a)$ ó $P(b | a) = P(b)$ ó $P(a \land b) = P(a)P(b)$. Ecuación 1.10

La independencia entre las variables $X$ e $Y$ se puede escribir de la siguiente manera (nuevamente, todas son equivalentes):

$P(X |Y ) = P(X )$ ó  $P(Y | X ) = P(Y )$ ó $P(X ,Y ) = P(X )P(Y )$. Ecuación 1.11

Las afirmaciones de independencia suelen basarse en el conocimiento del dominio. Como lo ilustra el ejemplo del clima y el dolor de muelas, pueden reducir drásticamente la cantidad de información necesaria para especificar la distribución conjunta completa. Si el conjunto completo de variables se puede dividir en subconjuntos independientes, entonces la distribución conjunta completa se puede *factorizar* en distribuciones conjuntas separadas en esos subconjuntos. Por ejemplo, la distribución conjunta completa del resultado de $n$ lanzamientos de monedas independientes, $P(C_1, ..., C_n)$, tiene $2^n$ entradas, pero puede ser representado como el producto de $n$ distribuciones de una sola variable $P(C_i)$. En un sentido más práctico, la independencia de la odontología y la meteorología es algo bueno, porque de lo contrario la práctica de la odontología podría requerir un conocimiento profundo de la meteorología, y viceversa. 

Cuando estén disponibles, entonces, las afirmaciones de independencia pueden ayudar a reducir el tamaño de la representación del dominio y la complejidad del problema de inferencia. Desafortunadamente, la separación clara de conjuntos completos de variables por independencia es bastante rara. Cada vez que una conexión, sin embargo indirecta, existe entre dos variables,  la independencia no se mantendrá. Además, incluso los subconjuntos independientes pueden ser bastante grandes; por ejemplo, la odontología puede implicar docenas de enfermedades y cientos de síntomas, todos los cuales están interrelacionados. Para manejar tales problemas, necesitamos métodos más sutiles que el simple concepto de independencia.

### 1.6 Baye's Rules and its use

Definimos la **regla del producto** (Ecuación (1.4)). De hecho puede ser escrita en dos formas:

$P(a \land b) = P(a|b)P(b)$ y $P(a \land b) = P(b|a)P(a)$

Igualando los dos lados derechos y dividiendo por $P(a)$, obtenemos

$P(b|a) = \frac{P(a|b)P(b)}{P(a)}$. Ecuación 1.12

Esta ecuación se conoce como **regla de Bayes (Bayes' rule)** (también como ley de Bayes o teorema de Bayes). Esta simple ecuación subyace los sistemas de IA más modernos para la inferencia probabilística.

El caso más general de la regla de Bayes para multivariable puede ser escrita en notación de **P** como sigue:

$P(Y|X) = \frac{P(X|Y)P(Y)}{P(X)}$.

Como antes, esto debe considerarse como la representación de un conjunto de ecuaciones, cada uno de los cuales trata con valores específicos de las variables. También tendremos ocasión de utilizar una versión más general condicionada a alguna evidencia de fondo **e**:

$P(Y|X,e) = \frac{P(X|Y,e)P(Y|e)}{P(X|e)}$. Ecuación 1.13

#### 1.6.1 Applying Bayes'rule: The simple case

En la superficie, la regla de Bayes no parece muy útil. Nos permite calcular el único término $P(b|a)$ en términos de tres términos: $P(a|b)$, $P(b)$, y $P(a)$. Eso parece dos pasos hacia atrás; pero la regla de Bayes es útil en la práctica porque hay muchos casos donde necesitamos tener una buena estimación de la probabilidad para estos tres números y necesitamos calcular en cuarto. A menudo, percibimos como evidencia el efecto *"effect"* de alguna causa desconocida y nos gustaría determinar esa causa. En este caso, la regla de Bayes se transforma en

$P(cause | effect) = \frac{P(effect | cause)P(cause)}{P(effect)}$. 

La probabilidad condicional $P(effect | cause)$ cuantifica la relación en la dirección **causal**, mientras $P(cause | effect)$ describe la dirección del diagnóstico. En una tarea como el diagnóstico médico, a menudo tenemos probabildeidades condicionales de relaciones causales. El doctor sabe $P(symptoms | disease)$ y quiere derivar un diagnóstico, $P(disease | symptoms)$.

## 13 Probabilistic reasoning

### 13.1 Representing Knowledge in a uncertain domain

En esta sección se introduce una estructura de datos llamada **red bayesiana (Bayesian network)**[^1] para representar las dependencias entre variables. La red Bayesiana pueden representar esencialmente *cualquier* distribución de probabilidad conjunta completa y, en muchos casos, puede hacerlo de manera muy concisa. 

Una red bayesiana es un grafo dirigido en el cual cada nodo es anotado con información de probabilidad cuantitativa. La especificación completa es como sigue:

1. Cada nodo corresponde a una variable aleatoria, que puede ser discreta o continua.
2. Los enlaces dirigidos o flechas conectan pares de nodos. Si hay una flecha desde el nodo *X* al nodo *Y*, se dice que *X* es padre de *Y*. El grafo no tiene ciclos dirigidos y, por lo tanto es un grafo acíclico dirigido, o DAG.
3. Cada nodo $X_i$ tiene información de probabilidad asociada $\theta(X_i|Parents(X_i))$ que cuantifica el efecto de los padres en el nodo utilizando un número finito de parámetros.

[^1] Las redes Bayesianas, a menudo se abrevian como "red de Bayes", se denominaron **redes de creencias** en los años 1980 y 1990. Una **red causal** es una red de Bayes con restricciones adicionales en el significado de las flechas (Sección 13.5). El termino **modelo gráfico** se refiere a una clase más amplia que incluye redes bayesianas.

La topología de la red (el conjunto de nodos y enlaces) especifica las relaciones de independencia condicional que se mantiene en el Dominion de una manera que se precisara en breve. El significado *intuitivo* de una flecha suele ser que $X$ tiene una *influencia sobre* $Y$, lo que sugiere que las causa deberían ser padres de los efectos. Generalmente es fácil para un experto en un dominio decidir que influencias directas existen en el dominio (de hecho, es mucho más fácil que especificar las probabilidades en sí). Una vez que se haya dispuesto la topología de la red de Beyes, solo necesitamos especificar la información de probabilidad local para cada variable, en la forma de distribución condicional dados sus padres. La distribución conjunta total para todas las variables es definida por la topología y la información de la probabilidad local.

Ahora considere el siguiente ejemplo. Tienes una nueva alarma antirrobo instalada en casa. Es bastante confiable para detectar un robo, pero ocasionalmente se desencadena por pequeños terremotos. (Este ejemplo se debe a Judea Pearl, residente de Los Ángeles, una zona propensa a terremotos). También tienes dos vecinos, Juan y María, que han prometido llamarte al trabajo cuando escuchen la alarma. John casi siempre llama cuando escucha la alarma, pero a veces confunde el tono del teléfono con la alarma y lo llama. Mary, por otro lado, le gusta la música bastante alta ya menudo no escucha la alarma. Dada la evidencia de quien llama y no llamada, nos gustaría estimar la probabilidad de un robo. 

Una red de Bayes para este dominio aparece en la "Figure 13.2. La estructura de la red muestra que el robo (Burglary) y temblores (earthquakes) afectan directamente la probabilidad deque suene la alarma, pero si John y María llaman depende solo de la alarma. La red representa así nuestras suposiciones de que no perciben los robos directamente, ellos no notan terremotos menores, y ellos no confirman antes de llamar.

![[Figure13_2.png]]

La información de la probabilidad local adjunta a cada nodo en la "Figuere 13.2" toma la forma de una **tabla de probabilidad condicional (conditional probability table (CPT))**. (CPT se puede usar solo para variables discretas; otra representaciones, incluidos aquellos adecuados para variables continuas, son descritas en la sección 13.2 ) Cada fila en la CPT contiene el valor de la probabilidad condicional de cada nodo para un **caso de condicionamiento (conditioning case)**. Una caso de condicionamiento es colo una posible combinación de los valores de los nodos padres, una miniatura de mundo posible, si así lo prefiere. Cada fila debe sumar 1, porque las entradas representan un conjunto exhaustivo de casos para la variable. Para una variable Booleana, una vez que conoces la probabilidad de un valor verdadero es $p$, la probabilidad de falso debe ser $1 - p$, así que a menudo omitimos el segundo número, como en la Figura 13.2. En general, una tabla para una variable Booleana con $k$  padres booleanos contienen $2^k$ probabilidades especificables independientemente. UN node son padres tiene solo una fila, representando la probabilidad prior de cada valor posible de la variable.

Note que la res no tiene nodes que correspondas a que María usualmente escucha música a todo volumen o a al tono de llamada del teléfono y la confusión de John. Estos factores se resumen en la incertidumbre asociada a los vínculos de "Alarm" a "JohnCalls" y "MaryCalls". Esto muestra tanto pereza como ignorancia en su funcionamiento: sería mucho trabajo descubrir por qué esos factores serían más o menos probables en cada caso particular y, de todos modos, no tenemos una forma razonable de obtener la información relevante.

La probabilidades en realidad resumen un conjunto potencialmente infinito de circunstancias en las que la alarma podría sonar o John o María podrían no llamar para informarlo. En esta forma, un pequeño agente podría afrontar con un mundo muy grande, al menos aproximadamente.

### 13.2 The Semantics of Bayesian Networks

La *syntax* de una red de Bayes consiste de una grafo acíclico dirigido con alguna información de probabilidad local adjunta a cada nodo. La *semantics* define como la sintaxis corresponde a la distribución conjunta sobre las variables de la red.

Asuma que la red de Bayes contiene $n$ variables, $X_1, \dots, X_n$. Una entrada genérica en la distribución conjunta es entonces $P(X_1 = x_1 \land \dots \land X_n = x_n)$, o $P(x_1, \dots, x_n)$ para abreviar. La semántica de la red de Bayes define cada entrada en la distribución conjunta como sigue:

$$ P(x_1,\dots,x_n) = \prod_{i=1}^{n}{\theta(x_i|parents(X_i))}, (13.1)$$
donde $parents(X_i)$ denota el valor de $Parents(X_i)$ que aparece en $x_1, \dots, x_n$. De este modo, cada entrada en la distribución condiciona es representada por el producto de los elementos apropiados de las distribuciones condicionales locales en la red de Bayes.

SI una red de Bayes es la representación de la distribución conjunta, entonces también puede ser utilizada para responder cualquier consulta (query), sumando todos los valores de probabilidad conjunta relevantes, cada uno se calcula multiplicando las probabilidades de las distribuciones condicionales locales. "Section 13.3 explains this in more detail, but also describes methods that are much more efﬁcient."

Hasta ahora, hemos pasado por alto un punto importante: ¿Cuál es el significado de los números que entran en las distribuciones condicionales locales $\theta(x_i|parents(X_i))$? Resulta que a partir de la ecuación (13.1) podemos demostrar que los parámetros $\theta(x_i|parents(X_i))$ son exactamente las probabilidades condicionales $P(x_i|parents(X_i))$ implicadas por la distribución conjunta. Recuerde que la probabilidad condicional pueden calcular a partir de la distribución conjunta de la siguiente manera:

$$
P(x_i|parents(X_i)) \equiv \frac{P(x_i, parents(X_i))}{P(parants(X_i))} 
= \frac{\sum_{y}{P(x_i,parents(X_i),y)}}{\sum_{x'_i,y}{P(x'_i,parents(X_i),y)}}
$$
donde $y$ representa los valores de todas las variables excepto $X_i$ y sus padres. Desde la última línea se puede demostrar que $P(x_i|parents(X_i)) = \theta(x_i|parents(X_i)$. Por lo tanto, podemos reescribir la ecuación (13.1) como

$$
P(x_1, \dots, x_n) = \prod_{i=1}^{n}{P(x_1|parents(X_i))}. 
(13.2)
$$
Esto significa que cuando uno estima valores para las distribuciones local, deben ser las probabilidades condicionales reales para la variable dados sus padres. Entonces, por ejemplo, cuando especificamos $\theta(JohnCalls=true|Alarm=true)=0.90$, debería sucedes que aproximadamente que suene la alarma, John llame. El hecho de que cada parámetro de la red tenga un significado preciso en términos de solo un pequeño conjunto de variables es crucialmente importante por la robustest y facilidad de especificación de los modelos.

#### A method for constructing Bayesian networks
La ecuación (13.2) define lo que significa una red bayesiana dada. El siguiente paso es explicar cómo construir una red bayesiana de tal manera que la distribución conjunta resultante sea una buena representación de un dominio dado. Ahora demostraremos que la ecuación (13.2) implica ciertas relaciones de independencia condicional que pueden usarse para guiar al ingeniero del conocimiento en la construcción de la topología de la red. Primero, reescribimos las entradas en la distribución conjunta en términos de probabilidad condicional, utilizando la regla del producto (ver página 390):

$$P(X_1, \dots, X_n) = P(X_n|X_{n-1},\dots, X_1)P(X_{n-1},\dots,X_1)$$
Luego repetimos el proceso, reduciendo cada probabilidad conjunta a una probabilidad condicional y una probabilidad conjunta en un conjunto más pequeño de variables. Terminamos con un gran producto:

$$P(X_1,\dots,X_n) = P(X_n|X_{n-1},\dots,X_1)P(X_{n-1}|X_{n-2},\dots,X_1)\dotsb P(X_2|X_1)P(X_1)$$
$$ = \prod_{i=1}^{n} P(X_i | X_{i-1},\dots,X_1) $$
Esta identidad se denomina **regla de la cadena** y es válida para cualquier conjunto de variables aleatorias. Al compararla con la ecuación (13.2), vemos que la especificación de la distribución conjunta es equivalente a la afirmación general de que, para cada variable $X_i$ en la red,

$$ P(X_i|X_{i-1},\dots,X_1) = P(X_i|Parents) (13.3)$$
siempre que las $Parents(X_i) \subseteq {X_{i-1},\dots, X_1}$. Esta última condición se satisface numerando los nodos en orden topológico, es decir, en cualquier orden consistente con la estructura del gráfico dirigido.
Lo que dice la ecuación (13.3) es que la red bayesiana es una representación correcta del dominio sólo si cada nodo es condicionalmente independiente de sus otros predecesores en el orden de nodos, dados sus padres. Podemos satisfacer esta condición con esta metodología:

1. *Nodes*: Primero, determine el conjunto de variables que se requieren para modelar el dominio. Ahora ordena, $\{X_1,\dots, X_n\}$. Cualquier orden funcionará, pero la red resultante será más compacta si las variables se ordenan de manera que las causas precedan a los efectos.
2. *Links*: Para $i =1$ a $n$ hacer:
	- Elija un conjunto mínimo de padres para $X_i$ de $X_1 , \dots , X_{i-1}$ , tal que se satisfaga la ecuación (13.3).
	- Para cada padre, inserte un enlace del padre a $X_i$.
	- Escribe la tabla de probabilidad condicional, $P(X_i|Parents(X_i))$.

Intuitivamente, los padres del nodo $X_1$ deberían contener todos aquellos nodos en $X_1, \dots, X{i-1}$ que influyen directamente en $X_i$.
#### Compactness and node ordering

Además de ser una representación completa y no redundante del dominio, una red de Bayes a menudo puede ser mucho más compacto que la distribución conjunta completa. Esta propiedad es la que hace posible manejar dominios con muchas variables.  La compacidad de las redes de Bayes es un ejemplo de una propiedad general de un **sistema estructurada localmente (locally structured system** (also called **sparse))**. En un sistema estructurado localmente, cada subcomponente interactua directamente con solo un número limitado de otros componentes, independientes del número total de componentes. La estructura local suele asociarse con un crecimiento linean en ligar de exponencial de la complejidad.

En el caso de las redes de Bayes, es razonable suponer que en la mayoría de los dominios cada variable aleatoria está directamente influenciada, por máximo, otras $k$, para alguna constante $k$. Si asumimos $n$ variables Booleanas para simplificar, entonces la cantidad de información necesaria para especificar cada tabla de probabilidad condicional será como máximo $2^k$, y la res completa puede ser especificada por $2^k \times n$. En contraste, la distribución conjunta contiene $2^n$. Para hacer esto concreto, suponga que tenemos $n = 30$ nodos, cada uno con cinco padres ($k = 5$). Entonces la red Bayesiana requiere 960 "registros", pero la distribución conjunta requiere más de un billón. 

La especificación de las tablas de probabilidad condicional para una red completa conectada, en el cual cada variable tiene todos los predecesores como padres, requiere la misma cantidad de información como es especificar la distribución conjunta en forma de tabla. Por esta razón, A menudo omitimos enlaces aunque exista una ligera dependencia, porque la ligera ganancia en precisión no compensa la complejidad adicional en la red. 

#### 12.2.1 Conditional independence relations in Bayesian networks

De la semántica de las redes de Bayes tal como se define en la ecuación (13.2), podemos derivar una serie de propiedades de independencia condicional. Ya hemos visto la propiedad de que una variable es condicionalmente independiente de sus otras predecesoras, dados sus padres. También es posible demostrar la propiedad más general de "no descendientes" que:

> [!NOTE] Descendant
> Each variable is conditionally independent of its non-descendants, given its parents.

*Cada variable es condicionalmente independiente de sus no **descendientes**, dados sus padres.*

![[Figure13.4.png]]

Por ejemplo, en la figura 13.2, la variable *JohnCalls* es independiente de *Burglary, Earthquake,* and *MaryCalls* dado el  valor de *Alarm*. La definición es es ilustrada en la Figura 13.4(a).

Resulta que la propiedad de no descendientes combinada con la interpretación de los parámetros de la red $\theta(X_i|Parents(X_i))$ como probabilidad condicional $P(X_i|Parents(X_i))$ basta para reconstruir la distribución conjunta completa dada en la ecuación (13.2). En otras palabras, se puede ver la semántica de las redes de Bayes de una manera diferente: en ligar de difinir la distribución conjunta completa como el producto de distribuciones condicionales, la res define un conjunto de propiedades de independencia condicional. La distribución conjunta completa se puede derivar de esas propiedades.

Otra importante propiedad de independencia importante está implicada en la propiedad de no descendientes: 

*una variable condicionalmente independiente de todos los demás nodos en la red, dado sus padres, hijos, e padres de los hijos, es decir, dada su **sabana de Markov (Markov blanket**.*

La propiedad de la sabana de Markov permite desarrollar algoritmos de inferencia que utiliza procesos de muestreo estocástico completamente locales y distribuidos, como se explica en la Sección 13.4.2.

La pregunta de independencia condicional más general que uno podría hacer en una red de Bayes es si un conjunto de nodos **X** es condicionalmente independiente de  otro conjunto **Y**, dado un tercer conjunto **Z**. Esto se puede determinar específicamente examinando la red de Bayes para ver si **Z d-separates X** y **Y**. Este proceso funciona de la siguiente manera:

1. Considere únicamente el **sub grafo ancestral (ancestral sub graph)** que consta de **X, Y, Z** y sus antepasados.
2. Agregue links entre cualquier par de nodos no conectados que comparten un hijo en común: ahora tenemos el llamado **grafo moral (moral graph)**.
3. Reemplace todas las enlaces dirigidos por enlaces no dirigidos.
4. Si el **Z** bloquea todos los caminos entre **X** y **Y** en el grafo resultante, entonces **Z** d-separates **X** y **Y**. En ese caso, **X** es condicionalmente independiente de **Y**, dado **Z**. Otro caso la red original de Bayes no requiere independencia condicional.

"In brief, then, d-separation means separation in the undirected, moralized, ancestral sub-graph. Applying the deﬁnition to the burglary network in Figure 13.2, we can deduce that Burglary and Earthquake are independent given the empty set (i.e., they are absolutely independent); that they are not necessarily conditionally independent given Alarm; and that JohnCalls and MaryCalls are conditionally independent given Alarm. Notice also that the Markov blanket property follows directly from the d-separation property, since a variable’s Markov blanket d-separates it from all other variables"

#### 13.2.2 Efficient representation of conditional distributions

Incluso si el máximo número de padres $k$ es pequeño, completar el CPT para un nodo requiere hasta $O(2^k)$ y quizás mucha experiencia con todos los casos posibles casos de condicionamiento.  De hecho, este es el peor de los casos posibles en el que la relación entre los padres e hijos es completamente arbitraria. Usualmente,  tales relaciones se pueden describir mediante una **distribución canónica (canonical distribution)** que se ajusta a algún patrón estándar. En esos casos, la tabla completa puede ser especificada solo nombrando el patrón y quizás suministrando algunos parámetros.

El ejemplo más simple lo proporcionan los **nodos deterministas**. Un nodo determinista tiene su valor especificado exactamente por los valores de sus padres, sin ninguna incertidumbre. La relación puede ser lógica: por ejemplo, la relación entre los nodos padre de *Canadian, US, Mexican* y el nodo hijo *NothAmerican* es simplemente que el hijo es la disyunción de los padres. La relación también puede ser numérica: por ejemplo, el *BestPrice* para un carro es el mínimo de los precios de cada vendedor en el area; y el *WaterStored* en un depósito a fin de año es la suma del importe original, más los flujos de entra (ríos, escorrentías, precipitaciones) y menos los flujos de salida (emisiones, evaporación, filtraciones).

Muchos sistemas de redes de Bayes permiten al usuario especificar funciones deterministas utilizando un lenguaje de programación de propósito general; esto permite incluir elementos complejos como modelos climáticos globales o simuladores de redes eléctricas dentro de un modelo probabilístico.

Otra patrón importante que ocurre a menudo en la práctica es la **independencia específica del contexto (context-specific independence (CSI))**. Una distribución condicional exhibe CSI si una variable condicionalmente independiente de algunos de sus padres dados ciertos valores de otros. 

> [!NOTE] context-specific independence 
> Para entender este patrón leer el ejemplo en la página 433 del pdf.

#### Bayesian nets with continuos variables
Muchos problemas del mundo real involucran cantidades continuas (continuous quantities), como altura, masa, temperatura y dinero. Por definición, una variable continua tiene un numero infinito de valores posibles, entonces es imposible especificar una probabilidad condicional explicita para cada valor. Una forma de manejar variables continuas es con **discretización**, es decir, dividir los valores posibles en un conjunto fijo de intervalos. Por ejemplo, las temperaturas podrían dividirse en tres categorías: ($<0^oC$), ($0^oC-100^oC$), y ($>100^oC$). Al elegir el número de categorías, existe una compensación entre la pérdida de precisión y los CPT grandes, lo que puede generar tiempos de ejecución lentos.

Otra enfoque es definir una variable continua utilizando una de las familias estándar de funciones de densidad de probabilidad. Por ejemplo la distribución Gaussiana (o normal) $\mathcal{N}(x, \mu, \sigma^2)$ se especifica mediante sólo dos parámetros, la media $\mu$ y la varianza $\sigma^2$. Otra solución, a veces llamada representación **no paramétrica (nonparametric)**, es definir la distribución condicional implícitamente con la colección de instancias, cada una de las cuales contiene valores específicos de las variables padres e hija. We explore this approach further in Chapter 19.

Una red con ambas variables discretas y continuas es llamada una **red Bayesiana híbrida (hybrid Bayesian network)**. Para especificar una res híbrida, tenemos que especificas dos nuevos tipos de distribuciones: la distribución condicional para una variable continua dado padres discretos; y la distribución condicional discreta dada padres continuos. Considere el ejemplo simple de la figura 13.6, en el que un cliente compra alguna fruta dependiendo de su costo, lo que depende a su vez del tamaño de la cosecha y de si está funcionando el plan de subsidios del gobierno. La variable *Cost* es continua y tiene padres continuos y discretos; la variable *Buys* es discreta y tiene un padre continuo.

![[Figure13_6.png]]

> [!NOTE] Variables continuas en redes de Bayes
> Ejemplo de como hacerlo, página 436 del pdf

### 13.3 Exact inference in Bayesian networks

La tarea básica de cualquier sistema de inferencia probabilística es calcular la distribución de probabilidad posterior (posterior) para un conjunto de **variables de consulta (query variables)**, dado algún **evento** observado, generalmente, alguna asignación de valores a un conjunto de **variables de evidencia**.[^2] Para simplificar la presentación, consideremos solo una variable de consulta a la vez;  los algoritmos se pueden ampliar fácilmente a consultas con múltiples variables. (Por ejemplo, podemos resolver la consulta $P(U,V|e)$ multiplicando $P(V|e)$ y $P(U|V,e)$.) Utilizaremos notación del capítulo 12: $X$ denota la variable de consulta; $E$ denota el conjunto de variables de evidencia $E_1, \dots, E_m$, y $e$ es un evento particular observado; $Y$ denota las variables ocultos (no evidencia, no consulta) $Y_1, \dots, Y_l$. Por lo tanto, el conjunto completo de variables es ${X} \cup E \cup Y$. Una consulta típica solicita la distribución de probabilidad posterior $P(X|e)$.

[^2] Otra tarea ampliamente estudiada es la de encontrar la **explicación más probable** para alguna evidencia observada. Esta y otras tareas se analizan en las notas al final del capítulo.

#### 13.3.1 Inference by enumeration
En el capitulo 12 se explico que cualquier probabilidad condicional puede ser calculada sumando términos de la distribución conjunta. Mas específicamente, una consulta P(X|e) pude ser respondida usando la ecuación ((1.8) [[AIMA#1.4. Inference using full joint distributions]]), el cual repetimos por conveniencia:

$$ P(X|e) = \alpha P(X,e) = \alpha \sum_{y}{P(X,e,y)}$$
Ahora, una red de Bayes tiene una representación completa de la distribución conjunta total. Específicamente, la ecuación (13.2)  muentra que los terminos $P(x,e,y)$ en la distribución conjunta puede ser escrita como el producto de probabilidades conjuntas de la red. Por lo tanto, *una 'query" puede ser contestada usando una red de Bayes calculando las sumas de los productos de la probabilidad condicionales de la red.*  