################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# À l’aide de la classe “Operation” crée auparavant, imprimer en console la valeur des attributs “nombre1” et “nombre2”.

class Operation:                                          # Création de la classe Operation
    def __init__(self, nombre1, nombre2):                 # Création de l'objet via un constructeur
        self.nombre1 = nombre1                            # Enregistre les valeurs des attribus passés en paramètre
        self.nombre2 = nombre2
    
    def show_infos(self):                                 # Methode appliquée pour afficher les infos
        print("le nombre 1 est : ", self.nombre1)
        print("le nombre 2 est : ", self.nombre2)
        
operation = Operation(8, 18)                              # Synthase : objet = Classe(attribut 1, attribut 2)
operation.show_infos()
                           