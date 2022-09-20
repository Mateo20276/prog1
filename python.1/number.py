import numpy as np
from pyrecord import Record

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
for i in range(620):
    print(f" {vcuentas[i].Numero_cuenta}  {vcuentas[i].Apellidos}   {vcuentas[i].Nombre}  {vcuentas[i].DNI}  {vcuentas[i].Tipo_Cuenta}  {vcuentas[i].Saldo}   {vcuentas[i].Actividad}" )