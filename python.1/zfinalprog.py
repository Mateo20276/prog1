import numpy as np
from pyrecord import Record
#Mateo Asenzo
#DNI: 44167155
#Legajo: 173577


#Bodegas es el vector de registro
#Uvas es el vectores de registro

def cortecontrol():
    a1 = open("BOTELLAS.TXT", "r")
    linea = a1.readline().strip()
    sup = linea.split(",")
    bodega = int(sup[2])
    tbotellas = 0
    timporte = 0
    vecbodegabotella = np.array([0]*len(int(Bodegas)))
    vecbodegaimoprte = np.array([0]*len(int(Bodegas)))
    vecuvasbotellas = np.arrat([0]*len(int(Uvas)))
    cont = 0
    while linea != "":
        bodegaant = bodega
        cbotellas = 0
        importe = 0
        cont = cont + 1
        while linea != "" and bodega != bodegaant:
            importe = importe + float(sup[3])
            iduvas = int(sup[1])
            vecuvasbotellas[iduvas] = vecuvasbotellas[iduvas] + 1
            linea = a1.readline().strip()
            cbotellas = cbotellas + 1
            if linea != "":
                sup = linea.split(",")
                bodega = int(sup[2])
        tbotellas = tbotellsa + cbotellas
        timporte = timporte + importe
        vecbodegabotella[cont] = cbotellas
        vecbodegaimporte[cont] = importe
        cont = cont + 1
        print(f"La cantidad de botellas vendidas de la bodega {bodegaant} fueron {cbotellas}")
        print(f"El importe obetenido de la bodega {bodegaant} fue de ${importe}")
    print(f"Total de botellas vendidas del mes: {tbotellas}")
    print(f"Total del importe obtenido del mes: ${timporte}")
    a1.close

cortecontrol()

def actualizarBodegas():
    for i in range(len(Bodegas)):
        Bodegas[i] = Rbodegas() #Rbodegas es el nombre del registro
        Cantbot[i] = Cantobot[i] + vecbodegabotella[i]
        Recaudacion[i] = Recaudacion[i] + vecbodegaimoprte[i]

actualizarBodegas()

def actualizarUvas():
    for i in range(len(Uvas)):
        Uvas[i] = Ruvas() #Ruvas es el nombre del registro
        Botellas[i] = Botellas[i] + vecuvasbotellas[i]

actualizarUvas()