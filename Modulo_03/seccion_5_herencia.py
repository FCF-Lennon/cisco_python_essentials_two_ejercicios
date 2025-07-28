
# Fundamentos de la POO: Herencia


"""
    La herencia permite crear nuevas clases basadas en clases existentes,
    heredando atributos y métodos, y extendiendo o modificando su comportamiento.
"""

# __str__() personalizado para mejorar la impresión de objetos

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return f"{self.name} en {self.galaxy}"

star = Star("Sol", "Vía Láctea")
print(star)  # Output: Sol en Vía Láctea

# __str__ devuelve una representación legible del objeto.


# Herencia simple de dos niveles:

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

# Las relaciones entre clases se pueden verificar con issubclass()


# Verificando relaciones con issubclass():

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    row = ""
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        row += str(issubclass(cls1, cls2)) + "\t"
    print(row)

# Cada clase es subclase de sí misma.
# La relación es transitiva: TrackedVehicle es subclase de Vehicle.


# Verificando instancias con isinstance():

vehicle = Vehicle()
land_vehicle = LandVehicle()
tracked_vehicle = TrackedVehicle()

for obj in [vehicle, land_vehicle, tracked_vehicle]:
    row = ""
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        row += str(isinstance(obj, cls)) + "\t"
    print(row)

# Un objeto es instancia de su clase y de todas sus superclases.


# El operador 'is':

class Example:
    def __init__(self, val):
        self.val = val

object_1 = Example(1)
object_2 = Example(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)  # False
print(object_2 is object_3)  # False
print(object_1 is object_3)  # True

print(object_1.val, object_2.val, object_3.val)  # 2 2 2

string_1 = "Python"
string_2 = "".join(["Py", "thon"])

print(string_1 == string_2)  # True
print(string_1 is string_2)  # False

# 'is' verifica si dos variables apuntan al mismo objeto en memoria.


# Cómo Python encuentra propiedades y métodos:

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Mi nombre es {self.name}."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Andy")
print(obj)  # Mi nombre es Andy.

# El método __str__ fue heredado desde la superclase.


# Variables de clase:

class Super:
    supVar = 2

class Sub(Super):
    subVar = 1

obj = Sub()
print(obj.supVar)  # 2
print(obj.subVar)  # 1


# Variables de instancia:

class Super:
    def __init__(self):
        self.supVar = 12

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 11

obj = Sub()
print(obj.supVar)  # 12
print(obj.subVar)  # 11


# Herencia de tres niveles:

class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    var = 300
    def fun(self):
        return 301

obj = Level3()
print(obj.var, obj.fun())  # 300 301


# Herencia múltiple y orden de búsqueda izquierda a derecha:

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())  # L LL RR Left


# Si cambiamos el orden:

class Sub(Right, Left):
    pass

obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())  # R LL RR Right


# Construyendo jerarquía y polimorfismo:

class One:
    def do_it(self):
        print("do_it de One")
    def do_anything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it de Two")

one = One()
two = Two()
one.do_anything()  # do_it de One
two.do_anything()  # do_it de Two

# La subclase redefine el comportamiento de la superclase (polimorfismo).


# Composición en lugar de herencia:

class Tracks:
    def control_track(self, left, stop):
        print("pistas:", left, stop)

class Wheels:
    def turn_front_wheels(self, left, stop):
        print("ruedas:", left, stop)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.control_track(left, not left) \
            if hasattr(self.controller, "control_track") \
            else self.controller.turn_front_wheels(left, not left)

vehicle1 = Vehicle(Wheels())
vehicle1.turn(True)
vehicle1.turn(False)

vehicle2 = Vehicle(Tracks())
vehicle2.turn(True)
vehicle2.turn(False)


# Herencia múltiple vs simple:

"""
    Aunque Python permite herencia múltiple, se recomienda evitarla salvo que sea 
    estrictamente necesario.

    La composición suele ser preferible para mantener claridad y simplicidad.
"""


# Orden de Resolución de Métodos (MRO) "Importante":

class Top:
    def m(self):
        print("superior")

class Middle(Top):
    def m(self):
        print("Medio")

class Bottom(Middle, Top):
    def m(self):
        print("abajo")

obj = Bottom()
obj.m()  # abajo
super(Middle, obj).m()  # Medio
super(Top, obj).m()  # superior

# Si definimos: class Bottom(Top, Middle): → TypeError: MRO inconsistente


# Problema del diamante:

class A:
    def m(self):
        print("A")

class B(A):
    def m(self):
        print("B")

class C(A):
    def m(self):
        print("C")

class D(B, C):
    pass

d = D()
d.m()  # B → sigue orden MRO de izquierda a derecha

# MRO: D → B → C → A


# Cuestionario sección:

# Ejercicio:

# Supongamos que el siguiente fragmento de código se ha ejecutado con 
# éxito:

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: ¡Guau!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, Corderito!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, Señor Intruso!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann") 



# Ahora responde las preguntas 1-4.

# Pregunta 01 - ¿Cuál es el resultado esperado del siguiente código?

""" 
    print(rocky) 
    print(luna) 
"""

# Respuesta:

# Collie says: ¡Guau! ¡No huyas, Corderito!
# Dobermann says: ¡Guau! ¡Quédese donde está, Señor Intruso!


# Pregunta 02 - ¿Cuál es el resultado esperado del siguiente código?

"""
    print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
    print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))
"""

# Respuesta:

# True False
# Falso True

"""
    SheepDog hereda de Dog, pero no de GuardDog.
    rocky es instancia de SheepDog, no de GuardDog.
    luna sí es instancia de GuardDog.
"""


# Pregunta 03 -  ¿Cuál es el resultado esperado de la siguiente pieza de código?

"""
    print(luna is luna, rocky is luna)
    print(rocky.kennel)
"""

# Respuesta:

# True False
# 2 

# Pregunta 04 - Define una subclase de SheepDog llamada LowlandDog, y equipala con un método __str__() 
# que anule un método heredado del mismo nombre. El nuevo método __str__() debe retornar la cadena 
# "¡No me gustan las montañas!".

# Desarrollo:

class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) +  " ¡No me gustan las montañas!"
    

doggy = LowlandDog("doggy")

print(doggy)