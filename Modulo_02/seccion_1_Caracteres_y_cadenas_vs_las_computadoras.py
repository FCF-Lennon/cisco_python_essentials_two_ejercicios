# ¿Cómo entienden las computadoras los caracteres?

"""
Hasta ahora has trabajado con números, pero las computadoras también manejan 
textos: como nombres, direcciones, correos, etc. Para hacerlo, necesitan 
convertir los caracteres (letras, símbolos, espacios, etc.) en números, 
porque las computadoras solo entienden números.
"""

# ASCII: el primer estándar
# Para lograr esa conversión, se creó un sistema llamado ASCII, que asigna 
# un número único a cada carácter. Por ejemplo:

"""
El espacio ( ) = 32
La letra A = 65
La letra a = 97

Curioso: la diferencia entre a y A es 32, el mismo número que el del espacio.

ASCII usa 8 bits, lo que permite codificar 256 caracteres, aunque los más 
importantes son los primeros 128. Estos cubren el alfabeto latino, números y 
algunos símbolos y comandos de control (como el salto de línea).
"""

# El problema de los idiomas

"""
ASCII no basta para todos los idiomas del mundo. Por eso surgió el concepto 
de internacionalización, abreviado como I18N (porque entre la I y la N hay 18 letras).

Cada idioma tiene caracteres distintos, por lo tanto se idearon las páginas 
de código: formas de usar los 128 números restantes del ASCII para distintos 
alfabetos (como el cirílico, griego, hebreo, etc.). El problema: el mismo número 
puede representar cosas distintas en cada página, lo cual es ambiguo y confuso.
"""

# Unicode: la solución moderna

"""
Para unificar todo esto, se creó Unicode, un sistema que asigna un número único 
y universal para cada carácter del mundo. Tiene capacidad para más de un millón 
de caracteres.

Los primeros 128 códigos de Unicode son idénticos a ASCII.
Se organiza en planos, grupos de caracteres por región o uso.
"""

# ¿Cómo se guarda Unicode en archivos?

# UCS-4

"""
Usa 4 bytes (32 bits) por carácter.
Es simple pero ocupa mucho espacio.
"""

# UTF-8: la forma eficiente

"""
Es el sistema más usado hoy.
Usa solo los bits necesarios:
Caracteres ASCII → 8 bits.
Caracteres de otros idiomas → 16 o 24 bits.
Es compatible con ASCII, lo que lo hace ideal.
"""

# ¿Y en Python 3?

"""
Python 3 es totalmente compatible con Unicode y UTF-8:

Puedes usar caracteres Unicode en nombres de variables.
Puedes imprimir, leer y guardar textos en cualquier idioma.
Así, Python 3 está internacionalizado, preparado para trabajar con usuarios
de cualquier cultura o idioma.
"""

# Ejercicios:

# Pregunta 1 - ¿Qué es BOM?

"""
BOM (Byte Order Mark) es un marcador al inicio de un archivo de texto que indica
el orden de los bytes y la codificación utilizada. Es útil para identificar si 
un archivo es UTF-8, UTF-16 o UTF-32, y para asegurar que se interprete 
correctamente en diferentes sistemas.
"""

# Pregunta 2 - ¿Está Python 3 internacionalizado?

"""
Respuesta: Sí, Python 3 está internacionalizado. Permite trabajar con caracteres
Unicode y UTF-8, lo que facilita el uso de textos en diferentes idiomas y   
culturas. Esto significa que puedes usar caracteres de cualquier idioma en
tus programas de Python 3, y que puedes leer, escribir e imprimir textos
en cualquier idioma sin problemas de codificación.        
"""

