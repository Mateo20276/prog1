# Funciones
import os, random
def pausa():
    print()
    print(" "*20,end=" ")
    input(" Presione Enter para continuar...")

def limpiar_pantalla():
#  Esto sirve para detectar el Sist Operativo
#  Y envía la orden de limpiar la pantalla según corresponda.
#  'posix' (sistemas POSIX y distribuciones de Linux).
#  'nt' (Windows).
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')

def mostrar(v):
    for i in range (len(v)):
        print(v[i],end="  ")
    print()

def cargaint(v,inf,sup):
    for i in range (len(v)):
        v[i]=random.randint(inf,sup)

def cargastr(v,cartel):
    # for i in range (len(v)):
    #     v[i]=input(f'Ingrese {cartel}: ')

# Para no tener que cargarlos
    v[0]='Maradona'
    v[1]='Messi'
    v[2]='Armani'
    v[3]='Romero'
    v[4]='Otamendi'
    v[5]='Pezzella'
    v[6]='Tagliafico'
    v[7]='Di María'
    v[8]='Paredes'
    v[9]='Lo Celso'


def elegir(ultimo):
    print()
    print(" "*22,end=" ")
    opc=int(input(" Elija una opción: "))
    while((opc>ultimo) or (opc<0)):
        print(" "*20,"Lo siento, la Opción es inválida")
        print(" "*22,end=" ")
        opc=int(input(" Elija una opción: "))
    return opc

# ---------------------------------------------------------------
# Funciones de Menú 1
def npc(v):
    n,p,c=0,0,0
    for i in range(len(v)):
        if v[i]<0:
            n=n+1
        elif v[i]>0:
            p=p+1
        else:
            c=c+1
    return n,p,c

def mayor(v):
    m=v[0]
    for i in range(1,len(v)):
        if v[i]>m:
            m=v[i]
    return m        

def pos_imp_y_suma(v):
    suma=0
    print(" "*20,'Elementos de las posiciones Impares del vector')
    print()
    for i in range(1,len(v),2):
        print(v[i],end=" ")
        suma=suma+v[i]
    print()
    print()
    print(" "*20,f'La suma de los valores en la posiciones impares es: {suma}')

# ---------------------------------------------------------------
# Funciones de Menú 2
def busca_ape(v,a):
    i=0
    esta=False
    while v[i]!=a and i<len(v)-1:
        i=i+1
    if v[i]==a:
        esta=True
    return esta

# ---------------------------------------------------------------
# Funciones Menú 3

def mayor_pos(v):
    m=v[0]
    p=0
    for i in range(1,len(v)):
        if v[i]>m:
            m=v[i]
            p=i
    pos=p+18
    return pos        

def edad_mayor_frec(v):
    vf=[0]*63 # 18 y 80
    for i in range(len(v)):
        vf[v[i]-18]=vf[v[i]-18]+1
    mfrec=mayor_pos(vf)
    return mfrec

# ---------------------------------------------------------------
# Funciones Menú 4
def elim_neg(v):
    for i in range(len(v)):
        if v[i]<0:
            v[i]=v[i]+15

def repetidos(v):
    cam=0
    for j in range(15):
        bus=j
        band=True
        for i in range(len(v)):
            if v[i]==j:
                if band:
                    band=False
                else:
                    v[i]=-1
                    cam=cam+1
    return cam
