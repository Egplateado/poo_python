class FabricaTelefonos():
    marca = "Samgsung"
    
    def elaborarHuawei(self):
        self.marca = "Huawei"
telefono = FabricaTelefonos()
telefono.elaborarHuawei()
print(telefono.marca)
