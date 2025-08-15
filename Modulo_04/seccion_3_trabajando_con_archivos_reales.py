# Trabajando con archivos reales

"""
    En esta sección aprenderás a manipular archivos de texto y binarios:
    - Cómo abrir, leer y contar caracteres/líneas.
    - Formas eficientes de lectura (carácter, línea, todo de golpe).
    - Cómo escribir en archivos de texto.
    - Qué es un bytearray y cómo usarlo con datos binarios.
    - Cómo copiar archivos completos.
    Nota: todos los ejemplos usan manejo de excepciones para evitar
    que tu programa explote si el archivo no existe o no tienes permisos.
"""

from os import strerror
import sys

# Procesamiento de archivos de texto:

"""
    Ejemplo básico de lectura carácter por carácter desde un archivo
    y conteo total de caracteres.

    Ventaja:
        - Control total sobre cada carácter leído.
    Desventaja:
        - Es la forma más lenta para archivos grandes.
"""

try:
    stream = open('./Modulo_04/Archivos/text.txt', 'rt', encoding='utf-8')  # 'rt' = read text
    counter = 0
    char = stream.read(1)  # lee un solo carácter
    while char != '':
        print(char, end='')   # end='' evita añadir saltos de línea extra
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# Lectura de todo el archivo de una sola vez

"""
    Usar read() sin argumentos carga todo el contenido en memoria.

    Ventaja:
        - Rápido y sencillo.
    Desventaja:
        - No apto para archivos gigantes, podría agotar la memoria.
"""

try:
    stream = open('./Modulo_04/Archivos/text.txt', 'rt', encoding='utf-8')
    content = stream.read()
    counter = 0
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# readline(): Lectura línea por línea

"""
    Lee una línea completa cada vez, ideal para procesar texto estructurado.
    Útil si no necesitas cargar todo el archivo de golpe.
"""

try:
    stream = open('./Modulo_04/Archivos/text.txt', 'rt', encoding='utf-8')
    ccounter = lcounter = 0
    line = stream.readline()
    while line != '':
        print(line, end='')
        ccounter += len(line)
        lcounter += 1
        line = stream.readline()
    stream.close()
    print("\nCaracteres en el archivo:", ccounter)
    print("Líneas en el archivo:", lcounter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# readlines(): Lectura como lista de líneas

"""
    readlines() lee varias líneas y las devuelve como lista.
    Si pasas un número como argumento, intentará no superar ese número de bytes.
"""

try:
    stream = open('./Modulo_04/Archivos/text.txt', 'rt', encoding='utf-8')
    ccounter = lcounter = 0
    for line in stream.readlines(15):  # Búfer pequeño para ejemplo
        for char in line:
            print(char, end='')
            ccounter += 1
        lcounter += 1
    stream.close()
    print("\nCaracteres en el archivo:", ccounter)
    print("Líneas en archivo:", lcounter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# Iteración directa sobre el objeto archivo

"""
    El propio objeto archivo es iterable, lo que permite recorrerlo línea por línea.
    Es la forma más pythonica y eficiente para leer texto secuencialmente.
"""

try:
    stream = open('./Modulo_04/Archivos/text.txt', 'rt', encoding='utf-8')
    ccounter = lcounter = 0
    for line in stream:
        print(line, end='')
        ccounter += len(line)
        lcounter += 1
    stream.close()
    print("\nCaracteres en el archivo:", ccounter)
    print("Líneas en el archivo:", lcounter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# Escritura en archivos de texto con write()

"""
    Abrir un archivo con 'wt' (write text) lo crea o lo sobrescribe.
    Usar write() no añade saltos de línea automáticamente, hay que incluirlos.
"""

try:
    file = open('./Modulo_04/Archivos/newtext.txt', 'wt', encoding='utf-8')
    for i in range(10):
        file.write(f"línea #{i + 1}\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# Ejemplo: enviar texto a stderr

"""
    sys.stderr es un flujo de salida para errores o mensajes urgentes.
    Va a la consola, separado de la salida normal (stdout).
"""
sys.stderr.write("Mensaje de Error\n")


# ¿Qué es un bytearray?

"""
    bytearray es una secuencia mutable de valores entre 0 y 255.
    Perfecto para manipular datos binarios como imágenes, audio o ejecutables.
"""

data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 - i  # Asigna valores descendentes

for b in data:
    print(hex(b))  # Muestra cada valor en hexadecimal


# Escritura de bytearray en un archivo binario

"""
    Al abrir en modo 'wb' (write binary) se escribe exactamente lo que hay en memoria.
"""
try:
    bf = open('./Modulo_04/Archivos/file.bin', 'wb')
    data = bytearray((10, 9, 8, 7, 6, 5, 4, 3, 2, 1))
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# Lectura de bytes desde un archivo binario

"""
    readinto() escribe directamente los bytes leídos en un bytearray ya creado.
"""
try:
    bf = open('./Modulo_04/Archivos/file.bin', 'rb')
    data = bytearray(10)
    bf.readinto(data)
    bf.close()
    print(list(data))
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# Lectura parcial usando read()

"""
    Puedes leer solo una parte del archivo binario especificando el número de bytes.
"""
try:
    bf = open('./Modulo_04/Archivos/file.bin', 'rb')
    chunk = bf.read(5)  # Lee 5 bytes
    bf.close()
    print(list(chunk))
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))



# Copiando archivos

"""
    Copia el contenido de un archivo binario a otro usando un búfer.
    El tamaño del búfer (en bytes) afecta el rendimiento:
        - Muy pequeño: lento por muchas operaciones de E/S.
        - Muy grande: consume más memoria pero reduce llamadas de E/S.
"""

# Comentado porque requiere interacción
# srcname = input("Ingresa el nombre del archivo fuente: ")
# try:
#     src = open(srcname, 'rb')
# except IOError as e:
#     print("No se puede abrir archivo fuente:", strerror(e.errno))
#     exit(e.errno)
#
# dstname = input("Ingresa el nombre del archivo de destino: ")
# try:
#     dst = open(dstname, 'wb')
# except IOError as e:
#     print("No se puede crear archivo de destino:", strerror(e.errno))
#     src.close()
#     exit(e.errno)
#
# buffer = bytearray(65536)  # 64 KB
# total = 0
# read_bytes = src.readinto(buffer)
# while read_bytes > 0:
#     dst.write(buffer[:read_bytes])
#     total += read_bytes
#     read_bytes = src.readinto(buffer)
#
# print(total, "byte(s) copiado(s)")
# src.close()
# dst.close()


# Laboratorio:

# Ejercicio 01 - Histograma de frecuencia de caracteres

"""

    Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos 
    saber con qué frecuencia aparece cada letra en el texto. Tal análisis puede 
    ser útil en criptografía, por lo que queremos poder hacerlo en referencia 
    al alfabeto latino.

    Tu tarea es escribir un programa que:

    - Pida al usuario el nombre del archivo de entrada.
    - Lea el archivo (si es posible) y cuente todas las letras latinas (las 
      letras mayúsculas y minúsculas se tratan como iguales).
    - Imprima un histograma simple en orden alfabético (solo se deben presentar 
      recuentos distintos de cero).
    
    Crea un archivo de prueba para tu código y verifica si tu histograma contiene 
    resultados válidos.
"""

# Suponiendo que el archivo de prueba contiene solo una línea con: aBc
# Nombre archivo: samplefile.txt

# El resultado esperado debería verse de la siguiente manera:

"""
    a -> 1
    b -> 1
    c -> 1
"""

# Consejo: Creemos que un diccionario es un medio perfecto de recopilación de datos
# para almacenar los recuentos. Las letras pueden ser las claves mientras que los 
# contadores pueden ser los valores.

# Desarrollo:

import errno
import string

path = "./Modulo_04/Archivos/"

try:
    nombre_archivo = input("Ingrese el nombre del archivo con su extención: ").lower().strip()
    
    if len(nombre_archivo) > 0:
        file = path + nombre_archivo
    else:
        raise Exception("El campo no puede estar vacio.")
    
    abrir_archivo = open(file, 'rt', encoding='utf-8')
    conteo_caracteres = {letra: 0 for letra in string.ascii_lowercase}
    # O tambien: {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

    for char in abrir_archivo.read().lower():
        if char in conteo_caracteres:
            conteo_caracteres[char] += 1

    abrir_archivo.close()

    for char in sorted(conteo_caracteres):
        if conteo_caracteres[char] > 0:
            print(f'{char} -> {conteo_caracteres[char]}')

except IOError as e:
    print(f'Error: {errno.errorcode[e.errno]}\nDescripción: {e.strerror}\nRuta: {e.filename}')
except Exception as e:
    print("Error:", e)


# Ejercicio 02 - Histograma de frecuencia de caracteres ordenado

"""
    El código anterior necesita ser mejorado. Está bien, 
    pero tiene que ser mejor.

    Tu tarea es hacer algunas enmiendas, que generen los 
    siguientes resultados:

    El histograma de salida se ordenará en función de la 
    frecuencia de los caracteres (el contador más grande 
    debe presentarse primero).

    El histograma debe enviarse a un archivo con el mismo
    nombre que el de entrada, pero con la extensión 
    '.hist' (debe concatenarse con el nombre original).
"""

# Suponiendo que el archivo de prueba contiene solo una
# línea con: cBabAa

# El resultado esperado debería verse de la siguiente
# manera: 

"""
    a -> 3
    b -> 2
    c -> 1
"""

# Consejo: Emplea una función lambda para cambiar el ordenamiento.

# Desarrollo:

import errno

path = './Modulo_04/Archivos/'
input_extension = '.txt'
output_extension = '.hist'

input_file = None
output_file = None

try: 
    file_name = input('Ingrese el nombre del archivo: ').strip().lower()
   
    if len(file_name) == 0:
        raise Exception('El campo no puede estar vacío.')
    
    input_file = open(path+file_name+input_extension, 'r', encoding='utf-8')
    character_counter = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
    
    for chr in input_file.read().lower():
        if chr in character_counter:
            character_counter[chr] += 1
    
    output_file = open(path + file_name + output_extension, 'w', encoding='utf-8')

    for chr in sorted(character_counter.keys(), key=lambda key : character_counter[key], reverse=True):
        value = character_counter[chr]
        if value > 0:
            output_file.write(f'{chr} -> {value}\n')
    

except IOError as e:
    print(f'Error: {errno.errorcode[e.errno]}\nDescripción: {e.strerror}\nRuta: {e.filename}')
except Exception as e:
    print(f'Error: {e}')
finally:
    if input_file:
        input_file.close()
    if output_file:
        output_file.close()

