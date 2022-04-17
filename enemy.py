from bala import bala
import pygame
import random
pygame.mixer.init()

all_list_balas_enemy = pygame.sprite.Group()

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
    
 
        

class meteorito(enemy):
    
    sound1 = pygame.mixer.Sound("./sounds/explosionaMeteorito.wav")

    def __init__(self, posicion_x, posicion_y, velocidad_x, velocidad_y):
         super().__init__( posicion_x, posicion_y, velocidad_x, velocidad_y)
         self.image = pygame.image.load("./assets/meteoro.png")
         self.image.convert()
         self.image.set_colorkey()
         self.rect = self.image.get_rect()
         self.rect.x = posicion_x
         self.rect.y = posicion_y
         
    def impacto(self):
        self.kill()
        self.sound1.play()
   

class asteroide(enemy):
    sonid = pygame.mixer.Sound("./sounds/asteroide.wav")
    sonidexplosion = pygame.mixer.Sound("./sounds/explosionAsteroide.wav")
    posicion_y = int
    vida = int
    hola = int

    def __init__(self, posicion_x, posicion_y, velocidad_x, velocidad_y):
        super().__init__( posicion_x, posicion_y, velocidad_x, velocidad_y)
        self.image = pygame.image.load("./assets/asteroide.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey()
        self.image.convert()
        self.vida = 3
        self.posicion_y = posicion_y
        self.rect.y = self.posicion_y
        self.rect.x = posicion_x
        self.hola = 1
        

    def movimiento(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        if self.rect.y > 10 and self.rect.y < 35:
            
            self.sonid.set_volume(0.2)
            self.sonid.play()

        if self.rect.y > 3000:
            self.rect.y = random.randrange(-1000,-9000, -500)
            self.velocidad_y =random.randint(10,15)


    def destruccion(self):
        if self.vida <= 0:
            self.kill()
            self.sonid.set_volume(0.1)
            self.sonidexplosion.play()
   
       
    def cambio(self):
        if self.vida == 2:
            self.image = pygame.image.load("./assets/asteroide1.png")
        if self.vida == 1:
            self.image = pygame.image.load("./assets/asteroide2.png")
        if self.rect.y > 1500:
            self.image = pygame.image.load("./assets/asteroide.png")
            self.vida = 3
            

        


class nave_enemiga(enemy):
    sonido = pygame.mixer.Sound("./sounds/nave.wav")
    

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

        if self.rect.x > 900 or self.rect.x < 0:
            self.velocidad_x *= -1
        
        if self.rect.y > 6000:
            self.rect.y = -100
            self.velocidad_y = 6
            self.velocidad_x = -8
            
     
            self.rect.y += self.velocidad_y
            

 
    def disparar(self):

        new_bala = bala(self.rect.centerx - 40, self.rect.centery)
        all_list_balas_enemy.add(new_bala)
        new_bala2 = bala(self.rect.centerx + 40, self.rect.centery)
        all_list_balas_enemy.add(new_bala2)
        new_bala.sonido()




    def chocar(self, tiempo, entrada,final):
        
        if tiempo > entrada and tiempo < final:
            
            self.velocidad_x = 0
            self.velocidad_y = 10
            self.rect.y += self.velocidad_y
            self.sonido.set_volume(0.2)
            if self.rect.y > 60 and self.rect.y < 80:
                self.sonido.play()
            
     
        

