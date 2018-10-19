 #Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
window = pygame.display.set_mode((640, 480))

#Variable qui continue la boucle si = 1, stoppe si = 0
continued = 1 

#Boucle infinie permettant de faire tourner l'écran en continue
while continued:
    continue