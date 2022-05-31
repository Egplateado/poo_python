class fabricade_muniecas():
    def __init__(self,ojo_color,vestido_color): #metodo init o constructor
        self.color = ojo_color
        self.color_vest = vestido_color
        print("El objeto {} ha sido creado".format(self.color))
        #El destructor o metodo del
    #metodo strinh 
    def __str__(self):
        return "EL OBJETO ES {}".format(self.color)
        
        
    def __del__(self):
        print("el objeto {} ha sido destruido".format(self.color))
barbie = fabricade_muniecas("verde" , "ROJO")
print(barbie.color_vest)
print(barbie)