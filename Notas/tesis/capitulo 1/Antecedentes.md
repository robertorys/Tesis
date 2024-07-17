
## Antecedentes sobre la inferencia Bayesiana. 

*Por inferencia queremos decir simplemente: razonamiento deductivo siempre que se disponga de suficiente información para permitirlo; razonamiento inductivo o probabilístico cuando (como ocurre casi invariablemente en los problemas reales) no se dispone de toda la información necesaria.* \citep{Jayns2003}

---

En el libro "Bayesian Programming" de \cite{Pierre2013}, se menciona que la lógica es la base matemática del razonamiento y el principio fundamental de la computación. Sin embargo, la lógica no puede utilizarse para modelar fenómenos debido a su limitación a problemas que disponen de información cierta y completa. Como se mencionó anteriormente, los modelos presentan problemas de incompletitud e incertidumbre. Por lo tanto, es necesario contar tanto con un marco matemático alternativo como con un marco computacional alternativo para abordar la incompletitud y la incertidumbre.

Es imprescindible contar de un marco matemático que maneje tanto la información certera como la incierta. La teoría de la probabilidad constituye dicho marco matemático alternativo. Esta teoría proporciona un modelo de razonamiento racional en presencia de incompletitud e incertidumbre. El empleo de la probabilidad como modelo de razonamiento se conoce como enfoque subjetivo o Bayesiano.

 La probabilidad es una extensión de la lógica, tan matemáticamente sensata y simple como la lógica, pero con más poder expresivo que la lógica. El primer concepto que usamos es la noción usual de una \textit{proposición lógica}. Las proposiciones son denotadas por nombres es minúsculas. Se pueden componer proposiciones para obtener nuevas proposiciones utilizando operadores lógicos habituales: $a \land b$, denotando la conjunción de la proposición $a$ y $b$, $a \lor b$ es la disyunción, y $\neg a$, la negación de la proposición $a$.
 
 Para poder lidiar con la incertidumbre, asignamos probabilidades a las proposiciones. Consideremos que, para asignar una probabilidad a una proposición $a$, es necesario tener al menos algún conocimiento previo, resumido en una proposición $\pi$. En consecuencia, la probabilidad de una proposición $a$ está siempre condicionada, al menos por $\pi$. Para cada diferente $\pi$, $P(\cdot | \pi)$ es una aplicación que asigna a cada proposición $a$ un valor real único $P(a|\pi)$ en el intervalo $[0,1]$.

Por supuesto, nos interesa razonar sobre las probabilidades de conjunciones, disyunciones y negaciones de proposiciones, denotadas respectivamente, por $P(a \land b | \pi)$, $P(a \lor b | \pi)$ y $P(\neg a | \pi)$.

También nos interesa la probabilidad de la proposición a condicionada tanto por el conocimiento preliminar $\pi$ como por alguna otra proposición b. Esto denota $P(a | b \land \pi)$.

---
En el libro "Bayesian Programming" de Pierre Bessiere (2013), se menciona que la lógica es la base matemática del razonamiento y el principio fundamental de la computación. Sin embargo, la lógica no puede utilizarse para modelar fenómenos debido a su limitación a problemas que disponen de información certera y completa. Como se mencionó anteriormente, los modelos presentan problemas de incompletitud e incertidumbre. Por lo tanto, es necesario contar tanto con un marco matemático alternativo como con un marco computacional alternativo para abordar la incompletitud y la incertidumbre.

Es imprescindible contar con un marco matemático que maneje tanto la información certera como la incierta. La teoría de la probabilidad constituye dicho marco matemático alternativo. Esta teoría proporciona un modelo de razonamiento racional en presencia de incompletitud e incertidumbre. El empleo de la probabilidad como modelo de razonamiento se conoce como enfoque subjetivo o bayesiano.

La probabilidad es una extensión de la lógica, tan matemáticamente sensata y simple como la lógica, pero con mayor poder expresivo. El primer concepto que utilizamos es la noción usual de una proposición lógica. Las proposiciones se denotan por nombres en minúsculas y se pueden componer para obtener nuevas proposiciones utilizando los operadores lógicos habituales: a∧ba \land ba∧b, denotando la conjunción de las proposiciones aaa y bbb; a∨ba \lor ba∨b, denotando la disyunción; y ¬a\neg a¬a, denotando la negación de la proposición aaa.

Para poder lidiar con la incertidumbre, asignamos probabilidades a las proposiciones. Consideremos que, para asignar una probabilidad a una proposición aaa, es necesario tener al menos algún conocimiento previo, resumido en una proposición π\piπ. En consecuencia, la probabilidad de una proposición aaa está siempre condicionada, al menos por π\piπ. Para cada diferente π\piπ, P(⋅∣π)P(\cdot|\pi)P(⋅∣π) es una función que asigna a cada proposición aaa un valor real único P(a∣π)P(a|\pi)P(a∣π) en el intervalo [0,1][0, 1][0,1].

Por supuesto, nos interesa razonar sobre las probabilidades de conjunciones, disyunciones y negaciones de proposiciones, denotadas respectivamente por P(a∧b∣π)P(a \land b|\pi)P(a∧b∣π), P(a∨b∣π)P(a \lor b|\pi)P(a∨b∣π) y P(¬a∣π)P(\neg a|\pi)P(¬a∣π).

También nos interesa la probabilidad de la proposición aaa condicionada tanto por el conocimiento preliminar π\piπ como por alguna otra proposición bbb. Esto se denota P(a∣b∧π)P(a|b \land \pi)P(a∣b∧π
##  ¿Qué es un Motor de Inferencia Bayesiana (MIB)?
### Redes de Bayes.
[[AIMA#13.1 Representing Knowledge in a uncertain domain]] 
Una red bayesiana es un grafo dirigido en el cual cada nodo es anotado con información de probabilidad cuantitativa. La especificación completa es como sigue:
1. Cada nodo corresponde a una variable aleatoria, que puede ser discreta o continua.
2. Los enlaces dirigidos o flechas conectan pares de nodos. Si hay una flecha desde el nodo *X* al nodo *Y*, se dice que *X* es padre de *Y*. El grafo no tiene ciclos dirigidos y, por lo tanto es un grafo acíclico dirigido, o DAG.
3. Cada nodo $X_i$ tiene información de probabilidad asociada $\theta(X_i|Parents(X_i))$ que cuantifica el efecto de los padres en el nodo utilizando un número finito de parámetros.

La topología de la red (el conjunto de nodos y enlaces) especifica las relaciones de independencia condicional que se mantiene en el Dominion de una manera que se precisara en breve. El significado *intuitivo* de una flecha suele ser que $X$ tiene una *influencia sobre* $Y$, lo que sugiere que las causa deberían ser padres de los efectos. Generalmente es fácil para un experto en un dominio decidir que influencias directas existen en el dominio (de hecho, es mucho más fácil que especificar las probabilidades en sí). Una vez que se haya dispuesto la topología de la red de Beyes, solo necesitamos especificar la información de probabilidad local para cada variable, en la forma de distribución condicional dados sus padres. La distribución conjunta total para todas las variables es definida por la topología y la información de la probabilidad local.
### Reglas de Inferencia Bayesiana.
[[AIMA#13.2 The Semantics of Bayesian Networks]]

Si una red de Bayes es la representación de la distribución conjunta, entonces también puede ser utilizada para responder cualquier consulta, sumando todos los valores de probabilidad conjunta relevantes, cada uno se calcula multiplicando las probabilidades de las distribuciones condicionales locales.

En el caso de las redes de Bayes, es razonable suponer que en la mayoría de los dominios de cada variable aleatoria está directamente influenciada, por máximo, otras $k$, para alguna constante $k$. Si asumimos $n$ variables Booleanas para simplificar, entonces la cantidad de información necesaria para especificar cada tabla de probabilidad condicional será como máximo $2^k$, y la red completa puede ser especificada por $2^k \times n$. En contraste, la distribución conjunta contiene $2^n$. Suponga que tenemos $n = 30$ nodos, cada uno con cinco padres ($k = 5$). Entonces la red Bayesiana requiere 960 registros, pero la distribución conjunta requiere más de un billón. 

La especificación de las tablas de probabilidad condicional para una red completa conectada, en el cual cada variable tiene todos los predecesores como padres, requiere la misma cantidad de información como es especificar la distribución conjunta en forma de tabla. Por esta razón, A menudo omitimos enlaces aunque exista una ligera dependencia, porque la ligera ganancia en precisión no compensa la complejidad adicional en la red. 

---
### Programación Bayesiana.
[[Bayesian programming#12 Bayesian programming formalism]]