class Estudiante():
    def __init__(self , nombre , nota):
        self._nombre = nombre
        self._nota = nota
    
    def resultados(self):
        if self._nota < 7:
            print("No has aprobado")
        else:
            print("Has Aprobado\n")
        
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota

Estudiante_1 = Estudiante("Omar" , 9)
Estudiante_2 = Estudiante("Karla" , 5)

print(f"el nombre del alumno es {Estudiante_1.nombre}\n")
print(f"El estudiante {Estudiante_1.nombre} tiene una nota de {Estudiante_1.nota}")
Estudiante_1.resultados()
print(f"el nombre del alumn@ es {Estudiante_2.nombre}\n")
print(f"El estudiante {Estudiante_2.nombre} tiene una nota de {Estudiante_2.nota}")
Estudiante_2.resultados()


    
    
    