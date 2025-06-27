# Errores, fallas y otras plagas

"""
    "Si algo puede salir mal, saldrá mal." – Ley de Murphy

    Cuando escribes código, estás haciendo un contrato con la incertidumbre.
    Mira este simple ejemplo:
"""

# import math
# y = math.sqrt(x)

"""
    ¿Cuáles son los dos problemas aquí?

    1. x viene de un input(), y podrías escribir "u" en vez de un número.
    2. x podría ser negativo, y math.sqrt() no está diseñado para números negativos.

    Y entonces, boom:
"""

# ValueError: could not convert string to float: 'u'
# ValueError: math domain error

"""
    Tu código se detuvo. Y no es porque Python sea malo, es porque no le dijiste qué 
    hacer cuando todo va mal.
"""


# Excepciones

"""
    Cuando algo se rompe, Python lanza una excepción. Como un grito de ayuda:
"""

# No puedo dividir por cero!" → ZeroDivisionError
# No entiendo esa cadena de texto como número!" → ValueError
# No hay nada en la posición 0 de esta lista vacía!" → IndexError

"""
    ¿Qué hace Python?

    - Detiene tu programa.
    - Crea un objeto de tipo excepción.
    - Espera que tú (el programador responsable) lo manejes.

    Y así nace el bloque try-except. Es como decir:

    "Inténtalo. Pero si todo se va al diablo, tengo un plan B."
"""

# Ejemplo 1 – División entre cero:
value = 10
value /= 0  # ZeroDivisionError: division by zero

# Ejemplo 2 – Acceso fuera del rango de una lista:
my_list = []
x = my_list[0]  # IndexError: list index out of range


# Manejando Excepciones como un profesional

# Método tedioso (no recomendado):
"""
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("Esta operación no puede ser realizada.")
"""

# Esto funciona, pero se vuelve ilegible con muchos casos. En Python preferimos:

# Método idiomático (Pythonic):

"""
    try:
        print(first_number / second_number)
    except ZeroDivisionError:
        print("Esta operación no puede ser realizada.")
"""
# ¡Y fin! Tu programa continúa como si nada hubiera pasado.


# Estructura básica de manejo de excepciones
"""
try:
    # código que podría fallar
except TipoDeExcepcion:
    # manejo del error
"""

# Si quieres cubrir múltiples errores, puedes usar múltiples except:
try:
    # código peligroso
    pass
except ValueError:
    print("Debes ingresar un valor entero.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except:
    print("Oh cielos, algo salió mal…")

# Atención:
"""
    - Solo uno de los bloques except se ejecuta.
    - El except genérico (sin nombre) debe ir al final.
    - No puede haber más de un bloque except sin nombre.
    - Y no puedes tener except si no hay try.
"""

# Ejemplo completo de flujo:
try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except:
    print("Oh cielos, algo salió mal…")
print("FIN.")

# Salidas posibles:
"""
    - 5 → 0.2, FIN.
    - 0 → No puedes dividir entre cero. FIN.
    - "Hola" → Debes ingresar un valor entero. FIN.
    - Ctrl+C → Oh cielos, algo salió mal… FIN.
"""

# Resumen:

"""
    - Las excepciones evitan que tu programa muera al primer error.
    - try-except permite continuar la ejecución de forma controlada.
    - Puedes tener múltiples bloques except, cada uno para una excepción distinta.
    - El bloque except sin nombre debe ser el último y actúa como una red de seguridad.

    ¡Manejar errores correctamente es señal de un programador maduro!

    Recuerda: Python no está diseñado para que tus programas nunca fallen.
    Está diseñado para que sepas cómo manejar los errores cuando lo hagan.
"""


# Ejercicio

# Pregunta 01 - ¿Cuál es el resultado esperado del siguiente código?

try:
    print("Vamos a intentar esto.")
    print("#"[2])
    print("¡Tuvimos éxito!")
except:
    print("Hemos fallado.")

print("Hemos terminado.")

# Respuesta:

"""
    Salida esperada:
    1. Vamos a intentar esto.
    2. Hemos fallado.
    3.Hemos terminado.

    Explicación:

    El índice 2 está fuera del rango del string "#", que solo tiene un carácter.
    Eso genera un IndexError, que se captura por el bloque except.
    Por lo tanto, no se imprime "¡Tuvimos éxito!".
"""

# Pregunta 02 - ¿Cuál es el resultado esperado del siguiente código?

"""
    try:
        print("alpha"[1/0])
    except ZeroDivisionError:
        print("cero")
    except IndexingError:
        print("índice")
    except:
        print("algo")
"""

# Respuesta:

"""
    Salida esperada:
    cero

    Explicación:
    
    La expresión 1/0 lanza un ZeroDivisionError *antes* de intentar indexar el string.
    Por lo tanto, se entra directamente al bloque `except ZeroDivisionError`.
    Nota: `IndexingError` no existe en Python; el error real por índices fuera de rango 
    es `IndexError`.
"""

