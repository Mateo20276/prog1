# import io
import random 
import numpy as np
from funciones_utiles import *
#from numpy.testing._private.utils import rand  # importamos funciones útiles de otro archivo

# Ejemplos de uso para archivos Secuenciales (de texto)

# Usamos w (write) para escribir
def escribir(nom): # nom es para escoger al azar nombres

    a1 = open('arch_prueba1.txt','w') # Abro el archivo
    for i in range(10): # cargo 10 líneas
        dia=random.randint(1,30)
        mes=random.randint(1,12)
        real=random.randint(10,500) + random.random()
        # preparo la variable para grabar en el archivo
        # transformo todo a String y lo separo con comas
        # al final uso \n para que haga un salto de línea
        linea=random.choice(nom)+','+ str(dia)+','+ str(mes)+','+ str(real) + '\n'
        a1.write(linea) # Escribo en el archivo toda la línea 
    
    a1.close()    # cierro el archivo

# Usamos r (read) para leer
def leer():
    a1 = open('arch_prueba1.txt','r')
    # leo una línea antes de entrar
    print(' '*13+' N Nombre         Día      Mes        Real')
    cont=1
    linea=a1.readline().strip()  # Uso strip para quitar el fin de linea \n
    while linea!='':  # cuando línea sea vacía '' finalizó el archivo
        s=linea.split(',') # divido la línea leida usando el separador coma
        # s se transforma en una lista, donde cada posición la debo transformar 
        # a su tipo correspondiente
        n1=s[0]       # String
        n2=int(s[1])  # Entero
        n3=int(s[2])  # Entero
        n4=float(s[3])# Real
        print(f'{" "*12} {cont:>2} {n1:<12} {n2:>4}     {n3:>4} {n4:>12.2f}')   # Muestro lo leido
        linea=a1.readline().strip() # Leo una nueva línea
        cont+=1

    a1.close() # cierro el archivo

# Usamos a (append) para agregar
# Automaticamente
def agregar_a(nom):
    a1 = open('arch_prueba1.txt','a') # Abro el archivo
    for i in range(3): # Voy a agregar 3 líneas
        dia=random.randint(1,30)
        mes=random.randint(1,12)
        real=random.randint(10,500) + random.random() 
        # preparo la variable para grabar en el archivo
        # transformo todo a String y lo separo con comas
        # al final uso \n para que haga un salto de línea
        linea=random.choice(nom)+','+str(dia)+','+str(mes)+','+str(real)+'\n'
        a1.write(linea) # Escribo en el archivo toda la línea 
    
    a1.close()    # cierro el archivo

# Usamos a (append) para agregar
# Manualmente
def agregar_m():
    a1 = open('arch_prueba1.txt','a') # Abro el archivo
    # Ingreso datos por teclado
    nom=input(' Ingrese un nombre (para terminar solo presione Enter): ')  # Ingreso el primer dato fuera
    while nom != '':   
        dia=input(' Elija el un número de día: ')
        mes=input(' Ahora un mes: ')
        algo=input(' Ahora escriba un numero real usando punto y no coma: ')
        linea=nom +','+ dia +','+ mes +','+ algo +'\n'
        a1.write(linea) # Escribo en el archivo toda la línea 
        nom=input(' Ingrese otro nombre (para terminar solo presione Enter): ') 

    a1.close()    # cierro el archivo


def menu0():
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Principal")
        print()
        print(" "*25,"1 Crear un Archivo y poner datos Automaticamente(w)")
        print(" "*25,"2 Mostrar el archivo (r)")
        print(" "*25,"3 Agregar datos a un archivo (a) Automaticamente")
        print(" "*25,"4 Agregar datos a un archivo (a) Manualmente")
        print()
        print(" "*28,"0 Salir")
        op=elegir(4)
        if op==1:
            limpiar_pantalla()
            escribir(nom)
            mensaje('El archivo fue cargado')
            pausa()
        elif op==2:
            limpiar_pantalla()
            leer()
            mensaje('Estos son los datos actuales del archivo')
            pausa()
        elif op==3:
            limpiar_pantalla()
            agregar_a(nom)
            mensaje('Se agregaron 3 lineas al archivo')
            pausa()
        elif op==4:
            limpiar_pantalla()
            agregar_m()
            mensaje('Se agregaron los datos por teclado')
            pausa()
        else:
            limpiar_pantalla()
            print(" "*25,"Nos vemos la próxima...")
            pausa()
            seguir=False
            limpiar_pantalla()

# Programa Principal
# Nombres para usar en la carga de los archivos
nom=['MARIA','EUGENIA','OSVALDO','JAVIER','TAMARA','AGUSTINA','MILAGROS',
         'BELEN','VERONICA','ESTEFANIA','NAHUEL','ALEXANDER','NICOLAS',
         'EZEQUIEL','ARIANA','ELIZABETH','DAIA','JORGE','MATIAS']

# vector para usar en la carga de los archivos
num=np.array([0]*10)
for i in range(10):
    num[i]=random.randint(10,50)    

# Ahora si comencemos
menu0()
