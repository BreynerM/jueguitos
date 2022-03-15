from turtle import width
import pygame,sys

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player():
        def __init__(self):
            self.rect = self.get_rect()
            self.rect.centerx = WIDTH // 2
            screen.fill = HEIGHT -10
            self.speed_x = 0

        def mov(self):
            self.speed_x = 0
            keystate = pygame.key.get_pressed()
            if keystate [pygame.K_LEFT]:
                self.speed_x = -5
            if keystate [pygame.K_RIGHT]:
                self.speed_x = 5
            self.rect.x += self.speed_x
            


#Cerrar ventana 
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False  

        pygame.display.flip()
        Player.draw(screen)
        

        
pygame.quit()
    

