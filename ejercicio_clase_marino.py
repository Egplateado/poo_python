class Marino():
    def hablar(self):
        return "Hola que hace"

class Pulpo(Marino):
    
    def hablar(self):
        return "Hola soy un pulpo"

class Foca(Marino):
    def __init__(self, mensaje):
        self._mensaje = mensaje
        
    @property
    def mensaje(self):
        return self._mensaje

foca = Foca("Hola soy una foca")
pulpo = Pulpo()

print(pulpo.hablar())
print(foca.mensaje)
