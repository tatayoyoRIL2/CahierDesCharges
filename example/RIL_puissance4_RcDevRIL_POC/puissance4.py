#######IMPORTATION DES LIB REQUISES#####

import pygame
import sys
import time
from pygame.locals import *

########################################

#########VARIABLES GLOBALES#############

origin = (0,0)
screen = pygame.display.set_mode((1280,720),RESIZABLE)

########################################

pygame.init()#lancement de pygame

######CHARGEMENT DES IMAGES DU JEU######

backGround=pygame.image.load("resource/Grille2.png").convert()
sizeBG = backGround.get_size()
yel = pygame.image.load("resource/PionJaune.png").convert_alpha() #convert_alpha() résoud la transparence
sizeYel = yel.get_size()
red = pygame.image.load("resource/PionRouge.png").convert_alpha()
sizeRed = red.get_size()

########################################

#######AFFICHAGE "PLATEAU" DU JEU#######

screen = pygame.display.set_mode(sizeBG)
screen.blit(backGround,origin)
pygame.display.flip() #update TOUT le screen

draw=1
while draw:
    for event in pygame.event.get():

        if event.type == QUIT:

            draw = 0

screen = pygame.display.quit()
