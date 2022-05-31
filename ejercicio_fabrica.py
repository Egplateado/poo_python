class Fabrica():
    def __init__(self , llantas , color , precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    
    @property
    def llantas(self):
        return self._llantas

    @property
    def color(self):
        return self._color

    @property
    def precio(self):
        return self._precio

class Carro(Fabrica):
    
    @property
    def llantas(self):
        return self._llantas

    @property
    def color(self):
        return self._color

    @property
    def precio(self):
        return self._precio

moto_1 = Moto(2 , "Negro" , 80900)
print(moto_1.color)
print(moto_1.llantas)
print(moto_1.precio)
carro_1 = Carro(4 , "plateado" , 800400)
print(carro_1.color)
print(carro_1.llantas)
print(carro_1.precio)