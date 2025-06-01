# ¿Qué es un paquete?

# Un paquete es un conjunto de módulos Python organizados en una carpete, 
# listos para ser usados con solo import.

# PyPI: Python Package Index (la Tienda de Quesos)
"""
PyPI (https://pypi.org/) es el repositorio oficial donde viven más de 300.000 paquetes de Python. 
Se le llama "la Tienda de Quesos" como una broma inspirada en Monty Python (referencia cultural del lenguaje).
Aquí puedes encontrar desde herramientas como requests, pandas, hasta paquetes de videojuegos como pygame.
"""

# Cómo instalar pip

# Verifica si pip ya está instalado:
"""pip --version"""
# Si estás en linux y tienes python 3:
"""pip3 --version"""
# Si no lo tienes, puedes instalarlo en Ubuntu con:
"""
    sudo apt update
    sudo apt install python3-pip
"""
# En windows, normalmente se instala junto con Python, pero debes asegurarte de marcar "Add Python to PATH"
# durante la instalación.

# Dependencias
# Cuando instalas un paquete, este puede depender de otros. A esto se le llama arbol de dependencias. Por 
# ejemplo:

"""
    Tu proyecto
    └── nyse
        └── wallstreet
            ├── bull
            └── bear
"""

# PIP es capaz de resolver automáticamente todas estas dependencias. Por eso, al instalar nyse, 
# también se instalarán wallstreet, bull y bear si no existen ya.

# Cómo usar PIP
# Var ayuda general:
""" pip help """
# Ver paquetes instalados:
""" pip list """
# Mostrar detalles de un paquete:
""" pip show nombre_paquete
    Ejemplo: pip show requests
"""
# Buscar paquetes (descontinuado en versiones recientes, usa PyPI web):
""" pip search nombre_paquete
    # Alternativa: https://pypi.org/search
"""
# Instalar un paquete:
# Instalación global (requiere permisos de administrador)
""" pip install nombre_paquete """
# Instalación solo para tu usuario (sin permisos de admin)
""" pip install --user nombre_paquete """
# Ejemplo:
""" pip install pygame """

# Programa de prueba simple usando pygame:
# Después de instalar pygame, puedes probarlo con el siguiente código:

"""
import pygame

run = True
width = 400
height = 100

pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYUP, pygame.MOUSEBUTTONUP):
            run = False 
"""

# ¿Qué hase este programa?
# Inicializa pygame.
# Crea una ventana de 400x100 pixeles.
# Muestra el texto "Welcome to pygame" centrado.
# Termina cuando presionas una tecla o haces clic.

# Ejemplo completo de flujo con PIP
# Verificar la instalacion de PIP o su Version
""" pip --version """
# Instalar un paquete
""" pip install requests """
# Ver que paquetes estan instalados
""" pip list """
# Mostrar informacion del paquete
""" pip show requests """
# Desinstalar un paquete
""" pip uninstall requests """


# Ejercicios:

# Pregunta 1: ¿De donde proviene el nombre "The Cheese Shop"?

"""
    Respuesta: De un sketch humorístico de la serie *Monty Python's Flying Circus*,
    donde un cliente entra a una tienda de quesos que no tiene quesos.
    El nombre es una broma interna, ya que Python tiene una conexión cultural con Monty Python.
"""

# Pregunta 2: ¿Por qué deberías asegurarte de cuál pip o pip3 es el correcto para ti?

"""
    Respuesta: Cuando Python 2 y Python 3 coexisten en el sistema operativo,
    el comando pip puede estar vinculado a Python 2, mientras que pip3 se asocia a Python 3.
    Es importante usar la versión correspondiente a tu entorno de desarrollo.
"""

# Pregunta 3: ¿Cómo puedes determinar si mi pip funciona con Python 2 o Python 3?

"""
    Respuesta: con pip --version este comando mostrará la versión de pip y también la 
    versión de Python con la que está vinculado.
    
    Ejemplo de salida:
    pip 23.3.1 from /usr/lib/python3.10/site-packages (python 3.10)
"""

# Pregunta 4: Desafortunadamente, no tienes privilegios de administrador.
# ¿Qué debes hacer para instalar un paquete en todo el sistema?

"""
Respuesta: Debería solicitar al administrador del sistema que instale el paquete,
ya que se requieren privilegios de superusuario para instalaciones globales.
"""