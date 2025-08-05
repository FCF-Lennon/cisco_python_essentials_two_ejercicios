# Módulo 4 - Generadores, Iteradores y Cierres

"""
    ¡Bienvenido al Módulo 4, sección uno!
    Comenzaremos aprendiendo sobre generadores, iteradores y cierres.
"""

# Generadores: dónde encontrarlos:

"""
    En Python, un generador es un fragmento de código capaz de producir 
    una serie de valores y controlar la iteración.
    Son un tipo especial de iterador.

    Ejemplo clásico:
"""

for i in range(5):
    print(i)

"""
    Salida:

    0
    1
    2
    3
    4

    range() es un generador e iterador a la vez.

    Diferencia clave:

    - Una función devuelve un único valor (una vez).
    - Un generador devuelve múltiples valores, uno a la vez, y puede ser invocado 
      múltiples veces implícitamente.
"""

# El protocolo iterador

"""
    Un iterador debe implementar:

    1. __iter__() → devuelve el objeto iterador.
    2. __next__() → devuelve el siguiente valor o lanza StopIteration cuando termina.
"""

# Implementación de un iterador de Fibonacci

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration("Fin de la secuencia")
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)

"""
    Este ejemplo muestra cómo se construye manualmente un iterador que 
    obedece el protocolo iterador.

    Salida:

    __init__
    __iter__
    __next__
    1
    __next__
    1
    __next__
    2
    __next__
    3
    __next__
    5
    __next__
    8
    __next__
    13
    __next__
    21
    __next__
    34
    __next__
    55
    __next__
"""

# Composición de iterador dentro de otra clase

class Class:
    def __init__(self):
        self.fib = Fib(10)

    def __iter__(self):
        return self.fib

for i in Class():
    print(i)

"""
    Aunque no se invoca directamente a Fib en el bucle, funciona porque 
    Class implementa __iter__() que retorna un iterador.
"""

# La sentencia yield:

"""
    El protocolo iterador manual es funcional, pero puede ser engorroso.
    Python introduce la palabra clave 'yield' para simplificarlo.
"""

# Ejemplo incorrecto usando return:

# def fun(n):
#     for i in range(n):
#         return i  # Esto rompe el bucle en la primera iteración

"""
    Este código devuelve solo el primer valor y no puede retomar el estado.
"""

# Reemplazando return con yield:

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

"""
    Ahora la función se convierte en un generador real, capaz de mantener 
    su estado y continuar la iteración.

    Salida esperada:
    0
    1
    2
    3
    4
"""

# Cómo construir un generador:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(8):
    print(v)

"""
    Generador que produce las primeras potencias de 2:
    1, 2, 4, 8, 16, 32, 64, 128
"""

# Generador con lista por comprensión:

t = [x for x in powers_of_2(5)]
print(t)

"""
    Generador usado dentro de una lista por comprensión.

    Salida:
    [1, 2, 4, 8, 16]
"""

# Generador transformado con list():

t = list(powers_of_2(3))
print(t)

"""
    Transformando los valores del generador en una lista directamente:
    
    Salida:
    [1, 2, 4]
"""

# Uso del operador 'in' con generadores:

for i in range(20):
    if i in powers_of_2(4):
        print(i)

"""
    Verifica si un valor está en la secuencia generada.

    Salida:
    1
    2
    4
    8
"""

# Generador de Fibonacci con yield:

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            f = p + pp
            pp, p = p, f
            yield f

fibs = list(fibonacci(10))
print(fibs)

"""
    Salida esperada:
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""

# Más acerca de listas por comprensión:

# Forma normal

list_1 = []
for x in range(6):
    list_1.append(10 ** x)

print(list_1)

# Forma con comprensión de listas:

list_2 = [10 ** x for x in range(6)]
print(list_2)

"""
    Ambas generan:
    [1, 10, 100, 1000, 10000, 100000]
    Pero la segunda es más compacta y legible.
"""

# Expresión condicional en comprensión:

list_cond = [1 if x % 2 == 0 else 0 for x in range(10)]
print(list_cond)

"""
    Salida:
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
"""

# Comparación entre lista por comprensión y generador:

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

"""
    Ambos imprimen:
    1 0 1 0 1 0 1 0 1 0

    Pero:
    - the_list es una lista en memoria.
    - the_generator produce valores uno por uno.

    Prueba:
    len(the_list) → 10
    len(the_generator) → TypeError
"""

# Generadores in situ (no almacenados):

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

"""
    Ambos muestran lo mismo, pero el segundo no crea la lista completa.
    Ideal cuando no necesitas todos los valores a la vez.
"""

# Funciones Lambda:

"""
    Una función lambda es una función anónima (sin nombre) definida con 
    la palabra clave `lambda`.

    Su sintaxis básica es:
        lambda parámetros: expresión
"""

# Ejemplo: funciones lambda con nombres asignados:

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# Explicación:
# - `two` devuelve 2.
# - `sqr` devuelve el cuadrado del argumento.
# - `pwr` eleva el primer argumento al segundo.

# Uso de lambdas:

"""
    Las lambdas son útiles como funciones temporales o en una sola línea, 
    especialmente dentro de otras funciones.
"""

# Ejemplo: función genérica que imprime el resultado de otra función

def print_function(args, fun):
    for x in args:
        print('f(', x, ') =', fun(x), sep='')

# Uso con una función lambda en lugar de una función tradicional:

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

# Lambdas y la función map():

"""
    La función map() aplica una función a todos los elementos de un iterable.
    Devuelve un generador.
"""

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

# Aplicar otra lambda a list_2 usando map():

for x in map(lambda x: x * x, list_2):
    print(x, end=" ")

# Lambdas y la función filter():

"""
    La función filter() selecciona elementos que cumplen una condición (función 
    que retorna True).
"""

from random import seed, randint

seed(0)
data = [randint(-10, 10) for _ in range(5)]
print(data)

# Filtrar: solo valores pares positivos:

filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(filtered)

# Cierres:

"""
    Un cierre es una función interna que recuerda el estado de su contexto externo 
    incluso si este ha terminado.
"""

# Ejemplo básico de cierre: 

def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())  # Output: 1

# Ejemplo más complejo: generar múltiples cierres con distintos comportamientos

def make_closure(exponent):
    def power(base):
        return base ** exponent
    return power

square = make_closure(2)
cube = make_closure(3)

for i in range(5):
    print(i, square(i), cube(i))

# Resumen de la Sección:

"""
    1. Un iterador debe implementar:
        - __iter__(): devuelve el propio objeto.
        - __next__(): devuelve el siguiente valor o lanza StopIteration.

    2. yield: suspende una función y guarda su estado, retornando un valor. Útil en generadores.

    3. Expresión condicional:
"""
print(True if 0 >= 0 else False)  # Output: True

# 4. Una lista por comprensión se convierte en generador usando paréntesis:

for x in (el * 2 for el in range(5)):
    print(x, end=" ")  # Output: 0 2 4 6 8
print()

# 5. Función lambda:

def foo(x, f):
    return f(x)

print(foo(9, lambda x: x ** 0.5))  # Output: 3.0

# 6. map() con lambda:

short_list = ['mython', 'python', 'cayó', 'en', 'el', 'piso']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)  # Output: ['Mython', 'Python', 'Cayó', 'En', 'El', 'Piso']

# 7. filter() con lambda:

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)  # Output: ['Python', 'Monty']

# 8. Cierre aplicado para etiquetas HTML

def tag(tg):
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner

b_tag = tag('<b>')
print(b_tag('Monty Python'))  # Output: <b>Monty Python</b>


# Cuestionario de sección:

# Pregunta 01 - ¿Cuál es el resultado esperado del siguiente código?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Sí, sabemos que y no siempre se considera una vocal.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')

# Respuesta: a e i o u y 


# Pregunta 02 - Escribe una función lambda que establezca el bit menos significativo 
# de un número entero en 1 (usando el operador |).
# Luego aplícala con la función map() sobre la lista [1, 2, 3, 4] para generar una lista nueva.
# Finalmente, imprime dicha lista. La salida esperada es: [1, 3, 3, 5]

any_list = [1, 2, 3, 4]
# even_list =  # Completa la línea aquí.
# print(even_list)
 
# Respuesta:

even_list = list(map(lambda x: x | 1, any_list))
print(f'\n{even_list}')


# Pregunta 03 - ¿Cuál es el resultado esperado del siguiente código?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
 
 
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))

# Respuesta: And*Now*for*Something*Completely*Different
