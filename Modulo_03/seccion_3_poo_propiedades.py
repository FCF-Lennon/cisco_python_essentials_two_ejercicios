
# Variables de instancia en Python


"""
    Una variable de instancia es una propiedad que pertenece solo al objeto
    (instancia de clase) y no a la clase misma.

    Cada objeto puede tener un conjunto diferente de propiedades. Estas
    pueden definirse dentro del constructor (__init__) o incluso
    dinámicamente después de creada la instancia.
"""

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val  # Variable de instancia definida en el constructor

    def set_second(self, val):
        self.second = val  # Variable de instancia creada mediante método

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5  # Variable de instancia agregada fuera de la clase

print(example_object_1.__dict__)  # {'first': 1}
print(example_object_2.__dict__)  # {'first': 2, 'second': 3}
print(example_object_3.__dict__)  # {'first': 4, 'third': 5}

"""
    Explicación:
    - example_object_1 solo tiene 'first'.
    - example_object_2 tiene 'first' y 'second'.
    - example_object_3 tiene 'first' y una propiedad externa 'third'.
"""


# Variables de instancia privadas


"""
    Cuando se usan dos guiones bajos (__), Python aplica *name mangling*:
    renombra internamente los atributos agregando el nombre de la clase.
"""

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val):
        self.__second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5  # Esto no se convierte en privado

print(example_object_1.__dict__)  # {'_ExampleClass__first': 1}
print(example_object_2.__dict__)  # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
print(example_object_3.__dict__)  # {'_ExampleClass__first': 4, '__third': 5}

# Accediendo a atributo renombrado
print(example_object_1._ExampleClass__first)  # 1

"""
    Nota: '__third' agregado desde fuera de la clase NO es privado.
    Solo se aplica name mangling dentro de la clase.
"""


# Variables de clase


"""
    Una variable de clase se define dentro de la clase pero fuera de
    los métodos. Se comparte entre todas las instancias.
"""

class ExampleClass:
    counter = 0  # Variable de clase

    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1  # Se incrementa cada vez que se crea un objeto

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
# {'_ExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2.counter)
# {'_ExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3.counter)
# {'_ExampleClass__first': 4} 3

"""
    Todas las instancias acceden al mismo valor de 'counter'.
    No aparece en __dict__ porque no es parte de la instancia.
"""


# Comparación de __dict__ clase vs objeto

class ExampleClass:
    varia = 1  # Variable de clase

print(ExampleClass.__dict__)  # Contiene 'varia' y otros metadatos

instance = ExampleClass()
print(instance.__dict__)  # {}

"""
    La variable 'varia' está en la clase, no en la instancia.
"""

# Comprobando atributos


"""
    Si intentas acceder a un atributo que no existe, obtendrás un AttributeError.
"""

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)
print(example_object.a)  # 1

# print(example_object.b)  # AttributeError si se descomenta

# Forma segura de acceder usando hasattr()
if hasattr(example_object, 'b'):
    print(example_object.b)  # No se ejecuta

"""
    hasattr(objeto, 'nombre_atributo') devuelve True o False según si el atributo existe.
    También funciona con clases.
"""

# Otro ejemplo:

class ExampleClass:
    a = 1  # Variable de clase
    def __init__(self):
        self.b = 2  # Variable de instancia

example_object = ExampleClass()

print(hasattr(example_object, 'b'))     # True
print(hasattr(example_object, 'a'))     # True
print(hasattr(ExampleClass, 'b'))       # False
print(hasattr(ExampleClass, 'a'))       # True

"""
    Resumen:
    - 'b' está en la instancia => True solo en la instancia.
    - 'a' está en la clase => accesible desde instancia y clase.
"""


# Cuestionario


# Pregunta 01 - ¿Cuáles de las propiedades de la clase Python son variables 
# de instancia y cuáles son variables de clase? ¿Cuáles de ellas son privadas?

class Python:
    population = 1          
    victims = 0             

    def __init__(self):
        self.length_ft = 3              
        self.__venomous = False        

# Respuesta:

"""
    Variables de clase: population, victims
    Variables de instancia: length_ft, __venomous
    Variables privadas: __venomous (por usar doble guion bajo dentro de la clase)
"""

# =============================

# Pregunta 02 - Vas a negar la propiedad __venomous del objeto version_2, 
# ignorando el hecho de que la propiedad es privada. ¿Cómo vas a hacer esto?

version_2 = Python()

# Respuesta:

"""
    Podemos acceder a la variable privada usando name mangling:
    version_2._Python__venomous = not version_2._Python__venomous
"""

version_2._Python__venomous = not version_2._Python__venomous
print("Valor de venomous:", version_2._Python__venomous)

# =============================

# Pregunta 03 - Escribe una expresión que compruebe si el objeto version_2 contiene 
# una propiedad de instancia denominada constrictor.

# Respuesta:

print("¿Tiene 'constrictor'?:", hasattr(version_2, "constrictor"))  # Imprime: False
