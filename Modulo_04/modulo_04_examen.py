# Preguntas:

# Pregunta 01 - ¿Qué palabra clave reservada usarías para definir una 
# función anónima?

"""
    Opciones:

    - lambda / Respuesta
    - yield
    - def
    - afun
"""


# Pregunta 02 - Selecciona las sentencias verdaderas. (Selecciona dos
# respuestas)

"""
    Opciones:

    - La función lambda puede evaluar sólo una expresión. / Respuesta
    - La función lambda puede aceptar cualquier número de argumentos. / Respuesta
    - La función lambda puede aceptar un máximo de dos argumentos. 
    - La función lambda puede evaluar multiples expresiones.
"""


# Pregunta 03 - Observa el código a continuación:

"""
    my_list = [1,2,3]
    # Insertar línea de código aquí.
    print(foo)
"""

# ¿Qué fragmento insertarias para que el programa genere el siguiente
# resultado (tupla)?: (1, 4, 27)

"""
    Opciones:

    - foo = list(map(lambda x: x*x, my_list))
    - foo = list(map(lambda x: x**x, my_list))
    - foo = tuple(map(lambda x: x*x, my_list))
    - foo = tuple(map(lambda x: x**x, my_list)) / Respuesta
"""


# Pregunta 04 - Observa el código a continuación:

"""
    my_tuple = (0, 1, 2, 3, 4, 5, 6)
    # Insertar línea de código aquí.
    print(foo)
"""

# ¿Qué fragmento insertarias para que le programa genere el siguiente
# resultado (final)?: [2, 3, 4, 5, 6]

"""
    Opciones:

    - foo = list(filter(lambda x: x==0 and x==1, my_tuple))
    - foo = tuple(filter(lambda x: x>1, my_tuple))
    - foo = tuple(filter(lambda x: x-0 and x-1, my_tuple))
    - foo = list(filter(lambda x: x-0 and x-1, my_tuple)) / Respuesta
"""


# Pregunta 05 - ¿Cuál es el resultado esperado de ejecutar el siguiente 
# código?

def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c

for x in I():
    print(x, end='')


"""
    Opciones:

    - Imprimirá abcdef
    - Imprimirá bdf
    - Imprimirá ace / Respuesta
    - Impirmirá una línea vacía.
"""


# Pregunta 06 - ¿Cuál es el resultado esperado al ejecutar el siguiente
# código?

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x, end='')


"""
    Opciones:

    - Imprimirá +++ 
    - Imprimirá ++
    - Imprimirá +
    - Imprimirá ++++++ / Respuesta
"""

# Pregunta 07 - ¿Cuál es el resultado esperado de ejecutar el siguiente
# código?

def o(p):
    def q():
        return '*' * p
    return q

r = o(1) 
s = o(2) 

print(r() + s())

"""
    - Imprimirá *** / Respuesta
    - Imprimirá **
    - Imprimirá ****
    - Imprimirá *
"""


# Pregunta 08 - ¿Cuáles de los siguientes modos de apertura te permiten
# realizar operaciones de lectura? (selecciona dos respuestas)

"""
    Opciones:

    - r / Respuesta
    - r+ / Respuesta
    - a
    - w
"""


# Pregunta 09 - ¿Cuál es el significado del valor representado por
# errno.EEXIST?

"""
    Opciones:

    - Archivo existente / Respuesta
    - Archivo inexistente
    - Permiso denegado
    - Número de archivo incorrecto
"""


# Pregunta 10 - ¿Cuál es el resultado esperado del siguiente código?

b = bytearray(3)
print(b)

"""
    Opciones:

    - bytearray(b'\x00\x00\x00') / Respuesta
    - 3
    - bytearray(b'3')
    - bytearray(0, 0, 0)
"""


# Pregunta 11 - ¿Cuál es el resultado esperado del siguiente código?

""" 
    import os

    os.mkdir('pictures')
    os.chdir('pictures')
    os.mkdir('thumbnails')
    os.chdir('thumbnails')
    os.mkdir('tmp')
    os.chdir('../')

    print(os.getcwd()) 
"""


"""
    Opciones:

    - Imprimirá la ruta al directorio root
    - Imrpimirá la ruta al directorio pictures / Respuesta
    - Imprimirá la ruta al directorio tmp
    - Imprimirá la ruta al diretorio thumbnails
"""


# Pregunta 12 - ¿Cuál es el resultado esperado del siguiente código?

""" 
    import os

    os.mkdir('thumbnails')
    os.chdir('thumbnails')

    sizes = ['small', 'medium', 'large']

    for size in sizes:
        os.mkdir(size)

    print(os.listdir()) 
"""

"""
    Opciones:

    - []
    - ['large', 'small', 'medium'] / Respuesta
    - ['.', '..', 'large', 'small', 'medium']
    - ['.', 'large', 'small', 'medium']
"""


# Pregunta 13 - ¿Cuál es el resultado esperado del siguiente código?

from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)


"""
    Opciones:

    - 345, 0:00:00
    - 345 days
    - 345 days, 0:00:00 / Respuesta
    - 345 
"""


# Pregunta 14 - ¿Cuál es el resultado esperado del siguiente código?

from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22) # mala practica
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

"""
    Opciones:

    - 19/11/27 11:27:22
    - 19/November/27 11:27:22 / Respuesta
    - 2019/11/27 11:27:22
    - 2019/Nov/27 11:27:22
"""


# Pregunta 15 - ¿Qué programa producirá la siguiente salida?: Mo Tu We Th Fr Sa Su

"""
    Opciones:

    a) import calendar
       print(calendar.weekheader(2)) / Respuesta
    b) import calendar
       print(calendar.weekheader())
    c) import calendar
       print(calendar.weekheader(3))
    d) import calendar
       print(calendar.week)
"""


# Pregunta 16 - ¿Cuál es el resultado esperado del siguiente código?

import calendar

c = calendar.Calendar()
for weekday in c.iterweekdays():
    print(weekday, end=" ")

"""
    Opciones:

    - 0 1 2 3 4 5 6 / Respuesta
    - Su Mo Tu We Th Fr Sa
    - Mo Tu We Th Fr Sa Su
    - 1 2 3 4 5 6
"""

