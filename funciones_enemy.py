import pygame
import random
from enemy import asteroide,meteorito, nave_enemiga
from bala import bala

all_list_sprite = pygame.sprite.Group()
all_list_meteoritos = pygame.sprite.Group()
all_list_asteroides = pygame.sprite.Group()
# list_tiempo = []
all_list_nave_enemiga = pygame.sprite.Group()
all_list_balas = pygame.sprite.Group()



def crear_meteroritos(i):
    for i in range (i):
        posicion_x = random.randrange(0,1000,100)
        posicion_y = random.randrange(-100, -500, -50)
        velocidad_x = random.randint(-2,2)
        velocidad_y = random.randint(1,3)
        new_meteorito = meteorito(posicion_x, posicion_y,velocidad_x, velocidad_y)
        all_list_sprite.add(new_meteorito)
        all_list_meteoritos.add(new_meteorito)


def crear_asteroides(number):
    for i in range(number):
        posicion_x = random.randrange(100,1000,200)
        posicion_y = random.randrange(-4000, -5500, -500)
        velocidad_x = 0
        velocidad_y = random.randint(10,12)
        new_asteroide = asteroide(posicion_x, posicion_y, velocidad_x,velocidad_y)
        all_list_sprite.add(new_asteroide)
        all_list_asteroides.add(new_asteroide)


def crear_naves_enemigas():
    posicion_x = random.randrange(0,1000,100)
    posicion_y = -100
    velocidad_y = 10
    velocidad_x = -8
    new_nave = nave_enemiga(posicion_x, posicion_y, velocidad_x, velocidad_y)
    all_list_sprite.add(new_nave)
    all_list_nave_enemiga.add(new_nave)

# def crear_intervalor():
#     xinicial = 20
#     for i in range(30):
#         xinicial += 30
#         xfinal = xinicial + 15
#         list_tiempo.append([xinicial,xfinal])
        
def bala_disparada(posicion_central, posicion_y, velocidad_y):
    new_bala = bala(posicion_central, posicion_y,velocidad_y)
    all_list_balas.add(new_bala)
    all_list_sprite.add(new_bala)




