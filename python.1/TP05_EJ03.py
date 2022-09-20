'''
3.	Utilizando el mismo archivo generado en el punto anterior, preparar un procedimiento que 
permita leer los datos y generar otro archivo(“temp_media.txt”), que contenga las temperaturas 
medias diarias con el siguiente formato:

	Día - Mes - Año - Temperatura_Media
 	
Ejemplo
Salida:
01 -01 - 2021 - 24.5
02 -01 - 2021 - 22
……..
03 - 06 - 2021 - 5
  ……….
30 - 12 - 2021 - 20 - 27
31 - 12 - 2021 - 20 -28
'''

import random
import os

def escribir_archivo():
   archivo1 = open("temperaturas.txt", "w")
   for x in range(3):
      dia = random.randint(1,30)
      mes = random.randint(1,12)
      año = 2021
      temp_minima = random.randint(0,20)
      temp_maxima = random.randint(15,40) 

      linea = (f"{str(dia)}, {str(mes)}, {str(año)}, {str(temp_minima)}, {str(temp_maxima)}\n")
      
      archivo1.write(linea)

   archivo1.close()

def leer_archivo():
   archivo1 = open("temperaturas.txt", "r")
   linea = archivo1.readline().strip()
   print(' '*10+' DIA      MES      AÑO      TEMPERATURA MINIMA      TEMPERATURA MAXIMA')

   while linea != "":
      separador = linea.split(",")

      dia = int(separador[0])
      mes = int(separador[1])
      año = int(separador[2])
      temp_minima = int(separador[3])
      temp_maxima = int(separador[4])

      print(f"{' '*11}{dia:<10}{mes:<5}{año:>6}{temp_minima:>18.2f}°{temp_maxima:>24.2f}°")

      linea = archivo1.readline().strip()
   print()
   print()
   archivo1.close()

def temperatura_media():
   archivo1 = open("temperaturas.txt", "r")
   linea = archivo1.readline().strip()
   print(' '*10+' DIA      MES      AÑO      TEMPERATURA MEDIA')
   
   minima_temperatura_total = 20

   maxima_temperatura_total = 0

   max_amplitud = 0
   # dia_max_amplitud = 0
   # mes_max_amplitud = 0
   while linea != "":
       separador = linea.split(",")
       dia = int(separador[0])
       mes = int(separador[1])
       año = int(separador[2])

       minima_temp = int(separador[3])
       maxima_temp = int(separador[4])

       temperatura_media = (maxima_temp + minima_temp) / 2

       print(f"{' '*11}{dia:<10}{mes:<5}{año:>6}{temperatura_media:>18}°")
       linea = archivo1.readline().strip()

   print()
   archivo1.close()


#escribir_archivo()
leer_archivo()
temperatura_media()

    




