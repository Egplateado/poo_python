class Animales():
    def __init__(self , mensaje):
        self._mensaje = mensaje
    def hablar(self):
        print(self._mensaje)
        
class Perro(Animales):
    def hablar(self):
        print("yo hago guaaaoou\n")
class Pez(Animales):
    def hablar(self):
        print("Yo no hablo\n")
    @property
    def hablar(self):
        return "yo no hablo"
        
perro = Perro("guauo")
perro.hablar()

animal = Animales("miau!!")
animal.hablar()
    
pez = Pez("nada")
print(pez.hablar)