# Sección 1 – Los fundamentos de la POO

# Los conceptos básicos del enfoque orientado a objetos

"""
    - La programación procedimental separa datos y funciones.
    - La programación orientada a objetos (POO) combina datos y funciones dentro de estructuras llamadas clases.
    - Python permite usar ambos enfoques.
    - La POO es útil para proyectos grandes y complejos, facilitando su mantenimiento y escalabilidad.
"""

# Enfoque procedimental versus el enfoque orientado a objetos

"""
    - En el enfoque procedimental:
        - Los datos (variables) y el código (funciones) están separados.
        - Las funciones pueden acceder y modificar datos libremente.

    - En el enfoque orientado a objetos:
        - Los datos y el código están encapsulados en objetos.
        - Las funciones internas de los objetos se llaman métodos.
        - Los objetos tienen propiedades (atributos) y métodos (acciones).
        - Las clases actúan como "recetas" para construir objetos.
"""

# Jerarquía de clases

"""
    Una jerarquía de clases representa una estructura de herencia.

    Ejemplo:

    - Clase general: Vehículos
        - Subclases:
            - Vehículos Terrestres
                - Con ruedas
                - Con pistas
                - Aerodeslizadores
            - Vehículos Acuáticos
            - Vehículos Aéreos
            - Vehículos Espaciales

    Otra jerarquía:

    - Animales
        - Mamíferos
            - Mamíferos Salvajes
            - Mamíferos Domesticados
"""

# ¿Qué es un objeto?

"""
    - Un objeto es una instancia de una clase.
    - Un objeto de una subclase también pertenece a todas sus superclases.
    - Ejemplo:
        - Un auto pertenece a la clase Vehículos con ruedas → Vehículos Terrestres → Vehículos.
        - Un gato llamado Rodolfo es un objeto de clase Mamíferos Domesticados → Mamíferos → Animales.
"""

# Herencia

"""
    - Una subclase hereda atributos y métodos de su superclase.
    - Esto permite crear nuevas clases sin duplicar código.
"""

# ¿Qué contiene un objeto?

"""
    Todo objeto puede tener:

    1. Un nombre (identificador).
    2. Un conjunto de propiedades (atributos).
    3. Un conjunto de métodos (acciones que puede realizar).

    Ejemplo 1:
    "Un Cadillac rosa pasó rápidamente."
        - Nombre: Cadillac
        - Clase: Vehículos con ruedas
        - Propiedad: Color = rosa
        - Actividad: Pasar (rápidamente)

    Ejemplo 2:
    "Rodolfo es un gato grande que duerme todo el día."
        - Nombre: Rodolfo
        - Clase: Gato
        - Propiedad: Tamaño = grande
        - Actividad: Dormir
"""

# Tu primera clase

class TheSimplestClass:
    pass

"""
    - Esta es la clase más simple posible.
    - No tiene atributos ni métodos.
    - La palabra clave 'class' se usa para definir una clase.
    - 'pass' indica que no hay contenido por ahora.
"""

# Tu primer objeto

my_first_object = TheSimplestClass()

"""
    - Aquí creamos un objeto a partir de la clase 'TheSimplestClass'.
    - El objeto se guarda en la variable 'my_first_object'.
    - Esto se llama instanciación: crear una instancia (objeto) de una clase.
"""

# RESUMEN DE SECCIÓN

"""
    1. Una clase es una idea abstracta. Los objetos son instancias concretas de esa clase.

    2. Herencia:
        - Clase derivada: subclase.
        - Clase base: superclase.
        - Se representa como una flecha desde subclase hacia superclase.

    3. Todo objeto tiene:
        - Un nombre.
        - Propiedades (pueden estar vacías).
        - Métodos (pueden estar vacíos).

    4. Para definir una clase se usa:

        class This_Is_A_Class:
            pass

    5. Para crear un objeto de una clase definida:

        this_is_an_object = This_Is_A_Class()
"""


# Cuestionario

# Pregunta 01 - Si asumimos que pitones y cobras son subclases de la misma superclase, 
# ¿cómo la llamarías?

"""
    Respuesta: Serpiente, Reptil, Vertebrado, Animal — todas estas respuestas son aceptables.
"""

# Pregunta 02 - Intenta nombrar algunas subclases de la clase Pitón.

"""
    Respuesta: Pitón india, Pitón de roca africana, Pitón bola, Pitón birmana — la lista es larga.
"""

# Pregunta 03 - ¿Puedes usar la palabra "class" para darle nombre a alguna de tus clases?

"""
    Respuesta: ¡No, no puedes! 'class' es una palabra clave reservada en Python.
"""