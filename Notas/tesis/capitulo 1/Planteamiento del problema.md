La anterior propuesta del motor de inferencia, presentar dos problemas principales, además de carecer de una descripción para variables continuas. Para realizar inferencia bayesiana exacta, presenta un problema con la memoria que require el código. En la antes descripción propuesta para la de inferencia exacta es la una generación de tuplas para la representación de todas las combinaciones de los eventos de las las variables especificadas. Sea $X = \{X_1, X_2, \dots, X_n\}$, donde a cada $X_i$ es el conjunto de los valores de una variable, la llave se generaría de la siguiente forma:

Dada la siguiente clase para las variables:
```python
Class Var:
	def __init__(self, name:str, values = None):
		self.name = name
		if values is not None:
			slef.values =list(values)
			self.card = len(values)
		else:
			self.values = None
			self.card = 0
			
	def set_values(self, values:list):
		self.values = values
		self.card = len(values)
		
	def print_var(self):
		return (self.name, self.card, self.values)
```
La generación de llaves se hacer de la siguiente manera:
```python
def genera_llaves(variables:list):
	llaves = []
	nombre = []
	valores = []
	
	for v in variables:
		nombre.append(v.name)
		valores.append(v.values)
	
	for element in product(*valores):
		x = chain(*(nombre,element))
		llaves.append(tuple(x))
	
	return llaves
```
Donde *chain* devuelve un objeto de cadena, cuya cadena contiene elementos del primer iterable hasta que se agote, luego elementos del siguiente iterable, hasta que se agoten todos los iterables.

Dada los anteriores algoritmos se deduce la complejidad espacial de la siguiente manera:

$$f_e(Y) = \prod_{y_i \in Y} CARD(y_i)$$
donde $Y \subseteq X$.

 Sea $\lambda = max\{CARD(y_i \in Y)\}$ y $n = CARD(Y)$, entonces
$$ \prod_{y_i \in Y} CARD(y_i) \leq  n^{\lambda}$$
por lo tanto 
$$O(f_e(X)) = n^{\lambda}$$

El primer problema que presenta es que, dada la anterior descripción, la memoria requerida para la inferencia crece de manera exponencial. Donde incluso, en problemas con puras variables boleanas, la memoria requerida para estas llaves es demasiado costo.

El segundo problema es que con las llaves descritas de la anterior forma es necesario de algoritmos complejos para poder emparejar el valor de una variable a las funciones de distribución de la descomposición de la distribución conjunta.

---
Para realizar inferencia Bayesiana exacta, presenta el problema en el que se necesita consultar el producto cartesiano de los valores de multiples variables
En este trabajo, se busca implementar un motor de inferencia Bayesina que  