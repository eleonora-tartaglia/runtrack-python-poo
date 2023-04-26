################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créer une classe “Operation” avec un constructeur (méthode qui sera appelée lors de l’instance de la classe). 
# Ajouter les attributs “nombre1” et “nombre2” initialisés avec des valeurs par défaut. 
# Instancier votre première classe et imprimer l’objet en console.


class Operation:                       # Création de la classe Operation
    
    def __init__(self):                # Création de l'objet via un constructeur
        self.nombre1 = 8               # Initialise les attributs avec des valeurs par défaut : ex 8 et 18
        self.nombre2 = 18
        
operation = Operation()                # Synthase : objet = Classe(attribu 1,attribu 2)

print(operation)                       # Imprime l'objet : Affiche : <__main__.Operation object at 0x1029d4c10>    ==> le resultat est aléatoire
