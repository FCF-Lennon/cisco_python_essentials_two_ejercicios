# Sección 2 – Un corto viaje desde el enfoque procedimental hacia el orientado a objetos

# ¿Qué es una pila?

"""
    Una pila es una estructura de datos que opera bajo el principio LIFO: 
    Last In, First Out (Último en entrar, primero en salir). 
    Las operaciones principales son:

    - push: agrega un elemento al tope.
    - pop: elimina el elemento del tope.
"""

# La pila: el enfoque procedimental

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Ejemplo de uso
push(1)
push(2)
push(3)

print(pop())  # Output: 3
print(pop())  # Output: 2
print(pop())  # Output: 1

"""
    Este enfoque es funcional, pero tiene problemas:

    - No hay protección de la estructura.
    - Difícil manejar múltiples pilas sin duplicar código.
"""

# Problemas del enfoque procedimental

"""
    - La lista stack es pública, puede ser modificada accidentalmente.
    - No es fácil reutilizar la estructura para múltiples pilas.
    - Difícil escalar o extender la funcionalidad sin duplicación.
"""

# La pila: el enfoque orientado a objetos

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# Crear e interactuar con objetos

stack1 = Stack()
stack2 = Stack()

stack1.push(3)
stack2.push(4)
stack1.push(5)

print(stack1.pop())  # Output: 5
print(stack2.pop())  # Output: 4
print(stack1.pop())  # Output: 3

"""
    Cada objeto tiene su propia lista interna (encapsulada).
    No se puede acceder directamente desde fuera.
"""

# Una pila desde cero con herencia

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum

# Ejemplo de uso
adding_stack = AddingStack()
adding_stack.push(1)
adding_stack.push(2)
adding_stack.push(3)
adding_stack.push(4)
adding_stack.push(5)

print(adding_stack.get_sum())  # Output: 15

print(adding_stack.pop())  # Output: 5
print(adding_stack.pop())  # Output: 4
print(adding_stack.get_sum())  # Output: 6

"""
    La clase AddingStack extiende Stack e introduce una suma acumulativa.
    Se usa herencia para reutilizar y modificar comportamiento.
"""

# RESUMEN DE SECCIÓN

"""
    1. Una pila opera bajo el modelo LIFO y ofrece push() y pop().
    2. El modelo orientado a objetos soluciona problemas de seguridad y reutilización 
    del modelo procedimental.
    3. Un método de clase accede a componentes internos mediante 'self'.
    4. El constructor se llama __init__ y se ejecuta al crear el objeto.
    5. Todos los métodos deben tener 'self' como primer parámetro.
    6. Los atributos privados se definen con doble guion bajo (__), y no son accesibles 
    directamente desde fuera de la clase.
"""

# Cuestionario:

# Pregunta 01 - Suponiendo que hay una clase llamada Snakes, escribe la primera línea de la declaración 
# de clase Python, expresando el hecho de que la nueva clase es en realidad una subclase de Snake.

"""
    Respuesta:

    class Vivora(Snakes): # Vivora hereda de Snakes
        def __init__(self):
            Snakes.__init__(self)
"""


# Pregunta 2 - Algo falta en la siguiente declaración, ¿qué es?

"""
    class Snakes:
        def __init__():
            self.sound = 'Sssssss'
"""

# Respuesta: Falta el parámetro 'self' en la definición del constructor __init__.
# Debe escribirse como: def __init__(self):


# Pregunta 03 - Modifica el código para garantizar que la propiedad venomous sea privada.

"""
    class Snakes:
        def __init__(self):
            self.venomous = True
"""

# Respuesta:
# Para que el atributo sea considerado privado, debe escribirse con doble guion bajo al inicio.
# La línea correcta sería: self.__venomous = True
 