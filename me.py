import pygame
from bala import bala_jugador

BLACK=(0,0,0)


all_list_balas_player = pygame.sprite.Group()

class jugador(pygame.sprite.Sprite):
    
    impactaAster = pygame.mixer.Sound("./sounds/naveMeterorito.wav")
    imMetero = pygame.mixer.Sound("./sounds/naveAsteroide.wav")
    velocidad = int
    vida = int

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120,120))
        self.image = pygame.image.load("./assets/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.velocidad = 10
        self.vida = 6
        
        self.rect.centerx = 400
        self.rect.y = 450

    def mover(self, wigth):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.x = 0

        if tecla[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > wigth:
                self.rect.right = wigth
            

    def disparar(self, event, disparo):

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if disparo == True:
                    new_bala = bala_jugador(self.rect.centerx, self.rect.top)
                    all_list_balas_player.add(new_bala)
                    new_bala.sonido()

    def impactoAster(self):
        self.impactaAster.set_volume(0.1)
        self.impactaAster.play()
        
    def impactoMeter(self):
        self.imMetero.set_volume(0.5)
        self.imMetero.play()       

    def explotar(self):
        if self.vida <= 0:
            self.kill()
            
    
            