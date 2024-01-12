from re import T
from tkinter import TRUE
import pygame
import os

# Colores del juego
Blanco = (255,255,255)
Negro = (0,0,0)
Rojo = (255,0,0)
Amarillo = (255,255,0)

#Tamaño de pantalla y titulo del juego
Largo_pantalla = 600
Ancho_pantalla = 600

Pantalla = pygame.display.set_mode((Largo_pantalla,Ancho_pantalla))
pygame.display.set_caption("Snake")

#Fondos de pantalla
Fondo_pantalla_1 = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes','Fondo_1.jpg')), (Largo_pantalla,Ancho_pantalla))
Fondo_pantalla_2 = pygame.transform.scale(pygame.image.load(os.path.join('Imagenes','Fondo_2.jpg')), (Largo_pantalla,Ancho_pantalla))

#Cantidad de FPS
FPS = 60

clock = pygame.time.Clock()
run = True

#FUNCIÓN DE DIBUJO DE FONDOS Y OBJETOS 
def draw_window(Pantalla,Fondo_pantalla_2):

    Pantalla.blit(Fondo_pantalla_2,(0,0))
    pygame.display.update()

Pantalla.blit(Fondo_pantalla_1,(0,0))
pygame.display.update()
pygame.time.delay(4000)

while run:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False
            pygame.quit()

    draw_window(Pantalla,Fondo_pantalla_2)
    


