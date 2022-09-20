from pyrecord import Record
import random

alumnos =   Record.create_type("alumnos","legajo","nombre","apellido","n1","n2","n3", legajo )

notas = [alumnos]*2

for i in range(2):
    notas[i] = alumnos()
    notas[i].legajo = random.randint(10, 100)
    notas[i].nombre = random.randint(10, 100)
    notas[i].apellido = 4
    notas[i].n1 = random.randint(10, 100)
    notas[i].n2 = random.randint(10, 100)
    notas[i].n3 = random.randint(10, 100)


for i in range(len(notas)):
    print(str(notas[i].legajo) + "   " + str(notas[i].nombre) + "   " + str(notas[i].apellido) + "   " + str(notas[i].n1) + "   " + str(notas[i].n2) + "   " + str(notas[i].n3))

print(notas)
    
