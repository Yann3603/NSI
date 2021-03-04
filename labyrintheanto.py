from math import sqrt
from math import atan,pi
import random as rd 

class Noeud:
    def __init__(self, x, y):
        self.aretes = []
        self.x = x
        self.y = y
        self.objets = []


    def get_aretes(self):
        """Getter de la liste des voisins (aretes) du noeud.

        Returns:
            list: voisins
        """
        return self.aretes

    def set_aretes(self,aretes):
        self.aretes=aretes


    def get_x(self):
        """Getter de la position x du noeud.

        Returns:
            int: position x
        """
        return self.x

    def get_y(self):
        """Getter de la position y du noeud.

        Returns:
            int: position y
        """
        return self.y

    def add_arete(self, nouveau):
        """MÃ©thode pour ajouter un voisin au noeud.

        Args:
            nouveau (objet Noeud): objet Noeud Ã  ajouter
        """
        self.aretes.append(nouveau)


    def set_x(self, posx):
        """Setter de la position x du noeud.

        Args:
            posx (int): position x
        """
        self.x = posx

    def set_y(self,posy):
        """Setter de la position x du noeud.

        Args:
            posy (int): position y
        """
        self.y = posy

    def set_objet(self,objet):
        """Setter d'un objet. Ajoute l'objet Ã  la liste des objets.

        Args:
            objet: instance de l'objet
        """
        self.objets.append(objet)


    def get_liste_objets(self):
        """Getter de la liste des objets                            

        Returns:
            list: liste des objets
        """
        return self.objets

    def has_objet(self,objet):
        """Testeur pour voir si un objet est prÃ©sent dans la liste ou non.

        Args:
            objet: nom de l'objet

        Returns:
            bool: True/False
        """
        return objet.get_objet() in self.objets
    
class coffre:
    def __init__(self, interaction,):
        self.interaction=interaction
        self.objets_coffre=[]
        self.liste_objet=[1,2,3,4,5]
        self.liste_munitions=[]
        
    def munitions_coffre():
        nbr=rd.randint(0,100)
            if 1<nbr<60
                self.objest_coffre.append("1")
            if 60<nbr<90
                self.objest_coffre.append("2")
            if 90<nbr<100:
                self.objest_coffre.append("3")
                
        
    def objets_coffre(self):
        for i in range(4):
            nbr=rd.randint(0,305)
                if 1< nbr <50:
                    self.objets_coffre.append("4")
                if 50< nbr <80:
                    self.objets_coffre.append("5")
                if 80< nbr <95:
                     self.objets_coffre.append("6")
                if 95<nbr<100:
                    self.objets_coffre.append("7")
                if 100<nbr<150:
                    self.objets_coffre.append("8")
                if 150<nbr<180:
                    self.objets_coffre.append("9")
                if 180<nbr<195:
                    self.objets_coffre.append("10")
                if 195<nbr<200:
                    self.objets_coffre.append("11")
                if 200<nbr<250:
                    self.objets_coffre.append("12")
                if 250<nbr<280:
                    self.objets_coffre.append("13")
                if 280<nbr<295:
                    self.objets_coffre.append("14")
                if 295<nbr<300:
                    self.objets_coffre.append("15")
                if 300<nbr<305:
                    self.objets_coffre.append("16")
        
             
            
            
            
        
        
        
        
    

class Arete:
    def __init__(self, sommet1, sommet2, visible):
        self.sommet1=sommet1
        self.sommet2=sommet2
        self.longueur= sqrt((sommet1.get_x() - sommet2.get_x())**2 + (sommet1.get_y() - sommet2.get_y())**2)
        self.visible=visible
        self.angle=self.angle()*180.0/3.1415 #on met en degré

    def angle(self):#renvoie l'angle du mur de l'arete
        if self.sommet1.get_x()==self.sommet2.get_x():
            if self.sommet2.get_y() >= self.sommet1.get_y():
                return -pi/2
            else:
                return pi/2
        else:
            return -atan((self.sommet2.get_y()- self.sommet1.get_y())/(self.sommet2.get_x()-self.sommet1.get_x()))

    def get_longeur(self):
        return self.longueur

    def get_sommet1(self):
        return self.sommet1

    def get_sommet2(self):
        return self.sommet2

    def get_longueur(self):
        return self.longueur

    def get_angle(self):
        return self.angle


class Objet:
    def __init__(self, objet):
        self.objet = objet

    def get_objet(self, objet):
        return self.objet

    def set_objet(self, objet):
        self.objet = objet


