from error import LargoExcedidoError
from anuncio import Video, Display, Social

class Campaña:
    """
    Clase que representa una campaña publicitaria.
    
    Atributos:
        nombre (str): Nombre de la campaña, debe tener un máximo de 250 caracteres.
        anuncios (list): Lista de anuncios que forman parte de la campaña.
    """
    def __init__(self, nombre, anuncios_data=[]):
        """
        Inicializa una campaña con un nombre y una lista de anuncios.
        
        Parámetros:
            nombre (str): Nombre de la campaña.
            anuncios_data (list): Lista de datos para crear anuncios.
        
        Excepciones:
            LargoExcedidoError: Si el nombre excede los 250 caracteres.
        """
        if len(nombre) > 250:
            raise LargoExcedidoError()
        self.nombre = nombre
        self.anuncios = self._crear_anuncios(anuncios_data)  # Usamos composición para crear anuncios

    def _crear_anuncios(self, anuncios_data):
        """
        Método privado que crea anuncios basados en la lista de datos recibida.
        
        Parámetros:
            anuncios_data (list): Lista de datos de anuncios.
        
        Retorna:
            list: Lista de instancias de anuncios (Video, Display, Social).
        """
        anuncios = []
        for anuncio in anuncios_data:
            if anuncio['tipo'] == 'video':
                anuncios.append(Video(**anuncio['params']))
            elif anuncio['tipo'] == 'display':
                anuncios.append(Display(**anuncio['params']))
            elif anuncio['tipo'] == 'social':
                anuncios.append(Social(**anuncio['params']))
        return anuncios

    def __str__(self):
        """
        Retorna una representación en cadena de la campaña, mostrando el nombre
        y la cantidad de anuncios de cada tipo.
        """
        count_video = sum(isinstance(a, Video) for a in self.anuncios)
        count_display = sum(isinstance(a, Display) for a in self.anuncios)
        count_social = sum(isinstance(a, Social) for a in self.anuncios)
        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Anuncios: {count_video} Video, {count_display} Display, {count_social} Social")
