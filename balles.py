import random
import pygame
from laby import *
from labyrinthe import *
from player4 import *


class Balle:
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

    def distanceBalleNoeud(self):
        if self.arete!=None:
            if self.direction == True:
                distanceBN = sqrt((self.arete.get_sommet2().get_x()-self.posX)**2+(self.arete.get_sommet2().get_y()-self.posY)**2)
            else:
                distanceBN = sqrt((self.arete.get_sommet1().get_x()-self.posX)**2+(self.arete.get_sommet1().get_y()-self.posY)**2)
        else:
            distanceBN=-1.0
        return distanceBN


    def tirer(self):
        distance = self.distanceBalleNoeud()
        tir = True
        while tir:
            if distance < 1.0 and distance > 0:
                self.arete = None
                tir = False
            else:
                if self.direction == True:
                    if self.arete.get_longueur() == 0:
                        self.posX = self.posX + 1
                        self.posY = self.posY + 1
                    else:
                        self.posX = self.posX + (((self.arete.get_sommet2().get_x()-self.arete.get_sommet1().get_x())/self.arete.get_longueur())*self.vitesse)
                        self.posY = self.posY + (((self.arete.get_sommet2().get_y()-self.arete.get_sommet1().get_y())/self.arete.get_longueur())*self.vitesse)
                else:
                    if self.arete.get_longueur() == 0:
                        self.posX = self.posX + 1
                        self.posY = self.posY + 1
                    else:
                        self.posX = self.posX + ((self.arete.get_sommet1().get_x()-self.arete.get_sommet2().get_x())/self.arete.get_longueur())*self.vitesse
                        self.posY = self.posY + ((self.arete.get_sommet1().get_y()-self.arete.get_sommet2().get_y())/self.arete.get_longueur())*self.vitesse
                for i in jeu.get_liste_joueurs(): # Avec un getter des joueurs dans le jeu
                    if i.get_x() == self.posX and i.get_y() == self.posY:
                        i.enlever_vie(self.degats)
