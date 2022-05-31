class FabricadeTelefonos():
    def __init__(self , marca , *colores, **modelos ):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos
        
telefono = FabricadeTelefonos("HUAWEI", "azul" , "NEGRO", "Gris" , "ROJO" , mi = 500, m2= 5001 , m3 = 402)
telefono.memoria = 128
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
print(telefono.memoria)
