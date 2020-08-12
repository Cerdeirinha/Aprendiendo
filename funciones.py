def saludar(nombre):
    return "hola {} bienvenido al juego de cody".format(nombre)

print("ingresa tu nombre")
nombre = input()

print(saludar(nombre))
