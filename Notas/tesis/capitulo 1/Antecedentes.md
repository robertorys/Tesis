
##  Redes de Bayes.
[[AIMA#13.1 Representing Knowledge in a uncertain domain]] 
Una red bayesiana es un grafo dirigido en el cual cada nodo es anotado con información de probabilidad cuantitativa. La especificación completa es como sigue:
1. Cada nodo corresponde a una variable aleatoria, que puede ser discreta o continua.
2. Los enlaces dirigidos o flechas conectan pares de nodos. Si hay una flecha desde el nodo *X* al nodo *Y*, se dice que *X* es padre de *Y*. El grafo no tiene ciclos dirigidos y, por lo tanto es un grafo acíclico dirigido, o DAG.
3. Cada nodo $X_i$ tiene información de probabilidad asociada $\theta(X_i|Parents(X_i))$ que cuantifica el efecto de los padres en el nodo utilizando un número finito de parámetros.

La topología de la red (el conjunto de nodos y enlaces) especifica las relaciones de independencia condicional que se mantiene en el Dominion de una manera que se precisara en breve. El significado *intuitivo* de una flecha suele ser que $X$ tiene una *influencia sobre* $Y$, lo que sugiere que las causa deberían ser padres de los efectos. Generalmente es fácil para un experto en un dominio decidir que influencias directas existen en el dominio (de hecho, es mucho más fácil que especificar las probabilidades en sí). Una vez que se haya dispuesto la topología de la red de Beyes, solo necesitamos especificar la información de probabilidad local para cada variable, en la forma de distribución condicional dados sus padres. La distribución conjunta total para todas las variables es definida por la topología y la información de la probabilidad local.
## Reglas de Inferencia Bayesiana.
[[AIMA#13.2 The Semantics of Bayesian Networks]]

## Antecedentes sobre la inferencia Bayesiana. 

##  ¿Qué es un Motor de Inferencia Bayesiana (MIB)?

## Programación Bayesiana.
