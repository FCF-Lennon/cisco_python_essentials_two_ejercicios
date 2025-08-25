# Sección 4 – El módulo os: interactuando con el sistema operativo

"""
    En esta sección aprenderemos cómo interactuar con el sistema operativo 
    utilizando el módulo incorporado `os` de Python.

    El módulo os nos permite:
    - Obtener información sobre el sistema operativo.
    - Crear y eliminar directorios.
    - Movernos entre carpetas.
    - Ejecutar comandos del sistema.

    Muchas de sus funciones son equivalentes a comandos de consola 
    (tanto en Unix/Linux como en Windows).
"""


# Introducción al módulo os:

"""
    El módulo `os` ofrece funciones que permiten trabajar con archivos, 
    directorios y procesos del sistema.

    Ejemplo de funciones:
    - mkdir → crear un directorio (similar al comando `mkdir` en la terminal).
    - listdir → listar archivos/directorios.
    - chdir → cambiar el directorio actual.
    - getcwd → obtener el directorio actual.
"""


# Obteniendo información sobre el sistema operativo:

import os

# En sistemas Unix:
# print(os.uname())  # Solo funciona en Linux/macOS, no en Windows.

# En Windows (y también en Unix) se recomienda usar:
import platform
print(platform.uname())   # Devuelve información del sistema

print(os.name)  # 'posix' en Linux/macOS, 'nt' en Windows, 'java' en Jython

"""
    - os.uname() → solo en Unix.
    - platform.uname() → multiplataforma, muestra datos del sistema.
    - os.name → distingue entre sistemas operativos:
        'posix' = Unix/Linux/Mac
        'nt'    = Windows
        'java'  = Jython
"""


# Creando directorios en Python:

# Ejemplo de rutas relativas y absolutas:
# os.mkdir("my_first_directory")        # Ruta relativa
# os.mkdir("./my_first_directory")      # Ruta relativa explícita
# os.mkdir("../my_first_directory")     # Directorio superior
# os.mkdir("/python/my_first_directory")  # Ruta absoluta (Unix)

os.mkdir("my_first_directory")   # Crea un directorio en el directorio actual
print(os.listdir())              # Muestra el contenido actual

"""
    Nota:
    - Si ejecutas el código dos veces, obtendrás FileExistsError.
    - listdir() devuelve los archivos y carpetas de la ruta especificada.
"""

# Creación recursiva de directorios:

# Crea toda la estructura de carpetas necesaria:
os.makedirs("my_first_directory/my_second_directory", exist_ok=True)

# Moverse al directorio:
os.chdir("my_first_directory")
print(os.listdir())  # ['my_second_directory']

"""
    makedirs() crea todos los directorios intermedios automáticamente.
    Es similar a `mkdir -p` en Unix o `mkdir` en Windows con rutas completas.
"""

# ¿Dónde estoy ahora?

# Mostrar directorio actual
print(os.getcwd())

# Cambiar y volver a mostrar
os.chdir("my_second_directory")
print(os.getcwd())

"""
    - getcwd() devuelve el directorio de trabajo actual (absoluto).
    - chdir() permite moverse entre directorios.
"""


# Eliminando directorios en Python:

# Eliminar un solo directorio vacío:
os.rmdir("my_second_directory")

# Eliminar directorio con subdirectorios:
os.makedirs("my_first_directory/my_second_directory", exist_ok=True)
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())

"""
    - rmdir() elimina solo directorios vacíos.
    - removedirs() elimina de manera recursiva (si todos están vacíos).
"""


# La función system():

# Ejecutar comandos del sistema operativo:
returned_value = os.system("mkdir test_dir")
print("Código de salida:", returned_value)

"""
    - system() ejecuta comandos de consola desde Python.
    - En Unix devuelve el estado de salida (0 = éxito).
    - En Windows devuelve el valor del shell tras ejecutar el comando.
"""


# RESUMEN DE SECCIÓN:

"""
    1. uname() (Unix) o platform.uname() (multiplataforma) devuelven 
    información del sistema.
    2. os.name permite distinguir el sistema operativo ('posix', 'nt', 'java').
    3. mkdir() crea directorios; makedirs() crea directorios recursivamente.
    4. listdir() devuelve archivos y directorios en una ruta.
    5. chdir() cambia el directorio actual; getcwd() devuelve el directorio actual.
    6. rmdir() elimina directorios vacíos; removedirs() elimina directorios recursivos.
    7. system() ejecuta comandos del sistema desde Python.
"""

