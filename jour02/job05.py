#############################################################################################################################################################
###################################################################            L’héritage               #####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :


# Récupérer votre classe “Forme” crée juste au-dessus.
# Créer une classe fille nommée “Cercle” qui hérite de la classe “Forme” et possédant un attribut radius.
# Surcharger la méthode “aire” dans la classe Cercle pour qu'elle renvoie l’aire du cercle.
# Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les différentes surcharges de la méthode aire en affichant les résultats en console.

class Forme:
    def __init__(self):
        pass
        
    def Aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
        
    def Aire(self):
        return (self.__radius * self.__radius) * 3.14

cercle = Cercle(8)
aire_cercle = cercle.Aire()
print("Ce bon sang de cercle a pour aire :", aire_cercle, "cm et je m'en tamponne, mais à un point si tu savais..")

print("J'en ai marre, il est minuit 44, c'est decidé, je vais me coucher !!!!!")