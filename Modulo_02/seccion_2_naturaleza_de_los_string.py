# La naturaleza de las cadenas en Python

# --- Cadenas: un breve repaso ---
# Las cadenas en Python son inmutables, es decir, no se pueden modificar una vez creadas.
# La función len() devuelve la longitud de la cadena.

print(len('hi'))          # 2
print(len(''))            # 0

# El carácter de escape \ no se cuenta como carácter visible.

i_am = 'I\'m'
print(len(i_am))          # 3


# ---  Cadenas multilínea ---
# Las cadenas multilínea se delimitan con tres comillas simples o dobles.
# Permiten incluir saltos de línea sin errores de sintaxis.

multiline = '''Línea #1
Línea #2'''
print(len(multiline))     # 17 (incluye el carácter invisible '\n')


# --- Operaciones con cadenas ---
# Las cadenas se pueden concatenar (+) y replicar (*).

str1 = 'a'
str2 = 'b'
print(str1 + str2)        # ab
print(str2 + str1)        # ba
print(str1 * 5)           # aaaaa
print(4 * str2)           # bbbb

# También se pueden usar operadores compuestos: += y *=
str1 += 'b'
print(str1)               # ab
str2 *= 2
print(str2)               # bb


# --- Funciones ord() y chr() ---
# ord() convierte un carácter en su punto de código Unicode.
# chr() convierte un punto de código en su carácter correspondiente.

print(ord('a'))           # 97
print(ord(' '))           # 32
print(chr(97))            # a
print(chr(945))           # α

# Estas expresiones siempre son verdaderas:

x = 'z'
print(chr(ord(x)) == x)
print(ord(chr(65)) == 65)


# --- Cadenas como secuencias ---
# Las cadenas permiten indexación e iteración.

s = "silly walks"
print(s[0])               # s
print(s[-1])              # s

for char in s:
    print(char, end=' ')  # s i l l y   w a l k s
print()


# --- Rebanadas ---
# Se pueden obtener subcadenas usando slicing.

s = "abcdefg"
print(s[1:3])             # bc
print(s[4:7])             # efg
print(s[:3])              # abc
print(s[-3:])             # efg


# --- Operadores in y not in ---
# Permiten verificar si una subcadena está (o no) en una cadena.

print("walk" in "silly walks")       # True
print("fly" in "silly walks")        # False
print("walk" not in "silly walks")   # False


# --- Inmutabilidad ---
# No se puede modificar una cadena como si fuera una lista.

alphabet = "abc"
# del alphabet[0]        # Error
# alphabet.append("d")   # Error
# alphabet.insert(0, "x")# Error

# Se debe crear una nueva cadena si se quiere modificar.
alphabet = "bcdef"
alphabet = "a" + alphabet + "z"
print(alphabet)           # abcdefz


# --- Más operaciones con cadenas ---

# min() y max() retornan el carácter con menor o mayor valor Unicode.
print(min("ABC"))                        # A
print(max("Los Caballeros Que Dicen 'Ni!'"))  # z

# index() retorna la primera posición de una subcadena.
text = "abracadabra"
print(text.index("b"))      # 1
print(text.index("c"))      # 4

# list() convierte la cadena en lista de caracteres.
print(list("abcabc"))       # ['a', 'b', 'c', 'a', 'b', 'c']

# count() cuenta la cantidad de veces que aparece un carácter o subcadena.
print("abcabc".count("a"))  # 2
print("abcabc".count("z"))  # 0


# Ejercicios:

# Pregunta 1 - ¿Cúal es la longitud de la siguiente cadena asumiendo que 
# no hay espacios en blanco entre las comillas?

multilinea = """
"""

print(len(multilinea)) # Imprime: 1

"""
    Respuesta:

    La longitud es 1, porque la cadena contiene un salto de línea (\n) implicito.
"""

# Pregunta 2 - ¿Cúal es el resultado esperado del siguiente código?

s = 'yesteryears'
the_list = list(s)
print(the_list[3:6]) # Impirme: ["t", "e", "r"]

# Pregunta 3 - ¿Cuál es el resultado esperado del siguiente código?

for ch in "abc":
    print(chr(ord(ch) + 1), end = '')

"""
    Respuesta:

    ASCII
    chr(97 + 1) = b
    chr(98 + 1) = c
    chr(99 + 1) = d

    Imprime: bcd
"""