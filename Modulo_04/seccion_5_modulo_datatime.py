
# Sección 5 - El módulo datetime en Python


"""
    En esta sección aprenderás a trabajar con fechas y horas
    usando los módulos datetime y time. 
    Estos módulos permiten crear, manipular y formatear objetos
    de fecha y hora de manera sencilla y flexible.
"""


# Introducción:

"""
    Ejemplos de uso de fecha y hora:
    - Registro de eventos (logs).
    - Seguimiento de cambios en bases de datos.
    - Validación (ej. cupones de descuento).
    - Transferencias bancarias y auditoría.
"""


# Obtener la fecha local y crear objetos date:

from datetime import date

# today() - Devuelve la fecha actual local
hoy = date.today()
print(f"Hoy: {hoy}")
print(f"Año: {hoy.year}")  # Atributo de solo lectura para el año
print(f"Mes: {hoy.month}")  # Atributo de solo lectura para el mes
print(f"Día: {hoy.day}")   

# Crear una fecha específica
fecha_especifica = date(2019, 11, 4)
print(fecha_especifica)


# Crear fecha a partir de marca de tiempo:

import time

# time() - Devuelve segundos desde epoch (1/1/1970)
timestamp = time.time()
print(f"Marca de tiempo: {timestamp}")

# fromtimestamp() - Convierte timestamp a objeto date
fecha_desde_timestamp = date.fromtimestamp(timestamp)
print(f"Fecha: {fecha_desde_timestamp}")


# Crear fecha con formato ISO:

# fromisoformat() - Crea date desde string en formato ISO 8601 (AAAA-MM-DD)
fecha_iso = date.fromisoformat("2019-11-18")
print(fecha_iso)


# Reemplazar año, mes o día:

fecha_original = date(1991, 2, 5)
print(fecha_original)
# replace() - Devuelve nueva fecha cambiando los valores especificados
fecha_modificada = fecha_original.replace(year=1992, month=1, day=16)
print(fecha_modificada)


# Día de la semana:

# weekday() - Devuelve día de semana (0=Lunes, 6=Domingo)
# isoweekday() - Devuelve día de semana (1=Lunes, 7=Domingo)
d = date(2025, 9, 3)
print("Día semana (0-6):", d.weekday())
print("Día semana (1-7):", d.isoweekday())


# Crear objetos time:

from datetime import time 
# time() - Crea objeto time con hora, minuto, segundo, microsegundo
tiempo = time(14, 53, 20, 1)
print("Tiempo:", tiempo)
print("Hora:", tiempo.hour)
print("Minutos:", tiempo.minute)
print("Segundos:", tiempo.second)
print("Microsegundos:", tiempo.microsecond)


# Uso de sleep en el módulo time:

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.")
        # time.sleep(seconds)  # comentado para evitar pausa real
        print("¡Dormí bien! ¡Me siento genial!")

alumno = Student()
alumno.take_nap(5)


# Función ctime():
# ctime() - Convierte timestamp a string legible
import time
print(time.ctime(timestamp))
print(time.ctime())  # Sin parámetro usa hora actual


# Las funciones gmtime() y localtime():
# gmtime() - Timestamp a struct_time en UTC
# localtime() - Timestamp a struct_time en zona local
print(time.gmtime(timestamp))    # UTC
print(time.localtime(timestamp)) # Hora local


# Las funciones asctime() y mktime():
# asctime() - struct_time a string legible
# mktime() - struct_time a timestamp
st = time.gmtime(timestamp)
print("Struct_time a string:", time.asctime(st))

tupla_tiempo = (2019, 11, 4, 14, 53, 0, 0, 308, 0)
print("Tupla a timestamp:", time.mktime(tupla_tiempo))


# Crear objetos datetime:

from datetime import datetime

# datetime() - Combina fecha y hora en un solo objeto
dt = datetime(2019, 11, 4, 14, 53, 0)
print(f"Fecha y Hora: {dt}")
print(f"Fecha: {dt.date()}")  # date() - Extrae componente fecha
print(f"Hora: {dt.time()}")   # time() - Extrae componente hora


# Métodos de fecha y hora actuales:
# today() - Fecha/hora local actual
# now() - Similar a today() pero permite especificar zona horaria  
# utcnow() - Fecha/hora UTC actual
print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow()) # deprecated 


# Obtener timestamp "marca de tiempo" desde datetime:
# timestamp() - Convierte datetime a segundos desde epoch
print("Timestamp:", dt.timestamp())


# Dar formato a la fecha y hora con strftime():
# strftime() - Formatea fecha/hora según formato especificado
print(dt.strftime("%Y/%m/%d"))  # 2019/11/04
print(dt.strftime("%H:%M:%S"))          # 14:53:00
print(dt.strftime("%y/%B/%d %H:%M:%S")) # 19/November/04 14:53:00


# La función strftime() en el módulo time:
# strftime() del módulo time - Similar pero para struct_time
print("Struct_time: ", time.strftime("%Y/%m/%d %H:%M:%S", st))
print("Actual: ", time.strftime("%Y/%m/%d %H:%M:%S"))


# El método strptime():
# strptime() - Convierte string a datetime según formato
cadena = "2019/11/04 14:53:00"
dt_parseado = datetime.strptime(cadena, "%Y/%m/%d %H:%M:%S")
print("String a datetime: ", dt_parseado)
print("String a struct_time: ", time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


# Operaciones con timedelta:

from datetime import timedelta

# Resta de fechas devuelve timedelta
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print("Diferencia entre fechas: ", d1 - d2)

dt1 = datetime(2020, 11, 4, 14, 53)
dt2 = datetime(2019, 11, 4, 5, 46)
print("Diferencia entre datetime: ", dt1 - dt2)


# Crear objeto timedelta:
# timedelta() - Representa diferencia de tiempo
delta = timedelta(weeks=2, days=2, hours=3)
print("Timedelta creado: ", delta)
print("Días:", delta.days) # Días del objeto timedelta
print("Segundos:", delta.seconds) # Segundos restantes (horas, minutos convertidos)
print("Microsegundos:", delta.microseconds) # Microsegundos del objeto timedelta


# Operaciones con timedelta:
print("\nOperaciones con timedelta:")
print("Multiplicación:", delta * 2) # Multiplicación
print("Suma de fecha y timedelta:", d2 + delta) # Suma de fecha y timedelta
print("Suma de datetime y timedelta:", dt2 + delta) # Suma de datetime y timedelta


# Laboratorio - Los módulos datetime y time

"""
    Durante este curso, has aprendido sobre el método strftime, 
    que requiere conocimiento de las directivas para crear un formato.
    Ahora es el momento de poner en práctica estas directivas.

    Por cierto, tendrás la oportunidad de practicar el trabajo con documentación, 
    porque tendrás que encontrar directivas que aún no conoces.
"""

# Aque está tu tarea:

"""
    Escribe un programa que cree un objeto datetime para el 4 de
    noviembre de 2020, 14:53:00. El objeto creado debe llamar al método strftime
    con el formato apropiado para mostrar el siguiente resultado:

    2020/11/04 14:53:00
    20/November/04 14:53:00 PM
    Wed, 2020 Nov 04
    Wednesday, 2020 November 04
    Día de la semana: 3
    Día del año: 309
    Número de semana en el año: 44
"""

# Nota: Cada línea de resultado debe crearse llamando al método strftime()
# con al menos una directiva en el argumento de formato.


# Desarrollo:

from datetime import datetime

fecha_sin_formato = datetime(2020, 11, 4, 14, 53, 0)
print("\nLaboratorio: ")
print(fecha_sin_formato.strftime('%Y/%m/%d %H:%M:%S'))
print(fecha_sin_formato.strftime('%Y/%B/%d %H:%M:%S %p'))
print(fecha_sin_formato.strftime('%a, %Y %b %d'))
print(fecha_sin_formato.strftime('%A, %Y %B %d'))
print('Día de la semana: ', fecha_sin_formato.isoweekday())
print('Dia del año: ', fecha_sin_formato.strftime('%j'))
print('Número de semana en el año: ', fecha_sin_formato.isocalendar()[1]) # Depende de convención ISO 8601
print('Número de semana en el año: ', fecha_sin_formato.strftime('%W')) # Lunes como primer día de la semana
print('Número de semana en el año: ', fecha_sin_formato.strftime('%U')) # Domingo como primer día de la semana


# Cuestionario:

# Pregunta 01 - ¿Cuál es el resultado del siguiente fragmento de código?

from datetime import time

t = time( 14, 53)
print(t.strftime("%H:%M:%S"))

# Respuesta: imprimirá "14:53:00" según la directiva de formato %H:%M:%S.


# Pregunta 02 - ¿Cuál es el resultado del siguiente fragmento de código?

from datetime import datetime

dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)

print(dt1 - dt2)

# Respuesta: imprimirá la diferencia entre ambas fechas como un objeto timedelta.
# En este caso: "1 day, 0:00:00".

