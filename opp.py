#OPP we have atributos and metodos 
#Process --->> 1_ Create instance of the objet
#--->> 2_ Construct the objet   --->> 3_ use the instance of the objet
class animal():
    def __init__(self , name , sound , *color , ** lugar):# un * para tuplas y dos ** para lista
        self._name = name
        self._sound = sound
        self._color = color
        self._lugar = lugar
        
    @property
    def name(self):
        return self._name
    @property
    def sound(self):
        return self._sound
    @property
    def color(self):
        return self._color
    @property
    def lugar(self):
        return self._lugar

dog = animal("Osbibn" , "barf" , "gris" , "cafe" , "negro" , m1  = "Tlapa" , m2 = "Temalaca" , m3 = "Cuautla")
print(dog.name)
print(f"the dog produce the next sound {dog.sound}")
print(dog.color)
print(f"the dog live in the follow places {dog.lugar}")

