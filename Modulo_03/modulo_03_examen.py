# Preguntas:

# Pregunta 01 - Una estructura de datos descrita como LIFO es en realidad:

"""
    Opciones:

    - una pila / Respuesta
    - un arból
    - una lista
    - un montón
"""


# Pregunta 02 - Si el constructor de la clase se declara de la siguiente manera, 
# ¿cuál de las asignaciones es válida?

class Class:
    def __init__(self):
        pass

"""
    Opciones:

    - object = Class() / Respuesta
    - object = Class(self)
    - object = Class(object)
    - object = Class
"""


# Pregunta 03 - Si hay una superclase llamada A y una subclase llamada B, 
# ¿Cuál de las invocaciones presentadas deberia poner en lugar del comentario?



class A:
    def __init__(self):
        self.a = 1
    
class B(A):
    def __init__(self):
        # Colocar la línea seleccionada aquí.
        self.b = 2

"""
    Opciones:

    - A.__init__(self) / Respuesta
    - __init__()
    - A.__init__()
    - A.__init__(1)
"""


# Pregunta 04 - ¿Cuál será el efecto de ejecutar el siguiente código?

class A: 
    def __init__(self, v):
        self.v = v + 1

""" a = A(0)
print(a.__a) """

"""
    Opciones: 

    - 0
    - El código generará una excepción AttributeError / Respuesta
    - 2
    - 1
"""

# Pregunta 05 - ¿Cuál será la salida del siguiente código?

class A:
    def __init__(self, v = 1):
        self.v = v
    
    def set(self, v):
        self.v = v
        return v

a = A()
print(a.set(a.v + 1))

"""
    Opciones:

    - 0
    - 1
    - 2 / Respuesta
    - 3
"""

# Pregunta 06 - ¿Cuál será la salida del siguiente código?

class A:
    X = 0
    def __init__(self, v = 0):
        self.Y = v
        A.X += v

a = A() # Y = 0, X = 0
b = A(1) # Y = 1, X = 1
c = A(2) # Y = 2, X = 3

print(c.X)

"""
    Opciones:

    - 2
    - 1
    - 0
    - 3 / Respuesta
"""

# Pregunta 07 - ¿Cuál será la salida del siguiente código?

class A:
    A = 1

print(hasattr(A, 'A'))

"""
    Opciones:

    - True / Respuesta
    - False
    - 1
    - 0
"""

 # Pregunta 08 - ¿Cuál será el resultado al ejecutar el siguiente código?

class A:
    def __init__(self):
        pass

""" a = A(1)
print(hasattr(a, 'A')) """

"""
    Opciones:

    - generá una excepción / Respuesta
    - False
    - True
    - 1
"""

# Pregunta 09 - ¿Cuál será el resultado de ejecutar el siguiente código?

class A:
    def __str__(self):
        return 'a'

class B(A):
    def __str__(self):
        return 'b'
    
class C(B):
    pass

o = C()
print(o)

"""
    Opciones:

    - imprimirá: c
    - imprimirá: a
    - imprimirá: b / Respuesta
    - generará una excepción
"""

# Pregunta 10 - ¿Cuál será el resultado de ejecutar el siguiente código?

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C, A))

"""
    Opciones:

    - imprimirá True / Respuesta
    - imprimirá False
    - generará una excepción
    - imprimirá 1
"""


# Pregunta 11 - ¿Cuál será el resultado de ejecutar el siguiente código?

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

    - generará una excepción 
    - imprimirá b / Respuesta
    - imprimirá c 
    - imprimirá a
"""

# Pregunta 12 - ¿Cuál será el resultado de ejecutar el siguiente código?

class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'
    
class C(A, B):
    pass

o = C()
print(o)

"""
    Opciones:

    - imprimirá c
    - generará una excepción
    - imprimirá a / Respuesta
    - imprimirá b
"""


# Pregunta 13 - ¿Cuál será el resultado de ejecutar el siguiente código?

class A:
    v = 2

class B:
    v = 1

class C(B):
    pass

o = C()
print(o.v)

"""
    Opciones:

    - generará una excepción
    - imprimirá 2
    - imprimirá 1 / Respuesta
    - imprimirá una línea vacía
"""

# Pregunta 14 - ¿Cuál será el resultado de ejecutar el siguiente código?

def f(x):
    try:
        x = x / x
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')


f(1)
f(0)

"""
    Opciones:

    - imprimirá acac
    - generará una excepción no controlada
    - imprimirá bcbc
    - imprimirá bcac / Respuesta
"""


# Pregunta 15 - ¿Cuál será el resultado de ejecutar el siguiente código?

try: 
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))

"""
    Opciones:

    - imprimirá 1
    - imprimirá 2
    - imprimirá 3 / Respuesta
    - generará una excepción no controlada
"""


# Pregunta 16 - ¿Cuál será el resultado de ejecutar el siguiente código?

class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)


try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)


"""
    Opciones:

    - generará una excepción no controlada
    - imprimirá una línea vacía
    - imrpimirá ex / Respuesta 
    - imprimirá exex
"""

"""
    Justificación:

    En el constructor de Ex, se llama al constructor de Exception con msg + msg (o sea exex), 
    pero luego se sobreescriben los argumentos con self.args = (msg,).
    
    Como print(e) en una excepción usa __str__ que depende de self.args, y self.args contiene 
    'ex', se imprime solo ex.
"""

# Pregunta 17 - ¿Cuál será el resultado de ejecutar el siguiente código?

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
    print(x,end='')

"""
    Opciones:

    - generará una excepción no controlada
    - imprimirá abc / Respuesta pero con dudas
    - imprimirá 0
    - generará una excepción controlada
"""

