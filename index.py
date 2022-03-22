from funciones_enemy import *
from escenario import *
import pygame
pygame.init()



numero = 60
WHITE = (255, 255, 255)



# def explosion(position_x, position_y):
    
#         pr = pygame.draw.circle(screen,RED,(position_x, position_y),8)
#         pr = pygame.draw.circle(screen,RED,(position_x, position_y),8)
#         pr = pygame.draw.circle(screen,RED,(position_x, position_y),8)
#         pr = pygame.draw.circle(screen,RED,(position_x, position_y),8)
#         pr = pygame.draw.circle(screen,RED,(position_x, position_y),8)
#         pr_list.append(pr)

  


BLACK = (0,0,0)

disparo = bool
ancho = 1000
alto = 600
size = (ancho, alto)
screen = pygame.display.set_mode(size)
nave = 60
crear = 20
tinicial = 0
tfinal = 0
inicio = 20
crear_meteroritos(numero)
clock = pygame.time.Clock()
aux = 1
correr = True
supreme = 60

escenaro()

while correr:
    tiempo = int(pygame.time.get_ticks()/ 1000)
    if aux == tiempo:
        print(tiempo)
        aux += 1
        disparo = True
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False

    screen.fill(BLACK)

    for punto in all_puntos:
        
        pygame.draw.circle(screen,WHITE,(punto.posicion_x,punto.posicion_y),punto.grosor)
        punto.mover()

        
       

    all_list_meteoritos.draw(screen)
    
    
    for meter in all_list_meteoritos:
        meter.mover()
    
    
    all_list_asteroides.draw(screen)
    for aster in all_list_asteroides:
        aster.movimiento()
        
    all_list_nave_enemiga.draw(screen)
    for nave in all_list_nave_enemiga:
      
        nave.movimiento_nave()

    all_list_balas.draw(screen)
    
        # nave.chocar(tiempo)
        # print(nave.rect.y)
        # if nave.rect.x == player.posicion_x:
        #     nave.disparar()
    
    #         print(aster.rect.y)
    # if tiempo > 30 and tiempo < 35:
    #     all_list_asteroides.draw(screen)
    #     for aster in all_list_asteroides:
    #         aster.movimiento()

    # if tiempo == inicio:
        
    #     tinicial += 20
    #     tfinal = tinicial + 15
    #     inicio += 20
        
    if tiempo == crear:
        crear_asteroides(6)
        crear += 20
        
    if tiempo == nave:
        crear_naves_enemigas()
        entrada_nave = nave + 20
        final_nave = entrada_nave + 20
        nave+= 60
    

    if tiempo == supreme:
        entrada_nave = supreme + 20
        final_nave = entrada_nave + 5
        supreme += 60
        

    for nave in all_list_nave_enemiga:
        nave.chocar(tiempo, entrada_nave, final_nave)
        if nave.rect.y == 60:
            if disparo: 
                bala_disparada(nave.rect.centerx, nave.rect.centery, 15)
                disparo = False


    for balas in all_list_balas:
        balas.mover()
        
    # if tiempo > nave and tiempo > :
    #     for nave in all_list_nave_enemiga:
    #         nave.velocidad_x = 0
    #         nave.velocidad_y = 10
    #         nave.rect.y += 81
            

    
    pygame.display.flip()




pygame.quit()
  

    