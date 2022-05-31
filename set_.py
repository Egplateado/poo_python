class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    @property   
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter
    def cuenta(self , cuenta):
        self._cuenta = cuenta 
        
    
    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self , contador):
        self._contador = contador

a = A()
print(a.cuenta)
a.cuenta = 40
a.contador = 30
print(a.cuenta)
print("el valor del {} es".format(a.contador))