import random

def escribir():
    a1 = open("lluvia.txt", "w")
    for i in range(8):
        p = random.randint(0, 100)
        linea = (f"{i}-9-2021-{p} \n")
        a1.write(linea)
        

    a1.close
escribir()
def mostrar():
    a1 = open("lluvia.txt", "r")
    linea = a1.readline().strip()
    print(linea)
    while linea != "":    
        linea = a1.readline().strip()
        print(linea)

    a1.close


def verdatos():
    dsl = 0
    dclm = 0
    dcls = 0
    a1 = open("lluvia.txt", "r")
    linea = a1.readline()
    while linea != "":
       sep = linea.split("-")
       sep[3] = int(sep[3])
       if sep[3] == 0:
           dsl = dsl + 1
       if sep[3] > 0 and sep[3] < 50 :
           dclm = dclm + 1
       if sep[3] > 50 and sep[3] < 100:
           dcls = dcls + 1
       linea = a1.readline()
    print(f"Días sin lluvia: {dsl} ")
    print(f"Días con lluvia menores a 50 mm: {dclm} ")
    print(f"Días con lluvia mayores a 50 mm: {dcls} ")
    a1.close


escribir()
mostrar()
verdatos()
