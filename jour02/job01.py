#############################################################################################################################################################
###################################################################            L’héritage               ####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :

# Créer une classe Personne qui aura comme attribut age prenant un entier et initialisé à 14 par défaut. 
# Ajouter une méthode “afficherAge” qui affichera en console l’age de la personne et une méthode bonjour qui écrit en console ‘Hello’. 
# Créer une méthode “modifierAge” prenant en paramètre un entier et permettant de modifier l’age de la personne.
# Créer une classe Eleve qui hérite de la classe “Personne” sans attribut et une méthode publique “allerEnCours” qui affiche : “Je vais en cours” 
# ainsi qu’une méthode “affichageAge” qui écrit en console : ‘J’ai XX ans’
# Créer une classe Professeur avec un attribut privé “matiereEnseignée”, qui indiquera la matière du professeur, 
# et une méthode publique “enseigner” qui affiche :. ‘Le cours va commencer’.
# Instancier une classe “Personne” et une classe “Eleve”. Afficher l’age par défaut de l’élève en console.


# C'est ma Classe Personne
class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)
    
    def Bonjour(self):
        print("Bonjour toi !")
        
    def mofidierAge(self,new_age):
        self.age = new_age

# C'est ma Classe Eleve héritant de la classe Personne                                  sans attribut !!!!!!!!!!
class Eleve(Personne):
    def allerEnCours(self):
        print("Il faut y aller tu vas etre en retard en cours")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")
        
class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    
    def Enseigner(self):
        print("Allez en cours immediatement, ça va commencer !!!")

# j'instancie :    
personne = Personne()
eleve = Eleve()

eleve.afficherAge()