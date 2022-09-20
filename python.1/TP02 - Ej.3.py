# Realizar un programa que, dado una matriz cuadrada con valores enteros
# entre 1 y 50 (al azar), la muestra y luego realice las permutaciones de filas y
# columnas, utilizando un procedimiento que permuta dos elementos, y mostrarla.

import numpy as np
import random


# Programas Accesorios:

def carga_matriz(m):
    print()
    tamanio = np.size(m)
    fila,columna = np.shape(m)
    for f in range (fila):
        for c in range (columna):
            m[f,c] = random.randint(1,9)
    return m



def muestra_matriz(m):
    fila,columna = np.shape(m)
    for f in range (fila):
        for c in range (columna):
            print(m[f,c],end= " ")
        print()



def cambia_posicion(m):
    c = 0 
    f = 0
    flag = True
    c_limit = 0 
    while flag:
        aux1 = m[f,c]  
        m[f,c] = m[c,f] 
        m[c,f] = aux1
        c = c + 1
        if c > 3:
            c_limit = c_limit + 1
            c = c_limit
            f = c_limit
            if c_limit > 3:
                flag = False
    return muestra_matriz(m)


# Programa Principal:

matriz = np.array([[0]*4]*4)

carga_matriz(matriz)
print("La matriz: ")
muestra_matriz(matriz)
print()
print("Las filas son columnas ahora: ")
print(cambia_posicion(matriz))
