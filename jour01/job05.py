################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créez une classe Animal avec un attribut age initialisé à zéro et prénom initialisé vide dans son constructeur.
# Instancier un objet Animal et écrire en console l’attribut âge. Créer une méthode “vieillir” qui ajoute 1 à l'âge de l’animal. 
# Faire vieillir votre animal et afficher son âge en console.
# Créer une méthode ”nommer” qui prend en paramètre le nom de l’animal. Nommer votre animal et afficher en console le nom de l’animal.

class Animal:                                                  # Création de la classe Animal
    def __init__(self):                                        # Création de l'objet via un constructeur
        self.prenom = ""                                       # Passe les paramètres par défauts
        self.age = 0
    
    def show_infos(self):                                      # Methode appliquée pour afficher les infos
        print("Le nom de cet animal est : " + str(self.prenom) + ", il est âgé de :", str(self.age), " ans")

    def vieillir(self):
        self.age += 1
        
    def nommer(self):
        self.prenom = "Baltazar"
        print(self.prenom)
        
resultat = Animal()                                            # Synthase : objet = Classe(attribut 1, attribut 2
resultat.vieillir()                     
resultat.nommer()
resultat.show_infos()