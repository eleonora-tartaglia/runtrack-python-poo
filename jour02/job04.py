#############################################################################################################################################################
###################################################################            L’héritage               ####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :

# Créer une classe nommée “Forme” possédant une méthode nommée aire qui renvoie 0.
# Créer une classe “Rectangle” qui hérite de la classe “Forme” et qui possède deux attributs largeur et hauteur. 
# Surcharger la méthode aire dans la classe Rectangle afin qu’elle ne renvoie plus 0, mais l’aire du rectangle.
# Imprimer en console le résultat de la méthode aire de la classe Rectangle.

class Forme:
    def __init__(self):
        pass
        
    def Aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def Aire(self):
        return self.__largeur * self.__hauteur
    
rectangle = Rectangle(18, 8)

aire_rectangle = rectangle.Aire()
print("En ce qui concerne l'aire de ce foutu rectangle, voilà ta reponse tocard :", aire_rectangle)


    
    

        

        
