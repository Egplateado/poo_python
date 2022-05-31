class animals():
     def habla(self):
         print("Im a animal\n")
     def description(self):
         print("yo soy un/a {}".format(self._animal))
         
         
class dog(animals):
    def __init__(self , animal):
        self._animal = animal
        
    


class Abeja(animals):
    def __init__(self, animal):
        self._animal = animal
        


animal = animals()
animal.habla ()     
osbin = dog("Osbin")
osbin.description()
abeja = Abeja("Abeja")
abeja.description()