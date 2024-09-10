class Error(Exception):
    """
    Clase base para excepciones personalizadas.
    """
    pass

class LargoExcedidoError(Error):
    """
    Excepción lanzada cuando el nombre de una campaña excede los 250 caracteres permitidos.
    
    Atributos:
        message (str): Mensaje de error que se muestra cuando se lanza la excepción.
    """
    def __init__(self, message="El largo del nombre excede los 250 caracteres permitidos."):
        self.message = message
        super().__init__(self.message)

class SubTipoInvalidoError(Error):
    """
    Excepción lanzada cuando se ingresa un subtipo no válido para un anuncio.
    
    Atributos:
        message (str): Mensaje de error que se muestra cuando se lanza la excepción.
    """
    def __init__(self, message="El subtipo ingresado no es válido."):
        self.message = message
        super().__init__(self.message)
