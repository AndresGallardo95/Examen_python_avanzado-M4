from error import LargoExcedidoError
from anuncio import Video, Display, Social

class Campaña:
    def __init__(self, nombre, anuncios=[]):
        if len(nombre) > 250:
            raise LargoExcedidoError()
        self.nombre = nombre
        self.anuncios = anuncios

    def __str__(self):
        count_video = sum(isinstance(a, Video) for a in self.anuncios)
        count_display = sum(isinstance(a, Display) for a in self.anuncios)
        count_social = sum(isinstance(a, Social) for a in self.anuncios)
        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Anuncios: {count_video} Video, {count_display} Display, {count_social} Social")

    @property
    def anuncios(self):
        return self._anuncios

    @anuncios.setter
    def anuncios(self, value):
        self._anuncios = value
