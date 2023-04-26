################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créer une classe “Rectangle” avec des attributs privés, “longueur” et “largeur” initialisées dans le constructeur.
# Créer des accesseurs et mutateurs afin de pouvoir afficher et modifier les attributs de la classe.
# Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5. 
# Changer la valeur de la longueur et de la largeur et vérifier que les modifications soient bien prises en compte.

class Rectangle:                                                                  # Création de la classe Rectangle
    def __init__(self,longueur, largeur):                                         # Création de l'objet via un constructeur
        self.__longueur = longueur                                                # Enregistre les valeurs des attribus passés en paramètre
        self.__largeur = largeur
        
    def show_infos(self):
        print(self.__longueur)
        print(self.__largeur)
    
    def get_Longueur(self):                                                       # Encapsule la classe en mode privé
        return self.__longueur
    
    def set_Longueur(self, nouvelle_longueur):                                    # Modifie la new longueur
        self.__longueur = nouvelle_longueur
        
    def get_Largeur(self):
        return self.__largeur
    
    def set_Largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur
    
rectangle = Rectangle(10,5)

rectangle.set_Largeur(4)
rectangle.set_Longueur(8)
print(rectangle.get_Longueur())
print(rectangle.get_Largeur())