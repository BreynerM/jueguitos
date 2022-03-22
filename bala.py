import pygame


class bala(pygame.sprite.Sprite):
    velocidad_y = int

    def __init__(self, posicion_x, posicion_y, velocidad_y ):
        super().__init__()
        self.velocidad_y = velocidad_y
        self.image = pygame.image.load("./assets/a/bala.png")
        self.image.convert()
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.centerx = posicion_x
        self.rect.y = posicion_y

    def mover(self):
        self.rect.y += self.velocidad_y

        if self.rect.y > 600:
            self.kill()

