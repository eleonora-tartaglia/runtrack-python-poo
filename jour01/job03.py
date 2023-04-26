################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Modifier votre classe “Operation” afin d’y ajouter la méthode addition. 
# Cette méthode additionne “nombre1” et “nombre2” et affiche en console le résultat.

class Operation:                                                # Création de la classe Operation
    def __init__(self, nombre1, nombre2):                       # Création de l'objet via un constructeur
        self.nombre1 = nombre1                                  # Enregistre les valeurs des attribus passés en paramètre
        self.nombre2 = nombre2
    
    def addition(self):                                         # Methode appliquer pour effectuer l'operation voulue
        resultat = self.nombre1 + self.nombre2
        print("Le resultat de l'addition est :", resultat)
 
 
resultat = Operation(20,8)                                      # Synthase : objet = Classe(attribut 1, attribut 2)
resultat.addition()

