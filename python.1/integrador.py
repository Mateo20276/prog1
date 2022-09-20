# ----------------- PROGRAMACION1 UNLu INTEGRADOR 9/12/21 ---------------------
# Completar con tus datos:
# Nombre:
# DNI:
# Entrega: por GitHub (preferentemente) o por mail a: program1.unlu@gmail.com

# IMPORTANTE: No está permitido usar para resolver el examen estructuras de datos
# o funciones, que no hayamos visto en la materia, o en Introducción a la Programación.

# Escribir un programa que reciba un archivo de texto (MOVI.TXT) y un vector de 
# registros (PRECIOS) y realice lo solicitado en el siguiente enunciado.
       
# Una estación de servicio almacena en un archivo de texto (MOVI.TXT), organizado 
# de modo secuencial, la información diaria de los litros de combustible despachados 
# durante el mes de octubre.
# Cada una de las líneas del archivo MOVI.TXT tienen los siguientes datos, 
# separados por coma:
#     • día (1-31)
#     • hora (0-23)
#     • minutos (0-59)
#     • código_surtidor (1-15)
#     • código_combustible (1-10)
#     • litros_despachados
# El archivo MOVI.TXT se encuentra agrupado y ordenado por día.

# PRECIOS es un vector de REALES (float) de longitud 10 que almacena los precios
# por litro de los combustibles. El índice del vector PRECIOS se corresponde con el código
# de combustible menos 1. Por ejemplo, PRECIOS[2], sería el precio por litro del 
# combustible de código 3, y PRECIOS[0], sería el precio por litro del 
# combustible de código 1.


# SURTIDORES es un vector de REGISTROS de longitud 15 donde se almacena la 
# cantidad de litros que despachó cada surtidor históricamente, y su recaudación.
# Los registros del vector SURTIDORES tienen la siguiente estructura 
#     • código_surtidor (números enteros consecutivos entre 1-15, no se puede repetir)
#     • litros_despachados (integer)
#     • recaudación (float)
# El vector SURTIDORES está ordenado por código_combustible

# Se pide:

# a) Definir y cargar el vector PRECIOS (los valores de los precios por litros 
# (definirlos en forma random teniendo en cuenta que son FLOAT)

# b) Definir la estructura de los registros del vector SURTIDORES. Definir y 
# cargar el vector SURTIDORES: 
#      litros despachados random entre 100 y 1000 ENTERO
#      recaudación  random  entre 5000 y 20000  FLOAT

# c) Escribir un programa que utilizando la técnica del corte de control 
# sobre el archivo MOVI.TXT, muestre por pantalla un informe con los
# litros totales vendidos ese día y su recaudación, y al finalizar, el total del mes.
# Por ejemplo, el informe quedaría de esta forma:
# 		Dia         litros totales           recaudación
# 		  1                568                    $   43200.2
#  		  2                734                    $   87500.5
# 	          .                 .                     $       . 
# 		  .                 .                     $       .
# 		  31               512                    $   50700.9

# 	      Total mes           50000                   $   357800.6
       
# Además el programa deberá actualizar en el vector SURTIDORES los valores de 
# litros_despachados y recaudación

# Por último, el programa debe informar por pantalla cuál entre las siguientes 
# franjas horarias es la que tuvo mayor recaudación
#	 1) de  6:00 a 10:00
#	 2) de 11:00 a 14:00
#	 3) de 15:00 a 18:00

# NOTA IMPORTANTE: 
# El archivo MOVI.TXT debe ser leído una sola vez en todo el programa.  

from pyrecord import Record
import numpy as np
import random

T_surtidores = Record.create_type("T_surtidores","codigo_surtidor","litros_despachados","recaudacion",
                            codigo_surtidor = 0, litros_despachados = 0,recaudacion=0.0)   

registro_surtidores = np.array([T_surtidores()]*20) # se crea el vector de registro
precios_combustibles = np.array([0.0]*10) # se crea el vector de precios(reales)


def cargar_precios(vector):
    for i in range(len(vector)):
        vector[i] = random.randint(100,200)- + random.random()


def cargar_surtidor(registro):
    codigo_surtidor = 1
    for i in range(15):
        registro[i] = T_surtidores()
        registro[i].codigo_surtidor = codigo_surtidor
        registro[i].litros_despachados = random.randint(100,1000) # numero entero aleatorio
        registro[i].recaudacion = float(random.randrange(5000,20000)) # numero real aleatorio
        codigo_surtidor += 1

def procesar(registro,vector):
    a1 = open('MOVI.TXT','r')
    # leo una línea antes de entrar y cargo las variables
    linea=a1.readline().strip()  # Uso strip para quitar el fin de linea \n
    v=linea.split(',')
    dia=int(v[0])     
    litros_mes = 0
    recaudacion_mañana = 0.0
    recaudacion_medio_dia = 0.0
    recaudacion_tarde = 0.0
    recaudacion_mes = 0.0
    #---------------------------------  ---------------------------
    vector_litros_surtidor = np.array([0]*15)
    vector_recaudacion_surtidor = np.array([0.0]*15)
    #------------------------------------------------------------------------------------------------------------------------------------
    while linea!='': # cuando línea sea vacía '' finalizó el archivo
        dia_ant=dia
        litros_dia = 0
        recaudacion = 0.0
        print("DIA"," "*10,"LITROS TOTALES"," "*8,"RECAUDACION")
        while linea!='' and dia==dia_ant:  # cuando línea sea vacía '' finalizó el archivo
            dia = int(v[0])
            hora = int(v[1])
            minutos = int(v[2])
            codigo_surtidor = int(v[3])
            codigo_combustible = int(v[4])
            litros = int(v[5])
            litros_dia += litros
            recaudacion += (litros * vector[codigo_combustible-1])
            vector_litros_surtidor[codigo_surtidor-1] += litros
            vector_recaudacion_surtidor[codigo_surtidor-1] += recaudacion
            linea=a1.readline().strip() # Leo una nueva línea y cargo las variables

            if (hora >= 6 and ((hora < 10)  or (hora == 10 and minutos == 0))):
                    recaudacion_mañana += recaudacion
            elif (hora >= 11 and ((hora < 14)  or (hora == 14 and minutos == 0))):
                    recaudacion_medio_dia += recaudacion
            elif (hora >= 15 and ((hora <=18) or (hora == 18 and minutos == 0))):
                    recaudacion_tarde += recaudacion

            if linea!='':
                v=linea.split(',') # divido la línea leida usando el separador coma
                dia=int(v[0])     # 

        print(dia_ant," "*12,litros_dia," "*10,recaudacion)
        litros_mes += litros_dia
        recaudacion_mes += recaudacion
    print("Total mes:"," "*8,litros_mes," "*8,recaudacion_mes)

    # actualizar Surtidores

    for i in range(15):
        registro[i].litros_despachados += vector_litros_surtidor[i]
        registro[i].recaudacion += vector_recaudacion_surtidor[i]

    # informar que franja horario recaudo mas

    if recaudacion_mañana > recaudacion_medio_dia and recaudacion_mañana > recaudacion_tarde:
        print("De 6:00 a 10:00 fue el horario que mas se recaudo con : $",recaudacion_mañana)
    elif recaudacion_medio_dia > recaudacion_mañana and recaudacion_medio_dia > recaudacion_tarde:
        print("De 11:00 a 14:00 fue el horario que mas se recaudo con : $",recaudacion_medio_dia)
    elif recaudacion_tarde > recaudacion_mañana and recaudacion_tarde > recaudacion_medio_dia:
        print("De 15:00 a 18:00 fue el horario que mas se recaudo con : $",recaudacion_tarde)




    a1.close() # cierro el archivo

def principal():
    cargar_precios(precios_combustibles)
    cargar_surtidor(registro_surtidores)
    procesar(registro_surtidores,precios_combustibles)

principal()