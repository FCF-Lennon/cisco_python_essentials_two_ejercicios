# Modulos
# Importacion de módulos


# Para importar un módulo completo en Python, puedes usar la sentencia import nombre_del_modulo. 
# También es posible importar varios módulos a la vez, separados por comas:

""" 
import mod1
import mod1, mod2, mod3 / No recomendado
"""

# Aunque esta última forma es válida, no se recomienda por razones de estilo. Es más claro 
# y legible importar cada módulo en una línea separada:

"""
    import mod1
    import mod2
    import mod3
"""

# Cuando importas un módulo de esta forma, para acceder a cualquiera de sus entidades 
# (funciones, variables, clases, etc.), debes anteponer el nombre del módulo utilizando 
# la notación con punto (.). Ejemplo:

"""
    import my_module
    result = my_module.my_function(my_module.my_data)

    Este enfoque tiene la ventaja de evitar conflictos de nombres, ya que todas 
    las entidades importadas están "espaciadas" dentro del nombre del módulo.
"""

# Importación selectiva de entidades

# También puedes importar entidades específicas desde un módulo, sin necesidad 
# de anteponer el nombre del módulo al usarlas:

"""
    from module import my_function, my_data
    result = my_function(my_data)

    Este método puede hacer el código más conciso, pero tiene el riesgo de provocar 
    conflictos de nombres, especialmente si las entidades importadas tienen el mismo 
    nombre que variables o funciones locales.
"""

# Una variante aún más arriesgada es importar todo el contenido del módulo:

"""
    from my_moduloe import *
    result = my_function(my_data)

    Nota: No se recomienda esta forma, ya que puede generar conflictos 
    de nombres difíciles de detectar y mantener.
"""

# Uso de alias con as

# Puedes cambiar el nombre de una entidad importada "sobre la marcha" usando as. 
# Esto es útil cuando hay conflictos de nombres o simplemente para usar nombres más cortos:

"""
    from module import my_function as fun, my_data as dat
    result = fun(dat)
"""

# También puedes usar as para cambiar el nombre de un módulo completo:

"""
    import my_module as mm
    result = mm.my_function(mm.my_data)
"""


# Ejercicios:

# Pregunta 1: Quieres invocar la función make_money() del módulo mint. Tu código comienza con:

"""
    import mint
"""

# ¿Cómo la invocas correctamente?

"""
    Respuesta: mint.make_money()
"""


# Pregunta 2: Quieres invocar make_money() desde el módulo mint. Tu código comienza con:

"""
    from mint import make_money
"""

# ¿Cuál es la forma adecuada de invocar a la función?

"""
    Respuesta: make_money()
"""

# Pregunta 3: Has escrito tu propia función make_money. Sin embargo, 
# necesitas importar una función con el mismo nombre desde el módulo 
# mint sin sobrescribir la tuya.

# ¿Qué forma de importación puedes usar?

"""
    Respuesta:
    un as o alias para la funcion del módulo mint
    from mint import make_money as make_more_money
"""

# Pregunta 4: Tu código comienza con:

"""
    from mint import *
"""
# ¿Cómo invocas la función make_money()?

"""
    Respuesta: make_money()
"""
