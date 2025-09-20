# Exmen Final: Curso de Python Essentials II (Cisco)

# Pregunta 01 - Sabiendo que una función llamada fun() reside en un módulo
# llamado mod, y que fue importada usando la siguiente sentencia: from mod import fun

# Elige la forma correcta de invocar la función fun():

"""
    - fun() / Respuesata
    - mod:fun()
    - mod.fun()
    - mod::fun()
"""


# Pregunta 02 - ¿Qué resultado aparecerá después de ejecutar el siguiente
# fragmento de código?

import math
print(dir(math))

"""
    Opciones:

    - Una cadena que contiene el nombre completo del módulo.
    - Una lista de todas las entidades que residen dentro del módulo math. / Respuesta
    - El número de entidades que residen dentro del módulo math.
    - Un mensaje de error.
"""


# Pregunta 03 - El código bytecode compilado de Python se almacena en archivos con la extensión:

""" 
    Opciones:

    - pyb 
    - pyc / Respuesta
    - py
    - pc
"""


# Pregunta 04 - Suponiendo que los siguientes tres archivos: a.py, b.py y c.py
# residen en el mismo directorio, ¿cuál será la salida producida después
# de ejecutar el archivo c.py?

"""
    # archivo a.py
    print("a", end="")

    # archivo b.py
    import a
    print("b", end="")

    # archivo c.py
    print("c", end="")
    import a
    import b
"""

# Opciones:

"""
    - cba
    - bc
    - bac
    - cab / Respuesta
"""


# Pregunta 05 - ¿Cuál será la salida del siguiente código, ubicado en
# el archivo p.py?

print(__name__)


"""
    Opciones:

    - main
    - p.py
    - __main__ / Respuesta
    - __p.py__
"""


# Pregunta 06 - La siguiente sentencia: from a.b import c

# provoca la importación de:

"""
    - La entidad c del módulo a del paquete b.
    - La entidad b del módulo a del paquete c.
    - La entidad a del módulo b del paquete c.
    - La entidad c del módulo b del paquete a. / Respuesta
"""


# Pregunta 07 - Si hay más de un bloque except: después de un try, podemos
# decir que:

"""
    Opciones:
    
    - Uno o más bloque except: serán ejecutados.
    - Ninguno de los bloques except: será ejecutado.
    - No más de un bloque except: será ejecutado. 
    - Exactamente un bloque except: será ejecutado. / Respuesta
"""


# Pregunta 08 - ¿Cuál es el resultado esperado del siguiente fragmento de código?

try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")

"""
    Opciones:

    - b
    - Un mensaje de error.
    - a / Reespuesta
    - 1
"""


# Pregunta 09 - La siguiente línea de código: for line in open("file.txt", 'rt'):

"""
    Opciones:

    - Es inválida porque open devuelve un objeto no iterable. 
    - Pudiera ser válida si line es una lista.
    - Es inválida porque open devuelve nada.
    - Es válida porque open devuelve un objeto iterable. / Respuesta
"""


# Pregunta 10 - ¿Cuál es el resultado esperado del siguiente fragmento de
# código?

""" 
    try:
        raise Exception
    except:
        print("c")
    except BaseException:
        print("a")
    except Exception:
        print("b") 
"""

"""
    Opciones:

    - El código provocará un error de sintaxis. / Respuesta
    - 1
    - b
    - a
"""


# Pregunta 11 - La siguiente sentencia: assert var != 0

"""
    Opciones:

    - Detendrá el programa cuando var sea distinto de 0. 
    - Es errónea.
    - No tiene efecto.
    - Detendrá el programa cuando var == 0. / Respuesta
"""


# Pregunta 12 - El siguiente código: 

x = "\\\\"
print(len(x))

"""
    Opciones:

    - Imprimirá 1.
    - Causará un error.
    - Imprimirá 2. / Respuesta
    - Imprimirá 3.
"""


# Pregunta 13 - El siguiente código:

"""
    x = "\\\"
    print(len(x))
"""

# Opciones:

"""
    - Imprimirá 3.
    - Causará un error. / Respuesta
    - Imprimirá 1.
    - Imprimirá 2.
"""


# Pregunta 14 - El siguiente código:

print(chr(ord('p') + 2))

"""
    Opciones:

    - Imprimirá s. 
    - Imprimirá r. / Respuesta
    - Imprimirá q.
    - Imprimirá t.
"""


# Pregunta 15 - El siguiente código:

print(float("1.3"))

"""
    Opciones:

    - Imprimirá 13
    - Imprimirá 1.3 / Respuesta
    - Imprimirá 1,3
    - Generará una excepción. 
"""


# Pregunta 16 - Si el constructor de la clase se declara de la siguiente
# manera:

class Class:
    def __init__(self, val=0):
        pass

# ¿Cuál de las asignaciones es inválida?

"""
    Opciones:

    - object = Class(1, 2) / Respuesta 
    - object = Class(None)
    - object = Class(1)
    - object = Class()
"""


# Pregunta 17 - ¿Cuál es el resultado esperado del siguiente código?

class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v
    

a = A()
b = a
b.set()
print(a.v)


"""
    Opciones:

    - 3 / Respuesta
    - 1
    - 2
    - 0
"""


# Pregunta 18 - ¿Cuál es el resultado esperado del siguiente código?

class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'a'))

"""
    Opciones:

    - 1
    - True 
    - False / Respuesta
    - 0
"""