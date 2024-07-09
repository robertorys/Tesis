La modelación de fenómenos no solo ha ayudado en entender como funciona un fenómeno, sino que también en predecir, medir, optimizar, simular, imitar, optimizar y controlar un fenómeno. Con el actual crecimiento de las tecnologías es posible traducir modelos de grandes dimensiones  en programas para poder hacer cálculos necesarios para generar una respuesta. Sin embargo, cualquier modelo y programa de un fenómeno presenta el problema de la incompletitud; en otras palabras, el modelo de un fenómeno real es incompleto. ''La incertidumbre es la consecuencia directa e inevitable de la incompletitu'' \citep{Pierre2013}. Esto sucede por el hecho de que en el momento de generar un modelo, existen variables ocultas en el mundo que no son consideradas, ya sea por falta de conocimientos o el alcance que permite la tecnología, esto hace que el modelo y el fenómeno tengan un comportamiento similar, pero nunca igual. 

En este estudio se busca mejorar la implementación de un programa  que se basa en uso de la probabilidad como un marco matemático que maneje tanto la información certera como la incierta, y como modelo de razonamiento,  el uso de la probabilidad como modelo del razonamiento se conoce como enfoque subjetivo o Bayesiano. Este programa esta basado principalmente en la descripción de programas Bayesionios en \citep{Pierre2013}. 

Este programa llamemos lo por ahora motor de inferencia Bayesiano, cuenta con una herramienta que ayuda con la generación descripciones para modelos probabilísticos y reducir el espacio necesario para guardar las probabilidades, pero solo con esta herramienta no es suficiente para poder llevarlo a problemas del mundo real. La importancia de este motor de inferencia es que tiene un amplio alcance en su uso. Ya sea para describir el modelo del entorno y en calculo de las predicciones de un agente artificial, o de manera general para predecir el comportamiento de fenómenos. Por esta razón es importante generar un motor de inferencia Bayesiano el cual pueda tratar con problemas más grandes. 


---

En el libro "Bayesian Programming" de \cite{Pierre2013}, se menciona que cuando un modelo es traducido a un programa y se ejecuta, puede utilizarse para comprender, medir, simular, imitar, optimizar, predecir y controlar un fenómeno. Sin embargo, cualquier modelo y programa de un fenómeno presenta el problema de la incompletitud; en otras palabras, el modelo de un fenómeno real es incompleto. ''La incertidumbre es la consecuencia directa e inevitable de la incompletitu'' \citep{Pierre2013}. Esto ocurre debido a la existencia de variables ocultas que no son consideradas, lo que resulta en que el modelo y el fenómeno tengan comportamientos similares, pero nunca idénticos. Por lo tanto, un modelo no puede proporcionar observaciones futuras exactas ni predicciones precisas del fenómeno modelado.

En este mismo libro, se menciona que la lógica es la base matemática del razonamiento y el principio fundamental de la computación. Sin embargo, la lógica no puede utilizarse para modelar fenómenos debido a su limitación a problemas que disponen de información cierta y completa. Como se mencionó anteriormente, los modelos presentan problemas de incompletitud e incertidumbre. Por lo tanto, es necesario contar tanto con un marco matemático alternativo como con un marco computacional alternativo para abordar la incompletitud y la incertidumbre.

Es imprescindible contar de un marco matemático que maneje tanto la información certera como la incierta. La teoría de la probabilidad constituye dicho marco matemático alternativo. Esta teoría proporciona un modelo de razonamiento racional en presencia de incompletitud e incertidumbre. El empleo de la probabilidad como modelo de razonamiento se conoce como enfoque subjetivo o Bayesiano.



---

La consideración de la probabilidad como modelo del razonamiento se denomina enfoque *subjetivista* o *Bayesiano*. Se opone al enfoque objetivista, que considera la probabilidad como modelo del mundo. Esta oposición no es sólo una controversia epistemológica; tiene muchas consecuencias fundamentales y prácticas.  

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
