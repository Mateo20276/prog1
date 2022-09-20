import random, os
import numpy as np



# Ejemplo de uso para Corte de Control

# Usamos w (write) para escribir el archivo que usaremos de ejemplo
def escribir(): 
    # Creo una lista para las carreras y así cargar en el archivo
    carreras=np.array([17,12,5,15,9,3])
    a1 = open('corte_control_prueba.txt','w') # Creo y Abro el archivo
    for c in range(6): # Cargo una materia para grabar
        carr=carreras[c]
        for i in range(random.randint(5,10)): # Genero los registros de cada materia
            leg=random.randint(2000000,5000000)
            mat=random.randint(11070,14890)
            nota=random.randint(1,10)
            # preparo la variable para grabar en el archivo
            # transformo todo a String y lo separo con comas
            # al final uso \n para que haga un salto de línea
            linea=str(leg)+','+ str(mat)+','+ str(carr)+','+ str(nota) + '\n'
            a1.write(linea) # Escribo en el archivo toda la línea 

    a1.close()    # cierro el archivo

# Usamos r (read) para leer
def corte_control():
    a1 = open('corte_control_prueba.txt','r')
    # leo una línea antes de entrar y cargo las variables
    linea=a1.readline().strip()  # Uso strip para quitar el fin de linea \n
    s=linea.split(',') # divido la línea leida usando el separador coma
    carr=int(s[2])     # Tomo carrera para cargar carrera anterior
    while linea!='': # cuando línea sea vacía '' finalizó el archivo
        suma=0
        cont=0
        carr_ant=carr
        while linea!='' and carr==carr_ant:  # cuando línea sea vacía '' finalizó el archivo
            # Acumulo y cuento
            leg=int(s[0])
            mat=int(s[1])
            nota=int(s[3])
            suma=suma+nota
            cont=cont+1
            # Muestro
            print(f'{" "*12} {carr:>8}{leg:>12} {nota:>4} ')   # Muestro lo leido
            linea=a1.readline().strip() # Leo una nueva línea y cargo las variables
            if linea!='':
                s=linea.split(',') # divido la línea leida usando el separador coma
                carr=int(s[2])     # Tomo carrera para cargar comparar con carrera anterior

        #Salí del While calculo y muestro el promedio
        prom=suma / cont
        print(f'{" "*25} Promedio  {prom:>4} ')
        # Y vuelvo a empezar
    a1.close() # cierro el archivo

# Programa Principal

if not os.path.exists('corte_control_prueba.txt'):
    print(' '*12,'El archivo con los datos No Existe')
    print(' '*12,'lo crearemos')
    escribir()
    print(' '*18,'Ya Cree el archivo')
    input('Presione Enter para continuar')

corte_control()
