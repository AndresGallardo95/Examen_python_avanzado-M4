from campaña import Campaña
from anuncio import Video
from error import SubTipoInvalidoError, LargoExcedidoError

def main():
    # Creación de una campaña con 1 anuncio de tipo Video
    video_ad = Video(duracion=10, url_archivo="video.mp4", url_clic="http://video.click", sub_tipo="instream")
    campaña = Campaña(nombre="Campaña de Video", anuncios=[video_ad])

    # Modificar la campaña
    try:
        nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
        campaña.nombre = nuevo_nombre

        nuevo_subtipo = input("Ingrese un nuevo subtipo para el anuncio: ")
        video_ad.sub_tipo = nuevo_subtipo

    except (SubTipoInvalidoError, LargoExcedidoError) as e:
        with open("error.log", "a") as f:
            f.write(str(e) + "\n")

    print(campaña)

if __name__ == "__main__":
    main()
