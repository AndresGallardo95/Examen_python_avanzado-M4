# Proyecto de Programación Orientada a Objetos en Python

Este proyecto implementa una serie de clases orientadas a la creación y gestión de campañas publicitarias. El código está diseñado siguiendo los principios de la **Programación Orientada a Objetos (POO)** y cumple con los siguientes objetivos:

1. Crear diferentes tipos de anuncios (Video, Display, Social) dentro de una campaña publicitaria.
2. Gestionar los atributos y comportamientos específicos de cada tipo de anuncio, como la compresión y redimensionamiento.
3. Validar los datos ingresados para asegurar la integridad de la información.
4. Manejar excepciones y registrar errores en un archivo de logs (`error.log`).

El proyecto está estructurado en varios módulos, cada uno con su propia responsabilidad.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- **`anuncio.py`**: Define la clase base abstracta `Anuncio` y las clases derivadas `Video`, `Display` y `Social`.
- **`campaña.py`**: Implementa la clase `Campaña`, que contiene los anuncios y gestiona la composición de estos.
- **`error.py`**: Contiene las excepciones personalizadas que se lanzan en condiciones específicas.
- **`demo.py`**: Script principal que simula la creación de una campaña, permite modificar sus atributos y maneja excepciones.

### Archivos:

📁 proyecto │ ├── anuncio.py ├── campaña.py ├── error.py └── demo.py

## Instalación y Requisitos

### Requisitos previos

Este proyecto requiere Python 3.6 o superior. Asegúrate de tenerlo instalado en tu sistema antes de ejecutar el código.

### Instalación

1. Clona el repositorio del proyecto en tu máquina local:
    ```bash
    git clone [https://github.com/tuusuario/proyecto-publicidad.git](https://github.com/AndresGallardo95/Examen_python_avanzado-M4.git)
    ```


3. No se necesitan dependencias adicionales, ya que todo el código utiliza bibliotecas estándar de Python.


## Uso

1. Ejecuta el archivo `demo.py` para crear una campaña publicitaria y modificar sus atributos.
   
   ```bash
   python demo.py

2.El programa te solicitará que ingreses un nuevo nombre para la campaña y un nuevo subtipo para el anuncio de tipo Video.

3.Si ocurre alguna excepción, como un nombre demasiado largo o un subtipo no válido, el error se registrará en el archivo error.log.
