import numpy as np
'''Posibles enunciados para el 1er Parcial

Indicar las diferencias entre un dato de tipo arreglo y una lista.
       
Se requiere procesar los datos de 3000 personas que respondieron a una encuesta sobre 10 productos, en las localidades de Luján, 9 de Julio y Chivilcoy. Para ello, se cuenta con los siguientes datos: Apellido (string), Nombre (string), Sexo (carácter (F/M), Estado Civil (carácter S,C,V), Localidad (string) y la  Respuesta dada (numérico con valores de 1 a 10 (Son los productos)).
       
    1) Definir las estructuras de datos más adecuadas para almacenar la información 
    2) Y las funciones necesarias para obtener la siguiente información: 
        a) Informar la cantidad de varones y de mujeres que votaron al producto ganador.
        b) Informar en qué localidad el producto ganador obtuvo la mayor cantidad de votos.

Se reciben como parámetros dos arreglos de 20 elementos cada uno, de tipo booleano. En el primero de ellos, llamado V1, se encuentran cargadas las 20 respuestas de un alumno; en el otro, llamado V2, se encuentran cargadas las respuestas correctas. Escribir un subprograma que retorne el puntaje obtenido por el alumno, conociendo que cada respuesta correcta vale un punto.

Se necesita procesar los datos de una encuesta realizada a un grupo de jóvenes respecto de su preferencia entre dos aplicaciones de mensajería y chat.
Para ello, se deberá escribir un algoritmo que permita el ingreso de los datos y su validación, hasta que se ingrese como valor de corte el valor 0 para la edad. 
Los datos se deberán validar de la siguiente manera:
    aplicación: 1 ó 2;
    sexo: 1 o 2 (correspondiente a femenino y masculino respectivamente);
    edad: entre 15 y 25 años inclusive.
      Se deben Validar

Se deberán además generar las funciones necesarias para obtener la siguiente información:
    a) Cuál fue la app más votada y cuántos votos obtuvo.
    b) Qué porcentaje de mujeres y de hombres eligieron la app ganadora.'''


f = 25

c = 3
vec = np.array([[0]*c]*f)

def appl(vec):
    edad = 1
    for i in range(f):
        l = edad
        if l !=0:
            
            edad = int(input("Escriba su edad entre 15 y 20, escribe 0 si no queires agregar a mas participantes: "))
            while (edad < 15 or edad > 25) and edad != 0:
                print("Escribe nuevamente la edad")
                edad = int(input("Escriba su edad entre 15 y 25: "))
            if edad != 0:
                
                sexo = int(input("Escriba su sexo, 1 masculino o 2 femenino: "))
                while (sexo != 1 and sexo != 2):
                    print("Escribe nuevamente tu sexo: ")
                    sexo = int(input("Escriba su sexo, 1 masculino o 2 femenino: "))
                
                aplicacion = int(input("Vote una app: 1 o 2: "))
                while (aplicacion != 1 and aplicacion != 2):
                    print("Escribe nuevamente tu aplicacion favorita: ")
                    sexo = int(input("Vote una app: 1 o 2: "))
                
                vec[i][0] = edad
                vec[i][1] = sexo
                vec[i][2] = aplicacion
            else:
                print("Se a cortado el programa")
    print(vec)
        
    

m = np.array([[1,2,3,1],[4,5,6,1]])
print(m)
print(m.shape[1])
