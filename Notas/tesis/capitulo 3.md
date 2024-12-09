\section{Estructuras de datos}
Se propone utilizar el paradigma de programación orientada a objetos para la descripción de las estructuras de datos, aprovechando que este enfoque permite especificar atributos y métodos para una clase. Este paradigma ofrece una solución al problema de determinar qué valor de las variables corresponde a las variables de la descomposición. Especificando atributos para las variables que almacenen los valores posibles de cada variable y un método para establecer un evento y modificar los valores posibles para que solo considere este evento, sin perder la información de los demás eventos posibles.

Dado que en la propuesta las variables serán objetos, se propone la siguiente metodología para trabajar con el problema de determinar qué valor de las variables corresponde a las variables de la descomposición.  La generación de combinaciones se realizará de manera que se cree una lista de valores, donde dada la tupla $(V_{i_1},V_{i_2},\dots, V_{i_n})$, cada valor $V_{i_j}$ corresponderá a un evento a establecer para la variable a la variable $X_j$.

De forma que a las distribuciones se les para sus variables especificados como objetos, de forma que las distribuciones solo deberán consultar el atributo que contenga el valor del evento establecido. De este modo, a las distribuciones se les asignarán sus variables especificadas como objetos, de manera que las distribuciones solo necesitarán consultar el atributo que contenga el valor del evento establecido. Esta metodología simplifica el proceso de inferencia, facilitando el manejo y la manipulación de las variables y sus correspondientes valores dentro del motor de inferencia Bayesiano. 
Se propone utilizar \textit{pyhton} para la implementación de las clases, aprovechando la versatilidad que este lenguaje tiene en la especificación de tipos de datos en los parámetros. Lo cual nos permite establecer cualquier tipo de dato para la representación de valores para las variables. A continuación se especifica los diagramas de clases.

\subsection{Clase para variables}
\begin{figure}[ht]
    \centering
    \includegraphics[width=0.3\linewidth]{images/Clases/ClaseVar.png}
    \caption{Diagrama de clase para las variables.}
    \label{fig:ClaseVar}
\end{figure}

Para la clase de las variables se propone el diagrama que se muestra en la imagen \ref{fig:ClaseVar}.

Se describen los atributos de la siguiente manera:
\begin{itemize}
    \item \textit{values}: Conjunto de valores posibles para las variables.
    \item \textit{event}: Valor del evento, tiene que pertener a \textit{values}.
    \item \textit{infer}: Boleano para identificar que se realizara inferencia sobre esta variable.
\end{itemize}

\subsection{Clase para distribuciones}

\subsubsection{Distribución marginal}
\begin{figure}[ht]
    \centering
    \includegraphics[width=0.3\linewidth]{images/Clases/ClaseDistrib.png}
    \caption{Diagrama de clase para las distribuciones marginales.}
    \label{fig:ClaseDistrib}
\end{figure}

Para la clase de las distribuciones marginales se propone el diagrama que se muestra en la imagen \ref{fig:ClaseDistrib}.

Se describen los atributos de la siguiente manera:
\begin{itemize}
    \item \textit{var}: Objeto de tipo Var, guarda la variable de la distribución.
    \item \textit{table}: Diccionario con la de probabilidad da cada valor de la variable. 
\end{itemize}

\subsubsection{Distribución condicional}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.3\linewidth]{images/Clases/ClaseCondDistrib.png}
    \caption{Diagrama de clase para las distribuciones condicionales.}
    \label{fig:ClaseCondDistrib}
\end{figure}

Para la clase de las distribuciones condicionales se propone el diagrama que se muestra en la imagen \ref{fig:ClaseCondDistrib}.

Se describen los atributos de la siguiente manera:
\begin{itemize}
    \item \textit{var}: Objeto de tipo Var, guarda la variable de la distribución.
    \item \textit{indep}: Conjunto de objetos de de tipo Var, guarda las variables independientes en la distribución condicional.
    \item \textit{table}: Diccionario con la de probabilidad da cada valor de la variables. 
\end{itemize}


\subsubsection{Distribución conjunta}
\begin{figure}[ht]
    \centering
    \includegraphics[width=0.3\linewidth]{images/Clases/ClaseJointDistrib.png}
    \caption{Diagrama de clase para las distribuciones conjuntas.}
    \label{fig:ClaseJointDistrib}
\end{figure}

Para la clase de las distribuciones condicionales se propone el diagrama que se muestra en la imagen \ref{fig:ClaseJointDistrib}.

Se describen los atributos de la siguiente manera:
\begin{itemize}
    \item \textit{vars}: Conjunto de objetos de de tipo Var, guarda las variables de la distribución.
    \item \textit{table}: Diccionario con la de probabilidad da cada valor de la variables. 
\end{itemize}

\subsection{Clases para el motor de inferencia}
\begin{figure}[ht]
    \centering
    \includegraphics[width=0.3\linewidth]{images/Clases/ClaseModel.png}
    \caption{Diagrama de clase para los modelos probabilísticos.}
    \label{fig:ClaseModel}
\end{figure}

Para la clase del motor de inferencia se proponen dos diagramas \ref{fig:ClaseModel} y \ref{fig:ClaseMib}.

El diagrama de la imagen \ref{fig:ClaseModel} representa la cales para especificar las variables y descomposición de un modelo probabilístico, además se propone un método para recuperar los valores posibles de las variables para una inferencia.

Se describen los atributos de la siguiente manera:
\begin{itemize}
    \item \textit{vars}: Conjunto de objetos de de tipo Var, guarda las variables de la distribución conjunta.
    \item \textit{descomp}: Conjunto de objetos de tipo Distrib y CondDistrib para guardad la descomposición de la distribución conjunta.
\end{itemize}

\begin{figure}[ht]
    \centering
    \includegraphics[width=0.3\linewidth]{images/Clases/ClaseMib.png}
    \caption{Diagrama de clase para el motor de inferencia.}
    \label{fig:ClaseMib}
\end{figure}

El diagrama de la imagen \ref{fig:ClaseMib} representa la cales para crear un motor de inferencia el cual tiene la tarea de realiza la inferencia.

Se describen los atributos de la siguiente manera:
\begin{itemize}
    \item \textit{jointDistrib}: Objeto de tipo Model.
\end{itemize}


\section{Diseño de algoritmos}
Para la inferencia exacta se proponen dos algoritmos: uno para el cálculo de las marginales y otro para las distribuciones condicionales.

Dada la complejidad temporal de la regla de marginales, descrita en la ecuación \eqref{espacial_marginal}, se observa que la memoria requerida crece de manera exponencial. Para abordar este problema, se propone utilizar la función '\textit{product}' de la librería '\textit{itertools}', que emplea el concepto de generadores en Python. Esto permite consultar uno a uno los elementos del producto cartesiano de los iterables pasados como parámetro, evitando así la necesidad de almacenar todas las combinaciones en memoria.

A continuación, se presentan los algoritmos para la inferencia exacta.

\begin{algorithm}[htb]
    \caption{Algoritmo para el cálculo de marginales con `product'}\label{alg:cap3:marginal}
    \begin{algorithmic}
        \State \textbf{Global variables:}
        \State $X = \{X_1,\dots,X_n\}$
        
        \Procedure{marginal}{$V,E$} \Comment{$V \subset X$}
            \For {$k=1$ \textbf{to} $|E|$}
                \State $v_k = E_k$
            \EndFor
            
            \State $p = 0$
            
            \For {$PX$ \textbf{in} $product([X_1,\dots, X_n])$}
                \State $p = P(X_1 = PX_1,\dots, X_n = PX_n) + p$
            \EndFor
            \State \textbf{return} $p$
        \EndProcedure
    \end{algorithmic}
\end{algorithm}

\begin{algorithm}[htb]
    \caption{Algoritmo para el cálculo de condicionales  con `product'}\label{alg:cap3:condicional}
    \begin{algorithmic}
        \State \textbf{Global variables:}
        \State $X = \{X_1,\dots,X_n\}$
        \Procedure{condicional}{$Y,Z,H,O$} \Comment{$Y \subset X$ and $Z \subset X$}
            \For {$k=1$ \textbf{to} $|H|$}
                \State $y_k = H_k$
            \EndFor
            \For {$k=1$ \textbf{to} $|O|$}
                \State $z_k = O_k$
            \EndFor
            
            \State $np = 0$
            \For {$NP$ \textbf{in} $product([X_1,\dots,X_n])$}
                \State $np = P(X_1 = NP_1, X_2 = NP_2, \dots, X_n = NP_n) + np$
            \EndFor

            \State $dp = 0$
            \For {$DP$ \textbf{in} $product([X_1,\dots,X_n])$}
                \State $dp = P(X_1 = DP_1, X_2 = DP_2, \dots, X_n = DP_2) + dp$
            \EndFor
            
            \State \textbf{return} $\frac{np}{dp}$
        \EndProcedure
    \end{algorithmic}
\end{algorithm}


\begin{algorithm}[htb]
    \caption{Algoritmo para el muestreo directo}\label{alg:cap3:direct-sampling}
    \begin{algorithmic}
        \State \textbf{Global variables:}
        \State $X = \{X_1,\dots,X_n\}$
        \Procedure{direct-sampling}{$V, E, N$} \Comment{$V \subset X$}
            \State $c = 0$
            \For {$i=1$ \textbf{to} $N$}
                \For{$k=1$ \textbf{to} $|X|$}
                    \State $x_k =$ choice $x_j \in X_k$ with probability $P(x_j|parents(X_k))$
                \State \textbf{If} $v_1,\dots,v_{|V|} == e_1,\dots,e_{|e|}$ \textbf{then}  c = c + 1
                \EndFor
            \EndFor
            \State \textbf{return} $c$
        \EndProcedure
    \end{algorithmic}
\end{algorithm}

\begin{algorithm}[htb]
    \caption{Algoritmo para el cálculo de marginales con muestreo directo}\label{alg:cap3:marginal-ds}
    \begin{algorithmic}
        \Procedure{marginal}{$V, E, N$} \Comment{$V \subset X$}
            \State $c =$ \textbf{\textit{DIRECT-SAMPLING}} $(V,E,N)$
            \State \textbf{return} $\frac{c}{N}$
        \EndProcedure
    \end{algorithmic}
\end{algorithm}



A partir de los algoritmos \eqref{alg:cap3:marginal} y \eqref{alg:cap3:condicional}, se observa que, dado que ya no es necesario generar las combinaciones de las variables, la complejidad temporal se vuelve lineal. En el algoritmo \eqref{alg:cap3:marginal}, esta complejidad depende únicamente de los argumentos, mientras que en el algoritmo \eqref{alg:cap3:condicional} depende tanto de los argumentos como de los subconjuntos de $N$ y $D$. No obstante, la complejidad temporal sigue siendo la misma para ambos casos.
