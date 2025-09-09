
# El módulo calendar - trabajando con funciones
# relacionadas con el calendario


"""
    En esta sección aprenderás a usar el módulo `calendar` de Python 
    para crear y manipular calendarios en texto, trabajar con días 
    de la semana, verificar años bisiestos y generar calendarios 
    personalizados con objetos de clase.
"""


# Introducción al módulo calendar:


"""
    Los días de la semana en el módulo calendar se representan como enteros:
    0 = Lunes (calendar.MONDAY), ..., 6 = Domingo (calendar.SUNDAY).
"""


# Tu primer calendario

import calendar

print(calendar.calendar(2020))
# Muestra el calendario completo del año 2020 en formato de texto.

calendar.prcal(2020)
# Igual que la función anterior, pero imprime directamente sin print().


# El calendario para un mes específico:

print(calendar.month(2020, 11))
# Muestra el calendario del mes de noviembre de 2020.

calendar.prmonth(2020, 11)
# Igual que month(), pero imprime directamente sin usar print().


# La función setfirstweekday():

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2020, 12))
# Cambia el primer día de la semana a domingo y muestra diciembre 2020 con esa configuración.


# La función weekday():

print(calendar.weekday(2020, 12, 24))
# Devuelve el día de la semana como entero: 3 = jueves.
# (El 24 de diciembre de 2020 fue jueves).


# La función weekheader():

print(calendar.weekheader(2))
# Devuelve abreviaturas de los días de la semana con 2 caracteres: Mo Tu We Th Fr Sa Su.

print(calendar.weekheader(3))
# Si se da un valor mayor a 3, igualmente devuelve abreviaturas de 3 caracteres: Mon Tue Wed ...


# ¿Cómo comprobar si un año es bisiesto?:

print(calendar.isleap(2020))
# Devuelve True porque 2020 es un año bisiesto.

print(calendar.leapdays(2010, 2021))
# Devuelve 3 porque entre 2010 y 2020 hubo 3 años bisiestos: 2012, 2016 y 2020.


# Clases para la creación de calendarios:

"""
    Principales clases:
    - Calendar: genera datos crudos de calendario.
    - TextCalendar: genera calendarios en formato de texto.
    - HTMLCalendar: genera calendarios en formato HTML.
    - LocalTextCalendar / LocalHTMLCalendar: versiones con soporte de localización.
"""


# Creando un objeto Calendar:

c = calendar.Calendar(calendar.SUNDAY)
for day in c.iterweekdays():
    print(day, end=" ")
# Devuelve un iterador de los días de la semana.
# Comienza en domingo (6) porque lo configuramos así: 6 0 1 2 3 4 5
print()


# El método itermonthdates():

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
# Devuelve objetos datetime.date para cada día de noviembre 2019.
# Incluye días de octubre y diciembre para completar las semanas.
print()


# Otros métodos que retornan iteradores:

c = calendar.Calendar(calendar.MONDAY)
for day in c.itermonthdays(2019, 11):
    print(day, end=" ")
# Devuelve números de los días del mes (1–30).
# Los 0 representan días de meses adyacentes para completar las semanas.
print()


# El método monthdays2calendar():

c = calendar.Calendar()
weeks = c.monthdays2calendar(2020, 11)
for week in weeks:
    print(week)
# Devuelve una lista de semanas del mes.
# Cada semana es una lista de tuplas (día_del_mes, día_de_la_semana).
# Los días fuera del mes aparecen como 0.
