 #Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
window = pygame.display.set_mode((640, 480))
#Affichage de l'image de test
background = pygame.image.load("img/background_test.png").convert()
window.blit(background, (0,0))
#Affichage perso de test
myCaracter = pygame.image.load("img/perso_test.png").convert_alpha()
window.blit(myCaracter, (640/2, 480/2))
#Rafraichissement de l'écran pour afficher les images
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continued = 1 
#Boucle infinie permettant de faire tourner l'écran en continue
while continued:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continued = 0      #On arrête la boucle
