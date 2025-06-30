# Excepciones Integradas en Python

"""
    Las excepciones son parte normal del trabajo de un programador.

    Aquí se presentan algunas de las más útiles, junto a:
    - Su nombre
    - Su posición en la jerarquía de excepciones
    - Una descripción breve
    - Un ejemplo funcional
"""


# ArithmeticError
"""
    Ubicación: BaseException ← Exception ← ArithmeticError

    Descripción:
    Excepción abstracta que engloba errores aritméticos como división por cero
    o argumentos matemáticos inválidos.
"""

# No se muestra código específico, pero ZeroDivisionError hereda de aquí.


# AssertionError
"""
Ubicación: BaseException ← Exception ← AssertionError

Descripción:
Excepción concreta que se lanza cuando un assert falla, es decir,
cuando su condición es False, None, 0 o cadena vacía.
"""

# from math import tan, radians

# angle = int(input('Ingresa un ángulo entero en grados: '))
# assert angle % 180 != 90
# print(tan(radians(angle)))


# BaseException
"""
    Ubicación: BaseException

    Descripción:
    La raíz de toda la jerarquía de excepciones en Python.
    Todas las excepciones derivan de esta clase.

    Nota: usar `except:` o `except BaseException:` es prácticamente lo mismo.
"""


# IndexError
"""
    Ubicación: BaseException ← Exception ← LookupError ← IndexError

    Descripción:
    Se lanza cuando se intenta acceder a un índice inexistente en una secuencia.
"""

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Listo\n')


# KeyboardInterrupt
"""
    Ubicación: BaseException ← KeyboardInterrupt

    Descripción:
    Ocurre cuando el usuario interrumpe el programa con Ctrl+C.

    Nota: no deriva de Exception, por eso `except Exception` no lo captura.
"""

# from time import sleep

# seconds = 0
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("¡No hagas eso!")


# LookupError
"""
    Ubicación: BaseException ← Exception ← LookupError

    Descripción:
    Excepción abstracta que representa errores de búsqueda en colecciones
    como listas, diccionarios, tuplas, etc.

    IndexError y KeyError heredan de esta clase.
"""


# MemoryError
"""
    Ubicación: BaseException ← Exception ← MemoryError

    Descripción:
    Se lanza cuando una operación requiere más memoria de la disponible.

    Advertencia: este código puede congelar tu sistema. No lo ejecutes en entornos sensibles.
"""

# string = 'x'
# try:
#     while True:
#         string = string + string
#         print(len(string))
# except MemoryError:
#     print('¡Esto no es gracioso!')


# OverflowError
"""
    Ubicación: BaseException ← Exception ← ArithmeticError ← OverflowError

    Descripción:
    Se lanza cuando una operación numérica genera un valor demasiado grande
    para ser representado correctamente.
"""

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.\n')


# ImportError
"""
    Ubicación: BaseException ← Exception ← ImportError

    Descripción:
    Se lanza cuando una instrucción import falla.

    Nota: StandardError ya no existe en Python 3, así que se ignora esa referencia.
"""

try:
    import math
    import time
    # import abracadabra  # <- módulo inexistente
except:
    print('Una de tus importaciones ha fallado.\n')


# KeyError
"""
    Ubicación: BaseException ← Exception ← LookupError ← KeyError

    Descripción:
    Se lanza cuando se accede a una clave inexistente en un diccionario.
"""

dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)


# Ejerccios:

# Pregunta 1: ¿Cuál de las excepciones se utilizará para proteger al código de ser interrumpido por el uso del teclado?

# Respuesta: KeyboardInterrupt


# Pregunta 2: ¿Cuál es el nombre de la más general de todas las excepciones de Python?

# Respuesta: BaseException

# Pregunta 3: ¿Cuál de las excepciones será generada a través de la siguiente evaluación fallida?

huge_value = 1E250 ** 2

# Respuesta: OverflowError


"""
    Nota:
    Este tipo de error ocurre cuando el número excede el límite que puede representar internamente Python
    con los tipos numéricos estándar.
"""
