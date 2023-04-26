################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Récupérer la classe “Livre”. Ajouter l'attribut privé suivant :“disponible” initialisé par défaut a True.
# Créer une méthode nommée “vérification” qui vérifie si le livre est disponible, c'est-à-dire que la valeur de son attribut disponible est égale à True. 
# Cette méthode doit retourner True ou False. Ajouter une méthode “emprunter” qui rend le livre indisponible, autrement dit la valeur de “disponible” 
# devient False. Bien sûr, pour pouvoir emprunter un livre, il faut que celui-ci soit disponible, vérifier donc que celui-ci soit disponible sans utiliser 
# l’attribut “disponible”. Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode “rendre” qui dans un premier temps vérifie si le 
# livre a bien été emprunter ( sans utiliser l’attribut “disponible”), puis change la valeur de l’attribut “disponible”.
       
class Livre:                             
    def __init__(self, titre, auteur, disponible):                                  
        self.__titre = titre                              
        self.__auteur = auteur
        self.__disponible = True
    
    def get_Titre(self):                                      
        return self.__titre

    def get_Auteur(self):
        return self.__auteur
    
    def get_Disponible(self):
        return self.__disponible
            
    def set_Disponible(self, chang_disponible):
        self.__disponible = chang_disponible
        
    def verification(self):
        if not self.__disponible:
            print("Ce livre n'est pas dispo")

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Vous en avez du bol, j'ai bel et bien le bouquin que vous recherchez !!")
        else:
            print("Negatif allez dans une autre bibli !!")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Et bien dis donc vous en avez mis du temps pour le rendre ce bouquin.. j'ai failli vous tirez les oreilles !!!!")
        else:
            print("Je ne vois pas comment tu peux me rendre un bouquin que tu n'as même pas emprunté tocardo !")


livre = Livre("On a pas toujours du caviar" ,"Johannes Mario Simmel", True)
disponible = Livre("On a pas toujours du caviar" ,"Johannes Mario Simmel : "," Ce livre est dispo")
print(livre.get_Disponible())   
livre.verification()

livre.emprunter()  # Le livre est emprunté
livre.get_Disponible()  # False (la valeur de l'attribut "disponible" a été mise à False)

livre.rendre()  # Rendre le livre
livre.get_Disponible()  # True (la valeur de l'attribut "disponible" a été mise à True)
