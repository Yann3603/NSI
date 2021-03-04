from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
"""
from labyrinthe import *
from player import *
from random import sample, choice, randint
from math import sqrt
import pygame
import pygame.gfxdraw
from pygame.locals import *
import time
import os
"""

def choix_grolard():
    FenetreChoix.destroy()


def choix_speedy():
    FenetreChoix.destroy()


def choix_alibabar():
    FenetreChoix.destroy()


def choix_romuald():
    FenetreChoix.destroy()


FenetreChoix = Tk()
titre = "Choix du joueur"
FenetreChoix.geometry("980x900")
gross_font = font.Font(FenetreChoix, size = 50)
FenetreChoix.configure(background = "midnight blue")
FenetreChoix.title(titre)

Affichage = Label(FenetreChoix, text = "Veuillez choisir un personnage", height = 2, width = 50,font = ("courier", 14), bg = "midnight blue", fg = "white")
Affichage.place(relx = 0.5, rely = 0.1, anchor = CENTER)




#----------------------------------------------------------------------------------------------------------------------

Proprietegrolard = Label(FenetreChoix, text = "GROLARD\n\n pv = 190\n vitesse = 1.6\n Taille du sac = 4\n", font = ("courier", 11),height = 10, width = 23, bg = "DodgerBlue2", fg = "white", borderwidth=2, relief="solid")
Proprietegrolard.place(relx = 0.02, rely = 0.25)

bouton_grolard = Button(FenetreChoix, text = "Choisir", height = 1, width = 6, bg = "gray15", fg = "red",activebackground = "Red", command = lambda x="": choix_grolard())
bouton_grolard.place(relx = 0.100, rely = 0.5)

#----------------------------------------------------------------------------------------------------------------------

Proprietespeedy = Label(FenetreChoix, text = "SPEEDY\n\n pv = 85\n vitesse = 2.5\n Taille du sac = 2", font = ("Courier", 11), height = 10, width = 23, bg = "DodgerBlue2", fg = "white", borderwidth=2, relief="solid")
Proprietespeedy.place(relx = 0.26, rely = 0.25)

bouton_speedy = Button(FenetreChoix, text = "Choisir", height = 1, width = 6, bg = "gray15", fg = "red",activebackground = "Red", command = lambda x="": choix_speedy())
bouton_speedy.place(relx = 0.34, rely = 0.5)

#----------------------------------------------------------------------------------------------------------------------

Proprietealibabar = Label(FenetreChoix, text = "ALI BABAR\n\n pv = 90\n vitesse = 1.9\n Taille du sac = 6", font = ("Courier", 11), height = 10, width = 23, bg = "DodgerBlue2", fg = "white", borderwidth=2, relief="solid")
Proprietealibabar.place(relx = 0.51, rely = 0.25)

bouton_alibabar = Button(FenetreChoix, text = "Choisir", height = 1, width = 6, bg = "gray15", fg = "red",activebackground = "Red", command = lambda x="": choix_alibabar())
bouton_alibabar.place(relx = 0.59, rely = 0.5)

#----------------------------------------------------------------------------------------------------------------------

Proprieteromuald = Label(FenetreChoix, text = "ROMUALD\n\n pv = 100\n vitesse = 2\n Taille du sac = 3", font = ("Courier", 11), height = 10, width = 23, bg = "DodgerBlue2", fg = "white", borderwidth=2, relief="solid")
Proprieteromuald.place(relx = 0.75, rely = 0.25)

bouton_romuald = Button(FenetreChoix, text = "Choisir", height = 1, width = 6, bg = "gray15", fg = "red",activebackground = "Red", command = lambda x="": choix_romuald())
bouton_romuald.place(relx = 0.82, rely = 0.5)

FenetreChoix.mainloop()