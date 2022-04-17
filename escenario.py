import random

all_puntos = []

class escenario():
    posicion_x = int
    posicion_y = int
    grosor = int
    velocidad = float

    def __init__(self, posicion_x, posicion_y, grosor, velocidad):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.grosor = grosor
        self.velocidad = velocidad

    def mover(self):
        self.posicion_y += self.velocidad
        if self.posicion_y > 600:
            self.posicion_y = -10



def escenaro():
    for i in range (120):
        position_x = random.randrange(1,1000,20)
        position_y = random.randrange(1,600,30)
        velocidad = 0.8
        grosor = 1
        punto = escenario(position_x, position_y, grosor,velocidad)
        all_puntos.append(punto)

