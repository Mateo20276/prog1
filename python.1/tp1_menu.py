# Importar código fuente
from tp1_funciones import *

# ---------------------------------------------------------------
def menu1():
    v1=[0]*250  #-100 y 100
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Ejercicio 1")
        print()
        print(" "*25,"1 Cargar Valores")
        print(" "*25,"2 Mostrar Vector")
        print(" "*25,"3 Cant de Pos, Neg y Ceros")
        print(" "*25,"4 Mayor Número Cargado")
        print(" "*25,"5 Posiciones Impares y su suma")
        print()
        print(" "*28,"0 Salir")
        op=elegir(5)
        if op==1:
            print()
            cargaint(v1,-100,100)
            print(" "*20,'El vector fue cargado')
            pausa()
        elif op==2:
            print()
            mostrar(v1)
            pausa()
        elif op==3:
            print()
            neg,pos,cer=npc(v1)
            print(" "*20,f'La cantidad de Negativos es: {neg}')
            print(" "*20,f'La cantidad de Positivos es: {pos}')
            print(" "*20,f'La cantidad de Ceros es    : {cer}')
            pausa()
        elif op==4:
            may=mayor(v1)
            print()
            print(" "*20,f'El número Mayor en el vector es: {may}')
            pausa()
        elif op==5:
            pos_imp_y_suma(v1)
            pausa()
        else:
            seguir=False

# ---------------------------------------------------------------
def menu2():
    v2=[" "]*10 # apellidos
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Ejercicio 2")
        print()
        print(" "*25,"1 Cargar Apellidos")
        print(" "*25,"2 Mostrar Vector")
        print(" "*25,"3 Buscar un Apellido")
        print()
        print(" "*28,"0 Salir")
        op=elegir(3)
        if op==1:
            print()
            cargastr(v2,"Apellido")
            print(" "*20,'El vector fue cargado')
            pausa()
        elif op==2:
            print()
            mostrar(v2)
            pausa()
        elif op==3:
            print()
            print(" "*20,end=" ")
            ape=input(" Ingrese el apellido a buscar: ")
            if busca_ape(v2,ape):
                esta="SI"
            else:
                esta="NO"
            print(" "*20,f'El apellido {ape} {esta} está en el vector')
            pausa()
        else:
            seguir=False

# ---------------------------------------------------------------
def menu3():
    v3=[0]*5000 # 18 y 80
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Ejercicio 3")
        print()
        print(" "*25,"1 Cargar Vector Edades")
        print(" "*25,"2 Mostrar Vector Edades")
        print(" "*25,"3 Mostrar edad Mayor Frecuencia")
        print()
        print(" "*28,"0 Salir")
        op=elegir(3)
        if op==1:
            print()
            cargaint(v3,18,80)
            print(" "*20,'El vector fue cargado')
            pausa()
        elif op==2:
            mostrar(v3)
            pausa()
        elif op==3:
            print()
            masf=edad_mayor_frec(v3)
            print(" "*20,f'La edad que más se repite es: {masf}')
            pausa()
        else:
            seguir=False

# ---------------------------------------------------------------
def menu4():
    v4=[0]*40   # -10 y 10
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Ejercicio 4")
        print()
        print(" "*25,"1 Cargar Vector")
        print(" "*25,"2 Mostrar Vector")
        print(" "*25,"3 Eliminar Negativos")
        print(" "*25,"4 Eliminar Repetidos")
        print()
        print(" "*25,"0 Salir")
        op=elegir(4)
        if op==1:
            print()
            cargaint(v4,-10,10)
            print(" "*25,'El vector fue cargado')
            pausa()
        elif op==2:
            mostrar(v4)
            pausa()
        elif op==3:
            elim_neg(v4)
            print(" "*20,'Se eliminaron todos los negativos')
            pausa()
        elif op==4:
            print()
            modif=repetidos(v4)
            print(" "*20,'Se quitaron las repeticiones')
            print(" "*20,f'La cantidad de modificaciones fue: {modif}')
            pausa()
        else:
            seguir=False

# ---------------------------------------------------------------
def menu0():
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Principal")
        print()
        print(" "*25,"1 Ejercicio 1")
        print(" "*25,"2 Ejercicio 2")
        print(" "*25,"3 Ejercicio 3")
        print(" "*25,"4 Ejercicio 4")
        print()
        print(" "*28,"0 Salir")
        op=elegir(4)
        if op==1:
            menu1()
        elif op==2:
            menu2()
        elif op==3:
            menu3()
        elif op==4:
            menu4()
        else:
            limpiar_pantalla()
            print(" "*25,"Nos vemos la próxima...")
            pausa()
            seguir=False
            limpiar_pantalla()
# Programa principal

menu0()