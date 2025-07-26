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


# Laboratorio:

# Ejercicio 1 - La clase Timer

"""
    Necesitamos una clase capaz de contar segundos. ¿Fácil? No es tan 
    fácil como podrías pensar, ya que tendremos algunos requisitos 
    específicos.

    Léelos con atención, ya que la clase sobre la que escribes se 
    utilizará para lanzar cohetes en misiones internacionales a Marte. 
    Es una gran responsabilidad. ¡Contamos contigo!

    Tu clase se llamará Timer (temporizador en español). Su constructor
    acepta tres argumentos que representan horas (un valor del rango 
    [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) 
    y segundos (del rango [0..59]).

    Cero es el valor predeterminado para todos los parámetros anteriores. 
    No es necesario realizar ninguna comprobación de validación.

    La clase en sí debería proporcionar las siguientes facilidades:

    - Los objetos de la clase deben ser "imprimibles", es decir, deben 
      poder convertirse implícitamente en cadenas de la siguiente forma: 
      "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera 
      de los valores es menor que 10.
    - La clase debe estar equipada con métodos sin parámetros llamados 
      next_second() y previous_second(), incrementando el tiempo almacenado 
      dentro de los objetos en +1/-1 segundos respectivamente.
      
      Emplea las siguientes sugerencias:

    - Todas las propiedades del objeto deben ser privadas.
    - Considera escribir una función separada (¡no un método!) para 
      formatear la cadena con el tiempo.

    Completa la plantilla que te proporcionamos en el editor. Ejecuta 
    tu código y comprueba si el resultado es el mismo que el nuestro.
"""

# Salida:

"""
    23:59:59
    00:00:00
    23:59:59
"""

# Desarrollo:

def format_time (val):
    second = str(val)
    if len(second) == 1: 
        second = '0' + second
    return second 

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return  format_time(self.__hours) + ":" + \
                format_time(self.__minutes) + ":" + \
                format_time(self.__seconds)
    
    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
       self.__seconds -= 1
       if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                   self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    

# Ejercicio 02 - Días de la semana

"""
    Tu tarea es implementar una clase llamada Weeker. Sí, tus ojos no te engañan, este nombre 
    proviene del hecho de que los objetos de esta clase podrán almacenar y manipular los días 
    de la semana.

    El constructor de la clase acepta un argumento: una cadena. La cadena representa el nombre 
    del día de la semana y los únicos valores aceptables deben provenir del siguiente conjunto:

    Lun Mar Mie Jue Vie Sab Dom

    Invocar al constructor con un argumento desde fuera de este conjunto debería generar la 
    excepción WeekDayError (defínela tu mismo; no te preocupes, pronto hablaremos sobre la 
    naturaleza objetiva de las excepciones). La clase debe proporcionar las siguientes facilidades:

    - Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente 
      en cadenas de la misma forma que los argumentos del constructor.
    - La clase debe estar equipada con métodos de un parámetro llamados add_days(n) y subtract_days(n), 
      siendo n un número entero que actualiza el día de la semana almacenado dentro del objeto mediante 
      el número de días indicado, hacia adelante o hacia atrás.
    - Todas las propiedades del objeto deben ser privadas.
    
    Completa la plantilla que te proporcionamos en el editor, ejecuta su código y verifica si tu 
    salida se ve igual que la nuestra. Completa la plantilla que te proporcionamos en el editor, 
    ejecuta su código y verifica si tu salida se ve igual que la nuestra.
"""

# Salida Esperada:

"""
    Lun
    Mar
    Dom
    Lo siento, no puedo atender tu solicitud
"""

# Desarrollo:

class WeekDayError(Exception):
    pass

class Weeker:
    __semana = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
 
    def __init__(self, day):
        try:
            self.__index_day = Weeker.__semana.index(day)
        except ValueError:
            raise WeekDayError("Día de la semana no válido")
      
    def __str__(self):
        return self.__semana[self.__index_day] # Devuelve el día de la semana como cadena

    def add_days(self, n):
        self.__index_day = (self.__index_day + n) % 7


    def subtract_days(self, n):
        self.__index_day = (self.__index_day - n) % 7
       
try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")


# Ejercicio 03 - Puntos en un plano

"""
    Visitemos un lugar muy especial: un plano con el sistema de coordenadas cartesianas 
    (puedes obtener más información sobre este concepto aquí: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

    Cada punto ubicado en el plano puede describirse como un par de coordenadas habitualmente 
    llamadas x y y. Queremos que escribas una clase en Python que almacene ambas coordenadas como números flotantes. 
    Además, queremos que los objetos de esta clase evalúen las distancias entre cualquiera de los dos puntos 
    situados en el plano.

    La tarea es bastante fácil si empleas la función denominada hypot() (disponible a través del módulo math) 
    que evalúa la longitud de la hipotenusa de un triángulo rectángulo (más detalles aquí: 
    https://en.wikipedia.org/wiki/Hypotenuse) y aquí: https://docs.python.org/3.7/library/math.html#trigonometric-functions. 
"""

# Así es como imaginamos la clase:

"""
    - Se llama Point.
    - Su constructor acepta dos argumentos (x y y respectivamente), ambos por defecto se igualan a cero.
    - Todas las propiedades deben ser privadas.
    - La clase contiene dos métodos sin parámetros llamados getx() y gety(), que devuelven cada una de las 
      dos coordenadas (las coordenadas se almacenan de forma privada, por lo que no se puede acceder a ellas 
      directamente desde el objeto).
    - La clase proporciona un método llamado distance_from_xy(x,y), que calcula y devuelve la distancia entre 
      el punto almacenado dentro del objeto y el otro punto dado en un par de números flotantes.
    - La clase proporciona un método llamado distance_from_point(point), que calcula la distancia 
      (como el método anterior), pero la ubicación del otro punto se da como otro objeto de clase Point.

    Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra.
"""

# Salida esperada:

"""
    1.4142135623730951
    1.4142135623730951
"""

# Desarrollo:

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))


# Ejercicio 04 - Triangulo

"""
    Ahora vamos a colocar la clase Point (ver Lab anterior) dentro de otra clase. Además, vamos a 
    poner tres puntos en una clase, lo que nos permitirá definir un triángulo. ¿Cómo podemos hacerlo?

    La nueva clase se llamará Triangle y esto es lo que queremos:

    - El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.
    - Los puntos se almacenan dentro del objeto como una lista privada.
    - La clase proporciona un método sin parámetros llamado perimeter(), que calcula el perímetro del 
      triángulo descrito por los tres puntos; el perímetro es la suma de todas las longitudes de los lados 
      (lo mencionamos para que conste, aunque estamos seguros de que tú mismo lo conoces perfectamente).

    Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida 
    se ve igual que la nuestra.
"""

# A continuación puedes copiar el código de la clase Point, el cual se utilizo en el laboratorio anterior:

"""
    class Point:
        def __init__(self, x=0.0, y=0.0):
            self.__x = x
            self.__y = y
"""

# Salidad esperada:

""" 
    3.414213562373095
"""

# Desarrollo:

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
       self.__puntos = [vertice1, vertice2, vertice3]

    def perimeter(self):
        total = 0
        for i in range(len(self.__puntos)):
            p1 = self.__puntos[i]
            p2 = self.__puntos[(i + 1) % len(self.__puntos)]
            total += math.hypot(p2._Point__x - p1._Point__x, p2._Point__y - p1._Point__y)
        return total

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())


# o tambien:

"""
    import math


    class Point:
        def __init__(self, x=0.0, y=0.0):
            self.__x = x
            self.__y = y

        def getx(self):
            return self.__x

        def gety(self):
            return self.__y

        def distance_from_xy(self, x, y):
            return math.hypot(abs(self.__x - x), abs(self.__y - y))

        def distance_from_point(self, point):
            return self.distance_from_xy(point.getx(), point.gety())


    class Triangle:
        def __init__(self, vertice1, vertice2, vertice3):
            self.__vertices = [vertice1, vertice2, vertice3]

        def perimeter(self):
            per = 0
            for i in range(3):
                per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
            return per


    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())
"""

