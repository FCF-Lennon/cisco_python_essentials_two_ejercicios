# Exmen Final: Curso de Python Essentials II (Cisco)

# Pregunta 01 - Sabiendo que una función llamada fun() reside en un módulo
# llamado mod, y que fue importada usando la siguiente sentencia: from mod import fun

# Elige la forma correcta de invocar la función fun():

"""
    - fun() / Respuesta
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
    - No más de un bloque except: será ejecutado. / Respuesta
    - Exactamente un bloque except: será ejecutado. 
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
    - a / Respuesta
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


# Pregunta 19 - ¿Cuál es el resultado esperado del siguiente código?

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(A, C))


"""
    Opciones:

    - El código imprimirá False. / Respuesta
    - El código imprimirá True.
    - El código impirmirá 1.
    - El código generará una excepción.
"""


# Pregunta 20 - El flujo o stream sys.stderr normalmente se asocia con:

"""
    Opciones:

    - La pantalla / Respuesta
    - El teclado 
    - La impresora
    - Un dispositivo nulo
""" 


# Pregunta 21 - ¿Cuál es el resultado esperado al ejecutar el siguiente código?

""" 
    class A:
        def __init__(self, v):
            self.__a = v + 1

    a = A(0)
    print(a.__a) 
"""

"""
    Opciones:

    - El código imprimirá 0
    - El código imprimirá 1
    - El código generará una excepción AttributeError / Respuesta
    - El código imprimirá 2
"""


# Pregunta 22 - ¿Cuál es el resultado esperado al ejecutar el siguiente código?

""" 
    class A:
        def __init__(self):
            pass

    a = A(1)
    print(hasattr(a, 'A'))
"""
"""
    Opciones:

    - El código generará una excepción / Respuesta
    - El código imprimirá True
    - El código imprimirá 1
    - El código imprimirá False
"""


# Pregunta 23 - ¿Cuál es el resultado esperado al ejecutar el siguiente código?

class A:
    def a(self):
        print('a')
    
class B:
    def a(self):
        print('b')

class C(B, A):
    def c(self):
        self.a()

o = C()
o.c()


"""
    Opciones:

    - El código imprimirá b / Respuesta
    - El código imprimirá a 
    - El código generará una excepción
    - El código imprimirá c
"""

# Pregunta 24 - ¿Cuál es el resultado esperado al ejecutar el siguiente
# código?

try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))

"""
    Opciones:

    - El código imprimirá 3 / Respuesta
    - El código imprimirá 2
    - El código imprimirá 1
    - El código generará una excepción no controlada.
"""


# Pregunta 25 - ¿Cuál es el resultado esperado al ejecutar el siguiente
# código?

def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in my_fun(2):
    print(x, end='')

"""
    Opciones:

    El código imprimirá +
    El código imprimirá ++++++ / Respuesta
    El código imprimirá +++
    El código imprimirá ++
"""


# Pregunta 26 - ¿Cuál es el resultado esperado al ejecutar el siguiente
# código?

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')


"""
    Opciones:

    - El código imprimirá abc / Respuesta
    - El código imprimirá 210
    - El código imprimirá 012
    - El código imprimirá cba
"""


# Pregunta 27 - ¿Cuál es el resultado esperado al ejecutar el siguiente
# código?

def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())


"""
    Opciones:

    - El código imprimirá *** / Respuesta
    - El código imprimirá *
    - El código imprimirá **
    - El código imprimirá ****
"""


# Pregunta 28 - Si s es un stream abierto en modo lectura, la siguiente
# línea: q = s.read(1)

# leerá:

"""
    Opciones:

    - Una línea del stream
    - Un kilobyte del stream 
    - un buffer del stream
    - un carácter del stream / Respuesta
"""


# Pregunta 29 - Suponiendo que la invocación open() se ha realizado correctamente,
# el siguiente fragmento de código.

""" 
    for x in open('file', 'rt'):
        print(x) 
"""

# será:

"""
    Opciones:

    - Leerá el archivo línea por línea. / Respuesta
    - Leerá todo el archivo en una sola vez.
    - Provocará una excepción.
    - Leerá el archivo carácter por carácter. 
"""


# Pregunta 30 - Si deseas llenar un arreglo de bytes con datos leídos
# de un stream, ¿qué método puedes usar?

"""
    Opciones:

    - El método readbytes()
    - El método readfrom()
    - El método read()
    - El método readinto() / Respuesta
"""


# Pregunta 31 - ¿Cuál de los siguientes comandos usarias para verificar
# la versión de pip? (Selecciona dos respuestas)

"""
    Opciones:

    - pip version
    - pip-version
    - pip --version / Respuesta
    - pip3 --version / Respuesta
"""


# Pregunta 32 - ¿Cuál comando pip usarias para desinstalar un paquete
# previamente instalado?

"""
    Opciones:

    - pip uninstall nombre_del_paquete / Respuesta
    - pip delete nombre_del_paquete
    - pip --remove nombre_del_paquete
    - pip --unistall nombre_del_paquete
"""


# Pregunta 33 - Observa el siguiente código:

"""
    numbers = [0, 2, 7, 9, 10]
    # Inserta la línea de código aquí.
    print(list(foo))
"""

# ¿Qué línea insertarias para que el programa produzca la salida esperada?
# [0, 4, 49, 81, 100]

"""
    Opciones:

    - foo = map(lambda num: num ** 2, numbers) / Respuesta
    - foo = filter(lambda num: num ** 2, numbers)
    - foo = lambda num: num ** 2, numbers
    - foo = lambda num: num * 2, numbers
"""


# Pregunta 34 - Observa el siguiente código:

""" 
    numbers = [i*i for i in range(5)]
    # Inserta la línea de código aquí.
    print(foo) 
"""

# ¿Qué línea insertarias para que el programa produzca la salida esperada?
# Salida: [1, 9]

"""
    Opciones:

    - foo = list(map(lambda x: x // 2, numbers))
    - foo = list(filter(lambda x: x / 2, numbers))
    - foo = list(map(lambda x: x % 2, numbers))
    - foo = list(filter(lambda x: x % 2, numbers)) / Respuesta 
"""


# Pregunta 35 - Observa el código a continuación:

""" 
    import random
    # Inserta las líneas de código aquí.
    print(a, b, c) 
"""

# ¿Qué líneas de código insertarias para que sea posible que el programa
# genere la siguiente salida?: 6 82 0

"""
    Opciones:

    - A:
      a = random.randrange(10, 100, 3)
      b = random.randint(0, 100)
      c = random.choice((0, 100, 3))

    - B: 
      a = random.choice((0, 100, 3))
      b = random.randrange(10, 100, 3)
      c = random.randint(0, 100)

    - C: / Respuesta
      a = random.randint(0, 100)
      b = random.randrange(10, 100, 2)
      c = random.choice((0, 100, 3))

    - D:
      a = random.randint(0, 100)
      b = random.choice((0, 100, 3))
      c = random.randrange(10, 100, 3)

"""


# Pregunta 36 - ¿Cuál es el resultado esperado del siguiente código?

""" 
    import os

    os.mkdir('pictures')
    os.chdir('pictures')

    print(os.getcwd()) 
"""

"""
    Opciones:

    - El código imprimirá el contenido del directorio creado.
    - El código imprimirá la ruta al directorio creado. / Respuesta
    - El código imprimirá el propietario del directorio creado.
    - El código imprimirá el nombre del directorio creado.
"""


# Pregunta 37 - ¿Qué información se puede leer usando la función uname
# proporcionada por el módulo os? (Selecciona dos respuestas)

"""
    Opciones:

    - Última fecha de inicio de sesión.
    - Nombre del sistema operativo. / Respuesta
    - Ruta actual.
    - Identificador de hardware. / Respuesta
"""


# Pregunta 38 - ¿Cuál es el resultado esperado del siguiente código?

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

"""
    Opciones:

    - 11:27:22 / Respuesta
    - 0 days, 11:27:22 
    - 0 days
    - 11 hours, 27 minutes, 22 seconds
"""


# Pregunta 39 - ¿Cuál es el resultado esperado del siguiente código?

from datetime import timedelta

delta = timedelta(weeks=1, days=7, hours=11)
print(delta * 2)

"""
    Opciones:

    - 28 days, 22:00:00 / Respuesta 
    - 7 days, 22:00:00
    - 2 weeks, 14 days, 22 hours
    - El código generará una excepción
"""


# Pregunta 40 - ¿Cuál es el resultado esperado del siguiente código?

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))

"""
    Opciones:

    - Sun Mon Tue Wed Thu Fri Sat / Respuesta
    - Tu
    - Su Mo Tu We Thu Fr Sa
    - Tue
"""

