# Preguntas:

# Pregunta 1 - Sabiendo que una función llamada fun() reside dentro de un módulo llamado mod, 
# selecciona la forma correcta de importarlo.

"""
    opciones:

    from mod import fun / respuesta
    import fun from mod
    import fun
    from fun import mod
"""

# Pregunta 2 - Sabiendo que una función llamada fun() reside dentro de un módulo llamado mod, 
# y se ha importado usando la siguiente línea:

""" import mod """

# Selecciona la forma en que se puede invocar desde tu código.

"""
    opciones:

    mod.fun() / respuesta
    mod->fun()
    mod::fun()
    fun()
"""

# Pregunta 3 - Una función que devuelve una lista de todas las 
# entidades disponibles en un módulo lleva por nombre:

"""
    opciones:

    listmodule()
    entities()
    dir() / respuesta
    content()
"""

# Pregunta 4 - Un archivo pyc contiene: 

"""
    opciones:

    un interprete de python
    un compillador de python
    código compilado de python / respuesta
    código fuente de python
"""

# Pregunta 5 - Cuando se importa un módulo, su contenido:

"""
    opciones:

    es ignorado
    se ejecuta tantas veces como se importe
    puede ser ejecutado (explicitamente) 
    se ejecuta una vez (implicitamente) / respuesta

    Cuando importas un módulo, su contenido se ejecuta una vez 
    (incluso aunque lo importes varias veces). Luego queda en sys.modules.
"""

# Pregunta 6 - Una variable predefinida de Python que almacena el nombre del módulo actual 
# lleva por nombre:

"""
    opciones:

    __mod__
    __name__ / respuesta
    __modname__
    __module___
"""

# Pregunta 7 - La siguiente línea de código:

""" form a.b import c """

# causa la importación de:

"""
    opciones:

    la entidad c del módulo a del paquete b
    la entidad a del módulo b del paquete c 
    la entidad c del módulo b del paquete a / respuesta
    la entidad b del módulo a del paquete c
"""

# Pregunta 8 - ¿Cuál es el valor esperado asignado a la variable result después de que se ejecute
# el siguiente código?

"""
    import math

    result = math.e !=  math.pow(2, 4)
    print(int(result))
"""

"""
    opciones:

    0
    False
    1 / respuesta
    True
"""

# Pregunta 9 - ¿Cuál es el resultado esperado del siguiente código?

"""
    from random import randint

    for i in range(2):
        print(randint(1, 2), end='')
"""

"""
    opciones:

    12
    Existen millones de combinaciones podibles y no se puede predecir el resultado exacto.
    12, o 21
    11, 12, 21, o 22 / respuesta
"""

# Pregunta 10 - Selecciona las sentencias verdaderas. (Selecciona 2 respuestas)

"""
    opciones:

    - La función system del módulo platform devuelve una cadena con el nombre del sistema operativo. / respuesta
    - La función version del módulo platform devuelve una cadena con la versión de tu instalación 
      de python.
    - La función processor del módulo platform devuelve un número entero con la cantidad de procesos 
      que se están ejecutando actualmente en tu sistema operativo.
    - La función version del módulo platform devuelve una cadena con la versíon de tu sistema operativo. / respuesta
"""

# Pregunta 11 - Durante la primera importación de un módulo, Python despliega los archivos pyc 
# en el directorio llamado:

"""
    opciones:

    Mymodules
    __init__
    Hashbang
    __pycache__ / respuesta
""" 

# Pregunta 12 - El conjunto de caracteres escrito como #! se emplea para:

"""
    opciones:

    - crear un docstring(cadena de documentación).
    - decirle a un sistema operativo unix o similar a unix cómo ejecutar el contenido 
      de un archivo python. / respuesta
    - hacer que una entidad de módulo en particular sea privada.
    - decirle a un sistema operativo MS Windows cómo ejecutar el contenido de un archivo Python.
"""

# Pregunta 13 - Se puede obtener una lista de las dependencias de los paquetes en pip 
# empleando el comando:

"""
    opciones:

    dir
    show / respuesta
    deps
    list
"""

# Pregunta 14 - El comando pip list presenta una lista de:

"""
    opciones:

    paquetes instalados localmente. / respuesta
    comandos pip disponibles.
    paquetes locales obsoletos.
    todos los paquetes disponibles en PyPI.
"""

# Pregunta 15 - ¿Cuáles de las siguientes sentencias son verdaderas acerca del comando pip search?
# (Selecciona dos respuestas).

"""
    opciones:

    Busca en todos los paquetes de PyPI.  / respuesta
    Necesita una conexión a internet para funcionar. / respuesta
    Todas sus búsquedas están limitadas a paquetes instalados localmente.
    Busca solo a través de los nombres de los paquetes.
    Nota: El comando pip search fue descontinuado oficialmente en versiones recientes de pip.
"""

# Pregunta 16 - ¿Cúales de las siguientes sentencias son verdaderas acerca del comando pip install?
# (Selecciona dos respuestas).

"""
    opciones:

    Siempre instala la versión más reciente del paquete y eso no se puede cambiar.
    Permite al usuario instala una versión especifica del paquete. / respuesta
    Instala un paquete por usuario cuando la opción --user es especificada. / respuesta
    Instala un paquete en todo el sistema cuando la opción --system es especificada.
"""

# Pregunta 17 - ¿Cúal de las siguientes sentencias es verdadera acerca de la actualización
# de paquetes de python ya instalados?

"""
    opciones:

    Solo se puede hacer desinstalado e instalando los paquetes una vez más.
    Es realizada por el comando install acompañado de la opción -U. / respuesta
    Es un proceso automático que no requiere la atención del usuario. 
    Se puede hacer reinstalando el paquete usando el comando reinstall. 
"""

# Pregunta 18 - ¿Qué comando de pip se puede emplear para eliminar un paquete
# instalado?

"""
    opciones:

    pip remove package
    pip --uninstall package
    pip uninstall package / respuesta
    pip install --uninstall package
"""

