class Universidad():
    def __init__(self , nombre_u):
        self._nombre_u = nombre_u

class Carrer():
    def __init__(self , especialidad):
        self._especialidad = especialidad
        
class Estudiante(Universidad , Carrer):
    def __init__(self ,nombre_u ,especialidad , nombre , edad):
        super().__init__(nombre_u)
        super().__init__(especialidad)
        self._nombre = nombre
        self._edad = edad
        print(f"El estudiante se llama {self._nombre}, tiene {self._edad} años , en la especialidad de {self._especialidad} ,en la universidad de {self._nombre_u} ")


persona = Estudiante("UPIITA", "ISISA" , "OMAR" , 24)
