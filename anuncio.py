from error import SubTipoInvalidoError

class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self.ancho = max(ancho, 1)  # Validación de ancho mayor a 0
        self.alto = max(alto, 1)  # Validación de alto mayor a 0
        self._url_archivo = url_archivo  # Se utiliza _ para encapsular como atributo privado
        self._url_clic = url_clic  # Se utiliza _ para encapsular como atributo privado
        self._sub_tipo = sub_tipo  # Atributo encapsulado con validación en setter

    # Getters y Setters para url_archivo
    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    # Getters y Setters para url_clic
    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    # Getter y setter para sub_tipo con validación de subtipo permitido
    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"El subtipo '{value}' no es válido para el formato {self.FORMATO}.")
        self._sub_tipo = value

    # Método estático para mostrar formatos y subtipos permitidos
    @staticmethod
    def mostrar_formatos():
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

    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass


# Clase Video que hereda de Anuncio
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion, *args, **kwargs):
        super().__init__(ancho=1, alto=1, *args, **kwargs)
        self.duracion = max(duracion, 5)  # Validación de duración mayor a 0, si no se asigna 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


# Clase Display que hereda de Anuncio
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


# Clase Social que hereda de Anuncio
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
