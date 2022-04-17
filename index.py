from dis import dis
from funciones_enemy import *
from escenario import *
import pygame
from enemy import all_list_balas_enemy

from me import *
pygame.init()
pygame.mixer.init()

numero = 80
WHITE = (255, 255, 255)
RED =(255,160,122)
ORANGE = (255,69,0)
BLACK = (0,0,0)
nombre = ()

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

sonido_explosion_enemigos = pygame.mixer.Sound("./sounds/explosion.wav")

disparo == True

player = jugador()
all_list_sprite.add(player)
all_list_sprite_jugador.add(player)

canales = 64

canciones = ["./sounds/fondo.mp3","./sounds/fin.mp3"]

pygame.mixer.music.load(canciones[0])
print(pygame.mixer.set_num_channels(canales))
print(pygame.mixer.get_num_channels())



pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

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
        player.disparar(event,disparo)

    screen.fill(BLACK)

    for punto in all_puntos:
        pygame.draw.circle(screen,WHITE,(punto.posicion_x,punto.posicion_y),punto.grosor)
        
        
        punto.mover()


    
        
    all_list_sprite.draw(screen)

    
    player.mover(ancho)
    player.explotar()
    if player.vida == 0:
        disparo = False
        pygame.mixer.music.stop()
        
        
    
   
          
    music = pygame.mixer.music.get_busy()
    if music == False:
        pygame.mixer.music.load(canciones[1])
        pygame.mixer.music.play()
        
   
        
   

    all_list_balas_player.draw(screen)

    for meter in all_list_meteoritos:
        meter.mover()
       
    
    
    all_list_asteroides.draw(screen)
    for aster in all_list_asteroides:
        aster.movimiento()
        aster.cambio()
        
        
        
        
        
    all_list_nave_enemiga.draw(screen)
    for nave in all_list_nave_enemiga:
      
        nave.movimiento_nave()

    all_list_balas_enemy.draw(screen)
    
      
   
    hit = pygame.sprite.groupcollide(all_list_balas_player, all_list_meteoritos, True, True)
    if hit:
        crear_meteroritos(1)

    for aster in all_list_asteroides:
        hit = pygame.sprite.spritecollide(aster, all_list_balas_player,True)
        if hit:
           
            aster.vida -= 1
            aster.destruccion()
            
        collision5 = pygame.sprite.spritecollide(aster,all_list_sprite_jugador,False)
        if collision5:
            player.vida -= 3
            screen.fill(ORANGE)
            aster.kill()
            player.impactoMeter()
   
        
        
    hit3 = pygame.sprite.groupcollide(all_list_balas_player,all_list_balas_enemy,True, True)    

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
                nave.disparar()
                disparo = False


    for balas in all_list_balas_enemy:
        balas.mover()
        
    for balas in all_list_balas_player:
        balas.moverbala()
            
    for metero in all_list_meteoritos:
        collision2 = pygame.sprite.spritecollide(metero, all_list_sprite_jugador,False)
        if collision2:
            player.vida -= 1
            metero.kill()
            player.impactoAster()
            screen.fill(ORANGE)
            
    
    collision3 = pygame.sprite.groupcollide(all_list_sprite_jugador,all_list_nave_enemiga,False,True)
    if collision3:
        player.vida -= 5
        screen.fill(ORANGE)


    collision4 = pygame.sprite.spritecollide(player, all_list_balas_enemy,True)
    if collision4:
        player.vida -= 1
        screen.fill(ORANGE)


        
        


    collision4 = pygame.sprite.spritecollide(player, all_list_balas_enemy,True)
    if collision4:
        screen.fill(ORANGE)
        player.vida -= 1

    
        

    pygame.display.flip()

   
pygame.quit()