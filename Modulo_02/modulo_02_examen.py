
# Prueba del módulo

# Pregunta 01 - El entrar al bloque try: implica que:

"""
    Opciones:

    - todas las instrucciones de este bloque se ejecuten
    - algunas de las instrucciones de este bloque no se ejecuten / Respuesta
    - ninguna de las instruccuiones de este bloque se ejecuten
    - el bloqué será omitido
"""

# Pregunta 02 - El bloque except: sin nombre:

"""
    Opciones:

    - debe ser el último / Respuesta
    - debe ser el primero
    - no se puede utilizar si se ha utilizado algún bloque con nombre
    - se puede colocar en cualquier lugar
"""

# Pregunta 03 - La excepción base en Python se llama:

"""
    Opciones:

    - TopException
    - BaseException / Respuesta
    - PythonException
    - Exception
"""

# Pregunta 04 - La siguiente sentencia: assert var == 0

"""
    Opciones:

    - no tiene efecto
    - es erronea
    - detendrá el programa cuando var == 0 
    - detendrá el programa cuando var != 0 / Respuesta
"""

# Pregunta 05 - ¿Cuál es el resultado esperado del siguiente código?

try:
    print("5"/0)
except ArithmeticError:
    print("arit")
except ZeroDivisionError:
    print("cero")
except:
    print("algo")

"""
    Opciones:

    - arit
    - algo / Respuesta, lanza (TypeError), que no es capturado por ArithmeticError ni ZeroDivisionError.
    - cero
    - 0
"""

# Pregunta 06 - ¿Cúales de las siguientes son ejemplos de excepciones 
# integradas concretas de Python? (Selecciona dos respuestas)

"""
    Opciones:

    - ImportError / Respuesta
    - AritmeticError
    - IndexError / Respuesta
    - BaseException
"""

# Pregunta 07 - ASCII es:

"""
    Opciones:

    - el nombre de un Módulo Estándar de Python
    - el nombre de una variable predefinida de Python
    - el nombre es un carácter
    - la abreviatura de Amirican Standard Code for Information Interchange / Respuesta
"""

# Pregunta 08 - UTF-8 es:

"""
    Opciones:

    - la novena versión del estándar UTF
    - un sinónimo para la palabra byte
    - el nombre de una versión de Python
    - una forma de codificar puntos de código Unicode / Respuesta
"""

# Pregunta 09 - UNICODE es un estándar:

"""
    Opciones:

    - empleado por programadores en universidades
    - como ASCII, pero mucho más expansivo / Respuesta
    - para codificar números punto flotante
    - honrado por todo el universo
"""

# Pregunta 10 - El siguiente código:

x = '\''
print(len(x))

"""
    Opciones:

    - 20
    - 3
    - 1 / Respuesta
    - 2
"""

# Pregunta 11 - El siguiente código:

print(ord('c') - ord("a")) # 99 - 97

"""
    Opciones:

    - 1
    - 3
    - 2 / Respuesta
    - 0
"""

# Pregunta 12 - El siguiente código:

print(chr(ord('z') - 2)) # 122 - 2 = 120 => x

"""
    Opciones:

    - x / Respuesta 
    - y
    - z
    - a
"""

# Pregunta 13 - El siguiente código:

print(3 * 'abc' + 'xyz')

"""
    Opciones:

    - abcabcxyzxyz
    - abcxyzxyzxyz
    - xyzxyzxyzxyz
    - abcabcabcxyz / Respuesta
"""

# Pregunta 14 - El siguiente código:

print('Mike' > "Mikey")

"""
    Opciones:

    - False / Respuesta
    - 1
    - True
    - 0

    Nota: La comparación de strings se hace carácter por carácter. 
    Como 'Mike' y 'Mikey' coinciden hasta la letra 'e', pero 'Mikey'
    tiene una 'y' adicional, la cadena 'Mike' se considera menor.
"""

# Pregunta 15 - El siguiente código:

print(float("1, 3"))

"""
    Opciones:

    - genera una excepción ValueError / Respuesta
    - imprime 13
    - imprime 1,3
    - imprime 1.3
"""