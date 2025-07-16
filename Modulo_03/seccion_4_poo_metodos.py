# Métodos a detalle

"""
    Un método es una función definida dentro de una clase. Todos los métodos deben tener 
    al menos un parámetro, y por convención, el primero se llama `self`, que representa 
    la instancia del objeto que invoca el método.
"""

# Ejemplo básico de método con parámetro self
class Classy:
    def method(self, par):
        print("método:", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

# Output:
# método: 1
# método: 2
# método: 3
# `self` se pasa automáticamente por Python y permite acceder a atributos y otros métodos del objeto.

# Accediendo a atributos dentro del método:
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3
obj.method()

# Output:
# 2 3
# `self` permite acceder tanto a atributos de clase como a los del propio objeto.

# Invocar métodos desde dentro de la clase usando self:
class Classy:
    def other(self):
        print("otro")

    def method(self):
        print("método")
        self.other()

obj = Classy()
obj.method()

# Output:
# método
# otro

# Constructor __init__
"""
    El método especial __init__ es el constructor de la clase. Se ejecuta automáticamente 
    cuando se crea una instancia.
    No puede retornar valores explícitamente.
"""

class Classy:
    def __init__(self):
        print("objeto")

obj = Classy()

# Output:
# objeto

# Constructor con argumento predeterminado:
class Classy:
    def __init__(self, value=None):
        print("objeto")
        print(value)

obj = Classy()
obj2 = Classy("Hola")

# Output:
# objeto
# None
# objeto
# Hola

# Métodos parcialmente ocultos (name mangling):
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("oculto")

obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("fallido")

obj._Classy__hidden()

# Output:
# visible
# fallido
# oculto

# Los métodos que comienzan con doble guión bajo están sujetos a "name mangling" y no 
# pueden ser accedidos directamente.

# Atributos internos de clases y objetos

# __dict__ contiene los atributos de instancia en forma de diccionario:
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()
print(obj.__dict__)
print(Classy.__dict__)

# Output (ejemplo aproximado):
# {'var': 2}
# {'__module__': '__main__', 'varia': 1, '__init__': <function...>, ...}

# __name__ solo existe en clases, no en instancias:
print(Classy.__name__)
# print(obj.__name__)  # Esto provocará un error

# Output:
# Classy

# __module__ contiene el nombre del módulo donde se definió la clase
print(Classy.__module__)

# Output:
# __main__

# __bases__ muestra las superclases directas:
class SuperOne: pass
class SuperTwo: pass
class Sub(SuperOne, SuperTwo): pass

def printBases(cls):
    print('(', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(object)
printBases(SuperOne)
printBases(Sub)

# Output:
# (object )
# (object )
# (SuperOne SuperTwo )

# Reflexión e introspección:
"""
    Python permite examinar y modificar objetos en tiempo de ejecución.
    Esto se conoce como introspección (examinar) y reflexión (modificar).
"""

# Investigando Clases:

class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__:
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

# Output:
# {'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
# {'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}
# La función incrementa en 1 los atributos enteros cuyo nombre comienza con 'i'.


# Preguntas:

# Pregunta 1 - La declaración de la clase Snake se muestra a continuación. Enriquece 
# la clase con un método llamado increment(), el cual incrementa en 1 la propiedad victims.

"""
    class Snake:
        def __init__(self):
            self.victims = 0
"""
    
# Respusta:

class Snake:
        def __init__(self):
            self.victims = 0
        def increment(self):
            self.victims += 1

# El método increment() permite aumentar en 1 el número de víctimas de la serpiente.


# Pregunta 2 - Redefine el constructor de la clase Snake para que tenga un parámetro que 
# inicialice el campo victims con un valor pasado al objeto durante la construcción.

# Respuesta:

class Snake:
    def __init__(self, cantidad_victimas):
        self.victims = cantidad_victimas


# Pregunta 3 - ¿Puedes predecir el resultado del siguiente código?

class Snake:
    pass
 
 
class Python(Snake):
    pass
 
# Respuesta: 

print(Python.__name__, 'es una', Snake.__name__) # Imprime: "Python es una Snake"
print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__) # Imprime: "Snake puede ser una Python"

# Explicación:

"""
    - Python.__name__ da el nombre de la clase "Python".
    - Python.__bases__ devuelve una tupla con las clases base de Python, 
      en este caso (Snake,).
    - Snake.__name__ da el nombre de la clase base.
    Por eso se imprime que "Python es una Snake", y que "Snake puede ser una Python" — 
    esta última línea invierte los roles gramaticalmente para enfatizar la relación de 
    herencia.
"""
