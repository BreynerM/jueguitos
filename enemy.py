from turtle import position


class meterorito():
    size = int
    velocidad_x = float
    velocidad_y = int
    color = ()
    position_x = int
    position_y = int
    

    def __init__(self, size, velocidad_x, velocidad_y, color, position_x , position_y, ):
        self.size = size
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.color = color
        self.position_x = position_x
        self.position_y = position_y



class asteroide(meterorito):



    def __init__(self, size, velocidad_x, velocidad_y, color, position_x, position_y):
        super().__init__(size, velocidad_x, velocidad_y, color, position_x, position_y)



class nave(meterorito):
    ancho = int
    alto = int

    def __init__(self, size, velocidad_x, velocidad_y, color, position_x, position_y, ancho, alto):
        super().__init__(size, velocidad_x, velocidad_y, color, position_x, position_y)
        self.alto = alto
        self.ancho = ancho

    



        


