class A():
    def __init__(self):
        self.contador = 0
    def incremento(self):
        self.contador += 1
    def counter(self):
        return self.contador
class B():
    def __init__(self):
        self.__contador = 0
    def incremento(self):
        self.__contador += 1
    def counter(self):
        return self.__contador
    
a = A()
print(a.counter())
a.incremento()
print(a.counter())
print(a.contador)
print("oBJETO b")
b = B()
print(b.counter())
b.incremento()
print(b.counter())  
print(b.__contador) 