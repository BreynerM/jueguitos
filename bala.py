import pygame
pygame.mixer.init()

class bala(pygame.sprite.Sprite):
    velocidad_y = int
    sound = pygame.mixer.Sound("./sounds/laser.ogg")
    def __init__(self, posicion_x, posicion_y ):
        super().__init__()
        self.image = pygame.image.load("./assets/bala.png")
        self.image.convert()
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.centerx = posicion_x
        self.rect.y = posicion_y
        self.sound.set_volume(0.2)
        self.velocidad_y = 25

    def mover(self):
        self.rect.y += self.velocidad_y

        if self.rect.y > 600:
            self.kill()
    
    def sonido(self):
        self.sound.play()

class bala_jugador(bala):

    def __init__(self, posicion_x, posicion_y):
        super().__init__(posicion_x, posicion_y)
        self.image = pygame.image.load("./assets/balajugador.png")
        self.velocidad_y = 20

    def moverbala(self):
        
        self.rect.y -= self.velocidad_y

        if self.rect.y < 0:
            self.kill()
        
    
    

