#############################################################################################################################################################
###################################################################            L’héritage               #####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :

# Créer une classe “Vehicule“ avec comme attribut une marque , une année et un prix. Créer la méthode “informationsVehicule“ qui écrit en console la marque, le modèle, l'année et le prix du véhicule.
# Créer la classe ”Voiture“ qui hérite de la classe ”Vehicule”. Dans le constructeur de la classe Voiture, ajouter un attribut “portes” qui contient le nombre entier 4. 
# Créer dans cette classe , une méthode “informationsVehicule” qui affiche, en console, les informations générales du véhicule et le nombre de portes de la voiture.
# Instancier un objet, Voiture passer les attributs dont la classe a besoin et faites appel à la méthode “informationsVehicule”.


# Créer une classe Moto qui hérite de la classe “Vehicule” et ajouter l'attribut “roue” qui contient par défaut l’entier 2. 
# Créer à nouveau une méthode “informationsVehicule” dans la classe Moto qui affiche l'intégralité des informations de la moto.
# Instancier un objet Moto et faites appel à la méthode informationsVehicule.


# Créer la méthode “demarrer” dans la classe Véhicule qui écrit en console “Attention, je roule”. 
# Surcharger la méthode démarrer dans la classe Moto et Voiture afin d’afficher un message personnalisé. Faites démarrer votre voiture et votre moto.

class Vehicule:
    def __init__(self, marque, modele, annee, prix):                     
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        
    def informationsVehicule(self):
        print(self.marque, self.modele, self.annee, self.prix)
        
    def Demarrer(self):
        print("Attention tout le monde, je suis au volant de ma titine, il est fortement conseillé de s'echapper rapidement !!!!")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
        
    def informationsVehicule(self):
        print("La marque de ma titine c'est :", self.marque)
        print("Son modele est :", self.modele)
        print("C'est une vieille fille, elle est née en :", self.annee)
        print("En plus elle vaut très chere la coquine :", self.prix)
        print("Par contre elle n'a pas", self.portes, "portes, elle en a que 2.")
    
    def Demarrer(self):
        print("Attention tout le monde, je suis au volant de ma titine, il est fortement conseillé de s'echapper rapidement !!!!")
        
        
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        print("La marque de ma mobylette c'est :", self.marque)
        print("Son modele est :", self.modele)
        print("C'est aussi une vieille fille, elle est née en :", self.annee)
        print("En plus elle vaut assez chere, elle aussi :", self.prix)
        print("Elle a", self.roue, "roue, parce qu'une seule ça ne suffit pas voyons..")
    
    def Demarrer(self):
        print("Attention tout le monde, je suis au volant de ma mobylette, sauve qui peut !!!!")

vehicule_number3 = Vehicule("Ford", "Mustang", 1968, 48000)
voiture = Voiture("Ford", "Mustang", 1968, 48000)
voiture.informationsVehicule()

vehicule_number2 = Vehicule("Triumph", "Trophy", 1951, 18000)
mobylette = Moto("Triumph", "Trophy", 1951, 18000)
mobylette.informationsVehicule()

voiture.Demarrer()

mobylette.Demarrer()









        
        
        