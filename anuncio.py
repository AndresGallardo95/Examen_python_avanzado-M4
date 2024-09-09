class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self.ancho = max(ancho, 1)
        self.alto = max(alto, 1)
        self._url_archivo = url_archivo  # Cambiamos a privado con _
        self._url_clic = url_clic  # Cambiamos a privado con _
        self.sub_tipo = sub_tipo

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    def mostrar_formatos(self):
        print(f"FORMATO: {self.FORMATO}")
        for subtipo in self.SUB_TIPOS:
            print(f"- {subtipo}")

    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass
