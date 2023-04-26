################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créer une classe “Voiture” qui a pour attributs privés une marque, un modèle , une année, un kilométrage et un attribut nommé “en_marche” initialisé à défaut 
# sur False. Cette classe doit posséder des mutateurs et assesseur pour chaque attribut. Créer une méthode “demarrer” qui change la valeur de l’attribut 
# “en_marche” en True, une méthode “arreter” qui change la valeur de l’attribut “en_marche” en False.
# Ajouter à la classe “Voiture” l’attribut privé “reservoir” qui est initialisé à 50 par défaut dans le constructeur. 
# Créer une méthode privée “verifier_plein” qui retourne la valeur de l’attribut “reservoir”. Cette méthode est appelée dans la méthode “demarrer” . 
# Si la valeur du reservoir est supérieur à 5 la voiture peut demarrer.

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir                                    # initilisé à 50 

            # Les accesseurs

    def get_Marque(self):
        return self.__marque
    
    def get_Modele(self):
        return self.__modele
    
    def get_Annee(self):
        return self.__annee
    
    def get_Kilometrage(self):
        return self.__kilometrage
    
    def get_En_marche(self):
        return self.__en_marche
    
    def get_Reservoir(self):
        return self.__reservoir
    
            # Mutateurs
    
    def set_Marque(self, new_marque):
        self.__marque = new_marque
        
    def set_Modele(self, new_modele):
        self.__modele = new_modele
    
    def set_Annee(self, new_annee):
        self.__annee = new_annee
    
    def set_Kilometrage(self, new_kilometrage):
        self.__kilometrage = new_kilometrage
        
    def set_En_marche(self, new_en_marche):
        self.__en_marche = new_en_marche
        
    def set_Reservoir(self, new_reservoir):
        self.__reservoir = new_reservoir

            # Verifier le reservoir

    def __verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else:
            return False

            # Methode pour demarrer la titine

    def Demarrer(self):       
        if self.get_En_marche() is False and self.__verifier_plein() is True:
            self.__en_marche = True
            print("La titine démarre")
        
            # methode pour arreter la titine
        
    def Arreter(self):
        if self.__en_marche is True:
            self.__en_marche = False
            print("La titine va incessament sous peu s'arreter")
            
voiture = Voiture("Jaguar", "Type E", 1969, 8888)

voiture.Demarrer()
voiture.Arreter()
