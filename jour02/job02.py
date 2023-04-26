#############################################################################################################################################################
###################################################################            L’héritage               ####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :

# À l’aide de la classe “Personne” , Eleve et Professeur écrit au-dessus, faites dire bonjour à votre élève grâce à la méthode “bonjour” 
# ainsi que “je vais en cours” grâce à la méthode “allerEnCours”. Redéfinir l’age de l’élève à 15 ans.
# Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le cours grâce à la méthode enseigner.

class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)
        
    def mofidierAge(self,new_age):
        self.age = new_age

# C'est ma Classe Eleve héritant de la classe Personne                            >>>>                     sans attribut !!!!!!!!!!
class Eleve(Personne):
    def Bonjour(self):
        print("Bonjour Monsieur le Professeur !")
        
    def allerEnCours(self):
        print("Oulala !!!! Je suis très en retard : vite il faut se dépécher d'aller en cours")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
        super().__init__(40)                                                    #  je prends l'init de la classe personne
    
    def Bonjour(self):
        print("Bonjour les branquignolles !")
    
    def Enseigner(self):
        print("Aujourd'hui on va apprendre la langue des robots : si vous etes proche d'un arbre : \naccrochez vous aux branches si vous ne voulez pas tomber !!!")
    
personne = Personne()
eleve = Eleve()
professeur = Professeur("Python")

eleve.Bonjour()
eleve.allerEnCours()
eleve.mofidierAge(15)
eleve.afficherAge()

professeur.Bonjour()
professeur.Enseigner()

