from turtle import Screen
import pygame,sys

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
size = (800, 500)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mixer.init()

coord_x = 350
coord_y = 425 

x_speed = 0
y_speed = 0


#Cerrar ventana 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = -10
            if event.key == pygame.K_RIGHT:
                x_speed = 10

        screen.fill(WHITE)

        coord_x += x_speed

        pygame.draw.rect(screen, BLACK, (coord_x, coord_y, 50,50))
        

        pygame.display.flip()




  

    