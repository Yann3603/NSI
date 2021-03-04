from math import sqrt
from math import atan,pi

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

    def coffre(self,objet):
        """Testeur pour voir si un objet est prÃ©sent dans la liste ou non.

        Args:
            objet: nom de l'objet

        Returns:
            bool: True/False
        """
        self.coffre=coffre

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
        
class Coffre:
    def __init__(self, objets):
        self.objets=[]
        
    def get_objet(self, objet):
        return self.objets

    def add_objets(self, objets):
        self.objets.append(objets)

# test Lucas
