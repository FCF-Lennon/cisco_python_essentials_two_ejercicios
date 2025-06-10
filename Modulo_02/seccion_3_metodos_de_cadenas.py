# Métodos de cadenas

"""
    Las cadenas en Python son inmutables, lo que significa que no puedes 
    cambiarlas directamente. Cuando usas un método de cadena, Python siempre 
    crea y devuelve una nueva cadena con las modificaciones, dejando la 
    original intacta. Esto es un concepto fundamental a recordar. 
"""

# El método capitalize()

"""
    Este método es sencillo pero muy útil: toma la primera letra de una cadena 
    (el carácter en el índice 0) y la convierte a mayúscula, mientras que el 
    resto de las letras se convierten a minúsculas. No importa si la primera 
    letra no es visible, como en el caso de un espacio inicial, solo el primer 
    carácter en el índice 0.
"""

# Output: Abcd (Aquí la 'A' ya era mayúscula y el resto minúsculas, por lo que 
# no hay cambio visible)
print("Abcd".capitalize())

# Si 'α' es una letra y se puede capitalizar en el juego de caracteres
# Output: Αβγδ (Dependerá del comportamiento del juego de caracteres para 
# el alfabeto griego)
print("αβγδ".capitalize()) 

# Output: Alpha
print("alpha".capitalize())

# El primer carácter es un espacio, por lo que la "A" no se capitaliza.
# Output:  alpha
print(" Alpha".capitalize()) 

# Output: 123 (No hay letras para capitalizar)
print("123".capitalize())


# El método center()

"""
    El método center() te permite centrar una cadena dentro de un ancho 
    específico. Lo hace agregando espacios (o un carácter de relleno que 
    tú elijas) a ambos lados de la cadena. Si el ancho especificado es 
    menor que la longitud de la cadena, la cadena original se devuelve 
    sin cambios.

    Variante de un parámetro: Agrega espacios.
"""

print('[' + 'alpha'.center(11) + ']') # Output: [   alpha   ]

# Aquí, la cadena "alpha" (5 caracteres) se centra en un espacio de 11 
# caracteres. Esto resulta en (11 - 5) / 2 = 3 espacios a cada lado 
# (redondeando si es impar).

print('[' + 'Beta'.center(4) + ']') # Ancho igual a la cadena
# Output: [Beta]

print('[' + 'Beta'.center(6) + ']') # Ancho un poco mayor
# Output: [ Beta ]

# Variante de dos parámetros: Rellena con un carácter específico.

print('[' + 'gamma'.center(20, '*') + ']')
# Output: [*******gamma********]

# En este caso, "gamma" (5 caracteres) se centra en 20 caracteres, 
# rellenando el espacio sobrante con asteriscos (*).


# El médodo endswith()

"""
    Este método actúa como un verificador: comprueba si una cadena 
    termina con una subcadena específica y devuelve True o False. 
    Es crucial que la subcadena esté exactamente al final de la cadena.
"""

# Suponiendo que el ejemplo original mostraba algo como:
# print("python".endswith("on")) # True
# print("python".endswith("ona")) # False

# Ejemplos con resultados predecibles:
print("omega".endswith("ga"))    # True
print("omega".endswith("meg"))   # False (No termina con "meg")
print("omega".endswith("a"))     # True
print("omega".endswith("GA"))    # False (Es sensible a mayúsculas/minúsculas)


# El método find()

"""
    Similar al método index(), find() busca una subcadena y devuelve el 
    índice de su primera aparición. La gran diferencia es que find() es 
    más "seguro": si la subcadena no se encuentra, devuelve -1 en lugar 
    de generar un error. Solo funciona con cadenas.
"""

# Variante de un parámetro (búsqueda desde el inicio):

print("eta".find("ta"))
# Output: 1 (La 't' de "ta" está en el índice 1)

print("eta".find("abc"))
# Output: -1 (No se encuentra "abc")

# Nota: Para verificar si un solo carácter está en una cadena, el operador 
# in ('a' in 'kappa') es más rápido que find().

# Asumiendo que el texto original se refiere a un ejemplo con 'alpha'
print("alpha".find("ph")) # 'ph' empieza en el índice 2
# Output: 2

# Asumiendo que el texto original se refiere a un ejemplo con 'alpha'
print("alpha".find("a")) # La primera 'a' está en el índice 0
# Output: 0

# Asumiendo que el texto original se refiere a un ejemplo con 'alpha'
print("alpha".find("xyz")) # 'xyz' no está en la cadena
# Output: -1

# Variante de dos parámetros (búsqueda desde un índice específico)
# Puedes indicar desde qué índice comenzar la búsqueda.

print('kappa'.find('a', 2))
# Output: 4

# Aquí, find() busca 'a' en "kappa" pero a partir del índice 2. La primera 
# 'a' está en el índice 1, pero como la búsqueda empieza desde el 2, 
# encuentra la segunda 'a' en el índice 4.


# Uso para encontrar todas las ocurrencias:

# Puedes usar find() en un bucle para localizar todas las apariciones 
# de una subcadena.

# Suponiendo que el texto se refiere a una cadena larga como esta:
# "This is a test string with the word 'the' appearing multiple times.
# Let's find all occurrences of the word 'the' in this text."

# Y el código similar a:
# text = "This is a test string with the word 'the' appearing multiple times. 
# Let's find all occurrences of the word 'the' in this text."
# pos = text.find("the")
# while pos != -1:
#     print(pos)
#     pos = text.find("the", pos + 1)

# Output:
# 15 (índice de la primera 'the')
# 80 (índice de la segunda 'the')
# 198 (índice de la tercera 'the')
# 221 (índice de la cuarta 'the')
# 238 (índice de la quinta 'the')


# Variante de tres parámetros (búsqueda dentro de un rango):
# El tercer argumento define el índice final (exclusivo) hasta donde buscar.

print('kappa'.find('a', 0, 1)) # Busca 'a' entre el índice 0 (inclusive) y 1 (exclusivo)
# Output: -1 (La 'a' en el índice 1 está fuera del límite de búsqueda 
# de '0' hasta '1' (excluyendo el '1'))

print('kappa'.find('a', 1, 2)) # Busca 'a' entre el índice 1 (inclusive) y 2 (exclusivo)
# Output: 1 (La 'a' está en el índice 1)


# El método isalnum()

"""
    El método isalnum() es una pregunta simple: ¿la cadena está compuesta solo 
    por caracteres alfanuméricos? Es decir, solo letras (a-z, A-Z) y dígitos 
    (0-9). Si hay cualquier otro carácter (espacios, símbolos, puntuación) o 
    si la cadena está vacía, devuelve False.
"""

print('alpha123'.isalnum())  # True (solo letras y dígitos)
print('alpha'.isalnum())     # True (solo letras)
print('123'.isalnum())       # True (solo dígitos)
print('alpha 123'.isalnum()) # False (contiene un espacio)
print('alpha!'.isalnum())    # False (contiene un signo de exclamación)
print(''.isalnum())          # False (cadena vacía)
print(' '.isalnum())      # False (espacio)
print('!'.isalnum())      # False (símbolo)
print('2024'.isalnum())   # True (solo dígitos)


# El método isalpha()

"""
    isalpha() es aún más estricto que isalnum(): comprueba si la cadena 
    contiene solo letras. Si hay dígitos, espacios o cualquier otro símbolo, 
    devolverá False.
""" 

print('alpha'.isalpha())   # True
print('alpha123'.isalpha())# False (contiene dígitos)


# El método isdigit()

"""
    Como su nombre lo indica, isdigit() verifica si la cadena está compuesta 
    solo por dígitos (0-9). Cualquier otro carácter, incluyendo espacios o 
    letras, resultará en False.
"""

print('123'.isdigit())     # True
print('123a'.isdigit())    # False


# El método islower()

"""
    islower() es un método de verificación de caso: retorna True si todas las 
    letras en la cadena están en minúsculas. Si la cadena no contiene letras 
    o tiene al menos una letra en mayúscula, devuelve False.
"""

print('alpha'.islower())   # True
print('Alpha'.islower())   # False


#  El método isspace()

"""
    Este método verifica si la cadena consiste solamente en espacios en blanco. 
    Esto incluye el carácter de espacio, tabulaciones (\t), saltos de línea 
    (\n), etc. Si hay cualquier otro carácter que no sea un espacio en blanco, 
    devuelve False.
"""

print(' '.isspace())      # True
print('\t\n'.isspace())   # True
print(' a'.isspace())     # False


# El método isupper()

"""
    Similar a islower(), isupper() retorna True si todas las letras en la cadena 
    están en mayúsculas. Si la cadena no contiene letras o tiene al menos una letra 
    en minúscula, devuelve False.
"""

print('ALPHA'.isupper())   # True
print('Alpha'.isupper())   # False
print('alpha'.isupper())   # False


# El método join()

"""
    El método join() es un poco más avanzado, ya que se invoca desde la cadena que 
    actuará como separador entre los elementos. Su función es unir todos los elementos 
    de una lista (o tupla) de cadenas en una sola cadena, utilizando la cadena desde 
    la que se llama join() como el "pegamento" entre ellos. Si algún elemento de la 
    lista no es una cadena, se generará una excepción TypeError.
"""

my_list = ["omicron", "pi", "rho"]
separator = ","
print(separator.join(my_list)) # Output: omicron,pi,rho

# Aquí, la coma , se usa para unir "omicron", "pi" y "rho".


# 12 El método lower()
"""
    El método lower() es el opuesto a upper(): crea una copia de la cadena original 
    y convierte todas las letras mayúsculas a sus equivalentes en minúsculas. Si no 
    hay letras mayúsculas, la cadena se devuelve sin cambios.
"""

print("SIGMA=60".lower()) # Output: sigma=60

# El método lstrip()

"""
    lstrip() es como una "tijera" para el lado izquierdo: elimina los espacios en 
    blanco (o un conjunto específico de caracteres) del principio de la cadena.
"""

# Variante sin parámetros: Elimina espacios en blanco iniciales.

print("[" + "   tau ".lstrip() + "]")
# Output: [tau ] (Los corchetes son solo para visualizar los límites; el resultado es "tau ")

"""
    Variante con un parámetro: Elimina cualquier carácter contenido en el argumento 
    del principio de la cadena, de forma repetitiva mientras encuentre esos caracteres.
"""

print("cisco.com".lstrip("cisco."))
# Output: m (Elimina 'c', 'i', 's', 'c', 'o', '.', 'c', 'o' del inicio)

print("pythoninstitute.org".lstrip("yth"))
# Output: oninstitute.org

"""
    Este último ejemplo puede ser sorprendente. lstrip("yth") no significa que quita "yth" 
    como bloque, sino que quita cualquier 'y', 't', o 'h' del inicio de la cadena, de forma 
    continua, hasta que encuentra un carácter que no está en el conjunto. La 'p' en 
    "pythoninstitute.org" no está en "yth", por lo que la remoción se detiene ahí.
"""


# El método replace()

"""
    El método replace() es para sustituciones: devuelve una copia de la cadena donde todas 
    las apariciones de una subcadena han sido reemplazadas por otra.
"""

# Variante de dos parámetros:

print("Apple juice".replace(" juice", "")) # Output: Apple

# Aquí, " juice" se reemplaza por una cadena vacía, lo que efectivamente lo elimina.

print("www.pythoninstitute.org".replace("www", "http://www.")) # Output: http://www.pythoninstitute.org

print("This is it!".replace("is", "are")) # Output: Thare are it!

print("Apple".replace("A", "B")) # Este ejemplo no está en el texto pero ilustra el punto
# Output: Bpple

# Variante de tres parámetros:
# El tercer argumento es un número entero que limita el número de reemplazos que se realizarán.

print("This is it!".replace(" is", " are", 1)) # Output: Thare is it!

# Solo la primera ocurrencia de " is" se reemplaza por " are".


# El método rfind()

"""
    Los métodos rfind() son como find(), pero comienzan su búsqueda desde el final de la cadena 
    hacia el principio (r por "reversa"). Devuelven el índice de la primera ocurrencia encontrada 
    desde la derecha, o -1 si no la encuentran.
"""

print("theta".rfind("a")) # Busca 'a' desde la derecha. La última 'a' está en el índice 4.
# Output: 4

print("theta".rfind("x")) # 'x' no está en la cadena.
# Output: -1

print("tau sigma".rfind("sigma")) # 'sigma' empieza en el índice 4.
# Output: 4


# El método rstrip()

"""
    rstrip() es el "gemelo" de lstrip(): elimina los espacios en blanco (o un conjunto específico 
    de caracteres) del final (derecha) de la cadena.
"""

print("[" + " upsilon ".rstrip() + "]") # Output: [ upsilon] (Los corchetes son solo para visualizar 
# los límites; el resultado es " upsilon")

print("cisco.com".rstrip(".com")) # Output: cis (Elimina '.', 'c', 'o', 'm' del final, de forma continua)


# El método split()

"""
    split() es fundamental para analizar texto: divide una cadena en una lista de subcadenas. 
    Por defecto, utiliza los espacios en blanco (incluyendo tabulaciones y saltos de línea) como 
    delimitadores y no los incluye en la lista resultante. Si la cadena original está vacía, 
    la lista resultante también lo estará.
"""

print("phi       chi\npsi".split()) # Output: ['phi', 'chi', 'psi']

# Aquí, múltiples espacios y un salto de línea son tratados como un solo delimitador.

"""
    Nota: La operación inversa (unir elementos de una lista en una cadena) se realiza con el método join().
"""

# El método startswith()

"""
    Este método es el "espejo" de endswith(): comprueba si una cadena dada comienza con una subcadena 
    específica. Devuelve True o False según el resultado.
"""

print("omega".startswith("meg")) # Output: False
print("omega".startswith("om")) # Output: True


# El método strip()

"""
    strip() es una combinación de lstrip() y rstrip(): crea una nueva cadena eliminando todos los 
    espacios en blanco iniciales y finales (o un conjunto específico de caracteres).
"""

print("[" + "   aleph   ".strip() + "]") # Output: [aleph]

# Se eliminaron los espacios al principio y al final.


# El método swapcase()

"""
    swapcase() es para cambiar el "caso" de las letras: crea una nueva cadena donde las letras en 
    mayúscula se convierten en minúsculas y viceversa. Cualquier otro carácter (números, símbolos) 
    permanece sin cambios.
"""

print("Yo solo sé que no sé nada".swapcase()) # Output: yO SOLO SÉ QUE NO SÉ NADA


# El método title()

"""
    El método title() es útil para dar formato de título a una cadena: cambia la primera letra de 
    cada palabra a mayúsculas y convierte todas las demás letras de esa palabra a minúsculas.
"""

print("Yo solo sé que no sé nada. Parte 1.".title()) # Output: Yo Solo Sé Que No Sé Nada. Parte 1.


# El método upper()

"""
    Finalmente, upper() es el método que hace una copia de la cadena de origen y reemplaza todas 
    las letras minúsculas con sus equivalentes en mayúsculas, devolviendo la nueva cadena.
"""

print("Yo solo sé que no sé nada. Parte 2.".upper()) # Output: YO SOLO SÉ QUE NO SÉ NADA. PARTE 2.


# Ejercicios:

# Pregunta 1 - ¿Cuál es el resultado esperado del siguiente código?

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

# Respuesta: ABC123xyx


# Pregunta 2 - ¿Cuál es el resultado esperado del siguiente código?

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
print(f"\n{s2[-2]}")

# Respuesta: [¿Dónde, están, las, nieves, de, antaño?], Imprime: de


# Pregunta 3: ¿Cuál es el resultado esperado del siguiente código?

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s) 

# Respuesta: Where*are*the*snows?


# Pregunta 4: ¿Cuál es el resultado esperado del siguiente código?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)

# Respuesta: 
# primera pasada: "It is either hard or impossible"
# segunda pasada: "It is either hard or possible"
