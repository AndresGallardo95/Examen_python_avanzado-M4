from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    """
    Clase base abstracta que representa un anuncio genérico.
    
    Atributos:
        ancho (int): Ancho del anuncio.
        alto (int): Alto del anuncio.
        _url_archivo (str): URL del archivo del anuncio.
        _url_clic (str): URL de clic del anuncio.
        _sub_tipo (str): Subtipo de anuncio, validado por clase derivada.
    """
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self.ancho = max(ancho, 1)  # Validación de ancho mayor a 0
        self.alto = max(alto, 1)  # Validación de alto mayor a 0
        self._url_archivo = url_archivo  # Encapsulamos para usar getters y setters
        self._url_clic = url_clic  # Encapsulamos para usar getters y setters
        self._sub_tipo = sub_tipo  # Validación de subtipo a nivel de clase derivada

    @abstractmethod
    def comprimir_anuncio(self):
        """
        Método abstracto para comprimir un anuncio.
        Debe ser implementado en las clases derivadas.
        """
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        """
        Método abstracto para redimensionar un anuncio.
        Debe ser implementado en las clases derivadas.
        """
        pass

    @property
    def url_archivo(self):
        """Obtiene el URL del archivo del anuncio."""
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        """Asigna un nuevo URL al archivo del anuncio."""
        self._url_archivo = value

    @property
    def url_clic(self):
        """Obtiene el URL de clic del anuncio."""
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        """Asigna un nuevo URL de clic al anuncio."""
        self._url_clic = value

    @property
    def sub_tipo(self):
        """Obtiene el subtipo del anuncio."""
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        """
        Asigna un subtipo al anuncio, lanzando una excepción si no es válido.
        
        Excepciones:
            SubTipoInvalidoError: Si el subtipo ingresado no está permitido.
        """
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"El subtipo '{value}' no es válido para el formato {self.FORMATO}.")
        self._sub_tipo = value

    @staticmethod
    def mostrar_formatos():
        """
        Muestra los formatos disponibles y sus subtipos permitidos.
        Este método utiliza colaboración entre las clases Video, Display y Social.
        """
        formatos = [
            {"formato": Video.FORMATO, "subtipos": Video.SUB_TIPOS},
            {"formato": Display.FORMATO, "subtipos": Display.SUB_TIPOS},
            {"formato": Social.FORMATO, "subtipos": Social.SUB_TIPOS}
        ]
        for i, formato in enumerate(formatos, start=1):
            print(f"FORMATO {i}:")
            print("==========")
            for subtipo in formato["subtipos"]:
                print(f"- {subtipo}")
            print()

# Clase Video que hereda de Anuncio
class Video(Anuncio):
    """
    Clase que representa un anuncio de tipo Video.
    """
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion, *args, **kwargs):
        super().__init__(ancho=1, alto=1, *args, **kwargs)
        self.duracion = max(duracion, 5)  # Si la duración es <= 0, se asigna 5

    def comprimir_anuncio(self):
        """Imprime un mensaje indicando que la compresión no está implementada."""
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Imprime un mensaje indicando que el recorte no está implementado."""
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

# Clase Display que hereda de Anuncio
class Display(Anuncio):
    """
    Clase que representa un anuncio de tipo Display.
    """
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        """Imprime un mensaje indicando que la compresión no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Imprime un mensaje indicando que el redimensionamiento no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

# Clase Social que hereda de Anuncio
class Social(Anuncio):
    """
    Clase que representa un anuncio de tipo Social.
    """
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        """Imprime un mensaje indicando que la compresión no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Imprime un mensaje indicando que el redimensionamiento no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
