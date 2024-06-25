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
Es muy importante para adquirir una sensación intuitiva clara de lo que significa una probabilidad condicional y la regla de conjunción. Un primer paso hacia esta comprensión puede ser los silogismos lógicos clásicos en us formas probabilísticas.

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
 $$= 1 - \frac{(1 - P(b|a))P(a)}{\neg b} $$
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
El primer concepto que usamos es la noción usual de una *proposición lógica*. Las proposiciones son denotadas por nombres es minusculas. Se pueden componer proposiciones para obtener nuevas proposiciones utilizando operadores lógicos habituales: $a \land b$, denotando la conjunción de la proposición $a$ y $b$, $a \lor b$ es la disyunción, y $\neg a$, la negación de la proposición $a$.

### 12.3  Probability of a propositions

Para poder lidiar con la incertidumbre, asignamos probabilidades a las proposiciones.

Consideremos que, para asignar una probabilidad a una proposición $a$, es necesario tener al menos algún *conocimiento previo*, resumido en una proposición $\pi$. En consecuencia, la probabilidad de una proposición $a$ está siempre condicionada, al menos por $\pi$. Para cada diferente $\pi$, $P(\cdot | \pi)$ es una aplicación que asigna a cada proposición $a$ un valor real único $P(a|\pi)$ en el intervalo $[0,1]$.

Por supuesto, nos interesa razonar sobre las probabilidades de conjunciones, disyunciones y negaciones de proposiciones, denotadas respectivamente, por $P(a \land b | \pi)$, $P(a \lor b \ \pi)$ y $P(\neg a | \pi)$.

También nos interesa la probabilidad de la proposición a condicionada tanto por el conocimiento preliminar $\pi$ como por alguna otra proposición b. Esto denota $P(a | b \land \pi)$.

### 12.4 Normalization and conjunctions postulates 

El razonamiento probabilístico requiere soló dos reglas básicas:

1. La regla de la conjunción, que de la probabilidad de una conjunción de proposiciones.
$$ P(a \land b | \pi) = P(a | \pi) \times P(b | a \land pi) $$
$$ = P(b | \pi) \times P(a \land \pi)$$


