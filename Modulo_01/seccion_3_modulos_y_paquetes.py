# 1. ¿Qué es un paquete?

# Un paquete en Python es una forma de organizar y agrupar módulos relacionados entre sí, de manera jerárquica.
# Así como un módulo es un archivo .py que contiene funciones o clases, un paquete es una carpeta que contiene
# múltiples módulos o incluso otros paquetes (subpaquetes).

# Diferencias entre módulos y paquetes

# Concepto    | Módulo                | Paquete
# ------------|------------------------|---------------------------
# Forma       | Archivo .py           | Carpeta con __init__.py
# Contenido   | Funciones, clases, variables | Módulos y/o subpaquetes
# Propósito   | Reutilizar código     | Organizar módulos

# ---------------------------------------------

# 2. Tu primer módulo
# Paso 1: Crear un archivo llamado module.py
# Este será tu módulo, al principio puede estar vacío.

# Paso 2: Crear otro archivo llamado main.py
# Este archivo importará y utilizará el módulo.

""" import module """

# Ambos archivos deben estar en la misma carpeta. Al ejecutar main.py, no verás nada si module.py está vacío,
# lo cual indica que la importación fue exitosa.

# ¿Qué es __pycache__?
# Cuando importas un módulo, Python crea una carpeta __pycache__ que contiene archivos .pyc,
# que son versiones compiladas del módulo. Esto acelera futuras importaciones.

# ---------------------------------------------

# 3. Código ejecutado al importar
# Si escribes este código en module.py:

"""print("Me gusta ser un módulo.")"""

# Verás ese mensaje tanto si ejecutas directamente el archivo como si lo importas desde main.py.
# Esto se debe a que el código de un módulo se ejecuta en la primera importación.

# ---------------------------------------------

# 4. La variable __name__
# Esta variable especial indica si el archivo se está ejecutando directamente o si se está importando como módulo.

"""print(__name__)"""

# Al ejecutar module.py directamente: imprime __main__
# Al importar desde main.py: imprime module

# Esto permite usar:
# if __name__ == "__main__":
# Para pruebas o ejecución directa

# ---------------------------------------------

# 5. Variables dentro de módulos
# Si defines variables como counter = 0 en tu módulo, pueden ser accedidas desde el archivo que lo importa:
# import module
# print(module.counter)

# Pero es recomendable marcar variables internas como privadas usando un guion bajo (_) o doble (__), por ejemplo:
# __counter = 0
# Esto no impide el acceso externo, pero comunica que no deben usarse fuera del módulo.

# ---------------------------------------------

# 6. Funciones en un módulo

# Un ejemplo de módulo útil (module.py):

# #!/usr/bin/env python3 - en Unix 

""" 
__counter = 0
def suml(the_list):
    global __counter
    __counter += 1
    return sum(the_list)

def prodl(the_list):
    global __counter
    result = 1
    for x in the_list:
        result *= x
    return result

if __name__ == "__main__":
    print("Probando módulo...")
    test_list = [1, 2, 3, 4, 5]
    print(suml(test_list))  # 15
    print(prodl(test_list)) # 120 
"""

# Y en main.py:

""" 
from module import suml, prodl
print(suml([0, 0, 0]))
print(prodl([1, 1, 1])) 
"""

# ---------------------------------------------

# 7. Importar módulos desde otras carpetas
# Si tu módulo está en otra carpeta, debes modificar la ruta:

""" 
from sys import path
path.append("C:\\Users\\user\\py\\modules")  # ruta absoluta
import module 
"""

# O usar una ruta relativa:

""" path.append("..\\modules") """

# ---------------------------------------------

# 8. Tu primer paquete

# Un paquete es una carpeta que:
# - Contiene módulos y subpaquetes
# - Debe incluir un archivo __init__.py (puede estar vacío)

# Ejemplo de estructura:

""" packages/
├── extra/
│   ├── __init__.py
│   ├── iota.py
│   ├── good/
│   │   ├── __init__.py
│   │   ├── alpha.py
│   │   ├── beta.py
│   │   └── best/
│   │       ├── __init__.py
│   │       ├── sigma.py
│   │       └── tau.py
│   └── ugly/
│       ├── __init__.py
│       ├── psi.py
│       └── omega.py 
"""

# ---------------------------------------------

# 9. Importando desde paquetes

# Opción 1: Importar todo el módulo

""" 
from sys import path
path.append("..\\packages")
import extra.iota
print(extra.iota.funI())
"""

# Opción 2: Importar directamente la función

""" 
from extra.iota import funI
print(funI()) 
"""

# Opción 3: Importar con alias

""" 
import extra.good.best.sigma as sig
print(sig.funS()) 
"""

# ---------------------------------------------

# 10. Conclusión

# Módulos y paquetes en Python te permiten organizar tu código en estructuras reutilizables y mantenibles.
# Algunas ideas clave:

# - Usa __name__ == "__main__" para probar tus módulos.
# - Marca las variables internas con _ o __ si no deben ser modificadas.
# - Usa __init__.py para declarar paquetes.
# - Usa sys.path.append() para importar desde ubicaciones personalizadas.
# - Piensa en los paquetes como carpetas de módulos, y en los módulos como archivos reutilizables.

# Ejercicios

# Pregunta 1: Deseas evitar que el usuario de tu módulo ejecute tu código como un script ordinario. 
# ¿Cómo lograrías tal efecto?

"""
Respuesta:
Utilizando la condición if __name__ == "__main__": dentro del módulo.
Esto asegura que el bloque de código solo se ejecute si el archivo se ejecuta directamente,
y no cuando se importa como un módulo.
"""

# Pregunta 2: Algunos paquetes adicionales y necesarios se almacenan dentro del directorio D:\Python\Project\Modules.
# Escribe un código asegurándote de que Python recorra el directorio para encontrar todos los módulos solicitados.

"""
Respuesta:
from sys import path
path.append("D:\\Python\\Project\\Modules")
import mod1, mod2
"""

# Pregunta 3: El directorio mencionado en la pregunta anterior contiene un subárbol con la siguiente estructura:
"""
abc
└── def
    └── mymodule.py
"""
# Asumiendo que D:\Python\Project\Modules se ha adjuntado con éxito a la lista sys.path,
# escribe una directiva de importación que te permita usar todas las entidades de mymodule.

"""
Respuesta:
import abc.def.mymodule
"""
