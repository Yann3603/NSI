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

class Player:
    def __init__(self, Pv, posX,posY, vitesse,direction, arete, noeud):
        self.pv = 100
        self.posX = posX
        self.posY = posY
        self.vitesse = vitesse
        self.direction = direction #True si on va de Sommet1 vers sommet2
        self.arete = arete
        self.noeud = noeud
        self.Sac=[]
        self.Vie=True
        self.Gauche = False
        self.JambeDroit= True

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

    def distance(self,P1,P2):
        return sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)

    def distanceJoueurNoeud(self):
        di1=sqrt((self.arete.get_sommet1().get_x()-self.posX)**2+(self.arete.get_sommet1().get_y()-self.posY)**2)
        di2=sqrt((self.arete.get_sommet2().get_x()-self.posX)**2+(self.arete.get_sommet2().get_y()-self.posY)**2)
        return di1,di2

    def deplacement(self):
        distance1,distance2 = self.distanceJoueurNoeud()
        if distance2 < 1.50 and self.direction:#on approche sufisamment du noeud sommet2: on rentre dedans
             self.noeud = self.arete.get_sommet2()
             self.posX=self.noeud.get_x()
             self.posY=self.noeud.get_y()
             self.arete=None
        elif distance1 < 1.5 and not self.direction:#on approche sufisamment du noeud sommet1: on rentre dedans
                self.noeud = self.arete.get_sommet1()
                self.posX=self.noeud.get_x()
                self.posY=self.noeud.get_y()
                self.arete=None
        else: #On est dans une arete et on avance dedans à la vitesse
            if self.direction == True:
                if self.arete.get_longueur()==0:
                    ancienX = self.posX
                    self.posX = self.posX+1
                    self.posY = self.posY+1
                    if self.posX < ancienX:
                        self.Gauche = False
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True
                    else :
                        self.Gauche = True
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True
                else:
                    ancienX = self.posX
                    self.posX=self.posX+(((self.arete.get_sommet2().get_x()-self.arete.get_sommet1().get_x())/self.arete.get_longueur())*self.vitesse)
                    self.posY=self.posY+(((self.arete.get_sommet2().get_y()-self.arete.get_sommet1().get_y())/self.arete.get_longueur())*self.vitesse)
                    if self.posX < ancienX:
                        self.Gauche = False
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True
                    else :
                        self.Gauche = True
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True

            else:
                if self.arete.get_longueur()==0:
                    ancienX = self.posX
                    self.posX = self.posX+1
                    self.posY = self.posY+1
                    if self.posX < ancienX:
                        self.Gauche = False
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True
                    else :
                        self.Gauche = True
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True
                else:
                    ancienX = self.posX
                    self.posX=self.posX+((self.arete.get_sommet1().get_x()-self.arete.get_sommet2().get_x())/self.arete.get_longueur())*self.vitesse
                    self.posY=self.posY+((self.arete.get_sommet1().get_y()-self.arete.get_sommet2().get_y())/self.arete.get_longueur())*self.vitesse
                    if self.posX < ancienX:
                        self.Gauche = False
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True
                    else :
                        self.Gauche = True
                        if self.JambeDroit == True:
                            self.JambeDroit = False
                        else :
                            self.JambeDroit = True

    def variationpv(self, Degat):
        self.Pv-=self.random.rand()*Degat
        if self.Pv<=0:
            #delete player
            self.vie=False


    def affi2d(self,labyrin,ListeNoeud,ListeJoueur):
        """ Viewer qui permet de voir le labyrinthe autour du joueur vu du dessus"""
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
        xfen=800
        yfen=600
        perx=400
        pery=300
        loupe=4
        PosXFondBlanc = 645
        PosYFondBlanc = 35
        TailleXFondBlanc = 150
        TailleYFondBlanc = 565
        TailleXFondBlancGauche = 150
        TailleYFondBlancGauche = 565
        PosXFondBlancGauche = 0
        PosYFondBlancGauche = 35
        pygame.init()
        #Ouverture de la fenêtre
        fenetre = pygame.display.set_mode((xfen, yfen))
        masque = pygame.image.load("masque.bmp").convert()
        masque = pygame.transform.scale(masque, (800, 600))
        masque.set_colorkey((255, 255, 255))
        perso = pygame.image.load("personnageDroite1 jambe gauche devant.png").convert()
        perso = pygame.transform.scale(perso, (25, 25))
        perso.set_colorkey((255,255,255))
        fondBlancDroit = pygame.image.load("FondBlanc.png").convert()
        fondBlancDroit = pygame.transform.scale(fondBlancDroit, (TailleXFondBlanc, TailleYFondBlanc))
        fondBlancDroit.set_colorkey((0, 0, 0))
        fondBlancGauche = pygame.image.load("FondBlanc.png").convert()
        fondBlancGauche = pygame.transform.scale(fondBlancDroit, (TailleXFondBlancGauche, TailleYFondBlancGauche))
        fondBlancGauche.set_colorkey((0, 0, 0))
        imageEquipements = pygame.image.load("Equipements.png").convert()
        imageEquipements = pygame.transform.scale(imageEquipements, (150, 35))
        imageEquipements.set_colorkey((0, 0, 0))
        imageCoffre = pygame.image.load("Coffre.png").convert()
        imageCoffre = pygame.transform.scale(imageCoffre, (150, 32))
        imageCoffre.set_colorkey((0, 0, 0))
        imageArmure = pygame.image.load("Armure.png").convert()
        imageArmure = pygame.transform.scale(imageArmure, (150, 30))
        imageArmure.set_colorkey((0, 0, 0))
        imageFondArmure = pygame.image.load("FondBlanc.png").convert()
        imageFondArmure = pygame.transform.scale(imageFondArmure, (150, 130))
        imageArmure.set_colorkey((0, 0, 0))
        listeTouche = ["K_KP1"]
        cont=True
        while cont:#boucle
            if self.noeud == None:  # On est dans une arete, on l'affiche
                if self.Gauche == True:
                    if self.JambeDroit == True:
                        perso = pygame.image.load("personnageGauche1 jambe droite devant.png").convert()
                        perso = pygame.transform.scale(perso, (25, 25))
                        perso.set_colorkey((255,255,255))
                    else :
                        perso = pygame.image.load("personnageGauche1 jambe gauche devant.png").convert()
                        perso = pygame.transform.scale(perso, (25, 25))
                        perso.set_colorkey((255,255,255))
                        
                    #perso = pygame.image.load("MarioGauche.png").convert()
                    #perso = pygame.transform.scale(perso, (25, 25))
                    #perso.set_colorkey((255,255,255))
                else: 
                    if self.JambeDroit == True:
                        perso = pygame.image.load("personnageDroite1 jambe droite devant.png").convert()
                        perso = pygame.transform.scale(perso, (25, 25))
                        perso.set_colorkey((255,255,255))
                    else :
                        perso = pygame.image.load("personnageDroite1 jambe gauche devant.png").convert()
                        perso = pygame.transform.scale(perso, (25, 25))
                        perso.set_colorkey((255,255,255))
                    #perso = pygame.image.load("MarioDroit.png").convert()
                    #perso = pygame.transform.scale(perso, (25, 25))
                    #perso.set_colorkey((255,255,255))
                fenetre.fill((0,0,0))
                fenetre.blit(fondBlancDroit, (PosXFondBlanc,PosYFondBlanc))
                #couleur=(248, 142, 85)
                couleur=(255,255,255)
                fenetre.blit(imageEquipements, (645, 0))
                fenetre.blit(imageFondArmure, (485, 465))
                fenetre.blit(imageArmure, (485, 430))
                for i in range(6):
                    pygame.draw.rect(fenetre,(0,0,0),(PosXFondBlanc,(35+(i*(TailleYFondBlanc//6))),TailleXFondBlanc,5)) #(posX, posY, TailleX, TailleY)
                keys = pygame.key.get_pressed()
                if keys[K_KP1]:
                    listeTouche.append("K_KP1")
                elif keys[K_KP2]:
                    listeTouche.append("K_KP2")
                elif keys[K_KP3]:
                    listeTouche.append("K_KP3")
                elif keys[K_KP4]:
                    listeTouche.append("K_KP4")
                elif keys[K_KP5]:
                    listeTouche.append("K_KP5")
                elif keys[K_KP6]:
                    listeTouche.append("K_KP6")
                if listeTouche[-1] == "K_KP1":
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+0*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(0*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(1*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(0*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                elif listeTouche[-1] == "K_KP2":
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+1*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(1*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(2*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(1*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                elif listeTouche[-1] == "K_KP3":
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+2*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(2*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(3*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(2*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                elif listeTouche[-1] == "K_KP4":
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+3*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(3*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(4*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(3*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                elif listeTouche[-1] == "K_KP5":
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+4*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(4*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(5*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(4*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                elif listeTouche[-1] == "K_KP6":
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+5*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(5*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(32+(6*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                    pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(5*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY


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
                    pygame.display.flip()
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
                            #couleur = (248, 142, 85)
                            couleur = (255,255,255)
                            pygame.draw.line(fenetre,couleur,(int(perx+(self.posX-arete.get_sommet1().get_x())*loupe), int(pery+(self.posY-arete.get_sommet1().get_y())*loupe)),(int(perx+(self.posX-arete.get_sommet2().get_x())*loupe),int(pery+(self.posY- arete.get_sommet2().get_y())*loupe)), 20)

                    arete=choixarete
                    couleur = (0, 0, 150)
                    pygame.draw.line(fenetre,couleur,(int(perx+(self.posX-arete.get_sommet1().get_x())*loupe), int(pery+(self.posY-arete.get_sommet1().get_y())*loupe)),(int(perx+(self.posX-arete.get_sommet2().get_x())*loupe),int(pery+(self.posY- arete.get_sommet2().get_y())*loupe)), 20)
                    for sommet in ListeNoeud:
                        pygame.draw.circle(fenetre, (0, 0, 255), (int(perx+(self.posX-sommet.get_x())*loupe),int( pery+(self.posY-sommet.get_y())*loupe)), 5)
                    for joueur in ListeJoueur:
                        fenetre.blit(perso, (perx-10, pery-10))
                    fenetre.blit(masque, (0, 0))
                    fenetre.blit(fondBlancGauche, (PosXFondBlancGauche,PosYFondBlancGauche))
                    fenetre.blit(fondBlancDroit, (PosXFondBlanc,PosYFondBlanc))
                    #pygame.draw.rect(fenetre,(255,255,255),(0,0,150,30))
                    fenetre.blit(imageCoffre, (0, 0))
                    fenetre.blit(imageEquipements, (645, 0))
                    fenetre.blit(imageFondArmure, (485, 465))
                    fenetre.blit(imageArmure, (485, 430))

                    for i in range(6):
                        pygame.draw.rect(fenetre,(0,0,0),(0,(35+(i*(TailleYFondBlancGauche//6))),TailleXFondBlancGauche,5)) #(posX, posY, TailleX, TailleY)
                    for i in range(6):
                        pygame.draw.rect(fenetre,(0,0,0),(PosXFondBlanc,(35+(i*(TailleYFondBlanc//6))),TailleXFondBlanc,5)) #(posX, posY, TailleX, TailleY)
                    keys = pygame.key.get_pressed()
                    if keys[K_KP1]:
                        listeTouche.append("K_KP1")
                    elif keys[K_KP2]:
                        listeTouche.append("K_KP2")
                    elif keys[K_KP3]:
                        listeTouche.append("K_KP3")
                    elif keys[K_KP4]:
                        listeTouche.append("K_KP4")
                    elif keys[K_KP5]:
                        listeTouche.append("K_KP5")
                    elif keys[K_KP6]:
                        listeTouche.append("K_KP6")
                    if listeTouche[-1] == "K_KP1":
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+0*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(0*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(1*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(0*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                    elif listeTouche[-1] == "K_KP2":
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+1*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(1*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(2*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(1*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                    elif listeTouche[-1] == "K_KP3":
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+2*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(2*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(3*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(2*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                    elif listeTouche[-1] == "K_KP4":
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+3*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(3*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(4*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(3*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                    elif listeTouche[-1] == "K_KP5":
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+4*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(4*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(5*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(4*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
                    elif listeTouche[-1] == "K_KP6":
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+5*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(5*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(32+(6*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                        pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(5*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY


                    pygame.display.flip()
                    time.sleep(0.1)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            cont=False
                            choix=False
            fenetre.blit(masque, (0, 0))
            fenetre.blit(fondBlancDroit, (PosXFondBlanc, PosYFondBlanc)) 
            fenetre.blit(imageEquipements, (645, 0))     
            fenetre.blit(imageFondArmure, (485, 465))
            fenetre.blit(imageArmure, (485, 430))
            for i in range(6):
                pygame.draw.rect(fenetre,(0,0,0),(PosXFondBlanc,(35+(i*(TailleYFondBlanc//6))),TailleXFondBlanc,5)) #(posX, posY, TailleX, TailleY)
            keys = pygame.key.get_pressed()
            if keys[K_KP1]:
                listeTouche.append("K_KP1")
            elif keys[K_KP2]:
                listeTouche.append("K_KP2")
            elif keys[K_KP3]:
                listeTouche.append("K_KP3")
            elif keys[K_KP4]:
                listeTouche.append("K_KP4")
            elif keys[K_KP5]:
                listeTouche.append("K_KP5")
            elif keys[K_KP6]:
                listeTouche.append("K_KP6")
            if listeTouche[-1] == "K_KP1":
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+0*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(0*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(1*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(0*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
            elif listeTouche[-1] == "K_KP2":
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+1*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(1*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(2*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(1*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
            elif listeTouche[-1] == "K_KP3":
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+2*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(2*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(3*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(2*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
            elif listeTouche[-1] == "K_KP4":
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+3*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(3*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(4*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(3*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
            elif listeTouche[-1] == "K_KP5":
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+4*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(4*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(5*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(4*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
            elif listeTouche[-1] == "K_KP6":
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,35+5*(TailleYFondBlanc//6),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc + TailleXFondBlanc,(35+(5*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6)+5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(32+(6*(TailleYFondBlanc//6))),TailleXFondBlanc+5,5)) #posX, posY, tailleX, tailleY
                pygame.draw.rect(fenetre,(255,0,0),(PosXFondBlanc-5,(35+(5*(TailleYFondBlanc//6))),5,(TailleYFondBlanc//6))) #posX, posY, tailleX, tailleY
            pygame.display.flip()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont = False
        pygame.quit()




class Sac:
    def __init__(self,Taille_sac,Poser,Echanger,Prendre,Plein,Objets):
        self.sac = 0
        self.Taille_sac = Taille_sac
        self.Poser = Poser
        self.Echanger = Echanger
        self.Prendre = Prendre
        self.Plein = Plein
        self.Objets = Objets
    def Poser(sac):
        if sac == True:
            sac = sac + 1

    def plein(sac,self):
        if self.sac == 20:
            return None
    def Prendre(self,objets):
        pass