import pygame, sys, random
from enemy import * 


size  = (800, 500)

lista_meter = []

RED = (255, 51, 81)
WHITE = (250, 250, 250)
BLACK = (10, 10, 10)




for i in range (30):
    size = random.randint(10, 20)
    velocidad_x = random.uniform(-1 ,1)
    velocidad_y = random.randint(1,3)
    position_x = random.randint(100,900)
    position_y = random.randint(0,100)
    color = RED
    meter = meterorito(size, velocidad_x, velocidad_y,color, position_x, position_y)
    lista_meter.append(meter)
    
    

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    screen.fill(WHITE)

    for meter in lista_meter:
        pygame.draw.circle(screen,meter.color,(meter.position_x, meter.position_y), meter.size)  
        meter.position_x += meter.velocidad_x
        meter.position_y += meter.velocidad_y
        
        if meter.position_y > 620:
            meter.position_y = 0
            meter.velocidad_y = random.randint(1 , 4)

        if meter.position_x > 1000 or position_x < 0:
            meter.position_x = random.randint(100,900)




    pygame.display.flip()
    clock.tick(30)
    

  

    