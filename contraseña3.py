class usuario():
    def __init__(nombre,contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
contraseña = 2000

print("introduce la contraseña1")
print("contraseña primera vez")
contraseña1 = input()

print("introduce la contraseña2")
print("contraseña segunda vez")
contraseña2 = input()
if (contraseña1 == contraseña2) and contraseña :
    print("pass")
elif (contraseña1 != contraseña2) and contraseña :
    print("no pass")    