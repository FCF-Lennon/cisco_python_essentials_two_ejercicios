# 1 - El Cifrado César: encriptando un mensaje

# Este es el primero de cuatro programas diseñados para enseñarte procesamiento de cadenas en Python. 
# En este caso, aprenderás el Cifrado César, una técnica muy antigua que desplaza cada letra del mensaje 
# una posición hacia adelante en el alfabeto.

""" 
    Ejemplo:

    "A" se convierte en "B",
    "B" se convierte en "C",
    "Z" se convierte en "A".

    Supuestos del programa:
    
    - Solo se procesan letras latinas (sin espacios ni dígitos).
    - Todo el texto estará en mayúsculas. 
"""

# Análisis línea por línea:

text = input("Ingresa tu mensaje: ") 
cipher = ''                          

for char in text:                    
    if not char.isalpha():      
        continue                     
    char = char.upper()             
    code = ord(char) + 1            
    if code > ord('Z'):            
        code = ord('A')            
    cipher += chr(code)             
print(cipher)                       

# Este pequeño programa:

""" 
    1. Recibe un mensaje desde la consola.
    2. Ignora cualquier carácter que no sea una letra.
    3. Convierte cada letra a mayúsculas.
    4. Desplaza la letra una posición en el alfabeto.
    5. Si llega a "Z", vuelve a "A".
    6. Agrega la letra cifrada al resultado.
    7. Imprime el resultado final. 
"""

# Ejemplo de ejecución:

"""
    Entrada: AVE CAESAR
    Salida esperada: BWFDBFTBS

"""


# 2 - El Cifrado César: descifrando un mensaje

# Ahora que entiendes el cifrado, la operación inversa es directa: simplemente resta 1 
# al valor ASCII de cada letra. Aquí está el código sin comentarios:

text = input("Ingresa tu mensaje cifrado: ")
decipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    decipher += chr(code)
print(decipher)

# Puedes probarlo usando el mensaje cifrado del ejemplo anterior (BWFDBFTBS) y verás que 
# el resultado será el mensaje original: AVECAESAR.

""" 
    (Aunque no se explica el código línea por línea, se puede observar que simplemente resta 
    uno al valor ASCII de cada letra. Si llega antes de 'A', vuelve a 'Z')
 """


# 3 - El Procesador de Números

# Este programa te permite sumar múltiples números ingresados en una sola línea. Lo hace de forma robusta, 
# usando try-except para prevenir errores si hay entradas inválidas.

# Código explicado línea a línea:

line = input("Ingresa los números separados por espacios: ")  
strings = line.split()  

if not strings:
    print("No ingresaste ningún número.")
else:
    total = 0.0                                              
    try:                                                          
        for substr in strings:                                   
            total += float(substr)                                
        print("La suma es:", total)                             
    except:                                                       
        print(substr, "no es un número válido.")                  

"""
    Ejemplo de entrada válida: 12.5 8.3 3.2
    Salida esperada: La suma es: 24.0
"""

# Observación: si el usuario no escribe nada, la salida será engañosa (dará La suma es: 0.0). 
# Puedes mejorar el código verificando si la lista strings está vacía antes de comenzar el bucle.

# 4 - Validador IBAN

# Este programa implementa una versión simplificada del validador IBAN, usado en Europa para verificar 
# si un número de cuenta bancaria es válido.

# Pasos simplificados del algoritmo (según el estándar):

""" 
    1. Quitar los espacios del IBAN ingresado.
    2. Mover los 4 primeros caracteres al final.
    3. Convertir letras a números: A = 10, B = 11, ..., Z = 35.
    4. Convertir todo a un número largo y calcular iban % 97.
    5. Si el resultado es 1, entonces el número es válido.
"""

# Código explicado:

iban = input("Ingresa el IBAN, por favor: ")     # Línea 3
iban = iban.replace(' ', '')                     # Línea 4

if not iban.isalnum():                           # Línea 6
    print("El IBAN contiene caracteres no válidos.")  # Línea 7
elif len(iban) < 15:                             # Línea 8
    print("El IBAN es demasiado corto.")         # Línea 9
elif len(iban) > 31:                             # Línea 10
    print("El IBAN es demasiado largo.")         # Línea 11
else:
    iban = (iban[4:] + iban[0:4]).upper()        # Línea 13
    iban2 = ''
    for ch in iban:                              # Línea 15
        if ch.isdigit():                         # Línea 16
            iban2 += ch                          # Línea 17
        else:
            iban2 += str(10 + ord(ch) - ord('A'))  # Línea 19
    iban_int = int(iban2)                        # Línea 20
    if iban_int % 97 == 1:                       # Línea 21
        print("El IBAN es válido.")              # Línea 22
    else:
        print("El IBAN no es válido.")           # Línea 24


# Datos de prueba válidos:

""" 
    Nota técnica:
    - ord(ch) obtiene el valor ASCII de la letra.
    - ord('A') = 65, entonces ord('B') - ord('A') = 1 y 10 + 1 = 11 → correcto.
"""

"""
    Datos de prueba válidos:

    🇬🇧 Inglaterra: GB72 HBZU 7006 7212 1253 00
    🇫🇷 Francia: FR76 30003 03620 00020216907 50
    🇩🇪 Alemania: DE02100100100152517108
"""

# Puedes probarlos tal cual, y también modificar un dígito para ver cómo el programa detecta el error.
    

# Laboratorio:

# Ejercicio 1 - Mejorando el Cifrado César

""" 
    Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el 
    código que te mostramos recientemente.

    El cifrado César original cambia cada carácter por otro a se convierte en b, z se 
    convierte en a, y así sucesivamente. Hagámoslo un poco más difícil y permitamos 
    que el valor desplazado provenga del rango 1..25.

    Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas 
    permanecerán en minúsculas) y todos los caracteres no alfabéticos deben permanecer 
    intactos.

    Tu tarea es escribir un programa el cual:

        - Le pida al usuario una línea de texto para encriptar.
        - Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: 
          debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y 
          no dejes que los datos incorrectos te engañen!).
        - Imprime el texto codificado.
          Prueba tu código utilizando los datos que te proporcionamos. 
"""

# Datos de prueba: 

""" 
    Entrada de muestra: abcxyzABCxyz 1232
    Salida de muestra: cdezabCDEzab 123

    Entrada de muestra: The die is cast25
    Salida de muestra: Sgd chd hr bzrs 
"""

# Respuesta:

# Laboratorio:

# Ejercicio 1 - Mejorando el Cifrado César

"""
Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el 
código que te mostramos recientemente.

El cifrado César original cambia cada carácter por otro (a se convierte en b, z en a, etc.).
Hagámoslo más interesante: ahora, el valor de desplazamiento será un número del 1 al 25.

Además:
- El código debe mantener la distinción entre mayúsculas y minúsculas.
- Los caracteres no alfabéticos deben permanecer intactos.

Tu tarea:
    - Solicitar al usuario una línea de texto para encriptar.
    - Solicitar un valor de desplazamiento entre 1 y 25 (validarlo).
    - Imprimir el texto codificado.

Prueba tu código con estos datos de prueba.
"""

# Datos de prueba:

"""
Entrada: abcxyzABCxyz 123
Salida esperada: cdezabCDEzab 123

Entrada: The die is cast25
Salida esperada: Sgd chd hr bzrs
"""

# --- Código de respuesta ---

# Pedir el texto a encriptar
text = input("Ingresa un mensaje: ")

# Validar el valor de desplazamiento
while True:
    try:
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("¡Valor de cambio fuera de rango!")
    except ValueError:
        print("¡Debes ingresar un número entero válido!")

cipher = ''

for char in text:
    if char.isalpha():
        # Determinar el código base según si es mayúscula o minúscula
        first = ord('A') if char.isupper() else ord('a')
        # Aplicar desplazamiento circular dentro del alfabeto
        code = (ord(char) - first + shift) % 26 + first
        cipher += chr(code)
    else:
        # Mantener caracteres no alfabéticos
        cipher += char

print("Texto encriptado:", cipher)


# Ejercicio 2 - Palíndromos

"""
    ¿Sabes qué es un palíndromo?

    Es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. Por ejemplo, 
    "kayak" es un palíndromo, mientras que "leal" no lo es.

    Tu tarea es escribir un programa que:

    Le pida al usuario algún texto.
    Compruebe si el texto introducido es un palíndromo e imprima el resultado.

    Nota:

    - Supón que una cadena vacía no es un palíndromo.
    - Trata a las letras mayúsculas y minúsculas como iguales.
    - Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
    - Existe más de una solución correcta: intenta encontrar más de una.
"""

# Prueba tu código utilizando los datos que te proporcionamos:

# Datos de prueba:

"""
    Entrada de muestra: Ten animals I slam in a net
    Salida de muestra: Es un palíndromo

    Entrada de muestra: Eleven animals I slam in a net
    Salida de muestra: No es un palíndromo
"""

# --- Código de respuesta ---

text = input("Ingrese un texto: ").lower()

# solo permite letras con tilde, ñ, etc

text = input("Ingrese un texto: ").lower()

# Filtrar solo letras (permite letras con tilde, ñ, etc.)
filtered = [char for char in text if char.isalpha()]

if len(text) and filtered == filtered[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


# o tambien:

"""
    text = input("Ingresa un texto: ")

    # Quitar todos los espacios...
    text = text.replace(' ','')

    # ... y revisar si la palabra es igual en ambos sentidos
    if len(text) > 1 and text.upper() == text[::-1].upper():
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
"""


# Ejercicio 3 - Anagramas

"""
    Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, 
    usando todas las letras originales exactamente una vez. Por ejemplo, las frases "rail safety" 
    y "fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.

    Tu tarea es escribir un programa que:

    - Le pida al usuario dos textos por separado.
    - Compruebe si los textos ingresados son anagramas e imprima el resultado.
    
    Nota:

    Supongamos que dos cadenas vacías no son anagramas.
    Tratar a las letras mayúsculas y minúsculas como iguales.
    Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
"""

# Prueba tu código utilizando los datos que te proporcionamos.

# Datos de prueba:

"""
    Entrada de muestra: Listen y Silent
    Salida de muestra: Anagramas

    Entrada de muestra: modern y norman
    Salida de muestra: No son anagramas
"""

# --- Código de respuesta ---

text1 = input("Imgrese el primer texto: ").upper().replace(" ", "")
text2 = input("Imgrese el segundo texto: ").upper().replace(" ", "")

if text1 and text2:
    if sorted(text1) == sorted(text2):
        print("Anagramas")
    else:
        print("No son anagramas")
else:
    print("No son anagramas")


# o tambien:

"""
    str_1 = input("Ingresa la primera cadena: ")
    str_2 = input("Ingresa la segunda cadena: ")

    strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
    strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
    if len(strx_1) > 0 and strx_1 == strx_2:
        print("Anagramas")
    else:
        print("No son anagramas")
"""

# Ejercicio 04 - El Dígito de la Vida

"""
    Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. Es simple: 
    solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, se debe 
    repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

    - 1 Enero 2017 = 2017 01 01
    - 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
    - 1 + 2 = 3

    3 es el dígito que buscamos y encontramos.

    Tu tarea es escribir un programa que:

    - Le pregunté al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, 
    el orden de los dígitos no importa).
    - Dé como salida El Dígito de la Vida para la fecha ingresada.
""" 

# Prueba tu código utilizando los datos que te proporcionamos.

# Datos de prueba:

"""
    Entrada de muestra: 19991229
    Salida de muestra: 6

    Entrada de muestra: 20000101
    Salida de muestra: 4
"""


# --- Código de respuesta ---

fecha = input("Ingrese su fecha de nacimiento (cualquier formato con 8 dígitos): ")

# Eliminar todo lo que no sea dígito
solo_digitos = ''.join(c for c in fecha if c.isdigit())

if len(solo_digitos) != 8:
    print("Formato de fecha inválido. Debe contener exactamente 8 dígitos.")
else:
    while len(solo_digitos) > 1:
        solo_digitos = str(sum(int(n) for n in solo_digitos))
    print("Tu Dígito de la Vida es:", solo_digitos)

# o tambien:

""" date = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
if len(date) != 8 or not date.isdigit():
    print("Formato de fecha inválida.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Tu Dígito de la Vida es: " + date)
 """
