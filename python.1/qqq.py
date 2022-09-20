def limpiar_pantalla():
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')
    return None