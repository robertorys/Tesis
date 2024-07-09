
## Antecedentes sobre la inferencia Bayesiana. 

En el libro "Bayesian Programming" de \cite{Pierre2013}, se menciona que la lógica es la base matemática del razonamiento y el principio fundamental de la computación. Sin embargo, la lógica no puede utilizarse para modelar fenómenos debido a su limitación a problemas que disponen de información cierta y completa. Como se mencionó anteriormente, los modelos presentan problemas de incompletitud e incertidumbre. Por lo tanto, es necesario contar tanto con un marco matemático alternativo como con un marco computacional alternativo para abordar la incompletitud y la incertidumbre.

Es imprescindible contar de un marco matemático que maneje tanto la información certera como la incierta. La teoría de la probabilidad constituye dicho marco matemático alternativo. Esta teoría proporciona un modelo de razonamiento racional en presencia de incompletitud e incertidumbre. El empleo de la probabilidad como modelo de razonamiento se conoce como enfoque subjetivo o Bayesiano.

Para modelar el razonamiento, se debe tener en cuanta los conocimientos previos del sujeto  que realiza el razonamiento. Este conocimiento preliminar juega el mismo papel que los axiomas en lógica.  Partir de diferentes conocimientos preliminares puede llevas a diferentes conclusiones. Partir de un conocimiento preliminar erróneo conducirá a conclusiones erróneas incluso con un razonamiento perfectamente correcto. Llegar a conclusiones erróneas siguiendo un razonamiento correcto demuestra que el conocimiento preliminar era erróneo, ofrece la oportunidad de corregirlo y, finalmente, conduce al aprendizaje. La incompletitud es simplemente la brecha irreductible entre el conocimiento preliminar y el fenómeno y la incertidumbre es una consecuencia directa y mensurable de esta imperfección. 

*Por inferencia queremos decir simplemente: razonamiento deductivo siempre que se disponga de suficiente información para permitirlo; razonamiento inductivo o probabilístico cuando (como ocurre casi invariablemente en los problemas reales) no se dispone de toda la información necesaria.* \citep{Jayns2003}
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

### Programación Bayesiana.
[[Bayesian programming#12 Bayesian programming formalism]]