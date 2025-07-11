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
 

# Laboratorio:

# Ejercicio 01 - Pila contadora:

"""
    Recientemente te mostramos cómo extender las posibilidades de Stack definiendo una nueva 
    clase (es decir, una subclase) que retiene todos los rasgos heredados y agrega algunos nuevos.

    Tu tarea es extender el comportamiento de la clase Stack de tal manera que la clase pueda 
    contar todos los elementos que son agregados (push) y quitados (pop). Emplea la clase Stack 
    que proporcionamos en el editor.

    Sigue las sugerencias:

    - Introduce una propiedad diseñada para contar las operaciones pop y nombrarla de una manera 
      que garantice que esté oculta.

    - Inicializala a cero dentro del constructor.

    - Proporciona un método que devuelva el valor asignado actualmente al contador (nómbralo get_counter()).
      Completa el código en el editor. Ejecútalo para comprobar si tu código da como salida 100.
"""

# Desarrollo

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val
    
class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())


# Ejercicio 02 - Colas alias FIFO:

"""
    Como ya sabes, una cola es una estructura de datos que realiza el modelo LIFO (último en entrar, 
    primero en salir). Es fácil y ya te has acostumbrado a ello perfectamente.

    Probemos algo nuevo ahora. Una cola (queue) es un modelo de datos caracterizado por el término FIFO: 
    primero en entrar, primero en salir. Nota: una cola (fila) regular que conozcas de las tiendas u oficinas 
    de correos funciona exactamente de la misma manera: un cliente que llegó primero también es el primero 
    en ser atendido.

    Tu tarea es implementar la clase Queue con dos operaciones básicas:

    - put(elemento), que coloca un elemento al final de la cola.
    - get(), que toma un elemento del principio de la cola y lo devuelve como resultado (la cola no 
      puede estar vacía para realizarlo correctamente).
    
    Sigue las sugerencias:

    - Emplea una lista como tu almacenamiento (como lo hicimos con la cola).
    - put() debe agregar elementos al principio de la lista, mientras que get() debe eliminar los elementos 
      del final de la lista.
    - Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) y generala 
      cuando get() intente operar en una lista vacía.
    
    Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si tu salida es similar 
    a la nuestra.
"""

# Salida Esperada:

"""
    1
    perro
    False
    Queue error
"""

# Eligir la clase base para la nueva excepción.

"""
    class QueueError(???):  
        # codigo
"""

# Desarrollo:

class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
        pass


class Queue:
    def __init__(self):
        self.__cola = []

    def put(self, elem):
        self.__cola.insert(0, elem)

    def get(self):
        if len(self.__cola) > 0:
             elem = self.__cola[-1]
             del self.__cola[-1]
             return elem
        else:
             raise QueueError
     
que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    

# Ejercicio 03 - Colas alias FIFO: parte 2:

"""
    Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método 
    sin parámetros que devuelva True si la cola está vacía y False de lo contrario.

    Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un 
    resultado similar al nuestro.
"""

# Salida Esperada:

"""
    1
    perro
    False
    Cola vacía
"""

# Desarrollo:

class Queue:
    def __init__(self):
        self.__cola = []

    def put(self, elem):
        self.__cola.insert(0, elem)

    def get(self):
        if len(self.__cola) > 0:
            elem = self.__cola[-1]
            del self.__cola[-1]
            return elem


class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def verificar_valor (self):
        return len(self._Queue__cola) == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.verificar_valor():
        print(que.get())
    else:
        print("Cola vacía")
        