import pygame, sys, random
pygame.init()
from enemy import * 


size  = (800, 500)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))

aux = 1

lista_meter = []
lista_aster = []


RED = (255, 51, 81)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
GREY = (185, 183, 183)
YELLOW =(243, 230, 15)


for j in range(3):
    size = 30
    velocidad_x = 0
    velocidad_y = random.randint(8,11)
    color = RED
    position_x= random.randrange(30,970, 100)
    position_y= 0
    aster = asteroide(size,velocidad_x,velocidad_y,color,position_x,position_y)
    lista_aster.append(aster)

    


for i in range (30):
    size = random.randint(10, 20)
    velocidad_x = random.uniform(-1 ,1)
    velocidad_y = random.randint(1,3)
    position_x = random.randint(100,900)
    position_y = random.randint(0,100)
    color = GREY
    meter = meterorito(size, velocidad_x, velocidad_y,color, position_x, position_y)
    lista_meter.append(meter)
    
    
nave_enemiga = nave(20,9,5,YELLOW,500,-20,40,40)




while True:
    
    tiempo = int(pygame.time.get_ticks()/1000)

    if aux == tiempo:
        aux += 1
        print(tiempo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    screen.fill(BLACK)

    if tiempo > 10 and tiempo < 40:
        for aster in lista_aster:
            pygame.draw.circle(screen, aster.color,(aster.position_x, aster.position_y), aster.size)
            aster.position_y += aster.velocidad_y


    for meter in lista_meter:
        pygame.draw.circle(screen,meter.color,(meter.position_x, meter.position_y), meter.size)  
        meter.position_x += meter.velocidad_x
        meter.position_y += meter.velocidad_y
        
        if meter.position_y > 620:
            meter.position_y = 0
            meter.velocidad_y = random.randint(1 , 4)

        if meter.position_x > 1000 or position_x < 0:
            meter.position_x = random.randint(100,900)

    

    if tiempo > 15 and tiempo < 120 :
        pygame.draw.rect(screen,nave_enemiga.color, pygame.Rect(nave_enemiga.position_x,nave_enemiga.position_y,nave_enemiga.ancho,nave_enemiga.alto))
        
        if nave_enemiga.position_x > 980 or nave_enemiga.position_x < 10:
            nave_enemiga.velocidad_x *= -1
            

        if nave_enemiga.position_y >= 60:
            nave_enemiga.position_y = 60 

        if tiempo > 20:
            nave_enemiga.velocidad_x = 0
            nave_enemiga.velocidad_y += 10

        
        print(nave_enemiga.position_x)
        nave_enemiga.position_y += nave_enemiga.velocidad_y
        nave_enemiga.position_x += nave_enemiga.velocidad_x


    



    pygame.display.flip()
    clock.tick(30)
    

  

    