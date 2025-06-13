# Cadenas en acción

# Comparando cadenas

# En Python, las cadenas se pueden comparar utilizando los mismos operadores que usamos 
# con números:

# ==   !=   >   >=   <   <=

# Sin embargo, hay un detalle importante: Python no entiende el significado de las palabras, 
# solo compara carácter por carácter, usando el valor de su código ASCII o Unicode. Esto puede 
# dar lugar a resultados que parecen extraños si no estás consciente de cómo funciona.

# Ejemplos simples:

'alpha' == 'alpha'   # True, porque son exactamente iguales
'alpha' != 'Alpha'   # True, porque la "a" minúscula no es igual a la "A" mayúscula

# Si comparamos dos cadenas distintas, Python analiza el primer carácter que no coincida entre 
# ambas. Si una cadena es más corta pero idéntica al principio, Python considera mayor a la 
# cadena más larga:

'alpha' < 'alphabet'  # True, porque 'alphabet' tiene más letras y empieza igual

# Además, Python distingue mayúsculas de minúsculas. Las letras mayúsculas tienen un valor 
# menor que las minúsculas:

'beta' > 'Beta'   # True, porque 'b' minúscula tiene un valor mayor que 'B' mayúscula
# Ahora bien, incluso si una cadena solo contiene números, Python la tratará como cadena, 
# no como número:

print('10' == 10)  # False, uno es cadena, el otro es número
print('10' != 10)  # True, por la misma razón

# Y si intentas usar otros operadores de comparación entre una cadena y un número (como >), 
# Python lanzará un error:

print('10' > 10)

# TypeError: '>' not supported between instances of 'str' and 'int'

# Ordenamiento

# Ordenar cadenas es una tarea común, por ejemplo, en listas de nombres o ciudades. En Python, 
# hay dos formas principales de ordenar listas de cadenas:

# Usando sorted()

greek = ['omega', 'alpha', 'pi', 'gamma']
print(greek)                    # ['omega', 'alpha', 'pi', 'gamma']
print(sorted(greek))           # ['alpha', 'gamma', 'omega', 'pi']

# sorted() no cambia la lista original, devuelve una nueva lista ordenada.

# Usando sort()

second_greek = ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()
print(second_greek)            # ['alpha', 'gamma', 'omega', 'pi']

# sort() modifica directamente la lista original.

# Cadenas versus números

# A veces es necesario convertir números a cadenas, o cadenas a números, por ejemplo, para 
# procesar datos ingresados por el usuario.

# Convertir número a cadena

# Usa la función str():

itg = 13
flt = 1.3
print(str(itg), str(flt))   # Salida: 13 1.3

# Convertir cadena a número

# Esto solo funciona si la cadena representa un número válido. Puedes usar:

# int() para enteros
# float() para decimales

print(float('14.3'))        # Salida: 14.3

# Si intentas convertir una cadena que no es un número válido, obtendrás un ValueError.

# En resumen:

# Python compara cadenas carácter por carácter, respetando mayúsculas y minúsculas.
# Las cadenas pueden ordenarse fácilmente con sorted() o sort().
# Para convertir entre cadenas y números, usa str(), int() o float(), pero con precaución.


# Ejercicios:

# Pregunta 1 - ¿Cuál de las siguientes líneas describe una condición verdadera?

"""
    Opciones:

    'smith' > 'Smith' 
    'Smiths' < 'Smith'
    'Smith' > '1000'
    '11' < '8'

    Respuesta:

    1, 3 y 4
"""

# Pregunta 2 - ¿Cuál es el resultado esperado del siguiente código?

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])  # Imprime: de


# Pregunta 3 - ¿Cuál es el resultado esperado del siguiente código?

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2) # Imprime: ValueError: invalid literal for int() with base 10: '12.8'


# Laboratorio: Un Display LED

"""
    Seguramente has visto un display de siete segmentos.

    Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar 
    un dígito decimal utilizando un subconjunto de siete segmentos. Si aún no sabes lo
      qué es, consulta la siguiente liga en Wikipedia: artículo.

    Tu tarea es escribir un programa que puede simular el funcionamiento de un display 
    de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

    Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por 
    supuesto), así es como lo imaginamos:

    # ### ### # # ### ### ### ### ### ###
    #   #   # # # #   #     # # # # # # # 
    # ### ### ### ### ###   # ### ### # # 
    # #     #   #   # # #   # # #   # # # 
    # ### ###   # ### ###   # ### ### ###

    Nota: el número 8 muestra todas las luces LED encendidas.
"""

# Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.
# Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.


# Datos de Prueba
# Entrada de muestra:

123

# Salida de muestra:

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

# Entrada de muestra:

9081726354

# Salida de muestra:

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 


# Respuesta:

# Lista que contiene para cada dígito (0-9) un patrón de 7 segmentos
# Cada carácter '1' o '0' indica si el segmento correspondiente está encendido o apagado.
digits = [ 
    '1111110',  # 0
    '0110000',  # 1
    '1101101',  # 2
    '1111001',  # 3
    '0110011',  # 4
    '1011011',  # 5
    '1011111',  # 6
    '1110000',  # 7
    '1111111',  # 8
    '1111011',  # 9
]

# Los segmentos están numerados así en el dígito de 7 segmentos:

#    -- 0 --
#   |       |
#  5|       |1
#   |       |
#    -- 6 --
#   |       |
#  4|       |2
#   |       |
#    -- 3 --

# La posición de cada segmento en el string de 'digits' es:
# índice 0 -> segmento 0 (línea superior horizontal)
# índice 1 -> segmento 1 (lado superior derecho vertical)
# índice 2 -> segmento 2 (lado inferior derecho vertical)
# índice 3 -> segmento 3 (línea inferior horizontal)
# índice 4 -> segmento 4 (lado inferior izquierdo vertical)
# índice 5 -> segmento 5 (lado superior izquierdo vertical)
# índice 6 -> segmento 6 (línea media horizontal)

def print_number(num):
    # Convertimos el número a cadena para iterar sus dígitos
    str_num = str(num)

    # Inicializamos una lista para almacenar las 5 líneas que formarán la figura final
    output_lines = ['' for _ in range(5)]

    # Iteramos sobre cada dígito para dibujarlo
    for digit_char in str_num:
        # Creamos una "matriz" 5x3 con espacios en blanco que representa la "pantalla" del dígito
        segments = [[' ' for _ in range(3)] for _ in range(5)]

        # Obtenemos el patrón de segmentos para el dígito actual
        pattern = digits[int(digit_char)]

        # Encendemos cada segmento según el patrón:

        # Segmento 0: línea superior horizontal (fila 0, columnas 0 a 2)
        if pattern[0] == '1':
            segments[0][0] = segments[0][1] = segments[0][2] = '#'

        # Segmento 1: lado superior derecho vertical (columnas 2, filas 0 a 2)
        if pattern[1] == '1':
            segments[0][2] = segments[1][2] = segments[2][2] = '#'

        # Segmento 2: lado inferior derecho vertical (columnas 2, filas 2 a 4)
        if pattern[2] == '1':
            segments[2][2] = segments[3][2] = segments[4][2] = '#'

        # Segmento 3: línea inferior horizontal (fila 4, columnas 0 a 2)
        if pattern[3] == '1':
            segments[4][0] = segments[4][1] = segments[4][2] = '#'

        # Segmento 4: lado inferior izquierdo vertical (columna 0, filas 2 a 4)
        if pattern[4] == '1':
            segments[2][0] = segments[3][0] = segments[4][0] = '#'

        # Segmento 5: lado superior izquierdo vertical (columna 0, filas 0 a 2)
        if pattern[5] == '1':
            segments[0][0] = segments[1][0] = segments[2][0] = '#'

        # Segmento 6: línea media horizontal (fila 2, columnas 0 a 2)
        if pattern[6] == '1':
            segments[2][0] = segments[2][1] = segments[2][2] = '#'

        # Añadimos el dígito dibujado a las líneas de salida
        for i in range(5):
            output_lines[i] += ''.join(segments[i]) + ' '  # Espacio para separar dígitos

    # Finalmente imprimimos línea por línea el número completo
    for line in output_lines:
        print(line)


# Ejecutar la función pidiendo un número
numero = int(input("Ingresa el número que deseas mostrar: "))
print_number(numero)
