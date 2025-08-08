
# Archivos:
# Flujos de archivos, procesamiento y diagnóstico


"""
    En esta sección aprenderemos:
    - Qué es un flujo (stream) y cómo acceder a archivos en Python.
    - Diferencias entre sistemas operativos al manejar rutas.
    - Modos de apertura de archivos y su manejo.
    - Cómo diagnosticar problemas con flujos.
"""


# Accediendo a archivos desde Python:

"""
    Los archivos almacenan datos de forma persistente (discos duros, SSD, 
    red, etc.).
    Son esenciales para manejar grandes cantidades de datos, ya que leerlos 
    desde el teclado es impráctico en volúmenes grandes.

    En Python, el acceso a un archivo se hace a través de un flujo (stream) 
    que se abre con `open()` y se cierra con `close()`.
"""


# Nombres de archivos:

"""
    Diferencias clave entre Windows y Unix/Linux:
    
    - Separadores: `\` en Windows, `/` en Unix/Linux.
    - Sensibilidad a mayúsculas: Unix/Linux distingue, Windows no.
    - En Windows, la barra invertida `\` es carácter de escape en cadenas,
      por lo que se debe escribir `\\` o usar `/`.

    Ejemplos:
"""
name_unix = "/dir/file"
name_windows = "\\dir\\file"
name_cross = "c:/dir/file"  # Funciona en Windows y Unix/Linux


# Flujos de archivos (Streams):

"""
    Un flujo es un canal abstracto entre el programa y el archivo.
    Operaciones básicas:
    
    - Lectura: datos del archivo → memoria.
    - Escritura: datos de memoria → archivo.

    Modos de apertura:
    
    - Lectura: solo leer.
    - Escritura: solo escribir.
    - Actualizar: leer y escribir.
"""


# Manejo de archivos:

"""
    En Python, `open()` devuelve un objeto de clase adecuada según el tipo
    de archivo y el modo. Para cerrarlo, se usa `close()`.

    Tipos de flujos:
    
    - Texto: caracteres y líneas (`TextIOBase`).
    - Binario: bytes (`BufferedIOBase`).

    Fin de línea:
    
    - Unix/Linux: \n
    - Windows: \r\n
    
    Python maneja esta diferencia automáticamente en modo texto.
"""


# Abriendo flujos con open():

"""
    Sintaxis:
        stream = open(file, mode='r', encoding=None)

    Parámetros:
    
    - file: nombre o ruta del archivo.
    - mode: 'r', 'w', 'a', 'r+', 'w+', 'x' (+ opcional 'b' para binario).
    - encoding: codificación (UTF-8 recomendado para texto).

    Ejemplo:
"""

try:
    stream = open("archivo.txt", "rt", encoding="utf-8")
    # Procesar el archivo aquí...
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


# Modos de texto y binario:

"""
    - Modo texto: por defecto ('t'), interpreta saltos de línea.
    - Modo binario: ('b'), no interpreta saltos de línea ni hace conversiones.
"""


# Ejemplo de apertura con try-except:

"""
    Cuidado al escribir rutas en Windows, usar barras dobles `\\` o prefijo `r""`.
"""

try:
    stream = open(r"C:\Users\User\Desktop\file.txt", "rt")
    # Procesamiento aquí...
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


# Flujos pre-abiertos:

import sys

"""
    Python abre automáticamente:
    
    - sys.stdin  → entrada estándar (teclado)
    - sys.stdout → salida estándar (pantalla)
    - sys.stderr → salida de errores (pantalla)

    Ejemplo:
"""
# print("Hola", file=sys.stdout)
# print("Error crítico", file=sys.stderr)


# Cerrando flujos:

"""
    Siempre cerrar archivos para liberar recursos:
        stream.close()

    Precaución: Si hay datos en buffer sin escribir, podrían perderse si no se cierra.
"""


# Diagnóstico de errores:

import errno
import os

try:
    # open("no_existe.txt", "rt")  # ← Genera FileNotFoundError
    pass
except IOError as exc:
    print("Código de error:", exc.errno)
    print("Descripción:", os.strerror(exc.errno))

"""
    Códigos comunes:

    - errno.EACCES  → Permiso denegado
    - errno.ENOENT  → Archivo o directorio no existe
    - errno.EMFILE  → Demasiados archivos abiertos
"""


# Resumen:

"""
    1. Abrir un archivo crea un flujo, cerrarlo libera recursos.
    2. Modos: lectura ('r'), escritura ('w'), actualización ('r+'), 
       adjuntar ('a'), exclusivo ('x').
    3. Flujos: texto (maneja líneas) o binario (maneja bytes).
    4. Flujos pre-abiertos: sys.stdin, sys.stdout, sys.stderr.
    5. Manejar errores con try-except y diagnosticar con errno y os.strerror().
"""

# Preguntas:

# Pregunta 01 - ¿Cómo codificas el valor del argumento mode de una función open() si 
# vas a crear un nuevo archivo de texto para llenarlo con solo un artículo?
# Respuesta: open(filename, mode="wt")  # w = escritura, t = texto

# Pregunta 02 - ¿Cuál es el significado del valor representado por errno.EACCES?
# Respuesta: Permiso denegado: no se permite acceder al archivo o a su contenido.

# Pregunta 03 - ¿Cuál es el resultado esperado del siguiente código, 
# suponiendo que el archivo llamado file no existe?

import errno
 
try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("ausente")
    else:
        print("desconocido")

# Respuesta: imprimirá 'ausente'
