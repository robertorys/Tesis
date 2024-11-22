[[Bayesian-Programming.pdf]]
## Introducción
### 1.1 Probability an alternative to logic

Las computadoras han aportado una nueva dimensión al modelo. Un modelo, una vez traducido a un programa y ejecutar en una computadora, puede usarse para comprender, medir, simular, imitar, optimizar, predecir y controlar. 

Sin embargo, Los modelos y programas adolecen de un defecto fundamental: *incompletitud*. Cualquier modelo de un fenómeno real es incompleto. La variables ocultas, no tomadas en cuenta en el modelo, influyen en el fenómeno. El efecto de las variables ocultas en que el modelo y el fenómeno nunca van a tener en mismo comportamiento. La *Incertidumbre* es la directa y consecuencia inevitable de lo incompleto. Es posible que un modelo no prevea exactamente las observaciones futuras en fenómenos, ya que estas observaciones están sesgadas por las variables ocultas, y es posible que no prediga exactamente las consecuencias de sus decisiones.

Calcular un precio de costos para reducir un precio de vuelta puede parecer una operación puramente aritmética que consiste en sumar costos elementales. Sin embargo, a menudo es posible que estos costos elementales no se conozcan con exactitud. Para una instancia, el costo de una pieza puede estar sesgado por los tipos de cambio, el costo de producción puede estar sesgado por el número de pedidos y los costos de transporte pueden estar sesgados por el periodo del año.  Los tipos de cambio, el número de pedidos y el período del año desconocido son variables ocultas que inducen incertidumbre en el cálculo del precio de costo.

Analizando el contenido de un correo electrónico para filtrar el spam es una tarea difícil, porque ninguna palabra o combinación de palabras puede darle certeza absoluta sobre la naturaleza del correo electrónico. A lo más, la presencia de ciertas palabras es una fuerte pista de que un correo electrónico es spam.  Puede que nunca sea una prueba concluyente, porque el contexto puede cambiar completamente su significado. Por ejemplo, si uno de tus amigos te envía un spam para discutir sobre el fenómeno del spam, de repente todo su contenido deja de ser spam. Un modelo lingüístico de spam es irremediablemente incompleto debido a esta información contextual limitada. Filtrar spam no es inútil y existe alguna solución muy eficaz, pero el resultado perfecto es una quimera.

El control de máquinas y el diagnostico de disfunciones son muy importantes para la industria. Sin embargo, el sueño de construir un modelo completo de una máquina y todos sus posibles fallos es una ilusión. Una vez más, esto no significa que el control y diagnóstico sean inútiles, sólo significa que los modelos de estas máquinas deben tener en cuenta su propia incompletitud y la incertidumbre resultante. 

En 1781, Sir William Herschell descubrió Urano el séptimo planeta del sistema solar. En 1846, Johan Galle observó por primera vez Neptuno, el octavo planeta. Mientras tanto, tanto Urbain Leverrier, astrónomo francés, como John Adan, inglés, se interesaron por la trayectoria "incierta" de Urano. El planeta no estaba siguiendo exactamente la trayectoria que predecía la teoría de la gravedad de Newton. Ambos llegaron a la conclusión de que estas irregularidades deberían ser el resultado de una variable oculta no tomada en cuanta por el modelo: la existencia de un octavo plantea. Incluso fueron mucho más allá y encontraron la posición más probable de este octavo planeta. El observador de Berlín recibió la predicción de Leverrier el 23 de septiembre de 1846 y Galle observó a Neptuno ese mismo día.

La lógica es a la vez la base matemática del razonamiento racional y el principio fundamental de la información actual. Sin embargo, la lógica, por esencia, se limita en los que la información es *completa* y *cierta*. Un *marco matemático alternativo* y un *marco informático alternativo* ambos son necesarios para lidiar con lo incompleto y la incertidumbre. 

La *teoría de la probabilidad* es este marco matemático alternativo. Es un modelo de razonamiento racional en presencia de incompletitud e incertidumbre. Es una extensión de la lógica donde tiene su lugar tanto la información cierta como la incierta. 

James C. Maxwell expresó este punto de manera sintética:

*La verdadera ciencia de la lógica actualmente sólo se ocupa de cosas ciertas, imposibles o enteramente dudosas, sobre ninguna de las cuales (afortunadamente) tenemos que razonar. Por lo tanto, la verdad lógica de este mundo es el cálculo de probabilidades, que tiene en cuenta la magnitud de la probabilidad de está, o debería estar en la mente de un hombre razonable.*

James C. Maxwell; quote in "Probability Theory - The Logic of Science" by Edward T. Jaynes (Jaynes, 2003)

Considerando la probabilidad como un *modelo de razonamiento* es llamado *subjetivista* o *aproximación Bayesiana*. Se opone al enfoque *subjetivista*, que considera la probabilidad como *modelo del mundo*. Esta oposición no es sólo una controversia epistemológical; Tiene muchas consecuencias fundamentales y prácticas.

Para modelar el razonamiento, se debe tener en cuanta los conocimientos previos del sujeto  que realiza el razonamiento. Este conocimiento preliminar juega el mismo papel que los axiomas en lógica.  Partir de diferentes conocimientos preliminares puede llevas a diferentes conclusiones. Partir de un conocimiento preliminar erróneo conducirá a conclusiones erróneas incluso con un razonamiento perfectamente correcto. Llegar a conclusiones erróneas siguiendo un razonamiento correcto demuestra que el conocimiento preliminar era erróneo, ofrece la oportunidad de corregirlo y, finalmente, conduce al aprendizaje. La incompletitud es simplemente la brecha irreductible entre el conocimiento preliminar y el fenómeno y la incertidumbre es una consecuencia directa y mensurable de esta imperfección. 

En contraste, modelar el mundo negando la existencia de un  "sujeto" y, en consecuencia, rechazando en conocimiento preliminar, conduce a situaciones complicadas y aparentes paradojas. Este rechazo implica que si las conclusiones son erróneas, el razonamiento podría ser aberrantes, sin dejar margen para  la mejora o el aprendizaje. Lo incompleto no significa nada sin un conocimiento previo, y la incertidumbre y el ruido deben ser propiedades misteriosas del mundo físico.

La escuela objetivista ha sido dominante durante el siglo XX, pero el enfoque subjetivista tiene una historia tan larga como la probabilidad misma. Se remonta a Jakob Bernouilli en 1713:

*La incertidumbre no está en las cosas sino en nuestra cabeza: la incertidumbre es falta de conocimiento.*
*Jakob Bernoulli, Ars Conjectandi (Bernouilli, 1713);*

al marqués Simón de Laplace, un siglo después, en 1812:

*La teoría de la probabilidad no es más que sentido común reducido al cálculo.*
*Simon de Laplace, Théorie Analytique des Probabilités (Laplace, 1812)*

a lo ya citado James C. Maxwell en 1850 y a el visionario Henri Poincaré en 1902:

*La aleatoriedad es sólo la medida de nuestra ignorancia*

*Para realizar cualquier cálculo de probabilidad, e incluso para que este cálculo tenga significado, tenemos que admitir, como un punto fuerte, una hipótesis o una convención, que siempre implica un cierto grado de arbitrariedad. En la  elección de esta convención, sólo podemos guiarnos por el principio de razón suficiente. 

De esta punto de vista, todas las ciencias no serán más que aplicaciones inconscientes del cálculo de probabilidades. Condenar este cálculo sería condenar toda la ciencia.
Henri Poincaré, La science et l’hypothèse (Poincaré, 1902)
*
 y finalmente, por Edward T. Jaynes en su libro Probability theory: the logic of science
(Jaynes, 2003) donde presenta brillantemente la alternativa subjetiva y establece clara y simplemente las bases del enfoque: 

 *Por inferencia queremos decir simplemente: razonamiento deductivo siempre que se disponga de suficiente información para permitirlo; razonamiento inductivo o probabilístico cuando (como ocurre casi invariablemente en los problemas reales) no se dispone de toda la información necesaria.* 
 Edward T. Jaynes, Probability Theory: The Logic of Science (Jaynes, 2003)
 

### 1.2 A need for a new computing paradigm

La teoría de la probabilidad es claramente la alternativa matemática buscando a la lógica. 

Sin embargo, queremos soluciones funcionales a problemas incompletos e inciertos. Como consecuencia, requerimos una marco comunicacional alternativa basada en la probabilidades de Bayesianas. 

Para crear cualquier marco comunicacional Bayesiano tan completo, requerimos una *nueva metodología de modelado* para construir modelos probabilístico, requerimos *nuevos algoritmos de inferencia* para automatizar el cálculo probabilístico, requerimos *nuevos lenguajes de programación* para implementar estos modelos en computadoras, y finalmente, deberíamos eventualmente requerir *nuevo hardware* para correr estos programas Bayesianos eficientemente.  La última meta es una *computadora Bayesiano*.

### 1.3 A need for a new modeling methodology
La existencia de un método sistemático y genérico para construir modelos es un requisito *sine qua non* para el éxito de un paradigma de modelado y computo. Esto es porque loa algorithms se imparten en el curso básico de informática brindando a los estudiantes los métodos básicos y necesarios para desarrollar programas clásicos. Un método tan sistemático y genérico existe dentro del marco bayesiano. Además, este método es muy sencillo aunque resulte atípico y un poco preocupante al principio.

### 1.4 A need for new inference algorithms
Una metodología de modelado no es suficiente para ejecutar programas bayesianos. También necesitamos un motor de inferencia bayesiano eficiente para automatizar el cálculo probabilístico. Esto supone que tenemos una colección de algoritmos de inferencia adaptados y ajustados a modelos más o menos específicos y una arquitectura de software para combinarlos en una herramienta coherente y única. 

En la literatura se han propuesto numerosos algoritmos de inferencia bayesiano de este tipo. 

## 2 Basic concepts

*Es mucho mejor una respuesta aproximada a la pregunta correcta, que a menudo es vaga que una respuesta exacta a al pregunta equivocada, que siempre puede precisarse.*
John W. Tuckey

### 2.3 The normalization postulate
$$ \sum_{x \in X}{P([X=x]) = 1}, (2.2) $$
Para simplificar usaremos la siguiente notación:
$$ \sum_{X}{P(X)} = 1, (2.3) $$

### 2.4 Probabilidad condicional
De manera análoga a la expresión (2.3) tenemos que para cualesquiera dos variables $X$ e $Y$
$$ \sum_{X}{P(X|Y) = 1}, (2.4) $$
### 2.6 The conjunction postulate (Bayes theorem) 

La probabilidad de la conjunción de dos variables $X$ y $Y$ pueden ser calculados de acuerdo con la regla de conjunción:

$$  P(X \land Y) = P(X) P(Y|X) = P(Y)P(X|Y), (2.7) $$

Esta regla pude ser más conocida bajo la forma de la llamado teorema de Bayes:

$$ P(X|Y) = \frac{P(X)P(Y|X)}{P(Y)}, (2.8) $$

Sin embargo, preferimos la primera forma, el cual establece que es un medio para calcular la probabilidad de una conjunción de variables de acuerdo tonto con las probabilidades de estas variables como con sus probabilidades.

### 2.7 Sillogisms
Es muy importante para adquirir una sensación intuitiva clara de lo que significa una probabilidad condicional y la regla de conjunción. Un primer paso hacia esta comprensión puede ser los silogismos lógicos clásicos sen us formas probabilísticas.

Recordemos primero los dos silogismos lógicos 

1. Modus Ponens: $a \land (a \Rightarrow b) \rightarrow b$ 
	Si $a$ es verdad y si $a$ implica $b$ entonces $b$ es verdad.
2. Modus Tollens: $\neg b \land (a \Rightarrow b) \rightarrow \neg a$
	 Si $b$ es falso y si $a$ implica $b$ entonces $a$ es falso.

Por ejemplo, si $a$ representa "$n$ puede dividirse por 9" y $b$ representa "$n$ puede dividirse por 3", y sabemos que $a \Rightarrow b$, y tenemos que:

1. Modus Ponens: Si "$n$ es dividido por 9" entonces "$n$ es dividido por 3".
2. Modus Tollens: Si "$n$ es dividido por 3" es falso entonces "$n$ dividido por 9" es también falso.

Usando probabilidades, podemos decir:

1. Modus Ponens: $P(b|a) = 1$, el cual significa que sabiendo que $a$ es verdad entonces podemos estar seguros de que $b$ es verdad.
2. Modus Tollens: $P(\neg a|\neg b) = 1$, el cual significa que sabiendo que $b$ es falso entonces podemos estar seguros de que $a$ es falso.

$P(\neg b|\neg a) = 1$ puede derivarse de $P(a|b)$, usando los postulados de normalización y conjunción:


$$ P(\neg a| \neg b) = 1 - P(a| \neg b)$$ por (2.3)
 $$= 1 - \frac{P(\neg b | a)P(a)}{P(\neg b)}$$
 por (2.8)
 $$= 1 - \frac{(1 - P(b|a))P(a)}{P(\neg b)} $$
 por(2.3)
 $$ = 1 $$
 porque $P(b|a) = 1$

Sin embargo, utilizando probabilidades podemos ir más allá que con la lógica:
1. De $P(b|a) = 1$, usando los postulados de normalización y conjunción podemos derivar que $P(a|b) \geq P(a)$, lo cual significa que si sabemos que $b$ es verdad, la probabilidad de que $a$ es verdad es mayor de lo que sería si no supiéramos nada sobre $b$. Obviamente, loa probabilidad de que "$n$ pude dividirse por 9" es mayor si sabes que  "$n$ puede dividirse por 3" que si no lo supiéramos. Esto razonamiento muy común lo cual está más allá del alcance de la lógica pura pero es muy simple en el marco bayesiano.
1. De $P(b|a) = 1$, usando los postulados de normalización y conjunción podemos derivar que $(P(\neg b | \neg a) \leq P(\neg b)$, lo cual significa que si sabemos que $a$ es falso, la probabilidad de que $b$ es falso es menor de lo que sería si no supiéramos nada sobre $a$. La probabilidad de que "$n$ es dividido por 3" es manor si sabemos que $n$ no se puede dividir por 9 de lo que sería si no supiéramos nasa sobre $n$.

## 12 Bayesian programming formalism
### 12.1 How simple! How subtle!

El propósito de este capitulo es presentar la programación bayesiana formalmente y demostrar que es muy simple y muy clara pero, sin embargo, muy poderosa y muy sutil. La probabilidad es una extensión de la lógica, tan matemáticamente sensata y simple como la lógica, pero con más poder expresivo que la lógica.

### 12.2 Logical propositions
El primer concepto que usamos es la noción usual de una *proposición lógica*. Las proposiciones son denotadas por nombres es minúsculas. Se pueden componer proposiciones para obtener nuevas proposiciones utilizando operadores lógicos habituales: $a \land b$, denotando la conjunción de la proposición $a$ y $b$, $a \lor b$ es la disyunción, y $\neg a$, la negación de la proposición $a$.

### 12.3  Probability of a propositions

Para poder lidiar con la incertidumbre, asignamos probabilidades a las proposiciones.

Consideremos que, para asignar una probabilidad a una proposición $a$, es necesario tener al menos algún *conocimiento previo*, resumido en una proposición $\pi$. En consecuencia, la probabilidad de una proposición $a$ está siempre condicionada, al menos por $\pi$. Para cada diferente $\pi$, $P(\cdot | \pi)$ es una aplicación que asigna a cada proposición $a$ un valor real único $P(a|\pi)$ en el intervalo $[0,1]$.

Por supuesto, nos interesa razonar sobre las probabilidades de conjunciones, disyunciones y negaciones de proposiciones, denotadas respectivamente, por $P(a \land b | \pi)$, $P(a \lor b \ \pi)$ y $P(\neg a | \pi)$.

También nos interesa la probabilidad de la proposición a condicionada tanto por el conocimiento preliminar $\pi$ como por alguna otra proposición b. Esto denota $P(a | b \land \pi)$.

### 12.4 Normalization and conjunctions postulates 

El razonamiento probabilístico requiere soló dos reglas básicas:

1. La regla de la conjunción, que de la probabilidad de una conjunción de proposiciones.
$$ P(a \land b | \pi) = P(a | \pi) \times P(b | a \land \pi) $$
$$ = P(b | \pi) \times P(a \land \pi)$$ 
(12.1)

2. La regla de la normalización, que establece que la suma de las probabilidades de $a$ y $\neg a$ es uno.
$$ P(a|\pi ) + P(\neg a | \pi) = 1 $$
(12.2)

En este libro, tomamos estas dos reglas como postulados.

Al igual que la lógica, donde el principio de resolución (Robinson, 1965; Robinson, 1979) es suficiente par resolver cualquier problema de inferencia, en probabilidades discretas, estas dos reglas (12.1 y 12.2) son suficientes para cualquier cálculo. De hecho, podemos derivar todas las demás reglas de inferencia necesarias a partir de estas dos.

### 12.5 Disjunction rule for propositions 

Por ejemplo, la regla relativa a la disyunción de proposición:
$$ P(a \lor b | \pi) = P(a|\pi)+P(b|\pi)-P(a \land b | \pi)$$
(12.3)

Pude derivarse de la siguiente manera:

$$ P(a \lor b|\pi) $$
$$ = (1 - P(\neg a \lor \neg b | \pi)) $$
$$ = 1 - P(\neg a | \pi) \times P(\neg b | \neg a \land \pi) $$
$$ = 1 - P(\neg a | \pi) \times (1 - P(b | \neg a \land \pi)) $$
$$ = P(a| \pi) + P(\neg a \land b | \pi)$$
$$ = P(a|\pi)+ P(b|\pi) \times P(\neg a| b \land \pi) $$
$$= P(a|\pi) + P(a| \pi) \times (1 - P(a | b \land \pi)) $$
$$ = P(a|\pi)+P(b|\pi)-P(a \land b | \pi)$$
(12.4)

### 12.6 Discrete variables

El segundo concepto que necesitamos es la noción de *variable discreta*. Las variables se denotan con nombres que comienzan con una letra minúscula.

Por definición, una *variable discreta* $X$ es un conjunto de proposiciones lógicas $x_i$, de manera que estas proposiciones son mutuamente excluyentes (para todo $i, j$ con $i \neq j$ , $x_i \land x_j$ es falso) y exhaustivas (al menos una de las proposiciones $x_i$). $x_i$ significa << la variable $X$ toma su valor $i$ >>.
$CARD(X)$ denota la cardinalidad de el conjunto $X$ (el número de proposiciones $x_i$).

### 12.7 Variable conjunction
La conjunción de dos variables $X$ y $Y$, denotado por $X \land Y$, se define como el conjunto de proposiciones $x_i \land y_j$ ($CARD(X) \times CARD(Y)$). $X \land Y$ es un conjunto de proposiciones mutuamente excluyente y exhaustivas. Como tal, es una nueva variable.[^1]

[^1] En cambio, la disyunción de dos variables, definida como el conjunto de proposiciones x i 2 y j , no es una variable. Estas proposiciones no son mutuamente excluyentes.

Por supuesto, la conjunción de $n$ variables también es una variable y, como tal, puede cambiar de nombre en cualquier momento y considerarse como una variable única en la secuela. 

### 12.8 Probability on variables

Para simplificar y aclarar, también utilizaremos fórmulas probabilísticas con variables que aparecen en lugar de proposiciones.
Por conveción, cada vez que aparece una variable $X$ en una fórmula probabilística $\Phi (X)$, debe entenderse como $\forall x_i \in X, \Phi(x_i)$.

Por ejemplo, dadas tres variables $X$, $Y$ y $Z$:
$$ P(X \land Y| Z \land \pi) = P(X | Z \land \pi) $$
(12.5)

representa:
$$\forall x_i \in X, \forall y_j \in Y, \forall z_k \in Z$$
$$ P(x_i \land y_i | z_k \land \pi) = P(x_i | z_k \land \pi)$$
(12.6)

### 12.9 Conjunction rule for variables

$$ P(X \land Y | \pi) = P(X | \pi) \times P(Y | X\land \pi) $$
$$ = P(Y | \pi) \times P(X | Y \land \pi) $$
(12.7)

De acuerdo con nuestra conveción para fórmulas probabilísticas que incluyen variables, esto puede reformularse así:

$$ \forall x_i \in X, \forall y_i \in Y $$
$$ P(x_i \land y_i | \pi) = P(x_i | \pi) \times P(y_i | x_i \land \pi) $$
$$ = P(y_i | \pi) \times P(x_i | y_i \land \pi)$$

(12.8)

lo cual puede deducirse directamente de la regla de conjunción para proposiciones (12.1).

### Normalization rule for variables

$$ \sum_{X}P(X|\pi) = 1 $$
(12.9)

La regla de la normalización obviamente pude derivarse de la siguiente manera:
$$ 1 = P(x_1 | \pi) + P(\neg x_i | \pi) $$
$$ = P(x_i | \pi) + P(x_2 \lor \dots \lor x_{CARD(X)} | \pi)$$
$$ P(x_1 | \pi) + P(x_2 | \pi) + \dots + P(x_{CARD(X)} | \pi) $$
$$ = \sum_{x_i \in X}P(x_i | \pi) $$
(12.10)
 donde la primera igualdad deriva de la regla de normalización para proposiciones (12.2), la segunda de la exhaustividad de las proposiciones $x_i$, y la tercera de aplicar la ecuación (12.3) y la exclusividad mutua de las proposiciones $x_i$.

### Marginalization rule

$$ \sum_X P(X \land Y | \pi) = P(Y | \pi) $$
(12.11)

La regla de la marginalización deriva por la aplicación sucesiva de la regla de conjunción (12.7) y la regla de normalización (12.9):

$$ \sum_X P(X \land Y | \pi) = \sum_X P(Y | \pi) \times P(X | Y \land pi)$$
$$ = P(Y| \pi) \times \sum_X P(X | Y \land \pi) $$
$$= P(Y | \pi)$$
(12.12)

### 12.12 Bayesian program

Definimos un *programa Bayesiano* como un medio para especificar una familia de distribuciones de probabilidad.

Los elementos constitutivos de un programa bayesiano se presenta en la Figura 12.1:

![[Figure12_1BP.png]]

- Un programa se constituye a partir de una descripción y una pregunta
- Una descripción se construye utilizando alguna especificación $(\pi)$ dada por el programador y un proceso de identificación o aprendizaje para los parámetros no completamente especificados por la especificación, utilizando un conjunto de datos $(\delta)$.
- Una especificación se construye a partir de un conjuntos de variables pertinentes, una descomposición y un conjunto de formas.
- Las formas son formas paramétricas o programas Bayesianos.

### 12.13 Description 
El propósito de una descripción es especificar un método eficaz para calcular una distribución conjunta en un conjunto de variables $\{X_1, X_2, \dots, X_n\}$ dado un conjunto de datos experimentales $\delta$ y alguna especificación $\pi$. Esta distribución conjunta es denotada como: $P(X_1 \land X_2 \land \dots \land X_n | \delta \land \pi)$.

### 12.14 Specification
Para especificar conocimientos preliminares, el programador deberá realizar lo siguiente:
1. Defina el conjunto de variables relevantes $\{X_1, X_2,  \dots, X_n\}$ en el que se define la distribución conjunta.
2. Descomponer la distribución conjunta:
Dada una partición $\{X_1, X_2, \dots, X_n\}$ en $k$ subconjuntos, definimos $k$ variables $L_1,\dots,L_k$, cada una correspondiente a uno de esos subconjuntos.
Cada variable $L_i$ se obtiene como la conjunción de las variables $\{X_{i_1}, X_{i_2}, ...\}$ pertenecientes al subconjunto $i$. La regla de la conjunción (12.7) conduce a:
$$ P(X_1 \land X_2 \land \dots \land X_n | \delta \land \pi) $$
$$ = P(L_1 | \delta \land \pi) \times P(L_2 | L_1 \land \delta \land \pi) \times \dots \times P(L_k | L_{k-1} \land \dots \land L_2 \land L_1 \land \delta \land \pi) $$
(12.13)
 La hipótesis de independencia condicional permiten entonces simplificaciones adicionales. Una hipótesis de independencia condicional para la variable $L_i$ se define eligiendo algunas variables $X_j$ entre las variables que aparecen en la conjunción $L_{i-1} \land \dots \land L_2 \land L_1$, llamando $R_i$ a la conjunción de esta variables elegidas y estableciendo:
$$P(L_i | L_{i-1}\land \dots \land L_2 \land L_1 \land \delta \land \pi) = P(L_i | R_i \land \delta \land \pi) $$
(12.4)
Obtenemos entonces:
$$P(X_1 \land X_2 \land \dots \land X_n | \delta \land \pi)$$
$$ = P(L_1 | \delta \land \pi) \times P(L_2 | R_2 \land \delta \land \pi) \times P(L_3 | R_3 \land \delta \land \pi) \times \dots \times P(L_k | R_k \land \delta \land \pi) $$
(12.15)
Esta simplificación de la distribución conjunta como producto de distribuciones más simples se denomina descomposición.
Esto garantiza que cada variable aparezca como máximo una ves a la izquierda de una barra de condicionamiento, que es la condición necesaria y suficiente para escribir descomposiciones matemáticas validas.

3. Definir las formas:
Cada distribución $P(L_i | R_i \land \delta \land \pi)$ que aparece en el producto se asocia entonces como una forma paramétrica (es decir, una función $f_\mu((L_i))$ u otro programa Bayesiano. En general, $\mu$ es un vector de parámetros que pueden depender de $R_i$ o $\delta$ o ambos. El aprendizaje tiene lugar cuando algunos de estos parámetros se calculan utilizando el conjunto de datos.

### 12.15 Questions 
Dada una descripción (es decir, $P(X_1, \land X_2 \land \dots \land X_n | \delta \land \pi)$), una pregunta se obtiene dividiendo $\{X_1, X_2, \dots, X_n\}$ en tres conjuntos: las variables buscadas, las variables conocidas y las variables libres.
Definimos las variables *Searched, Know* y *Free* como la conjunción de las variables pertenecientes a estos conjuntos. Definimos una pregunta cono la distribución:
$$ P(Searched | Known \land \delta \land \pi) $$ (12.16)

### 12.16 Inference 
Dada una distribución conjunta $P(X_1 \land X_2 \land \dots \land X_n | \delta \land \pi)$, siempre es posible calcular cualquier pregunta posible, utilizando la siguiente inferencia general:

$$ P(Searched | Known \land \delta \land \pi) = \sum_{Free}P(Searched \land Free | Known \land \delta \land \pi)$$
$$ = \frac{\sum_{Free}P(Searched \land Free \land Known | \delta \land \pi)}{P(Known | \delta \land \pi)} $$
$$ =\frac{\sum_{Free}P(Searched \land Free \land Known | \delta \land \pi)}{\sum_{Searched \land Free}P(Searched \land Free \land Known | \delta \land \pi)}$$
$$= \frac{1}{\Sigma} \times \sum_{Free} P(Searched \land Free \land Known | \delta \land \pi) $$
(12.17)

donde la primera igualdad resulta de la regla de marginalización (12.11), la segunda de la regla del producto (12.7) y la tercera corresponde a una segunda aplicación de la regla de marginalización. EL denominados parece ser un término de normalización. En consecuencia por convención, lo reemplazamos por $\Sigma$.
En teoría, esto nos permite resolver cualquier problema de inferencia Bayesiana. En la práctica, sin embargo, el coste de calcular exhaustivamente y con exactitud $P(Searched | Known \land \delta \land \pi)$ es demasiado grande en la mayoría de casos. El capítulo 14 revisa y explica las principales técnicas y algoritmos para abordar este problema de inferencia.

Antes de eso, el Capítulo 13 revisa los principales modelos bayesianos utilizando el formalismo actual.

## 13 Bayesian Models Revisited
El objetivo de esta sección es presentar los principales modelos probabilísticos utilizados actualmente para la concepción y el desarrollo.

Utilizamos sistemáticamente el formalismo de programación Bayesiana para presentar estos modelos, porque es preciso y conciso y simplifica si comparamos. Nos centraremos principalmente de estos modelos.

Elegimos dividir los diferentes modelos probabilísticos en dos categorías: los modelos probabilísticos de propósito general y los modelos probabilísticos orientados a problemas.

En la primera categoría, las elecciones de modelos realizan independientemente de cualquier conocimiento específico sobre el fenómeno modelado. La mayoría de las veces, estas decisiones se toman esencialmente para mantener la inferencia manejable. Sin embargo, las simplificaciones técnicas de estos modelos pueden ser compatibles con grandes clases de problemas y, en consecuencia, pueden tener numerosas aplicaciones.

En la segunda categoría, por lo contrario, las opciones de modelos y las simplificaciones se deciden de acuerdo con algún conocimiento específico sobre el fenómeno. Estas elecciones podrían eventualmente conducir a modelos muy poderosos desde un punto de vista computacional. Sin embargo, la mayoría de las veces, el conocimiento dependiente del problema, como la independencia condicional entre variables, conduce a simplificaciones y mejoras computacionales muy significativas y efectivas.

### 13.1 General purpose probabilistic models

#### 13.1.1 Graphical models and Bayesian networks

##### Bayesian network
Las redes Bayesianas (BN, por sus siglas en inglés 'Bayesian networks'), introducidas por primera vez por Judea Parl (Pear, 1988), han surgido como un método primario parea trabajar información probabilística e incierta. Son el resultado de la unión entre la teoría de la probabilidad y teoría de grafos. 

Las BN se definen mediante el siguiente programa bayesiano:

![[Figure13_1BP.png]]

- Las variables parientes no están registradas y no tienen una semántica específica,
- La descomposición, por lo contrario, es específica: es un producto de distribuciones con una y sólo una variable $X_i$ condicionada por una conjunción de otras variables $R_i$, llamadas sus padres. Existe una biyección obvia entre ls distribuciones de probabilidad conjuntas definidas por dichas descomposiciones y los *grafos acíclicos dirigidos* (DAG): los nodos están asociados con variables y los bordes orientados están asociadas con dependencias condicionales. El uso de gráfos en modelos probabilísticos conduce a una forma eficiente de definir hipótesis sobre conjunto de variables, una representación económica de la distribución de probabilidad conjunta y, lo más importante, una forma fácil y eficiente de realizar inferencias probabilísticas.
- Las formas paramétricas no están restringidas, pero muy a menudo se limitan a tablas de probabilidad.
- Se han desarrollado técnicas de inferencia muy eficientes para responder a preguntas $P(X_i|known)$, sin embargo, aparecen algunas dificultades con preguntas más generales.

> Readings on Bayesian networks and graphical models should start with the following introductory textbooks: Probabilistic Reasoning in Intelligent Systems : Networks of Plausible Inference (Pearl, 1988), Graphical Models (Lauritzen, 1996), Learning in Graphical Models (Jordan, 1998) and Graphical Models for Machine Learning and Digital Communication (Frey, 1998).

