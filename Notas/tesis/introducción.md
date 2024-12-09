\chapter{Introducción}
\chaptermark{Introducción}
\label{intro}

La modelación de fenómenos físicos no solo facilita la compresión de su funcionamiento, sino que también permite predecir, medir, optimizar, simular, imitar y controlar dichos fenómenos. Con el avance tecnológico actual, es factible convertir modelos en programas computacionales que realicen cálculos para facilitar el uso de los modelos. No obstante, todo modelo y programa enfrenta el desafío de la incompletitud; es decir, ningún modelo de un fenómeno real captura todos sus aspectos. Esto se debe a que, al desarrollar un modelo, existen variables ocultas en el entorno que no se consideran, ya sea por limitaciones tecnológicas o por falta de conocimiento. Por lo tanto, aunque los modelos pueden reproducir comportamientos similares a los fenómenos reales, nunca los replican exactamente. \citep{Pierre2013}

En este estudio se busca mejorar la implementación de un motor de inferencia Bayesiano (MIB1.0), el cual utiliza la probabilidad como marco matemático para tratar con la incompletitud y la incertidumbre,  este marco teórico maneja tanto la información certera como la incierta, y tiene la capacidad de ser un modelo de razonamiento. Este motor se basa en la descripción de programas Bayesianos del libro \textit{``Bayesian Programming"} \citep{Pierre2013}, el cual a su vez se fundamenta en la propuesta de la teoría de la probabilidad como un modelo de razonamiento de Edwar T. Jaynes en su libro \textit{``Probability Theory: The Logic of Science"} \citep{Jaynes2003}.

El motor facilita las descripciones de modelos probabilísticos y cuenta con algoritmos para realizar inferencia exacta sobre distribuciones de probabilidad sobre el moldeo probabilístico discreto. La importancia de este motor de inferencia radica en su amplio alcance de uso. Puede emplearse tanto para describir fenómenos y hacer predicciones, como para que un agente artificial pueda tomar decisiones. Sin embargo, este motor actualmente no es suficiente para abordar problemas del mundo real. Por ello, es crucial desarrollar un motor de inferencia Bayesiano capaz de manejar problemas más complejos y aplicar este método de inferencia a problemas del mundo real.

Este trabajo se enfoca en mejorar y extender las capacidades del motor de inferencia Bayesiana, superando las limitaciones actuales y permitiendo su aplicación efectiva en contextos prácticos y reales. Al hacerlo, se pretende avanzar en la precisión y utilidad de los modelos probabilísticos, abordando la incompletitud y la incertidumbre inherentes a la modelación de fenómenos físicos y otros sistemas complejos.

\section{Antecedentes}
Antes de plantear cuales son los principales problemas del motor de inferencia (MIB1.0), es necesario plantear que es un motor de inferencia, para esto  es necesario establecer el por qué funciona la teoría de la probabilidad como modelo de razonamiento. 

En el libro \textit{``Bayesian Programming"} \citep{Pierre2013} se menciona que que los modelos siempre presentan problemas de incompletitud e incertidumbre.

 \begin{quote}
     La incompletitud es simplemente la brecha irreductible entre el conocimiento preliminar y el fenómeno, y la incertidumbre es una consecuencia directa y mensurable de esta imperfección. \citep{Pierre2013} 
 \end{quote}

En otras palabras, o el conocimiento preliminar es incompleto o existen variables no consideradas.

Por ejemplo, en 1781 Sir William Herschel describió el séptimo planeta del sistema solar, Urano. Mientras tanto, tanto Urbain Leverrier, astrónomo francés, como John Adan se interesaron por la trayectoria incierta de Urano. El planeta no estaba siguiendo exactamente la trayectoria que predecía la teoría de la gravedad de Newton y ambos llegaron a la conclusión de que estas irregularidades deberían ser el resultado de una variable oculta no tomada en cuanta por el modelo: la existencia de un octavo plantea. Incluso fueron mucho más allá y encontraron la posición más probable de este octavo planeta. El observador de Berlín recibió la predicción de Leverrier el 23 de septiembre de 1846 y Johann Galle observó a Neptuno ese mismo día. Por lo tanto es necesario contar tanto con un marco matemático alternativo para poder abordar la incompletitud e incertidumbre que presentan los fenómenos. 

La lógica es la base matemática del razonamiento y el principio fundamental de la computación, lo cual nos haría pensar que es la mejor herramienta para poder describir fenómenos en una computadora y así poder hacer cálculos de mayor escala. Sin embargo, la lógica se limita a problema que disponen de información certera y completa.

Para poder usar la lógica para describir y explicar fenómenos, es necesario extenderla para poder trabajar con información no certera e incompleta. En otras palabras, se debe describir un razonamiento lógico que pueda manejar la incertidumbre.

Basado en las descripciones de la teoría de la probabilidad como un modelo de razonamiento de Edwar T. Jaynes, se observa como es que la probabilidad es una exención de la lógica, tan matemáticamente sensata y simple como la lógica, pero con mayor poder expresivo. 

Para entender como es que la teoría de la probabilidad proporciona un modelo de razonamiento racional en presencia de la incertidumbre, es importante entender como la probabilidad es una exención de la lógica.

\subsection{La probabilidad como una extensión de la lógica}

Edwar T. Jaynes en su libro \textit{``Probability Theory: The Logic of Science"} \citep{Jaynes2003} describe como la probabilidad extiende de la lógica de la siguiente manera.

Supongamos que un policía patrulla una calle aparentemente vacía durante una noche. De repente, escucha una alarma de una joyería, voltea hacia el otro lado de la calle y observa una ventana rota de la joyería. En ese momento, ve a un hombre enmascarado saliendo por la ventana rota, llevando una bolsa llena de joyas. El policía, inmediatamente, concluye que este hombre es un ladrón.

La conclusión del policía no fue una deducción lógica basada en la evidencia, ya que podría haber más evidencias que den explicaciones. Por ejemplo, el hombre podría ser el dueño de la joyería, quien al volver de una fiesta de disfraces, olvidó sus llaves. Al pasar por su tienda, un camión podría haber lanzado una piedra que rompió la ventana, y él simplemente estaba protegiendo su propiedad.

 Las pruebas no demostraban con certeza que el hombre estaba robando, pero sí lo hacían altamente probable. Por esto, aunque el razonamiento del policía no fue una deducción lógica, sí tiene cierto grado de validez.

 Este es un ejemplo de un tipo de razonamiento, en el cual no se tiene suficiente información, sin embargo se puede llegar a una conclusión. Por ejemplo, es casi imposible pasar una hora de vigilia sin enfrentarnos a una situación (por ejemplo, ¿lloverá o no?) en la que no disponemos de suficiente información para hacer un razonamiento deductivo, pero aún así debemos decidir qué hacer de inmediato.

El primer concepto que usamos, es la noción usual de una proposición lógica. Las proposiciones son denotadas por nombres es minúsculas. Se pueden componer proposiciones para obtener nuevas proposiciones utilizando operadores lógicos habituales: $a \land b$, denotando la conjunción de la proposición $a$ y $b$, $a \lor b$ es la disyunción, y $\neg a$, la negación de la proposición $a$. 

El razonamiento deductivo puede analizarse mediante la aplicación repetida de dos silogismos fuertes:

\begin{equation} \label{ModusPonens}
    \begin{array}{c}
    \text{Si } a \text{ es verdadero, entonces } b \text{ es verdadero} \\
    a \text{ es verdadero} \\ \hline
    \text{Por lo tanto, } b \text{ es verdadero}
\end{array}
\end{equation}

y su inverso:
\begin{equation} \label{ModusTollens}
    \begin{array}{c}
    \text{Si } a \text{ es verdadero, entonces } b \text{ es verdadero} \\
    b \text{ es falso} \\ \hline
    \text{Por lo tanto, } a \text{ es falso}
\end{array}
\end{equation}

Este es el tipo de razonamiento en el que se basa la lógica; sin embargo, en casi todas las circunstancias que enfrentamos no contamos con la información necesaria para hacerlo. Por ello, recurrimos a silogismos más débiles:

\begin{equation} \label{silogismoD1}
    \begin{array}{c}
        \text{Si } a \text{ es verdadero, entonces } b \text{ es verdadero} \\
        b \text{ es verdadero} \\ \hline
        \text{Por lo tanto, } a \text{ se vuelve más plausible}
    \end{array}
\end{equation}

La evidencia no prueba que $a$ sea verdadera, pero la verificación de una de sus consecuencias sí nos da más confianza en $a$. Por ejemplo, dadas las siguientes dos proporciones:

\begin{itemize}
    \item $a \equiv$ ``Empezará a llover a más tardar a las 10 de la mañana." 
    \item $b \equiv$ ``El cielo se nublará antes de las 10 de la mañana."
\end{itemize}

Observar las nubes a las 9:45 A.M. no nos proporciona una certeza lógica de que continuará la lluvia; sin embargo, nuestro sentido común, guiado por un silogismo débil, puede llevarnos a modificar nuestros planes y actuar como si creyéramos que lloverá, especialmente si las nubes son lo suficientemente oscuras.

Ahora bien, el razonamiento del policía se describe mejor mediante un silogismo aún más débil:

\begin{equation} \label{silogismoD3}
    \begin{array}{c}
        \text{Si } a \text{ es verdadero, entonces } b \text{ se vuelve más plausible} \\
        b \text{ es verdadero} \\ \hline
        \text{Por lo tanto, } a \text{ se vuelve más plausible}
    \end{array}
\end{equation}

La evidencia no prueba que $a$ sea verdadera, pero la verificación de una de sus posibles consecuencias sí nos da más confianza en $a$. Aunque este argumento puede parecer débil cuando se presenta de manera abstracta en términos de $a$ y $b$. En el caso del policía, la evidencia no prueba del todo que el hombre estaba robando, pero si el hombre estuviera robando hace más posible que se de la situación, por lo tanto es más posible que el hombre si estaba robando la joyería.

Estos ejemplos muestras que el cerebro, al realizar un razonamiento plausible, no solo determina si algo es más o menos plausible, sino que también evalúa el grado de plausibilidad. La probabilidad de que llueva a las 10 A.M. depende en gran medida de lo oscuras que sean las nubes. Además, el cerebro utiliza tanto información previa como datos nuevos específicos del problema; al decidir que hacer, intentamos recordar nuestra experiencia pasada con nubes y lluvia, así como lo que predijo el meteorólogo la noche anterior.

Para demostrar que el policía también estaba haciendo uso de la experiencia pasada de los policías en general, supongamos que hechos como estos ocurrieran varias veces cada noche a todos los policías, y que en todos los casos el hombre resultara ser completamente inocente. Muy pronto, los policías aprenderían a ignorar estos incidentes triviales.

De esta manera, nuestro razonamiento depende en gran medida de la información previa que nos ayuda a evaluar el grado de verosimilitud de un nuevo problema. Este proceso de razonamiento ocurre de manera inconsciente, casi instantánea, y ocultamos su complejidad llamándolo sentido común.

\subsubsection{Razonamiento probabilístico}

Para poder lidiar con el grado de plausibilidad de las proposiciones (en otras palabras, lidiar con la incertidumbre), usamos la teoría de la probabilidad para asignar un valor numérico a la plausibilidad. 

Consideremos que, para asignar una probabilidad a una proposición $a$, es necesario tener al menos algún conocimiento previo, resumido en una proposición $\pi$. En consecuencia, la probabilidad de una proposición $a$ está siempre condicionada, al menos por $\pi$. Para cada diferente $\pi$, $P(\cdot | \pi)$ es una aplicación que asigna a cada proposición $a$ un valor real único $P(a|\pi)$ en el intervalo $[0,1]$. Por supuesto, nos interesa razonar sobre las probabilidades de conjunciones, disyunciones y negaciones de proposiciones, denotadas respectivamente, por $P(a \land b | \pi)$, $P(a \lor b \ \pi)$ y $P(\neg a | \pi)$. \citep{Pierre2013}


\citeauthor{Pierre2013} resumieron el razonamiento probabilístico en soló dos reglas básicas:

\begin{enumerate}
    \item La \textit{regla del producto}, establece la probabilidad de una conjunción de proposiciones $a$ y $b$ de la siguiente manera: 
    
    \begin{equation} \label{reglaP_conjuncion}
        \begin{split}
             P(a \land b | \pi) &= P(a | \pi) P(b | a \land \pi) \\
             &  = P(b | \pi) P(a | b \land \pi)
        \end{split}
    \end{equation}

    \item La \textit{regla de normalización}, que establece que la suma de las probabilidades de $a$ y $a\neg$ es uno.
    \begin{equation} \label{reglaP_normalizacion}
        P(a| \pi) + P(a \neg | \pi) = 1
    \end{equation}
\end{enumerate}

Estas dos reglas (\eqref{reglaP_conjuncion} y \eqref{reglaP_normalizacion}) son suficientes para cualquier cálculo. De hecho, podemos derivar todas las demás reglas de inferencia necesarias a partir de estas dos.  Por ejemplo, la regla de la disyunción de proposiciones:

\begin{equation} \label{relgaP_disyuncion}
    \begin{split}
        P(a \lor b | \pi) &= 1 - P(\neg a \land \neg b | \pi) \\
        &= 1 - P(\neg a | \pi) \times P(\neg b| \neg a \land \pi) \\
        &= 1 - P(\neg a | \pi) \times (1 - P(b| \neg a \land \pi)) \\
        &= P(a| \pi) + P(\neg a \land b | \pi) \\
        &= P(a | \pi) + P(b | \pi) \times P(\neg a|b \land \pi) \\
        &= P(a | \pi) + P(b | \pi) \times (1 - P(a | b | \pi)) \\
        &= P(a | \pi) + P(b | \pi) - P(a \land b | \pi)
    \end{split}
\end{equation}

Toda la lógica consiste en los dos silogismos fuertes \eqref{ModusPonens} y \eqref{ModusTollens}, utilizando ahora el signo de implicación ($\Rightarrow$) para enunciar la premisa mayor.

\begin{equation} \label{MP}
    \begin{array}{c}
        a \Rightarrow b  \\
        a \text{ es verdadero} \\ \hline
        b \text{ es verdadero} 
    \end{array}
\end{equation}

\begin{equation} \label{MT}
    \begin{array}{c}
        a \Rightarrow b \\
        b \text{ es falso} \\ \hline
        a \text{ es falso}
    \end{array}
\end{equation}

y dejemos que $\pi$ represente su premisa mayor, ($\pi \equiv ``a \Rightarrow b"$), entonces estos silogismos corresponden a nuestra regla del producto \eqref{reglaP_conjuncion} en las formas

\begin{equation} \label{probabilidad_silogimos}
    P(b|a \land \pi) = \frac{P(a \land b|\pi)}{P(a|\pi)},   P(\neg a|\neg b \land \pi) = \frac{P(\neg a \land \neg b|\pi)}{P(\neg b|\pi)}
\end{equation}

respectivamente. Pero de \eqref{MP} tenemos que $p(b | a \land \pi) = 1$, el cual significa que sabiendo que $a$ es verdad entonces podemos estar seguros de que $b$ es verdadero.

Usando la regla de la normalización y producto en $P(\neg a|\neg b \land \pi)$, obtenemos lo siguiente:

\begin{equation}
    \begin{split}
        P(\neg a | \neg b \land \pi) &= 1 - P(a|\neg b \land \pi) \\
        & = 1 - \frac{P(\neg b | a \land \pi) P(a | \pi)}{P(\neg b | \pi)} \\
        & = 1 - \frac{(1 - (P(b | a \land \pi))P(a)}{P(\neg b | \pi)} \\
    \end{split}
\end{equation}
porque $P(b | a \land \pi) = 1$, entonces por la regla \eqref{reglaP_normalizacion}

\begin{equation}
    P(\neg a|\neg b \land \pi) = 1
\end{equation}

por lo tanto, sabiendo que $b$ es falso entonces podemos estar seguros de que $a$ es falso.

Pero estas reglas también tienen lo que no está contenido en la lógica deductiva: una forma cuantitativa de los silogismos débiles \eqref{silogismoD1} y \eqref{silogismoD3}. Para mostrar que estos enunciados cualitativo siempre se siguen de las reglas actuales, observemos que el primer silogismo débil

\begin{equation} \label{SD1R}
    \begin{array}{c}
        a \Rightarrow b  \\
        b \text{ es verdadero} \\ \hline
        \text{Por lo tanto, } a \text{ se vuelve más plausible} 
    \end{array}
\end{equation}
corresponde a la regla del producto \eqref{reglaP_conjuncion} en la forma

\begin{equation} \label{SD1P}
    P(a | b \land \pi) = P(a|\pi) \frac{P(b|a \land \pi)}{P(b | \pi)}.
\end{equation}
Pero de \eqref{MP}, $P(b|a \land \pi) = 1$, y dado que $P(b|\pi) \leq 1$, \eqref{SD1P} da

\begin{equation} \label{SD1PC}
    P(a|b \land \pi) \geq P(a|\pi) 
\end{equation}
como se afirma en el silogismo.

Finalmente, el silogismo del policía \eqref{silogismoD3}, el cual también está contenido la regla del producto, enunciada en la forma \eqref{SD1P}. Si ahora $\pi$ representa la premisa mayor, ``Si $a$ es verdadera, entonces $b$ se vuelve más plausible", ahora toma la forma

\begin{equation}
    P(b|a \land \pi) > P(b|\pi)
\end{equation}

y \eqref{SD1P} da inmediatamente

\begin{equation}
    P(a|b \land \pi) > P(a|\pi)
\end{equation}

De esta forma, se pude observar como es que la teoría de la probabilidad tiene la capacidad de funcionar como un modelo de razonamiento, que vas más allá de la lógica,  además de que se puede utilizar para problemas que no disponen de información certera y completa.

\subsection{Programación Bayesiana}
 Sin embargo, la teoría de la probabilidad por sí sola no es suficiente para describir de manera intuitiva los fenómenos del mundo real como un modelo probabilístico, ya que no cuenta con una metodología para describir un fenómeno, ni para formular preguntas a dicho modelo con el fin de calcular un grado de plausibilidad. Para abordar esta limitación, se introduce el concepto de programación Bayesiana (ver en la sección \eqref{cap2:mt:programacion_bayesiana}). Este enfoque no solo proporciona un marco conceptual, sino que también ofrece una metodología para generar descripciones probabilísticas tanto para los fenómenos como para las preguntas planteadas.
 
Un programa Bayesinao constituye principalmente de una descripción y un pregunta.


\begin{itemize}
    \item \textbf{Descripción}: El propósito de una descripción es especificar un método para calcular una distribución conjunta, donde la distribución conjunta representa nuestra base de conocimientos.

    \item \textbf{Pregunta}: el propósito de una pregunta es especificar método para calcular probabilidades para proposiciones de consulta dada una descripción, por ejemplo calicular la probabilidad del silogismo \eqref{silogismoD3} en su forma de probabilidad $P(a|b \land \pi)$.
\end{itemize}

\subsection{¿Qué es un Motor de Inferencia Bayesiano?}
Definamos un motor de inferencia Bayesiano como un sistema destinado a obtener respuestas a preguntas formuladas dentro de un modelo probabilístico. En este contexto, se implementa el concepto de programación Bayesiana para la descripción de los modelos, y se utilizan las redes de Bayes para la descomposición de la distribución conjunta (ver sección \eqref{cap2:redes_bayes}).

\subsubsection{Inferencia Bayesiana exacta}
Antes de presentar las reglas de inferencia probabilística es necesario establecer que es la inferencia.

La inferencia se refiere a dos tipos de razonamiento: deductivo, cuando siempre se dispone de suficiente información para permitirlo, e inductivo o probabilístico, cuando no se cuanta con toda la información necesaria,  lo cual es común en la mayoría de los problemas reales. \citep{Jaynes2003}

Las siguientes reglas detallan un método sencillo para la inferencia probabilística, el cual se basa en las reglas de inferencia en probabilidades (ver sección \eqref{cap2:mt:riv}). Para este propósito, se utiliza una distribución de probabilidad conjunta como la base de conocimientos, del cual se puede derivar respuestas a todas las proposiciones de consulta.

De la teoría de la probabilidad se tienen las siguientes ecuaciones para calcular dos distribuciones de con las cuales se pueden derivar todas las proposiciones de consulta de manera general.

Cada vez que aparece $X$ en una fórmula probabilística $\Phi (X)$, debe entenderse como $\forall x_i \in X, \Phi(x_i)$.

\begin{enumerate}
    \item \textbf{Marginal}: 
        \begin{equation} \label{inferencia_marginal}
            \begin{split}
                P(X_i) &= \sum_{X_1,\dots,X_{i-1},X_{i+1},\dots,X_n} P(X_1,\dots,X_n) 
            \end{split}
        \end{equation}
        donde cada $X_j$ es simplemente un conjunto de valores ($ X_j$ una variable).
        
    \item \textbf{Distribuciones condicionales}: 
        \begin{equation} \label{inferencia_condicional}
            \begin{split}
                P(X_i|X_j) &= \frac{P(X_i,X_j)}{P(X_j)} \\
                &= \frac{\sum_{X_1,\dots,X_{i-1},X_{i+1},\dots,X_{j-1},X_{j+1},\dots,X_n} P(X_1,\dots,X_n)} {\sum_{X_1,\dots,X_{i-1},X_{i+1},\dots,X_n} P(X_1,\dots,X_n)}
            \end{split}
        \end{equation}

       en la segunda igualdad se aplica la ecuación \eqref{inferencia_marginal}.
       
\end{enumerate}

Con las ecuaciones \eqref{inferencia_marginal} y \eqref{inferencia_condicional} se describen los dos siguientes algoritmos para realizar el calculo distribuciones de consulta.

Pero antes es necesario describir algunos datos auxiliares para facilitar la descripción de los algoritmos. Dado $X = \{X_1, X_2, \dots, X_n\}$ un conjunto de variables de un modelo probabilístico, sea $V = X$, $k$ el subíndice de una variable del conjunto $X$ y $e \in X_k$ el valor del evento a calcular, se describe el algoritmo \eqref{alg:cap1:marginal}, el cual realiza la inferencia sobre una distribución marginal.

\begin{algorithm}[ht]
    \caption{Algoritmo para el cálculo de marginales}\label{alg:cap1:marginal}
    \begin{algorithmic}
        \Procedure{marginal}{$V = \{V_1,\dots,V_n\}, k, e$} \Comment{V = X}
            \State $V_k = \{e\}$
            \State $PV = V_1 \times V_2 \times \dotsi \times V_n$
            \State $p = 0$
            \For {$i=1,2,\dots,|PV|$}
                \State $p = P(X_1 = PV_{i_1},\dots, X_n = PV_{i_n}) + p$
            \EndFor
            \State \textbf{return} $p$
        \EndProcedure
    \end{algorithmic}
\end{algorithm}


Sea $Y,Z \subseteq X$ tal que $Y \neq Z$ y $V = X$. Definamos dos listas auxiliares $H$ y $O$, donde $\forall H_i \in H, H_i \in Y_i$ y $\forall O_i \in O, O_i \in Z_i$, se describe el algoritmo \eqref{alg:cap1:condicional}, el cual realiza la inferencia sobre una distribución condicional.

\begin{algorithm}[ht]
    \caption{Algoritmo para el cálculo de condicionales}\label{alg:cap1:condicional}
    \begin{algorithmic}
        \Procedure{condicional}{$Y,Z,X,H,O$} 
            \State $N = X \setminus \{Y \cup Z\}$
            \State $D = X \setminus Y$
            
            \State $NP = H \times O \times N_1 \times \dotsi \times N_k$
            \State $np = 0$
            \For {$i=1,2,\dots,|NP|$}
                \State $np = P(X_1 = NP_{i_1}, X_2 = NP_{i_2}, \dots, X_n = NP_{i_n}) + np$
            \EndFor

            \State $DP = Y \times O \times D_1 \times D_2 \times \dotsi \times D_p$
            \State $dp = 0$
            \For {$i=1,2,\dots,|DP|$}
                \State $dp = P(X_1 = DP_{i_1}, X_2 = DP_{i_2}, \dots, X_n = DP_{i_n}) + dp$
            \EndFor
            
            \State \textbf{return} $\frac{np}{dp}$
        \EndProcedure
    \end{algorithmic}
\end{algorithm}

\section{Planteamiento del Problema}
Para realizar inferencia Bayesiana exacta, el motor de inferencia enfrenta un problema significativo relacionado con la memoria requerida. En la propuesta actual del motor de inferencia (MIB1.0), para la inferencia exacta se almacena cada una representación de todas las combinaciones posibles de eventos para las variables especificadas en los algoritmos \eqref{alg:cap1:marginal} y \eqref{alg:cap1:condicional}.

El espacio para almacenar el producto cartesiano de las variables para una marginal, del algoritmo \eqref{alg:cap1:marginal} se puede representar con la siguiente ecuación:

\begin{equation} \label{Ecuacion_espacial}
    E_m(X) = \prod_{X_i \in X} |X_i|
\end{equation}

donde $|X_i|$ denota la cardinalidad de la variable $X_i$, el número posible de los valores de 

De la ecuación anterior podemos calcular la complejidad espacial y temporal de la siguiente manera.

Sea $c = max\{|X_1|, |X_2|, \dots, |X_n|\}$ , entonces

\begin{equation}
     \prod_{X_i \in X} |X_i| \leq c^n
\end{equation}

por lo tanto,

\begin{equation} \label{espacial_marginal}
    O(E_m(X)) = c^n
\end{equation}

Como el algoritmo \eqref{alg:cap1:marginal} necesita calcular la probabilidad conjunta sobre todas las combinaciones posibles de las variables, con el valor de una variable fijada, se pude concluir que la complejidad espacial es la misma que la complejidad temporal. Sea $T_m$ la función que describe el tiempo del algoritmo \eqref{alg:cap1:marginal} sobre la entrada $V$, se tiene lo siguiente:

\begin{equation} \label{temporal_marginal}
    T_m(X) = E_m(X) \leq c^n 
\end{equation}
\begin{equation}
    \therefore O(T_m(X)) = c^n
\end{equation}

De manera similar, la complejidad espacial del algoritmo \eqref{alg:cap1:condicional} se puede representar con la siguiente ecuación:

\begin{equation} \label{espacial_condicional}
    E_c(Y,Z,X) = \prod_{X_i \in X \setminus \{Y \cup Z\}} |X_i| + \prod_{X_i \in X \setminus Y} |X_i|
\end{equation}

Sea $c = max\{|X_1|, |X_2|, \dots, |X_n|\}$ y $k = max\{n - |X \setminus Y|, n - |X \setminus \{Y \cup Z\}|\}$, entonces

\begin{equation}
   \begin{split}
       \prod_{X_i \in X \setminus \{Y \cup Z\}} |X_i| + \prod_{X_i \in X \setminus Y} |X_i| &\leq c^k + c^k \\
       &\leq 2c^k 
   \end{split}
\end{equation}

\begin{equation}
      \therefore O(E_c(Y,Z,X)) = c^k
\end{equation}

Como el algoritmo \eqref{alg:cap1:condicional} necesita calcular la probabilidad conjunta sobre todas las combinaciones del conjunto $NP$ y sobre todas las combinaciones del conjunto $DP$, esto quiere decir que la complejidad temporal se puede expresar con la siguiente ecuación:

\begin{equation} \label{temporal_condicional}
    T_c(Y,Z,X) = E_c(Y,Z,X) \leq 2c^k
\end{equation}

\begin{equation}
    \therefore O(T_c(Y,Z,X)) = c^k
\end{equation}

Con las complejidades de los algoritmos, se pueden observar dos problemas,  la memoria y tiempo requerido para la inferencia crece de manera exponencial
Incluso en problemas con variables exclusivamente booleanas, los recursos necesarios resultan demasiado costosos. Por lo tanto, en problemas con muchas variables y variables más complejas, el calculo de la inferencia se vuelve intratable.

Otro de los principales problemas es que el motor de inferencia heredado requiere una forma para poder determinar que valor de las variables le corresponde a las variables de la descomposición de la conjunta. Por ejemplo, supongamos la descomposición $P(CENO)=P(C)P(E)P(N
|CE)P(O|N)$, para este caso se necesita una tabla de probabilidad para cada distribución. Donde una tabla de probabilidad es un diccionario, el cual asigna un valor de probabilidad entre $[0,1]$ a una llave que representa un evento. Por ejemplo, para la variable $C=\{0,1\}$, el consultar la llave $(``C",0)$ en el diccionario equivale a consultar el valor que regresa $P(C=0)$.

Ya que la forma de guardar las combinaciones, para la marginal, es a través de una tupla con nombre y los valores, por ejemplo, para $P(C=0,E=2,N=1,O=0)$ se genera la llave

\begin{equation}
    key = (``C",``E",``N",``O",0,2,1,0).
\end{equation}

¿Cómo determinar que valor de la tupla le corresponde a $P(C)$, $P(E)$, $P(N|CE)$, y $P(O|N)$ ?, esto quiere decir, que de la tupla $key$ se tienen que generar todas las llaves para cada distribución de la descomposición. Tomemos la distribución $P(N|CE)$, de $key$ se tiene que generar $(``N",1)$ y $(``C",``E",0,2)$ para realizar la consulta de $P(N=1|C=0, E=2)$. Esto implica que el \textit{MIB1.0} necesita algún algoritmo para generar las lleves. Sin embargo, el algoritmo empleado para resolver la generación de llaves es difícil de analizar, además de que es un método planteado es poco eficiente para realizar las consultas de probabilidad. Esto deja ver otro problema del \textit{MIB1.0}, la complejidad de la codificación y la poca maleabilidad que tiene la implementación, lo cual complica la adaptación de nuevos métodos o modificación de la implementación.


Por lo tanto se plantean cuatro problemas a resolver:
\begin{enumerate}
    \item la memoria requerida para la inferencia crece de manera exponencial,
    \item la memoria requerida para la inferencia crece de manera exponencial,
    \item asignación de los valores a la descomposición de la conjunta,
    \item complejidad y maleabilidad de la implementación.
\end{enumerate}

\section{Objetivo}

El objetivo general de esta tesis es mejorar la eficiencia del MIB1.0, implementando un método para la asignación de los valores a la descomposición de la conjunta y métodos de aproximación para la inferencia. Se pretende desarrollar una implementación con una estructura sólida y fácil de manejar (MIB2.0). 

Además, esta investigación busca proporcionar visibilidad sobre el uso de este motor de inferencia y presentar los principales desafíos asociados con la implementación de un motor de inferencia Bayesiano. De este modo, se espera que la comunidad científica pueda, en el futuro, llevar esta herramienta a un nivel superior y aplicarla a problemas de mayor dimensión. 


\section{Objetivos específicos}
\begin{itemize}
    \item Diseñar mejoras para la implementación de la estructura de datos con el fin de disminuir la cantidad de memoria necesaria para describir el modelo probabilístico.
    \item Implementar métodos de aproximación para la inferencia.
    \item Analizar la complejidad temporal y espacial de los algoritmos.
    \item Desarrollar una implementación con una codificación robusta y flexible.
    \item Evaluar y comparar los tiempos de ejecución de la implementación del motor de inferencia Bayesiano (MIB2.0).  
\end{itemize}