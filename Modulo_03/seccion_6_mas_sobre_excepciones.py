
# Sección 6 – Más sobre excepciones en Python:


"""
    En esta sección se exploran las excepciones desde la perspectiva de la
    programación orientada a objetos, ampliando el uso de try-except y mostrando
    cómo las excepciones son clases que pueden personalizarse.
"""


# Más acerca de excepciones:


def safe_divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return result

print(safe_divide(1, 2))
print(safe_divide(1, 0))

# Explicación: el bloque `else` se ejecuta solo si no hubo excepción.
# En cambio, si hay error, solo se ejecuta `except`.

# finally siempre se ejecuta:

def safe_divide_finally(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("División fallida")
        result = None
    else:
        print("Todo salió bien")
    finally:
        print("Es momento de decir adiós")
    return result

print(safe_divide_finally(1, 2))
print(safe_divide_finally(1, 0))


# Las excepciones son clases:


try:
    int("¡Hola!")
except ValueError as e:
    print(e)

# Explicación: el objeto `e` contiene la información de la excepción,
# y al imprimirlo se usa su método __str__(), mostrando el mensaje de error.


# Jerarquía de clases de excepción:


def print_exception_tree(cls, nest=0):
    print("    " * nest + cls.__name__)
    for subclass in cls.__subclasses__():
        print_exception_tree(subclass, nest + 1)

# print_exception_tree(BaseException)
# Comentado para evitar salida extensa automática.
# Explicación: muestra el árbol de herencia de las excepciones en Python.


# Anatomía detallada de las excepciones:

def print_args(e):
    print(e)
    print(e.args)

try:
    raise Exception
except Exception as e:
    print_args(e)

try:
    raise Exception("mi excepción")
except Exception as e:
    print_args(e)

try:
    raise Exception("mi", "excepción")
except Exception as e:
    print_args(e)

# Explicación: `args` es una tupla que almacena los parámetros pasados al constructor.


# Cómo crear tu propia excepción:

# Excepción personalizada derivada de ZeroDivisionError

class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(x):
    if x == 0:
        raise MyZeroDivisionError("Mi división entre cero")
    if x == 1:
        raise ZeroDivisionError("División entre cero original")
    return 10 / x

for i in [2, 0, 1]:
    try:
        print(do_the_division(i))
    except MyZeroDivisionError:
        print("Mi división entre cero")
    except ZeroDivisionError:
        print("División entre cero")


# Jerarquía personalizada de excepciones (Ejemplo: Pizza):

class PizzaError(Exception):
    def __init__(self, pizza='desconocida', message=''):
        super().__init__(message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='desconocida', cheese='>100', message=''):
        super().__init__(pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no existe tal pizza en el menú")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "demasiado queso")
    print("¡Pizza lista!")

ordenes = [('calzone', 0), ('margherita', 110), ('mafia', 20)]

for pz, ch in ordenes:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ":", tmce.cheese)
    except PizzaError as pe:
        print(pe, ":", pe.pizza)


# RESUMEN DE SECCIÓN:

"""
    1. El bloque else: de un try se ejecuta si no hubo ninguna excepción.
    2. El bloque finally: se ejecuta siempre, ocurra o no una excepción.
    3. except ... as ...: permite capturar el objeto de la excepción.
    4. Las excepciones son clases y se pueden extender con atributos propios.
"""

try:
    assert __name__ == "__main__"
except:
    print("fallido", end=' ')
else:
    print("éxito", end=' ')
finally:
    print("terminado")

# Output esperado: éxito terminado
# assert pasa correctamente si se ejecuta como script principal.


# Cuestionario:

# Pregunta 01 - ¿Cuál es el resultado esperado del siguiente código?

import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("ok")


# Respuesta: Imprime 3.0 y ok


# Pregunta 02 - ¿Cuál es el resultado esperado del siguiente código?

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("ok")
finally:
    print("fin")


# Respuesta: Imprime inf y fin


# Pregunta 03 - ¿Cuál es el resultado esperado del siguiente código?

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)


try:
    raise NewValueError("Adventencia enemiga", "Alerta roja", "Alta disponibilidad")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')


# Respuesta: Imprime Adventencia enemiga! Alerta roja! Alta disponibilidad!

"""
    Aunque sobrescribas __init__ sin llamar a super().__init__(),
    Python automáticamente guarda los argumentos en args de la excepción,
    Por eso, el for arg in nve.args: imprime esos valores. versión +3.11
"""
