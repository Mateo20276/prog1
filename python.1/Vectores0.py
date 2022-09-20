edad = int(input("Escriba su edad entre 15 y 20: "))
while (edad < 15 or edad > 25) and edad != 0:
    print("Escribe nuevamente la edad")
    edad = int(input("Escriba su edad entre 15 y 25: "))