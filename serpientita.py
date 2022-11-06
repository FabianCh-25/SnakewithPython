import pygame, sys,time, random
#importamos librerias

#speed velocidad
speed= 15
#tamaño de la ventana
tamaño_ancho=720
tamaño_alto=480


check_errors = pygame.init()
if(check_errors[1]>0):
    print("Error "+ check_errors[1])
else:
    print("Iniciando juego Snake ")  
    
#Se abre la ventana del juego

   