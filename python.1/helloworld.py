import random
## aqui hay 3 metodos para ordenar numeros en un array
## los siguientes resultados fueron tomados con v=[10,9,8,7,6,5,4,3,2,1]
## metodo A:32 ciclos
## metodo B:81 ciclos
## metodo C:6 ciclos

def cargar(v):
    for i in range(len(v)):
        v[i]=random.randint(0,10)
    return v

def comprobar(v,o):
    t=1
    #mientras t no llegue a la penultima posicion de la array
    while t<len(v):
        #sí la posicion anterior es menor a la actual
        if v[t-1]<=v[t]:
            #esta ordenado
            o=True

        else:#de lo contrario
            #no esta ordenado y se interrumpe el while inmediatamente
            o=False
            t=len(v)-1

        t=t+1

    return o   

def ordenar_a(v,o):
    #comprobar que los numeros no esten ordenados desde el inicio
    comprobar(v,o)
    print("A")
    #ordenar numeros (si no estan ordenados de base) 
    if o==False:
        t=1
        for i in range(len(v)):
            j=1
            #mientras j no llegue a la penultima posicion del


#mientras no lo haga encontrado y la mitades no se crusen
while (not encontrado) and (izquierda <= derecha):
	#tomo el medio del vector
	medio = izquierda + (derecha - izquierda)//2

	#verifico si el eleento esta justo en el medio
	if vector[medio] == elemento:
		encontrado = True
		posicion = medio

	#si el elemento es mayor, ignoro la mitad izquierda

	elif vector[medio]<elemeto:
		izquierda = medio + 1

	#si elelemento es menor, ignoro la mitad derecha
	else:
		derecha = media - 1
