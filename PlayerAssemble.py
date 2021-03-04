# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:15:45 2021

@author: antonin.lelong
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:29:18 2021

@author:
"""
import labyrinthe
import pygame
import pygame.gfxdraw
from pygame.locals import *
import os
import random
from math import sqrt
from math import cos,sin,pi
import time

# bon courage

class Player:
    def __init__(self, posX,posY, vitesse,direction, arete, noeud):
        self.pv = 100
        self.posX = posX
        self.posY = posY
        self.vitesse = vitesse
        self.direction = direction
        self.arete = arete
        self.noeud = noeud
        self.Sac=[]
        self.vie=True

    def set_x(self,X):
        """Setter de la position x du joueur

        Args:
            X (int): position x du joueur
        """
        self.posX = X

    def get_x(self):
        """Getter de la position x du joueur

        Returns:
            int: position x
        """
        return self.posX

    def set_y(self,Y):
        """Setter de la position Y du joueur

        Args:
            Y (int): position Y du joueur
        """
        self.posY = Y

    def get_y(self):
        """Getter de la position y du joueur

        Returns:
            int: position y
        """
        return self.posY

    def affi2d(self,labyrin,ListeNoeud,ListeJoueur):
        """ Viewer qui permet de voir le labyrinthe autour du joueur vu du dessus"""
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
        xfen=800
        yfen=600
        perx=400
        pery=300
        loupe=4
        pygame.init()
        #Ouverture de la fenÃªtre
        fenetre = pygame.display.set_mode((xfen, yfen))
        masque = pygame.image.load("masque.bmp").convert()
        masque = pygame.transform.scale(masque, (800, 600))
        masque.set_colorkey((255, 255, 255))
        perso = pygame.image.load("perso.png").convert()
        perso = pygame.transform.scale(perso, (20, 20))
        perso.set_colorkey((0, 0, 0))

        cont=True
        while cont:#boucle
            if self.noeud == None:  # On est dans une arete, on l'affiche
                fenetre.fill((0,0,0))
                couleur=(150, 0, 100)
                for arete in labyrin:
                    pygame.draw.line(fenetre,couleur,(int(perx+(self.posX-arete.get_sommet1().get_x())*loupe), int(pery+(self.posY-arete.get_sommet1().get_y())*loupe)),(int(perx+(self.posX-arete.get_sommet2().get_x())*loupe),int(pery+(self.posY- arete.get_sommet2().get_y())*loupe)), 20)
                for sommet in ListeNoeud:
                    pygame.draw.circle(fenetre, (0, 0, 255), (int(perx+(self.posX-sommet.get_x())*loupe),int( pery+(self.posY-sommet.get_y())*loupe)), 5)
                for joueur in ListeJoueur:
                    fenetre.blit(perso, (perx-10, pery-10))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    self.direction = True
                    self.deplacement()
                if keys[pygame.K_DOWN]:
                    self.direction = False
                    self.deplacement()
            else: #On est dans un noeud, on l'affiche
                #On affiche toutes les sorties avec des flèches
                choix=True
                choixarete=self.noeud.get_aretes()[0]
                indice=0
                while choix:#Boucle tant que on a pas choisit l'arete
                    # On attend le choix du joueur pour la direction à prendre
                    # gauche droite choix de l'arete, espace pour entrer dans l'arete
                    fenetre.fill((0, 0, 0))
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        if indice < len(self.noeud.get_aretes()) - 1:
                            if self.noeud.get_aretes()[indice + 1].get_longeur() > 0.01:
                                choixarete = self.noeud.get_aretes()[indice + 1]
                                indice += 1
                    if keys[pygame.K_RIGHT]:
                        if indice > 0:
                            if self.noeud.get_aretes()[indice - 1].get_longeur() > 0.01:
                                choixarete = self.noeud.get_aretes()[indice - 1]
                                indice -= 1
                    if keys[pygame.K_SPACE]:
                        choix = False  # On rentre dans l'arete choisie
                        self.arete = choixarete
                        if self.noeud==self.arete.get_sommet1():
                            self.direction= True
                        else:
                            self.direction =False
                        self.noeud = None
                    for arete in labyrin:
                        if arete!=choixarete:
                            couleur = (150, 0, 100)
                            pygame.draw.line(fenetre,couleur,(int(perx+(self.posX-arete.get_sommet1().get_x())*loupe), int(pery+(self.posY-arete.get_sommet1().get_y())*loupe)),(int(perx+(self.posX-arete.get_sommet2().get_x())*loupe),int(pery+(self.posY- arete.get_sommet2().get_y())*loupe)), 20)

                    arete=choixarete
                    couleur = (0, 0, 150)
                    pygame.draw.line(fenetre,couleur,(int(perx+(self.posX-arete.get_sommet1().get_x())*loupe), int(pery+(self.posY-arete.get_sommet1().get_y())*loupe)),(int(perx+(self.posX-arete.get_sommet2().get_x())*loupe),int(pery+(self.posY- arete.get_sommet2().get_y())*loupe)), 20)
                    for sommet in ListeNoeud:
                        pygame.draw.circle(fenetre, (0, 0, 255), (int(perx+(self.posX-sommet.get_x())*loupe),int( pery+(self.posY-sommet.get_y())*loupe)), 5)
                    for joueur in ListeJoueur:
                        fenetre.blit(perso, (perx-10, pery-10))
                    fenetre.blit(masque, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.1)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            cont=False
                            choix=False

            fenetre.blit(masque, (0, 0))
            pygame.display.flip()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont=False
        pygame.quit()



   
   
class Sac:
    def __init__(self,taille_sac,plein):
        self.taille_sac = taille_sac
        self.objets = []
        self.sac= len(self.objet)
    
    def get_taille_max(self):
        return self.taille_sac
    
    def get_contenu(self):
        """
        Getter contenu du sac
        
        Returns:
            list: objet
        """
        return self.objets
        
    def get_taille_util(self):
        return self.sac
        
    

    def plein(self):
        if len(self.objets) == taille_sac:
            return True
        else:
            return False
            
            
    
    def Prendre(self,objets):
        if plein() != False:
            pass
        else:
            pass
        
    def poser():
        pass
    
    
    
    def Afficher():
        pass
    

class Balle:  # La classe balle est une classe enfant de la classe Player. Elle hérite donc de ses méthodes et valeurs
    def __init__(self, posX, posY, vitesse, direction, arete, type_balle):
        if type_balle == "perforante":
            self.degats = random.randint(25,30)
        elif type_balle == "explosive":
            self.degats = random.randint(35,45)
        else:
            self.degats = random.randint(20,23)
        self.posX = posX
        self.posY = posY
        self.vitesse = vitesse
        self.direction = direction
        self.arete = arete

    def set_type(self, type_balle):
        """Changer le type de la balle

        Args:
            type_balle (string): type de la balle (perforante/explosive/normale)
        """
        self.type_balle = type_balle

    def get_type(self):
        """Getter du type de balle

        Returns:
            string: type de la balle
        """
        return self.type_balle

        def set_x(self, X):
        """Setter de la position x du joueur

        Args:
            X (int): position x du joueur
        """
        self.posX = X

    def get_x(self):
        """Getter de la position x du joueur

        Returns:
            int: position x
        """
        return self.posX

    def set_y(self,Y):
        """Setter de la position Y du joueur

        Args:
            Y (int): position Y du joueur
        """
        self.posY = Y

    def get_y(self):
        """Getter de la position y du joueur

        Returns:
            int: position y
        """
        return self.posY
