from labyrinthe import *
from player6 import *
from random import sample, choice, randint
from math import sqrt
import pygame
import pygame.gfxdraw
from pygame.locals import *
import time
import os

class Jeu:
    def __init__(self,Dimplayarea,nbnoeud,nbarete):
        self.Dimplayarea=Dimplayarea
        self.nbnoeud=nbnoeud
        self.nbarete=nbarete
        self.labyrin=[]
        self.ListeNoeud=[]
        self.ListeJoueur=[]

    def add_joueur(self,joueur):
        self.ListeJoueur.append(joueur)

    def GenerateurLabyrinthe(self):
        """GÃ©nÃ¨re un labyrinthe alÃ©atoire, mais il vaudrai mieux en faire
         un Ã  la main plus jouable..."""
        Dimplayerfloor=self.Dimplayarea
        for i in range(self.nbnoeud): #On crÃ©e nbnoeud noeuds
            x=randint(0,Dimplayerfloor)
            y=randint(0,Dimplayerfloor)
            #if x not in self.ListeNoeud:#on teste si ces coordonnÃ©es ne sont pas dÃ©jÃ  utilisÃ©es
            self.ListeNoeud.append(Noeud(x,y))
        #On crÃ©e nbarete aretes et on mets Ã  jour les noeuds
        for i in range(self.nbarete):
            j,k=randint(0,9),randint(0,9)
            if abs(self.ListeNoeud[j].get_x()-self.ListeNoeud[k].get_x())>20:
                if self.ListeNoeud[j].get_y()<self.ListeNoeud[k].get_y():
                    a=Arete(self.ListeNoeud[j],self.ListeNoeud[k],True)
                else:
                    a=Arete(self.ListeNoeud[k],self.ListeNoeud[j],True)
                self.labyrin.append(a)
                self.ListeNoeud[j].add_arete(self.labyrin[-1])
                self.ListeNoeud[k].add_arete(self.labyrin[-1])
        #Il faut ensuite tester si un noeud n'a pas Ã©tÃ© utilisÃ©....et le détruire.
        for noeud in self.ListeNoeud:
            if len(noeud.get_aretes())==0:
                self.ListeNoeud.remove(noeud)
        #Maintenant on reclasse les listes des aretes pour chaque noeud
        for noeud in self.ListeNoeud:
            B=noeud.get_aretes()
            A=sorted(B,key=lambda aret : aret.angle)
            noeud.set_aretes(A)

    def viewerlaby(self):
        """ Viewer qui permet de voir le labyrinthe dans son entier avec les autres joueurs: le joueur pourra
        avoir accÃ¨s Ã  cela si seulement
        il a l'objet magique qui le permet!"""
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
        xfen=2*self.Dimplayarea
        yfen=2*self.Dimplayarea
        pygame.init()
        #Ouverture de la fenÃªtre
        fenetre = pygame.display.set_mode((xfen, yfen))
        for arete in self.labyrin:
            pygame.draw.line(fenetre,(0,0,100),(arete.get_sommet1().get_x()*2,arete.get_sommet1().get_y()*2),(arete.get_sommet2().get_x()*2,arete.get_sommet2().get_y()*2), 6)
        for sommet in self.ListeNoeud:
            pygame.draw.circle(fenetre,(0,0,255),(sommet.get_x()*2,sommet.get_y()*2),5)
        cont=True
        for joueur in self.ListeJoueur:
            pygame.draw.circle(fenetre, (255, 255, 255), (int(joueur.get_x() * 2),int(joueur.get_y() * 2)), 5)
        pygame.display.flip()
        while cont:#boucle d'attente
            joueur.gestionclavier()
            fenetre.fill((0,0,0))
            for arete in self.labyrin:
                pygame.draw.line(fenetre, (0, 0, 100),(arete.get_sommet1().get_x() * 2, arete.get_sommet1().get_y() * 2),(arete.get_sommet2().get_x() * 2, arete.get_sommet2().get_y() * 2), 6)
            for sommet in self.ListeNoeud:
                pygame.draw.circle(fenetre, (0, 0, 255), (sommet.get_x() * 2, sommet.get_y() * 2), 5)
            for joueur in self.ListeJoueur:
                pygame.draw.circle(fenetre, (255, 255, 255), (int(joueur.get_x() * 2), int(joueur.get_y() * 2)), 5)
            pygame.display.flip()
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont=False
        pygame.quit()

jeu=Jeu(500,10,20)
jeu.GenerateurLabyrinthe()
noeudjoueur1=jeu.ListeNoeud[randint(0,len(jeu.ListeNoeud)-1)]#un noeud au hasard pour le joueur
joueur1=Player( 100,float(noeudjoueur1.get_x()),float(noeudjoueur1.get_y()), 1,True ,None, noeudjoueur1)
jeu.add_joueur(joueur1)
#jeu.viewerlaby()
joueur1.affi2d(jeu.labyrin,jeu.ListeNoeud,jeu.ListeJoueur)
objets = ["", "", "", "", "pistolet", "couteau", "bombe", "bandage"]
