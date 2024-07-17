## Descripción
### Variables
atributos:
values: set
Omega: set
event: any

métodos:
setEvent(any): None
getValues(): list
clear(): None

### Distrib
atributois:
var: Var
dirJson: str = None
table: dict = None

métodos:
P() -> float

### CondDistrib
atributois:
vasr: set
indep: set
dirJson: str = None
table: dict = None

métodos:
P() -> float

### JointDistrib
atributois:
vasr: set
table: dict

métodos:
setTable(dict) -> None
## Problemas
### Problema 3

Supongamos que una compañía sabe que la contratación profesional de un candidato se efectúa luego de una entrevista, que se lleva a cabo en función de las calificaciones reportadas en el certificado del candidato y si éste tiene experiencia laboral o no. Generalmente, sólo se consideran los candidatos con calificaciones sobresalientes o regulares, y la entrevista arroja típicamente tres tipos de apreciación. 

La compañía ha recolectado datos históricos de los últimos 5 años sobre la evaluación de 500 candidatos y sabe que la proporción de candidatos con calificaciones regulares es del 30\%, mientras que los candidatos con experiencia laboral representan el 60\%. En la mejor condición, con calificaciones sobresalientes y experiencia laboral, los candidatos obtienen la más alta apreciación en la entrevista en un 80\%, y la peor apreciación en un 2\% de los casos. Estos porcentajes cambian respectivamente a 30\% y 10\% cuando las calificaciones no son las mejores, pero sí hay experiencia, y ambas son del 30\% con calificaciones sobresalientes pero sin experiencia. En el peor caso, con calificaciones regulares y sin experiencia, los candidatos obtienen la mejor apreciación en la entrevista en un 10\% y la peor en un 70\%. Por último, se sabe que la tasa de candidatos rechazados es de un 10\% cuando obtienen una apreciación favorable, un 60\% cuando obtienen una apreciación regular, y un 99\% cuando obtienen una apreciación desfavorable en la entrevista.

La compañía ha elaborado el siguiente modelo de contratación:
Variables:  
C := {0, 1}, representa las calificaciones; 0 si son calificaciones regulares, 1 otro caso.  
E := {0, 1}, representa la experiencia; 0 si cuentan con experiencia y  
1 si no cuentan con experiencia.  
N := {0, 1, 2}, representa la apreciación de la entrevista,  
O := {0, 1}, representa la contratación; 1 si son contratados y 0 si no.  

Modelo probabiístico:  
P (CENO) = P (C)P (E)P (N |CE)P (N |O)

Las preguntas propuestas son las siguientes:
\begin{enumerate}
    \item ¿Cuál es su tasa de contratación?
    \item ¿Cuantos candidatos ha contratado la compañía en los últimos 5 años?
    \item ¿Cuál es la tasa de apreciaciones favorables en la compañía?
    \item ¿Cuál es la tasa de apreciaciones regulares dado que se contrata a alguien?
    \item ¿Cuál es la tasa de apreciaciones regulares dado que se contrata a alguien?
    \item ¿Cuantos de los candidatos contratados obtuvieron una apreciación regular?
    \item ¿Cómo se distribuye la contratación de candidatos en función de sus calificaciones?
    \item ¿Cómo se distribuye la contratación de candidatos en función de su experiencia?
    \item ¿Cuál es la probabilidad de que alguien con experiencia laboral tenga calificaciones sobresalientes?
    \item ¿Cuál es la distribución conjunta del personal contratado y la apreciación de la entrevista?
\end{enumerate}
