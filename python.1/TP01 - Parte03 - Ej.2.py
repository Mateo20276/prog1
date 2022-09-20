# Dados dos arreglos ordenados: A(n) y B(m), construir un nuevo arreglo C
# que contenga los elementos de A y de B de tal forma que quede también
# ordenado. Si existen elementos repetidos en los arreglos originales, en C
# deberán aparecer solamente una vez.

# Programas Accesorios: 

def muestra_vector(v):
	for i in range(len(v)):
		print(v[i], end = " ")
	print()


def muestra_vector_util(v,tam_u):
	for i in range(tam_u+1):
		print(v[i], end = " ")
	print()


def ordena_vector3(v1,v2,v3):
    pos_v1 = 0 
    pos_v2 = 0 
    pos_v3 = 0

    # Se van ordenando en v3 los valores de v1 y v2 de forma ascendenete hasta que uno de los
    # dos vectores se termina. 

    while pos_v1 < len(v1) and pos_v2 < len(v2):
        flag_v1 = True
        flag_v2 = True
        
        while pos_v1 < len(v1)-1 and flag_v1:   # Acá consultamos si el número siguiente al índice actual es igual y 
                                                # para evitar repeticiones en el mismo vetor.
            flag_v1 = False
            if v1[pos_v1] == v1[pos_v1 + 1]:
                pos_v1 = pos_v1 + 1
                flag_v1 = True
        
        while pos_v2 < len(v2)-1 and flag_v2:   # Acá consultamos si el número siguiente al índice actual es igual y 
                                                # para evitar repeticiones en el mismo vetor.
            flag_v2 = False
            if v2[pos_v2] == v2[pos_v2 + 1]:
                pos_v2 = pos_v2 + 1
                flag_v2 = True

        if v1[pos_v1] < v2[pos_v2]:
            v3[pos_v3] = v1[pos_v1]
            pos_v1 = pos_v1 + 1
            pos_v3 = pos_v3 + 1

        elif v1[pos_v1] > v2[pos_v2]:
            v3[pos_v3] = v2[pos_v2]
            pos_v2 = pos_v2 + 1
            pos_v3 = pos_v3 + 1

        elif v1[pos_v1] == v2[pos_v2]:
            v3[pos_v3] = v1[pos_v1]
            pos_v1 = pos_v1 + 1
            pos_v2 = pos_v2 + 1
            pos_v3 = pos_v3 + 1

    # Se termina de completar v3 con los valores del vector que no se terminó de integrar en v3,
    # o sea, el vector más largo. 

    if pos_v1 < len(v1):
        for restante in range (pos_v1,len(v1)):
            v3[pos_v3] = v1[restante]
            pos_v3 = pos_v3 + 1
    
    elif pos_v2 < len(v2):
        for restante in range (pos_v2,len(v2)):
            v3[pos_v3] = v2[restante]
            pos_v3 = pos_v3 + 1
    
    return pos_v3


# Programa Principal:

vector1 = [1, 1, 3, 4, 6, 7, 7, 9, 9, 20]
vector2 = [1, 2, 3, 3, 5, 7, 8, 8, 10, 11, 15, 17]
vector3 = [0]*(len(vector1)+len(vector2))

tamaño_util = ordena_vector3(vector1,vector2,vector3) - 1

muestra_vector(vector3)
print()
muestra_vector_util(vector3,tamaño_util)