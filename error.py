class Error(Exception):
    """Clase base para excepciones."""
    pass

class LargoExcedidoError(Error):
    """Excepción lanzada cuando el nombre excede los 250 caracteres."""
    def __init__(self, message="El largo del nombre excede los 250 caracteres permitidos."):
        self.message = message
        super().__init__(self.message)

class SubTipoInvalidoError(Error):
    """Excepción lanzada cuando se ingresa un subtipo no válido."""
    def __init__(self, message="El subtipo ingresado no es válido."):
        self.message = message
        super().__init__(self.message)
