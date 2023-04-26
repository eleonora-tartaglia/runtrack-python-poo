################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créer une classe nommée “Student” qui a comme attributs privés un nom, un prénom, un numéro d’étudiants et un nombre de crédits par défaut à zéro. 
# La méthode “add_credits” permet d’ajouter un nombre de crédits au total de celui de l’étudiant. Ce mutateur doit s’assurer que la valeur passée en 
# argument est supérieure à zéro pour garantir l’intégrité de la valeur.
# Instancier un objet représentant l’étudiant John Doe qui possède le numéro d’étudiant 145. Ajoutez-lui des crédits à trois reprises et imprimer son total 
# de crédits en console.

# Pour des mesures de confidentialité, l'établissement ne souhaite pas divulguer la façon dont elle évalue le niveau de ses étudiants. 
# Pour répondre à cette problématique, créer une méthode nommée “studentEval” qui sera privé. 
# Cette méthode retourne “Excellent” si le nombre de crédits est égale ou supérieure à 90, “Très bien.” si le nombre est supérieur ou égal 
# à 80, “Bien” si le nombre est supérieur ou égale à 70, “Passable” si égale ou supérieure à 60 et “insuffisant” si inférieur à 60.
# Ajouter l’attribut privé nommé “level” dans le constructeur de la classe “Student” qui prend en valeur la méthode “studentEval”. 
# Créer une méthode studentInfo qui écrit en console les informations de l’étudiant (nom, prénom, identifiant et son niveau).

class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__cred_etudiant = 0
        self.__level = self.__student_Eval()

    def get_Nom(self):
        return self.__nom
    
    def get_Prenom(self):
        return self.__prenom
    
    def get_Num_etudiant(self):
        return self.__num_etudiant
    
    def get_Cred_etudiant(self):
        return self.__cred_etudiant
    
    def get_Level(self):
        return self.__level
    
    def set_Nom(self, new_name):
        self.__nom = new_name
    
    def set_Prenom(self, new_prenom):
        self.__prenom = new_prenom
    
    def set_Num_etudiant(self, new_nom_etudiant):
        self.__num_etudiant = new_nom_etudiant
    
    def set_Cred_etudiant(self, new_cred_etudiant):
        self.__cred_etudiant = new_cred_etudiant
    
    def set_Level(self, new_level):
        self.__level = new_level
            
    def add_Credits(self, credits):
        if credits >= 0:
            self.__cred_etudiant += credits

            
    def __student_Eval(self):
        if self.get_Cred_etudiant() >= 90:
            return "Excellent"
        elif self.get_Cred_etudiant() >= 80:
            return "Très bien"
        elif self.get_Cred_etudiant() >= 70:
            return "Bien"
        elif self.get_Cred_etudiant() >= 60:
            return "Passage"
        else:
            return "Insuffisant"

    def student_Info(self):                      # __student_Eval car en mode privé
        print("Nom = " , self.get_Nom())
        print("Prénom = " , self.get_Prenom())
        print("Numero d'étudiant = " , self.get_Num_etudiant())
        print("Niveau = " , self.__student_Eval())
                 
etudiant = Student("John", "Doe", 145)

print("Il vous reste : ", etudiant.get_Cred_etudiant(), " crédits sur votre carte étudiante")
for i in range(3):
    etudiant.add_Credits(30)
    print("Je suis super cool, je vous ai recredité de : ", etudiant.get_Cred_etudiant(), " crédits sur votre carte étudiante")

print(etudiant.get_Cred_etudiant())
etudiant.student_Info()

etudiant.set_Cred_etudiant(70)
etudiant.set_Nom("Tartaglia")
etudiant.set_Prenom("Eléonora")
etudiant.set_Num_etudiant(88)
print("----------------")
etudiant.student_Info()
