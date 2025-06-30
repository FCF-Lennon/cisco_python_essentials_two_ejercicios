# Anatomía de las Excepciones en Python

# 1. ¿Qué es una excepción?
"""
    Una excepción en Python es un evento que ocurre durante la ejecución del programa
    y que interrumpe su flujo normal. Cuando algo sale mal (por ejemplo, dividir por cero),
    Python lanza una excepción.
"""

# 2. Jerarquía de excepciones
"""
    Python tiene una jerarquía de excepciones: algunas son generales (más arriba en el árbol)
    y otras más específicas (más abajo). Esto significa que puedes capturar errores
    de forma muy específica o de manera más amplia.
"""

# Ejemplo de jerarquía:
"""
    BaseException
    ↑
    Exception
    ↑
    ArithmeticError
    ↑
    ZeroDivisionError
"""

# Explicación:
"""
    - ZeroDivisionError: se lanza cuando divides por cero.
    - ArithmeticError: agrupa errores aritméticos como ZeroDivisionError, OverflowError, etc.
    - Exception: clase base para la mayoría de excepciones.
    - BaseException: clase raíz de todas las excepciones en Python
    (incluso aquellas que no deberías capturar en general, como SystemExit).
"""

# 3. Capturando excepciones

# Código original:

try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.\n")

# También podrías usar una excepción más general:

try:
    y = 1 / 0
except Exception:
    print("Capturada por Exception.")

try:
    y = 1 / 0
except BaseException:
    print("Capturada por BaseException.")

print("FIN.\n")

# 4. El orden importa

# Ejemplo incorrecto:

try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre cero!")

print("FIN.\n")

# Forma correcta:

try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre cero!")
except ArithmeticError:
    print("¡Problema aritmético!")
print("FIN.\n")

# 5. Capturar múltiples excepciones
"""
    Usa tuplas para capturar múltiples errores de forma compacta.
"""

try:
    x = int("hola")
except (ValueError, TypeError):
    print("¡Ocurrió un error de tipo o valor!")

print("FIN.\n")

# 6. Propagación de excepciones
"""
    Las excepciones pueden ser manejadas dentro o fuera de una función.
"""

# Dentro de la función:
def bad_fun():
    try:
        return 1 / 0
    except ArithmeticError:
        print("¡Problema aritmético!")

bad_fun()
print("FIN.\n")

# Fuera de la función:
def bad_fun_externa():
    return 1 / 0

try:
    bad_fun_externa()
except ArithmeticError:
    print("¿Qué ocurrió? ¡Se generó una excepción!")

print("FIN.\n")

# 7. Lanzar tus propias excepciones

# raise
"""
    Puedes forzar una excepción con raise:
"""

# raise ValueError("Esto es un error de valor personalizado.")

# raise (sin argumentos)
"""
    Úsalo dentro de un except para volver a lanzar la excepción actual.
"""

try:
    x = 1 / 0
except ZeroDivisionError:
    print("¡Lo hice otra vez!")
    # raise  # Descomenta para relanzar el error

# 8. Validación rápida con assert

# Sintaxis:
"""
    assert condición, "mensaje opcional"

    Si la condición es False, se lanza un AssertionError.
"""

# Ejemplo práctico:
# x = float(input("Introduce un número positivo: "))
# assert x >= 0.0
# print("Todo bien.")

# Si ingresas un número negativo, se detendrá el programa con AssertionError.

# Úsalo como herramienta de verificación interna, no como validación para usuarios finales.

# Resumen general

"""
    - Las excepciones se heredan en una jerarquía: de general (BaseException) a concreta (ZeroDivisionError).
    - El orden en los bloques except importa: las excepciones más específicas deben ir primero.
    - Puedes manejar errores dentro o fuera de una función.
    - Usa raise para lanzar excepciones, y raise solo (dentro de un except) para relanzarlas.
    - Usa assert para verificar condiciones críticas que no deberían fallar.
"""

# Ejemplo Final: Todo junto
def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero"
    return a / b

try:
    resultado = dividir(10, 0)
    print(resultado)
except ZeroDivisionError:
    print("¡División entre cero!")
except AssertionError as e:
    print("Error:", e)

print("FIN FINAL.")


"""
    Nota: hacer esto. 
    assert b != 0, "El divisor no puede ser cero".
    
    Es equivalente hacer esto: 
    if not (b != 0):
        raise AssertionError("El divisor no puede ser cero")

    O mas directo:
    if b == 0:
        raise AssertionError("El divisor no puede ser cero")

    Cuándo NO usar assert:
    - No debes usar assert para validar entradas de usuarios finales.
    - Es más apropiado para pruebas internas, supuestos de desarrollo o debugging.
"""


# Ejercicios:

# Pregunta 1: ¿Cuál es la salida esperada del siguiente código?

try:
    print(1/0)
except ZeroDivisionError:
    print("cero")
except ArithmeticError:
    print("arit")
except:
    print("algo")

# Respuesta:

"""
    Imprime: cero.

    Explicación:
    Se lanza una excepción ZeroDivisionError, y como es capturada por el primer bloque except 
    (que es exactamente esa clase), las demás excepciones (más generales) no se ejecutan. 
    Python evalúa los bloques except en orden, y se queda con la **primera coincidencia**.
"""
 

# Pregunta 2: ¿Cuál es la salida esperada del siguiente código?

try:
    print(1/0)
except ArithmeticError:
    print("arit")
except ZeroDivisionError:
    print("cero")
except:
    print("algo")

# Respuesta:

"""
    Imprime: arit.

    Explicación:
    ZeroDivisionError es una subclase de ArithmeticError.
    Como el bloque except para ArithmeticError aparece primero, esa excepción lo captura antes de 
    llegar a ZeroDivisionError, dejando ese bloque **inaccesible**.
    El orden importa.
"""


# Pregunta 3: ¿Cuál es la salida esperada del siguiente código?

def foo(x):
    assert x
    return 1/x

try:
    print(foo(0))
except ZeroDivisionError:
    print("cero")
except:
    print("algo")

# Respuesta:

"""
    Imprime: algo.

    Explicación:
    El assert falla porque x es 0, lo que lanza un AssertionError.
    Esto detiene la ejecución de la función antes de llegar a la división,
    por lo tanto no se lanza ZeroDivisionError.
    Como no hay un except específico para AssertionError, lo captura el except genérico.
"""
