 # Escribir una función que reciba un arreglo de strings e indique si se
# encuentran ordenados de menor a mayor o no.

# Alfabeto: 




arreglo_desordenado = ["perro","heladera","casa","sillón","techo"]
arreglo_ordenado    = ["casa","heladera","perro","sillón","techo"]


# def bla(v):
#     for i in range(len(v)-1):
#         for j in range(len(v)-1):
#             if v[j] > v[j+1]:
#                 v[j],v[j+1] = v[j+1],v[j]
#     return v

# print(bla(arreglo_desordenado))

def ordenado(v):
    contador = 0
    desorden = False
    while contador < len(v)-1 and not desorden:
        if v[contador] > v[contador + 1]:
            desorden = True
        else:
            contador = contador + 1
    if desorden == True:
        return f"Está desordenado"
    else:
        return f"Está ordenado"




print(ordenado(arreglo_ordenado))





