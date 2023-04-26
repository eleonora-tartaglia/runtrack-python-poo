#############################################################################################################################################################
###################################################################            L’héritage               ####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :

# Créer une classe “Rectangle” avec comme attribut privé longueur et largeur. 
# Créer la méthode “périmètre” permettant de calculer le périmètre du rec ainsi que la méthode “surface“ permettant de calculer la surface du rectangle.
# Créer les accesseurs et mutateurs permettant de manipuler les attributs de la classe.
# Créer une classe “Parallélépipède“ héritant de la classe Rectangle avec en plus un attribut hauteur et une autre méthode volume permettant de 
# calculer le volume du parallélépipède.
# Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent.

class Rectangle:
    def __init__(self,longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def Perimetre(self):
        peri = (self.__longueur + self.__largeur) * 2 
        #print(peri)
        return peri
    
    def Surface(self):
        surf = (self.__longueur * self.__largeur)
        #print(surf)
        return surf
        
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur    
        
    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur

class Parallepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        self.hauteur = hauteur
        super().__init__(longueur, largeur)
    
    def Volume(self):
        vol = (self.get_longueur() * self.get_largeur() * self.hauteur)
        #print(vol)
        return vol

rectangle = Rectangle(28, 68)
parallepipede = Parallepipede(28, 68, 48)

perimetre_rectangle = rectangle.Perimetre()
print("Ce foutu rectangle a pour perimètre :", perimetre_rectangle, "µm")

surface_rectangle = rectangle.Surface()
print("Ce foutu rectangle a pour surface :", surface_rectangle, "µm")

new_longueur_rectangle = rectangle.set_longueur(18)
print("Après un coup de baguette magique, j'en change sa longueur :", rectangle.get_longueur(),"µm")

new_largeur_rectangle = rectangle.set_largeur(8)
print("Après un coup de baguette magique, j'en change sa largeur :", rectangle.get_largeur(),"µm")

volume_parallepipede = parallepipede.Volume()
print("Après avoir ajouter une hauteur, ça devient un foutu parallepipede en mode 3D qui a pour volume :", volume_parallepipede, "µm³")