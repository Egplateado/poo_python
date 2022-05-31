class Animales():
    def __init__(self , nombre):
        self._nombre = nombre
        
class Perro(Animales):
    def __init__(self , nombre ,  sonido):
        super().__init__(nombre)
        self._sonido = sonido
    @property
    def nombre(self):
        return self._nombre

perro = Perro("Firulais" , "gua_guauoo!")
print(perro.nombre)
        
         
            