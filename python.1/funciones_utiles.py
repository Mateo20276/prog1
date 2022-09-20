# Funciones
import os, random

# hace una pausa poniendo un cartel
def pausa():
    print()
    print(" "*20,end=" ")
    input(" Presione Enter para continuar...")

def mensaje(m):
    print()
    print(" "*20,m+'...')

#  Esto sirve para detectar el Sist Operativo
#  Y envía la orden de limpiar la pantalla según corresponda.
#  'posix' (sistemas POSIX y distribuciones de Linux).
#  'nt' (Windows).
def limpiar_pantalla():
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')
    return None
    
# Permite elegir aociones de menú
# Validando entre 0 y el pasado por parámetro
# Y retornando la opción elegida 
def elegir(ultimo):
    print()
    print(" "*22,end=" ")
    opc=int(input(" Elija una opción: "))
    while((opc>ultimo) or (opc<0)):
        print(" "*20,"Lo siento, la Opción es inválida")
        print(" "*22,end=" ")
        opc=int(input(" Elija una opción: "))
    return opc

