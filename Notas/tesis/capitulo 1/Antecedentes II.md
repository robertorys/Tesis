Antes de plantear que es un motor de inferencia Bayesuiano y  cuales son sus problemas, es necesario establecer el porque funciona la teoría de la probabilidad como modelo de razonamiento y porque es capas de tratar con la incompletitud. 

En el libro "Bayesian Programming" de \cite{Pierre2013}, se menciona que que los modelos siempre presentan problemas de incompletitud e incertidumbre. En otras palabras, es imposible encontrar todas las causas que afectan a un problema o fenómeno, podaríamos creer que hemos logrado encontrar todas las causas, pero no hay manera de probar afirmar que son todas las causas ; y también es imposible el recolectar toda la información completa de un problema.  

Por ejemplo, en 1781 Sir William Herschel describió el séptimo planeta del sistema solar, Urano. Mientras tanto, tanto Urbain Leverrier, astrónomo francés, como John Adan se interesaron por la trayectoria ''incierta'' de Urano. El planeta no estaba siguiendo exactamente la trayectoria que predecía la teoría de la gravedad de Newton. Ambos llegaron a la conclusión de que estas irregularidades deberían ser el resultado de una variable oculta no tomada en cuanta por el modelo: la existencia de un octavo plantea. Incluso fueron mucho más allá y encontraron la posición más probable de este octavo planeta. El observador de Berlín recibió la predicción de Leverrier el 23 de septiembre de 1846 y Johann Galle observó a Neptuno ese mismo día. Por lo tanto es necesario contar tanto con un marco matemático y computacional alternativo para poder abordar la la incompletitud e incertidumbre que presentan todos los fenómenos. 

 \begin{quote}
     La incompletitud es simplemente la brecha irreductible entre el conocimiento preliminar y el fenómeno, y la incertidumbre es una consecuencia directa y mensurable de esta imperfección. \citep{Pierre2013} 
 \end{quote}
 
 La lógica es la base matemática del razonamiento y el principio fundamental de la computación, lo cual nos haría pensar que es la mejor herramienta para poder describir fenómenos para poder trabajarlos en una computadora y  hacer cálculos de mayor escala. Sin embargo, la lógica no pude utilizarse para modelar fenómenos debido a su limitación a problemas que disponen de información certera y completa.  

En el mismo libro, se propone a la teoría de la probabilidad como un marco matemático alternativo. La probabilidad es una exención de la lógica, tan matemáticamente sensata y simple como la lógica, pero con mayor poder expresivo.   

Para entender como es que la teoría de la probabilidad proporciona un modelo de razonamiento racional en presencia de incompletitud e incertidumbre, es importante entender como la probabilidad es una exención de la lógica.

Siguiendo la descripción discutida en \cite{Jaynes2003}, se considera la siguiente situación: un policía patrulla una calle aparentemente vacía durante una noche oscura. De repente, escucha una alarma antirrobo, voltea hacia el otro lado de la calle y observa una joyería con una ventana rota. En ese momento, ve a un hombre enmascarado saliendo por la ventana rota, llevando una bolsa llena de joyas. El policía, sin vacilar, concluye que este hombre es un ladrón. Pero, ¿cómo llega a esta conclusión? Primero, examinemos cuidadosamente la naturaleza de tales problemas.

La conclusión del policía no fue una deducción lógica basada en la evidencia; ya que podría haber otras explicaciones. Por ejemplo, el hombre podría ser el dueño de la joyería, quien, al volver de una fiesta de disfraces, olvidó sus llaves. Al pasar por su tienda, un camión podría haber lanzado una piedra que rompió la ventana, y él simplemente estaba protegiendo su propiedad.

Aunque el razonamiento del policía no fue una deducción lógica, podemos admitir que tenía un cierto grado de validez. Las pruebas no demostraban la deshonestidad del hombre con certeza, pero sí la hacían altamente probable. Este es un ejemplo de un tipo de razonamiento que todos hemos desarrollado de manera más o menos competente, necesariamente, mucho antes de estudiar teorías matemáticas. Es casi imposible pasar una hora de vigilia sin enfrentarnos a una situación (por ejemplo, ¿lloverá o no?) en la que no disponemos de suficiente información para hacer un razonamiento deductivo, pero aún así debemos decidir qué hacer de inmediato.

Todas las discusiones sobre estas cuestiones comienzan contrastando el razonamiento deductivo con el razonamiento plausible. El razonamiento deductivo puede analizarse mediante la aplicación repetida de dos silogismos fuertes:

\begin{equation} \label{silogismoF1}
    \begin{array}{c}
    \text{Si } A \text{ es verdadero, entonces } B \text{ es verdadero} \\
    A \text{ es verdadero} \\ \hline
    \text{Por lo tanto, } B \text{ es verdadero}
\end{array}
\end{equation}

y su inverso:
\begin{equation} \label{silogismoF2}
    \begin{array}{c}
    \text{Si } A \text{ es verdadero, entonces } B \text{ es verdadero} \\
    B \text{ es falso} \\ \hline
    \text{Por lo tanto, } A \text{ es falso}
\end{array}
\end{equation}

Este es el tipo de razonamiento que quisiéramos emplear siempre; sin embargo, como se ha mencionado, en casi todas las circunstancias que enfrentamos no contamos con la información necesaria para hacerlo. Por ello, recurrimos a silogismos más débiles:

\begin{equation} \label{silogismoD1}
    \begin{array}{c}
        \text{Si } A \text{ es verdadero, entonces } B \text{ es verdadero} \\
        B \text{ es verdadero} \\ \hline
        \text{Por lo tanto, } A \text{ se vuelve más plausible}
    \end{array}
\end{equation}

La evidencia no prueba que A sea verdadera, pero la verificación de una de sus consecuencias sí nos da más confianza en A. Por ejemplo, dado


\begin{itemize}
    \item $A \equiv$ ''Empezará a llover a más tardar a las 10 de la mañana.'' 
    \item $B \equiv$ ''El cielo se nublará antes de las 10 de la mañana.''
\end{itemize}

Observar las nubes a las 9:45 a. m. no nos proporciona una certeza lógica de que continuará la lluvia; sin embargo, nuestro sentido común, guiado por un silogismo débil, puede llevarnos a modificar nuestros planes y actuar como si creyéramos que lloverá, especialmente si las nubes son lo suficientemente oscuras.

Otro silogismo débil:

\begin{equation} \label{silogismoD2}
    \begin{array}{c}
        \text{Si } A \text{ es verdadero, entonces } B \text{ es verdadero} \\
        A \text{ es falso} \\ \hline
        \text{Por lo tanto, } B \text{ se vuelve menos plausible}
    \end{array}
\end{equation}

En este caso, la evidencia no demuestra que B sea falsa; sin embargo, se ha eliminado una de las posibles razones que la sostendrían, lo que disminuye nuestra confianza en B. El razonamiento que utiliza un científico para aceptar o rechazar sus teorías se basa casi por completo en silogismos del segundo \eqref{silogismoD1} y tercer tipo \eqref{silogismoD2}.

Ahora bien, el razonamiento de nuestro policía ni siquiera era del tipo mencionado anteriormente. Se describe mejor mediante un silogismo aún más débil:

\begin{equation} \label{silogismoD3}
    \begin{array}{c}
        \text{Si } A \text{ es verdadero, entonces } B \text{ se vuelve más plausible} \\
        B \text{ es verdadero} \\ \hline
        \text{Por lo tanto, } A \text{ se vuelve más plausible}
    \end{array}
\end{equation}

Aunque este argumento puede parecer débil cuando se presenta de manera abstracta en términos de $A$ y $B$, reconocemos que la conclusión del policía tiene un gran poder persuasivo. Hay algo que nos lleva a crear que, en ese caso particular, su razonamiento es casi tan fuerte como una deducción lógica.

Estos ejemplos demuestran que el cerebro, al realizar un razonamiento plausible, no solo determina si algo es más o menos plausible, sino que también evalúa el grado de plausibilidad. La probabilidad de que llueva a las 10 a.m. depende en gran medida de lo oscuras que sean las nubes. Además, el cerebro utiliza tanto información previa como datos nuevos específicos del problema; al decidir que hacer, intentamos recordar nuestra experiencia pasada con nubes y lluvia, así como lo que predijo el meteorólogo la noche anterior.

Para demostrar que el policía también estaba haciendo uso de la experiencia pasada de los policías en general. Supongamos que hechos como estos ocurrieran varias veces cada noche a todos los policías, y que en todos los casos el hombre resultara ser completamente inocente. Muy pronto, los policías aprenderían a ignorar estos incidentes triviales.

De esta manera, nuestro razonamiento depende en gran medida de la información previa que nos ayuda a evaluar el grado de verosimilitud de un nuevo problema. Este proceso de razonamiento ocurre de manera inconsciente, casi instantánea, y ocultamos su complejidad llamándolo sentido común.

Cada vez que podemos construir un modelo matemático que reproduzca una parte del sentido común, prescribiendo un conjunto definido de operaciones, esto nos muestra cómo ''construir una máquina'' (es decir, escribir un programa de computadora) que opere con información incompleta y realice un razonamiento plausible en lugar de uno deductivo.

En lugar de preguntarnos ''¿Cómo podemos construir un modelo matemático del sentido común humano?'', deberíamos preguntarnos ''¿Cómo podríamos construir una máquina que pudiera llevar a cabo un razonamiento plausible y útil, siguiendo principios claramente definidos que expresen un sentido común idealizado?''.
