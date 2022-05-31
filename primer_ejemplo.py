from os import system

class FabricaDeTelefonos():
    marca = "Realme"
    color = "negro"
    memoria_Ram = 8
    almacenamiento = 128

    def llamar(self,mensaje):
        return mensaje
    def escucha(self):
        print("Estas escuchando musica\n")

telefono = FabricaDeTelefonos()
telefono.marca
telefono.color
telefono.llamar("Hola mundo\n")
print(telefono.color) 
print(telefono.llamar("Hello world\n"))
telefono.escucha()
print("Practicando git")
print("Este es otro ejemplo")