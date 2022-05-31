from os import system


class Calculadora():
    def __init__(self):
        self._num_1 = int(input("Ingrese el primer valor:\n"))
        self._num_2 = int(input("ingrese el segundo valor:\n"))
              
    def suma(self):
        self._suma = self._num_1 + self._num_2
        return self._suma
   
        
    def resta(self):
        self._resta = self._num_1 - self._num_2
        return self._resta
    
        
    def division(self):
        self._division = self._num_1 / self._num_2
        return self._division

    
    def multiplica(self):
        self._multiplica = self._num_1 * self._num_2
        return self._multiplica
    
   

         
calcula = Calculadora()
system("cls")
print(f"El resultado de la suma es {calcula.suma()}")
print(f"El resultado de la resta es {calcula.resta()}")
print(f"El resultado de la division es {calcula.division()}")
print(f"El resultado de la multiplicacion es {calcula.multiplica()}")


      
        