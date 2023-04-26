################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créez une classe “Personne” avec les attributs “nom” et “prenom" + ajoutez méthode “SePresenter()” qui retourne le nom et le prénom
# Instanciez plusieurs personnes avec les valeurs de construction de votre choix et faites appel à la méthode “SePresenter()” pour les voir

class Personne:                                                                 # Création de la classe Personne
    def __init__(self, prenom, nom):                                            # Création de l'objet via un constructeur                                                        # Enregistre les valeurs des attribus passés en paramètre
        self.prenom = prenom
        self.nom = nom     
        
    def SePresenter(self):                                                      # Methode appliquée pour effectuer ce que l'on veut
        print("Je me presente, je suis :", self.prenom, self.nom)

presentation1 = Personne("Princess Consuela","Banana Hammock")                  # Synthase : objet = Classe(attribut 1, attribut 2)
presentation2 = Personne("Joseph","Rouletabille")
presentation3 = Personne("Hercule","Poirot")


presentation1.SePresenter()                                                     # Affiche les données demandées
presentation2.SePresenter()
presentation3.SePresenter()