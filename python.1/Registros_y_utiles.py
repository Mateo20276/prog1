'''
En un colegio de primaria, una clase tiene un nivel, un profesor y contiene 20 
estudiantes. 
Cada estudiante tiene un nombre, apellido, una fecha de nacimiento
y tendrá diez notas en el año. 
Hay cinco clases. 
Proporcione las estructuras de los registros clase y estudiantes.
1)Escriba un algoritmo que muestre para cada clase, la lista de los estudiantes y
sus diez notas asociadas.
2) Utilizando el procedimiento anterior, realice las modificaciones necesarias para
que la lista de estudiantes esté siempre ordenada alfabéticamente.
3) Utilizando el procedimiento del punto 1, realice las modificaciones necesarias para
   obtener una lista ordenada por promedios de mayor a menor.

Reg Clase (Cinco instancias) Vector de 5 elementos
    nivel       Entero
    profesor    String 
  y podría ser tambien con
    alumnos     vector de 20 registros

Reg Estudiantes una matriz de 5x20  5 clase y 20 estudiantes
    nombre      String
    apellido    String
    fec_nac     String  podría ser un registro
    n1,n2,n3    Real    podría ser un vector

1) Recorrer la matriz por filas y muestro hago un print() después de cada fila
2) Ordenar cada fila de la matriz en forma independiente
3) Recorremos la fila x calculamos promedio y lo ponemos en un registro
   y lo guardamos en un vector. 
   ordeno el vector de 20 elementos
   nuevo reg 
       nombre
       prom
'''
# Como intercambiar al ordenar por un campo de un registro 

# for i in range(len(v)):
#     if v[i].prom < v[i+1].prom:
#         raux=v[i]
#         v[i]=v[i+1]
#         v[i+1]=raux


# Algunas ideas útiles para la carga automática de datos
# Y para mostrar los datos prolijamente
import random

# Cargar un vector aleatorio con números
random.randint(1,50) # genera enteros entre 1 y 50
random.random()      # genera real entre 0 y 1
   # generar reales entre 1 y 10000
   # ademas mostrarlos alineados a la derecha

nota=random.randint(1,9999) + random.random() # genera los reales
print(f'{nota:>12.2f}')  
        # >12 alinea a la derecha ocupando siempre 12 espacios
        # .2f muestra solo 2 decimales del float

#  Strings
# Generar una listas con nombres
nombre=['Juan','Maria','Pedro','Claudia','Belen','Veronica','Nahuel','Nicolas']
ciudad=['Luján','Mercedes','Chivilcoy','Rodriguez','Giles','Navarro','Moreno']

# ahora mostraremos todo prolijamente
print(' Nombre       edad    ciudad             saldo')
for i in range(20):
    nom=random.choice(nombre)   # Elegir un nombre al azar
    ciu=random.choice(ciudad)   # Elegir una ciudad al azar
    edad=random.randint(18,110) 
    saldo=random.randint(-9999,9999) + random.random() # genera los reales
    print(f'{nom:<12}   {edad:>4}     {ciu:<12} {saldo:>12.2f}')
