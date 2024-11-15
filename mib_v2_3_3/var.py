class Var:
    """Clase para el manejo de las variables (establecer y manejar los eventos).
    Atributos:
        name (any): Nombre de la varibale.
        values (set): Conjunto, de enteros, que contiene los valores que representan un evento.
        event (any): Valor que representa un evento.   
        
    Var(any,set) -> Nuevo objeto Var.
    """
    def __init__(self,name,values:set):
        self.name = name
        self.values = values
        self.event = None
    
    def getValues(self) -> list:
        """ Método obtner los valores de la variable para calcular la marginal.

        Return:
            list: lista con los valores de la variable.
        """  
        if self.event:
            return [self.event]
        else:
            return list(self.values)
    
    def getCard(self) -> int:
        if self.event:
            return 1
        else:
            return len(self.values)
    
    def reset(self) -> None:
        self.event = None
    