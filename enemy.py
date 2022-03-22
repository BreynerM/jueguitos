import pygame
import random



class enemy(pygame.sprite.Sprite):
    velocidad_x = int
    velocidad_y = int


    def __init__(self,posicion_x, posicion_y, velocidad_x, velocidad_y):
        super().__init__()
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y

    def mover(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.x > 1000 and self.rect.y > 700 or self.rect.x < 0 and self.rect.y > 700:
            self.rect.x = random.randrange(0,1000, 50)
            self.rect.y = random.randrange(-100,-200, -50)


        if self.rect.y > 700:
            self.rect.y = random.randrange(-100,-200, -50)

    def explosion(self):
        pass

    def cambio(self):

        if self.velocidad_x > 1000:
            self.velocidad_x *= -1

        elif self.velocidad_x < 0:
            self.velocidad_x *= -1
    
    # def disparar(self,velocidad_y):
        

class meteorito(enemy):


     def __init__(self, posicion_x, posicion_y, velocidad_x, velocidad_y):
         super().__init__( posicion_x, posicion_y, velocidad_x, velocidad_y)
         self.image = pygame.image.load("./assets/a/meteoro.png")
         self.image.convert()
         self.image.set_colorkey()
         self.rect = self.image.get_rect()
         self.rect.x = posicion_x
         self.rect.y = posicion_y


class asteroide(enemy):

    posicion_y = int

    def __init__(self, posicion_x, posicion_y, velocidad_x, velocidad_y):
        super().__init__( posicion_x, posicion_y, velocidad_x, velocidad_y)
        self.image = pygame.image.load("./assets/a/asteroide.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey()
        self.image.convert()
        self.posicion_y = posicion_y
        self.rect.y = self.posicion_y
        self.rect.x = posicion_x
        

    def movimiento(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.y > 3000:
            self.rect.y = random.randrange(-1000,-9000, -500)
            self.velocidad_y =random.randint(10,15)

        
      

        


class nave_enemiga(enemy):

    def __init__(self, posicion_x, posicion_y, velocidad_x, velocidad_y):
        super().__init__( posicion_x, posicion_y, velocidad_x, velocidad_y)
        self.image = pygame.image.load("./assets/a/navenemiga.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey()
        self.image.convert()
        self.rect.x = posicion_x
        self.rect.y = posicion_y

    def movimiento_nave(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.y >= 38 and self.rect.y <= 78:
            self.rect.y = 60

        if self.rect.x > 920 or self.rect.x < 0:
            self.velocidad_x *= -1
        
        if self.rect.y > 6000:
            self.rect.y = -100
            self.velocidad_y = 6
            self.velocidad_x = -8
            
     
            self.rect.y += self.velocidad_y
            

    # def disparar(self, jugador_posicion_x):

    #     pass

    def chocar(self, tiempo, entrada,final):
        print(tiempo)
        if tiempo > entrada and tiempo < final:
            self.velocidad_x = 0
            self.velocidad_y = 10
            self.rect.y += self.velocidad_y
            print(self.velocidad_y)
     
        





        


