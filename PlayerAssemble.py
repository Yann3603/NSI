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
        
    def distance(self,P1,P2):
        return sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)

    def distanceJoueurNoeud(self):
        if self.arete!=None:
            if self.direction == True:
                distanceJN = sqrt((self.arete.get_sommet2().get_x()-self.posX)**2+(self.arete.get_sommet2().get_y()-self.posY)**2)
            else:
                distanceJN = sqrt((self.arete.get_sommet1().get_x()-self.posX)**2+(self.arete.get_sommet1().get_y()-self.posY)**2)
        else:
            distanceJN=-1.0
        return distanceJN

    def deplacement(self):
        distance = self.distanceJoueurNoeud()
        if distance < 1.0 and distance>0:#on approche sufisemment d'un noeud: on rentre dedans
            if self.direction == True:
                self.noeud = self.arete.get_sommet2()
                self.posX=self.noeud.get_x()
                self.posY=self.noeud.get_y()
                self.arete=None
            else :
                self.noeud = self.arete.get_sommet1()
                self.posX=self.noeud.get_x()
                self.posY=self.noeud.get_y()
                self.arete=None
        elif distance==-1:#on est dans un noeud et il faut choisir quelle arete prendre maintenant
            self.arete=self.noeud.aretes[random.randint(0,len(self.noeud.aretes)-1)]#on choisit le premier pour l'instant, à modifier...
            self.noeud=None #on sort du noeud
        else: #On est dans une arete et on avance dedans à la vitesse
            if self.direction == True:
                if self.arete.get_longueur()==0:
                    self.posX = self.posX+1
                    self.posY = self.posY+1
                else:
                    self.posX=self.posX+(((self.arete.get_sommet2().get_x()-self.arete.get_sommet1().get_x())/self.arete.get_longueur())*self.vitesse)
                    self.posY=self.posY+(((self.arete.get_sommet2().get_y()-self.arete.get_sommet1().get_y())/self.arete.get_longueur())*self.vitesse)
            else:
                if self.arete.get_longueur()==0:
                    self.posX = self.posX+1
                    self.posY = self.posY+1
                else:
                    self.posX=self.posX+((self.arete.get_sommet1().get_x()-self.arete.get_sommet2().get_x())/self.arete.get_longueur())*self.vitesse
                    self.posY=self.posY+((self.arete.get_sommet1().get_y()-self.arete.get_sommet2().get_y())/self.arete.get_longueur())*self.vitesse

    def gestionclavier(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.arete== None:#On est dans un noeud et on veut prendre une arete
            self.arete = self.noeud.aretes[0]  # on choisit le premier pour l'instant, à modifier...
            self.noeud=None
            self.deplacement()
        if keys[pygame.K_RIGHT]and self.arete== None:
            self.arete = self.noeud.aretes[-1]  # On  est dans un noeud on choisit le dernier pour l'instant, à modifier...
            self.noeud=None
            #self.deplacement()
        if keys[pygame.K_UP] and self.noeud== None:
            self.direction=True
            self.deplacement()
        if keys[pygame.K_DOWN] and self.noeud == None:
            self.direction = False
            self.deplacement()

    def variationpv(self, Degat):
        self.Pv-=self.random.rand()*Degat
        if self.Pv<=0:
            #delete player
            self.vie=False

    def blitRotate(self,surf, image, pos, originPos, angle):
        w, h = image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        pivot = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot
        origin = (
        pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])
        rotated_image = pygame.transform.rotate(image, angle)
        surf.blit(rotated_image, origin)


    def afficheur(self,labyrin,ListeNoeud,ListeJoueur):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
        pygame.init()
        #Ouverture de la fenêtre
        xfen=1400
        yfen=1000
        cont=True
        #Ouverture de la fenêtre
        fenetre = pygame.display.set_mode((xfen, yfen))
        #Chargement des images
        perso = pygame.image.load("perso.png").convert()
        perso = pygame.transform.scale(perso, (50, 80))
        perso.set_colorkey((0, 0, 0))
        mur = pygame.image.load("mur4.bmp").convert()
        mur = pygame.transform.scale(mur, (200, 50))
        mur.set_colorkey((255, 255, 255))
        sol = pygame.image.load("sol.bmp").convert()
        sol = pygame.transform.scale(sol, (1200, 1200))
        sol.set_colorkey((255, 255, 255))
        salle = pygame.image.load("salle.png").convert()
        salle = pygame.transform.scale(salle, (400,300))
        salle.set_colorkey((0, 0, 0))
        masque = pygame.image.load("masque.bmp").convert()
        masque = pygame.transform.scale(masque, (800, 600))
        masque.set_colorkey((255, 255, 255))
        alpha = 0
        perx=375
        pery=260
        while cont:
        #Ouverture de la fenêtre
            fenetre.fill((0, 0, 0))
            self.gestionclavier()
            distance = self.distanceJoueurNoeud()
            if self.noeud==None:#On est dans une arete, on l'affiche
                #on récupère l'angle de l'arete
                alpha=self.arete.get_angle()
                #on affiche le fond
                fenetre.blit(sol,(-600+perx+self.posX-self.arete.get_sommet1().get_x(),-600+pery+self.posY-self.arete.get_sommet1().get_y()))
                #on affiche le mur du fond
                #on calcul l'endroit pour le premier mur
                w, h = mur.get_size()
                #pos = (fenetre.get_width() / 2-70+self.posX-self.arete.get_sommet2().get_x(), fenetre.get_height() / 2-70+self.posY-self.arete.get_sommet2().get_y())
                #on calcule v vecteur directeur de l'arete de norme 1
                v=((self.arete.get_sommet2().get_x()-self.arete.get_sommet1().get_x())/self.arete.get_longueur(),(self.arete.get_sommet2().get_y()-self.arete.get_sommet1().get_y())/self.arete.get_longueur())
                if v[0]<0:
                    u=(-10*v[1],10*v[0])#vecteur orthogonal à u vers le haut
                else:
                    u=(10*v[1],-10*v[0])#vecteur orthogonal à u vers le haut
                #On affiche les noeuds
                fenetre.blit(salle, (200+self.posX-self.arete.get_sommet2().get_x(), 150+self.posY-self.arete.get_sommet2().get_y()))
                fenetre.blit(salle, (200+self.posX-self.arete.get_sommet1().get_x(), 150+self.posY-self.arete.get_sommet1().get_y()))

                #on affiche le mur arrière
                #on recherche la valeur de k pour laquelle on peut voir le mur
                #while self.distance((self.arete.get_sommet1().get_x()+(k+1)*(w-10)*v[0],self.arete.get_sommet1().get_y()+(k+1)*(w-10)*v[1]),(self.posX,self.posY))>400:
                 #   k=k+1
                k=0
                while self.distance((self.arete.get_sommet1().get_x()+k*(w-20)*v[0],self.arete.get_sommet1().get_y()+k*(w-20)*v[1]),(self.posX,self.posY))<600:
                    pos=(perx+self.posX-(arete.get_sommet1().get_x()+(k-0.5)*(w-20)*v[0]+u[0]),self.posY+pery-(self.arete.get_sommet1().get_y()+(k-0.5)*(w-20)*v[1]+u[1]))
                    self.blitRotate(fenetre, mur, pos, (w / 2, h / 2), alpha)
                    k=k+1
                #on affiche le personnage
                fenetre.blit(perso, (perx, pery))
                #on affiche le mur du devant
                k=0
                while self.distance((self.arete.get_sommet1().get_x()+k*(w-20)*v[0],self.arete.get_sommet1().get_y()+k*(w-20)*v[1]),(self.posX,self.posY))<600:
                    pos=(perx+self.posX-(arete.get_sommet1().get_x()+(k-0.5)*(w-20)*v[0]-u[0]),self.posY+pery-(self.arete.get_sommet1().get_y()+(k-0.5)*(w-20)*v[1]-u[1]))
                    self.blitRotate(fenetre, mur, pos, (w / 2, h / 2), alpha)
                    k=k+1

            else: #On est dans un noeud, on l'affiche
                #On affiche toutes les sorties avec des flèches
                choix=True
                xd=400
                yd=300
                choixarete=self.noeud.get_aretes()[0]
                indice=0
                while choix:#Boucle tant que on a pas choisit l'arete
                    fenetre.blit(salle, (200, 150))
                    for arete in self.noeud.get_aretes() :
                        if arete.get_sommet2()==self.noeud and arete.get_longueur()>0.1:
                            flechex = (((arete.get_sommet1().get_x() - arete.get_sommet2().get_x()) / arete.get_longueur()) * 150)
                            flechey = (((arete.get_sommet1().get_y() - arete.get_sommet2().get_y()) / arete.get_longueur()) * 150)
                        else:
                            if arete.get_longueur()>0.1:
                                flechex = ((arete.get_sommet2().get_x() - arete.get_sommet1().get_x()) / arete.get_longueur()) * 150
                                flechey = ((arete.get_sommet2().get_y() - arete.get_sommet1().get_y()) / arete.get_longueur()) * 150
                                #On trace la fleche
                        if arete==choixarete:
                            pygame.draw.polygon(fenetre, (255, 0, 0),((xd+0, yd+00), (xd+flechex, yd+flechey), (xd-flechey*20/150, yd+flechex*20/150),(xd+0,yd+0)))
                        else:
                            pygame.draw.polygon(fenetre, (0, 255, 0),((xd+0, yd+00), (xd+flechex, yd+flechey), (xd-flechey*20/150, yd+flechex*20/150),(xd+0,yd+0)))
                    #on affiche le joueur"""
                    fenetre.blit(perso, (375, 260))
                    #On attend le choix du joueur pour la direction à prendre
                    #gauche droite choix de l'arete, espace pour entrer dans l'arete
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        if indice <len(self.noeud.get_aretes())-1:
                            if self.noeud.get_aretes()[indice + 1].get_longeur()>0.01:
                                choixarete = self.noeud.get_aretes()[indice+1]
                                indice+=1
                    if keys[pygame.K_RIGHT]:
                        if indice >0:
                            if self.noeud.get_aretes()[indice - 1].get_longeur()>0.01:
                                choixarete = self.noeud.get_aretes()[indice-1]
                                indice-=1

                    if keys[pygame.K_SPACE] :
                        choix=False #On rentre dans l'arete choisie
                        self.noeud=None
                        self.arete=choixarete
                    fenetre.blit(masque, (0, 0))
                    pygame.draw.rect(fenetre, (0, 0, 0), (800, 600, xfen, yfen))
                    for arete in labyrin:
                        pygame.draw.line(fenetre, (0, 0, 100),
                                         (800 + arete.get_sommet1().get_x(), 400 + arete.get_sommet1().get_y()),
                                         (800 + arete.get_sommet2().get_x(), 400 + arete.get_sommet2().get_y()), 6)
                    for sommet in ListeNoeud:
                        pygame.draw.circle(fenetre, (0, 0, 255), (800 + sommet.get_x(), 400 + sommet.get_y()), 5)
                    for joueur in ListeJoueur:
                        pygame.draw.circle(fenetre, (255, 255, 255),
                                           (800 + int(joueur.get_x()), 400 + int(joueur.get_y())), 5)
                    pygame.display.flip()
                    time.sleep(0.050)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            cont=False
                            choix=False

        #on affiche le masque
            fenetre.blit(masque, (0, 0))
            pygame.draw.rect(fenetre, (0, 0, 0), (800, 600, xfen, yfen))
            pygame.draw.rect(fenetre, (0, 0, 0), (800, 0, xfen, 600))
            pygame.draw.rect(fenetre, (0, 0, 0), (0, 600, 800, yfen))
            for arete in labyrin:
                pygame.draw.line(fenetre, (0, 0, 100),
                             (800 + arete.get_sommet1().get_x(), 400 + arete.get_sommet1().get_y()),
                             (800 + arete.get_sommet2().get_x(), 400 + arete.get_sommet2().get_y()), 6)
            for sommet in ListeNoeud:
                pygame.draw.circle(fenetre, (0, 0, 255), (800 + sommet.get_x(), 400 + sommet.get_y()), 5)
            for joueur in ListeJoueur:
                pygame.draw.circle(fenetre, (255, 255, 255),
                               (800 + int(joueur.get_x()), 400 + int(joueur.get_y())), 5)
            fenetre.blit(masque, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont=False
        pygame.quit()
        
        
'''
class Armes:
    def __init__(self,
'''

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
