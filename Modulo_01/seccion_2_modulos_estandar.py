# Módulos selectos ( math, random, platform, ect)

# ========================================
# 1.2.1 – Usando dir() con módulos
# ========================================

# La función dir() muestra los nombres definidos en un módulo.
import math

print("Contenido del módulo math:")
for name in dir(math):
    print(name, end="\t")

print("\n")

# ========================================
# 1.2.2 – Funciones del módulo math
# ========================================

import math

print("Trigonometría:")
print("sin(0):", math.sin(0))
print("cos(0):", math.cos(0))
print("tan(math.pi / 4):", math.tan(math.pi / 4))

print("\nConversiones:")
print("Grados -> Radianes:", math.radians(180))
print("Radianes -> Grados:", math.degrees(math.pi))

print("\nExponenciación y logaritmos:")
print("exp(1):", math.exp(1))
print("log(e):", math.log(math.e))
print("log10(100):", math.log10(100))
print("log2(8):", math.log2(8))
print("pow(2, 3):", pow(2, 3))  # Función incorporada, no necesita import

print("\nFunciones generales:")
print("ceil(2.3):", math.ceil(2.3))
print("floor(2.7):", math.floor(2.7))
print("trunc(2.9):", math.trunc(2.9))
print("factorial(5):", math.factorial(5))
print("hypot(3, 4):", math.hypot(3, 4))  # Debería dar 5

# ========================================
# 1.2.3 – Módulo random (números pseudoaleatorios)
# ========================================

import random

print("\nNúmeros pseudoaleatorios:")
for _ in range(5):
    print(random.random())  # Entre 0.0 y 1.0

print("\nSemilla fija (repetible):")
random.seed(42)
for _ in range(5):
    print(random.random())

print("\nrandrange y randint:")
print("randrange(1, 10):", random.randrange(1, 10))
print("randint(1, 10):", random.randint(1, 10))

print("\nchoice y sample:")
lista = list(range(1, 11))
print("choice:", random.choice(lista))
print("sample de 3 elementos:", random.sample(lista, 3))

# ========================================
# 1.2.5 y 1.2.6 – Módulo platform (información del sistema)
# ========================================

from platform import platform, machine, processor, system, version
from platform import python_implementation, python_version_tuple

print("\nInformación del sistema:")
print("Platform:", platform())
print("Machine:", machine())
print("Processor:", processor())
print("System:", system())
print("Version:", version())

print("\nInformación de Python:")
print("Implementación:", python_implementation())
print("Versión:", python_version_tuple())


# ========================================
# Ejercicios
# ========================================

# Pregunta 1: ¿Cuál es el valor esperado de la variable result después de que se ejecuta el siguiente código?

import math
result = math.e == math.exp(1)
print(result)  # Imprime un booleano: True

# Pregunta 2: (Completa el enunciado) Establecer la semilla del generador con el mismo valor 
# cada vez que se ejecuta tu programa garantiza que...

"""
Respuesta: los valores pseudoaleatorios generados por el módulo random serán exactamente los mismos cada vez.
"""

# Pregunta 3: ¿Cuál de las funciones del módulo platform utilizarías para determinar el 
# nombre del CPU que corre dentro de tu computadora?

"""
Respuesta: platform.processor()
"""

# Pregunta 4: ¿Cuál es el resultado esperado del siguiente fragmento de código?

import platform
print(len(platform.python_version_tuple()))  # Imprime: 3, ya que la tupla tiene tres elementos (mayor, menor, revisión)