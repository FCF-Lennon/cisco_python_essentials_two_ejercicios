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


# Laboratirio - El módulo os

"""
    No hace falta decir que los sistemas operativos te permiten buscar archivos
    y directorios. Mientras estubiabas esta parte del curso, se aprendió sobre
    las funcinoes del módulo os, que tienen todo lo que se necesita para escribir 
    un programa que buscará directorios en una ubicación determinada.
"""

# Para facilitar tu tarea, hemos preparado una estructura de directorio de 
# prueba para tí:

"""
    tree
    │
    ├── c
    │   └── other_courses
    │       ├── cpp
    │       └── python
    │
    ├── cpp
    │   └── other_courses
    │       ├── c
    │       └── python
    │
    └── python
        └── other_courses
            ├── c
            └── cpp
"""

# Tu programa debe cumplir con los siguientes requisitos:

"""
    1. Escribe una función o método llamado find que tome dos argumentos
       llamasdos path y dir. El argumento path debe aceptar una ruta relativa
       o absoluta a un directorio donde debe comenzar la búsqueda, mientras que
       el argumento dir debe ser el nombre de un directorio en el que deseas
       encontrar la ruta dada. Tu programa debería mostrar las rutas absolutas
       si encuentra un directorio con el nombre dado.
    2. La búsqueda en el directorio debe realizarse de forma resursiva. Esto
       significa que la búsqueda también debe incluir todos los subdirectorios
       en la ruta dada.

   

    Salida 
"""

# Entrada de muestra: path"./tree", dir="python"
# Salida de muestra: 

"""
    .../tree/python
    .../tree/cpp/other_courses/python
    .../tree/c/other_courses/python
"""

# Desarrollo:

import os
import errno

BASE_PATH = "./Modulo_04/tree"

# Nodos principales
languages = ["c", "cpp", "python"]

# Reglas: cada lenguaje tiene "other_courses" con los otros dos
for lang in languages:
    other_courses = [l for l in languages if l != lang]  
    for oc in other_courses:
        path = os.path.join(BASE_PATH, lang, "other_courses", oc)
        os.makedirs(path, exist_ok=True)

# Una forma de hacerlo:

"""
    def find (ruta, directorio):
        for root, dirs, _ in os.walk(ruta):
            if directorio in dirs:
                print(os.path.abspath(os.path.join(root, directorio)))
"""

# Otra forma:

import os
import errno

class DirectorySearcher:
    def find(self, path, dir):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"La ruta especificada no existe: {path}")
            if not os.path.isdir(path):
                raise NotADirectoryError(f"La ruta especificada no es un directorio: {path}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return False
        except NotADirectoryError as e:
            print(f"Error: {e}")
            return False
        except OSError as e:
            print(f"Error: {errno.errorcode.get(e.errno, 'UNKNOWN')}\nDescripción: {e.strerror}\nRuta: {path}")
            return False

        found = False
        try:
            for entry in os.listdir(path):
                full_path = os.path.join(path, entry)
                if entry == dir and os.path.isdir(full_path):
                    print(full_path)
                    found = True
                elif os.path.isdir(full_path):
                    if self.find(full_path, dir):
                        found = True
        except OSError as e:
            print(f"Error al listar el directorio: {path}\n{e}")
            return False

        return found

ruta = "./Modulo_04/tree"
directorio = "pyth"  # ejemplo de error de escritura

searcher = DirectorySearcher()
if not searcher.find(ruta, directorio):
    print(f"No se encontró el directorio '{directorio}' en la ruta '{ruta}'")



# Questionario:

# Pregunta 01 - ¿Cuál es el resultado del siguiente fragmento si se 
# ejecuta en Unix?

import os
print(os.name)

# Respuesta: Imprimirá 'posix', que es el identificador 
# de Unix/Linux/Mac. En cambio, para Windows sería 'nt'.


# Pregunta 02 - ¿Cuál es el resultado del siguiente fragmento de código?

import os

os.mkdir("hello")
print(os.listdir())

# Respuesta: Imprimirá una lista con los nombres de los archivos 
# y directorios en el directorio actual, incluyendo "hello".

