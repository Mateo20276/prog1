import numpy as np
from pyrecord import Record
from funciones_utiles import limpiar_pantalla
Rcuentas = Record.create_type("Rcuentas","Numero_cuenta","Apellido","Nombre","DNI","Tipo_Cuenta","Saldo","Actividad",
                            Numero_cuenta = 0,Apellido = "",Nombre = "",DNI = "",Tipo_Cuenta = 0,Saldo = 0.0,Actividad = False)

vcuentas = np.array([Rcuentas]*620)



def cargarveccuenta():
    a1 = open("cuentas.txt","r")
    linea = a1.readline().strip()
    sup = linea.split(",")
    while linea != "":

        for i in range (600):
            vcuentas[i] = Rcuentas()
            vcuentas[i].Numero_cuenta = int(sup[0])
            vcuentas[i].Apellidos = str(sup[1])
            vcuentas[i].Nombre = str(sup[2])
            vcuentas[i].DNI = str(sup[3]) 
            vcuentas[i].Tipo_Cuenta = int(sup[4])
            vcuentas[i].Saldo = float(sup[5])
            vcuentas[i].Actividad = bool(sup[6])
            linea = a1.readline().strip()
            sup = linea.split(",")
    for i in range(600, 620):
        vcuentas[i] = Rcuentas()
        vcuentas[i].Numero_cuenta = int(0)
        vcuentas[i].Apellidos = str(0)
        vcuentas[i].Nombre = str(0)
        vcuentas[i].DNI = str(0)
        vcuentas[i].Tipo_Cuenta = int(0)
        vcuentas[i].Saldo = float(0)
        vcuentas[i].Actividad = bool(False)        

    a1.close()

cargarveccuenta()


def dardealta1600():#Creé una nueva cuenta
    vcuentas[600].Numero_cuenta = 1600
    vcuentas[600].Actividad = True

dardealta1600()

Rcajeros = Record.create_type("Rcajeros","nro_cajero","ubicacion","cant_mov",   nro_cajero = 0, ubicacion = "", cant_mov = 0)                              

vcajeros = np.array([Rcajeros]*120)

def cargarveccajeros():
    a1 = open("cajeros.txt","r")
    linea = a1.readline().strip()
    sup = linea.split(",")
    while linea != "":
        for i in range(120):
            vcajeros[i] = Rcajeros()
            vcajeros[i].nro_cajero = int(sup[0])
            vcajeros[i].ubicacion = str(sup[1])
            vcajeros[i].cant_mov = int(sup[2])
            linea = a1.readline().strip()
            sup = linea.split(",")
    a1.close()

cargarveccajeros()

def saldocuenta():
    c = int(input("Escribe el numero de cuenta del que quieras saber la informacion: "))
    while c <1000 or c > 1620:
        print("Esa cuenta no existe")
        c = int(input("Escribe el numero de cuenta del que quieras saber la informacion: "))

    s = c - 1000
    print(f"El numero de cuenta con nombre {vcuentas[s].Nombre} y apellido {vcuentas[s].Apellidos} posee un saldo de ${vcuentas[s].Saldo}")
            


    

vec1 = np.array([0.0]*601)
vec2 = np.array([0]*120)
def datosmovimientos():
    a2 = open("operaciones.txt", "r")
    linea = a2.readline().strip()
    sup = linea.split(",")
    c = 0
    cuenta = sup[0]
    
    while linea != "":
        suma = 0
        
        ncuenta = cuenta
        
        while linea != "" and cuenta == ncuenta:
            caj = int(sup[4]) - 1
            if int(sup[5]) == 1:
                suma = suma + float(sup[6])
            elif int(sup[5]) == 2:
                suma = suma - float(sup[6])
            vec2[caj] +=  1    
            linea = a2.readline().strip()
            sup = linea.split(",")
            cuenta = sup[0]
        vec1[c] = suma
        c = c + 1



    a2.close



def totalmov():
    print(f"Cuenta         Movimiento")
    for i in range(601):
        print(f" {vcuentas[i].Numero_cuenta}      {vec1[i]}")

def cajmmov():
    c = 0
    for i in range(120):
        if vec2[i] > c:
            c = vec2[i]
            s = i
            l = s + 1
    print(f"El cajero {l} realizo la mayor cantidad de movimientos con un total de {c}")

        




 
def actsaldocuenta():
    for i in range(601):
        vcuentas[i].Saldo = vcuentas[i].Saldo + vec1[i]




def actsaldocajero():
    for i in range(120):
        vcajeros[i].cant_mov = vcajeros[i].cant_mov + vec2[i]

def dardealta(p):
    selec = str(input("Escribe tu DNI: "))
    locacion = False
    
    for i in range(620):
        if vcuentas[i].DNI == selec:
            if vcuentas[i].Actividad == True:
                print("El dni ya esta registrado, estos son tus datos:")
                print(f"Numero de cuenta: {vcuentas[i].Numero_cuenta}  Apellido: {vcuentas[i].Apellidos}  Nombre: {vcuentas[i].Nombre}")
                print(f"DNI: {vcuentas[i].DNI} Tipo de cuenta: {vcuentas[i].Tipo_Cuenta}  Saldo: {vcuentas[i].Saldo}  Actividad: {vcuentas[i].Actividad}")
            else:
                vcuentas[i].Actividad = True
                print("El dni ya esta registrado sin embargo estaba dado de baja, porque lo que se le ha dado de alta.")
                print("Esta es su información:")
                print(f"Numero de cuenta: {vcuentas[i].Numero_cuenta}  Apellido: {vcuentas[i].Apellidos}  Nombre: {vcuentas[i].Nombre}")
                print(f"DNI: {vcuentas[i].DNI} Tipo de cuenta: {vcuentas[i].Tipo_Cuenta}  Saldo: {vcuentas[i].Saldo}  Actividad: {vcuentas[i].Actividad}")
            locacion = True 
    if locacion == False:
        print("La cuenta no esta registrada, ingrese los siguientes datos para darla de alta: ")
        Apellido = str(input("Ingrese su apellido: "))
        Nombre = str(input("Ingrese su nombre: "))
        Tipodecuenta = int(input("Ingrese su tipo de cuenta: "))
        Saldo = float(input("Ingrese su saldo: "))
        vcuentas[p].Numero_cuenta = p + 1000
        vcuentas[p].Apellidos = Apellido
        vcuentas[p].Nombre = Nombre
        vcuentas[p].DNI = selec
        vcuentas[p].Tipo_Cuenta = Tipodecuenta
        vcuentas[p].Saldo = Saldo
        vcuentas[p].Actividad = True


#dardealta()

def borrarcuenta():
    baja = int(input("Ingrese la cuenta que quiera dar de baja: "))
    real = int(baja - 1000)
    if vcuentas[real].Actividad == False:
        print(f"El cliente {vcuentas[real].Apellidos} {vcuentas[real].Nombre} con DNI {vcuentas[real].DNI} ya estaba dado de baja.")
    else:
        vcuentas[real].Actividad = False
        print(f"El cliente {vcuentas[real].Apellidos} {vcuentas[real].Nombre} con DNI {vcuentas[real].DNI} ha sido dado de baja.")

#borrarcuenta()

def modificarcuenta():
    mod = int(input("Ingrese la cuenta que quiera modificar: "))
    while mod < 1000 or mod > 1620:
        mod = int(input("Ingrese la cuenta que quiera modificar: "))

    real = int(mod - 1000)
    print("Si desea modificar el apellido ingrese la letra A")
    print("Si desea modificar el nombre ingrese la letra N")
    print("Si desea modificar el DNI ingrese la letra D")
    print("Si desea modificar el tipo de cuenta ingrese la letra T")
    s = str(input().upper())
    if s == "A":
        ap = str(input("Ingrese el nuevo apellido: "))
        vcuentas[real].Apellidos = ap

    if s == "N":
        nom = str(input("Ingrese el nuevo nombre: "))
        vcuentas[real].Nombre = nom

    if s == "D":
        dni = str(input("Ingrese el nuevo dni: "))
        vcuentas[real].DNI = dni

    if s == "T":
        tpd = int(input("Ingrese el nuevo tipo de cuenta: "))
        vcuentas[real].Tipo_Cuenta = tpd

def menu():
    seguir = True
    l = int(601)
    while seguir:
        print("Que desea hacer?")
        print("1.Consultar saldo de cuenta")
        print("2.Informar el total anuela de los movimientos de cada cuenta")
        print("3.Informar que cajero registro mayor cantidad de movimientos")
        print("4.Actualizar el saldo de las cuentas")
        print("5.Actualizar la cantidad de movimientos de cada cajero")
        print("6.Dar de baja una cuenta")
        print("7.Dar de alta una cuenta")
        print("8.Modificar una cuenta")
        print("9.Volver todo al estado original")
        print("10.Mostrar toda la informacion de una cuenta")
        print("0.Terminar de realizar operacines")
        print("")
        num = int(input("Escriba el numero de la operacion a realizar: "))
        print("")
        while num < 0 or num > 10:
            num = int(input("Escriba el numero de la operacion a realizar: "))
            print("")
        limpiar_pantalla()
        if num == 1:#
            saldocuenta()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 2:#
            datosmovimientos()
            totalmov()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 3:#
            datosmovimientos()
            cajmmov()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 4:#
            actsaldocuenta()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 5:#
            actsaldocajero()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 6:#
            borrarcuenta()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 7:#
            dardealta(l)
            input("De un enter para continuar")
            limpiar_pantalla()
            l = l + 1
        if num == 8:#
            modificarcuenta()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 9:
            cargarveccuenta()
            dardealta1600()
            cargarveccajeros()
            input("De un enter para continuar")
            limpiar_pantalla()
        if num == 10:
            un = int(input("De que cuenta desea ver la información: "))
            while un < 1000 or un > 1620:
                print("Cuenta invalida")
                un = int(input("De que cuenta desea ver la información: "))
            una = un - 1000
            print("")
            print(f"Numero de cuenta:{vcuentas[una].Numero_cuenta}  Apellido: {vcuentas[una].Apellidos}   Nombre: {vcuentas[una].Nombre}")
            print(f"DNI: {vcuentas[una].DNI}  Tipo de cuenta: {vcuentas[una].Tipo_Cuenta}  Saldo: {vcuentas[una].Saldo}    Actividad: {vcuentas[una].Actividad}" )
            limpiar_pantalla()

            print("")
            input("De un enter para continuar")
            limpiar_pantalla()

        if num == 0:
            print("El programa ha finalizado")
            seguir = False
            input("De un enter para continuar")
            limpiar_pantalla()

menu()






    











