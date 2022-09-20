import random
import numpy as np
from pyrecord import Record

x = random.randint(0,20) #Le asigno un tamaño cualquiera ya que se desconoce el ultimo

# Vector registro Tambos
T_tambos= Record.create_type('T_tambos','id_tambos','nombre','cant_litros','recaudacion',
                            id_tambos= 0, nombre= '',cant_litros= 0, recaudacion= 0)

T_leche= Record.create_type('T_leche','nombres','litros_vendidos',
                            nombres='',litros_vendidos=0)

VR_tambos= np.array([T_tambos]*x)
VR_leche= np.array([T_leche]*100)

def cargar_tambos(vector):
    for i in range (len(VR_tambos)):
        vector[i] = T_tambos()

def cargar_leche(vector):
    for i in range (len(VR_leche)):
        vector[i] = T_leche()

def corte_control(bodegas, leche):
    file = open('botellas.txt', 'r')
    line = file.readline().strip()
    line_list = line.split(',')
    codigo_tambo= int(line_list[2])
    litros_mes= 0
    monto_mes= 0

    while line != '':
        codigo_ant= codigo_tambo
        recaudacion = 0.0
        litros_vendidos = 0
        vector_leche= np.array([0]*100)

        while (line != '') and (codigo_ant== codigo_tambo):
            id_importe= float(line_list[3])
            id_leche= int(line_list[1])
            litros_vendidos += 1 
            recaudacion += id_importe
            vector_leche[id_leche] +=1
            line = file.readline().strip()

            if line != '':
                line_list = line.split(',')
                codigo_tambo= int(line_list[2])

        print(f'Cantidad recaudada en el tambo{codigo_tambo}: {recaudacion}')
        print(f'Cantidad de leche vendida en el tambo{codigo_tambo}: {litros_vendidos}')

        VR_tambos[codigo_tambo].cant_litros+= litros_vendidos
        VR_tambos[codigo_tambo].recaudacion+= recaudacion

                
        litros_mes += litros_vendidos
        monto_mes += recaudacion
    
    print(f'Total generado del mes: Recaudacion:{monto_mes}    Litros vendidos:{litros_mes}')
    return vector_leche
    file.close()

def actualizar_VR_leche(vector, act):
    for i in range(len(vector)):
        vector[i].litros_vendidos = act[i]

cargar_tambos(VR_tambos)
cargar_leche(VR_leche)
ac
