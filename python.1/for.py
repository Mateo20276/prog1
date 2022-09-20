import numpy as np
import random

def cargar(vec,f,c):
    for x in range(f):
        for i in range(c):
            vec[x][i] = random.randint((1), 10)
f=3
c=3
vec = np.array([[0]*c]*f)
cargar(vec,f,c)
#print(vec)

#print(vec[1][2])
def suma(vec):
    sumatoria = 0
    for x in range(f):
        for i in range(c):
            sumatoria = sumatoria +  vec[x][i]
    print(sumatoria)
f=3
c=3
#suma(vec)
vc = [0]*c
vf = [0]*f
def suma_columnas(vec):
    for x in range(f):
        sum = 0
        for i in range(c):
            sum = sum + vec[x][i]
            vc[x] = int(sum)
    print(vc)

#suma_columnas(vec)

def suma_filas(vec):
    for x in range(c):
        sum = 0
        for i in range(f):
            sum = sum + vec[i][x]
            vf[x] = int(sum)
    print(vf)

#suma_filas(vec)
ma = np.array([[0]*4]*4)

cargar(ma,4,4)
print(ma)
def intercambio(m):
    r = 0
    for x in range(4):
        r = r + 1
        for i in range(4):
            if i >= r:
                v = m[x][i]
                m[x][i] = m[i][x]
                m[i][x] = v
    print(ma)
print()
intercambio(ma)

