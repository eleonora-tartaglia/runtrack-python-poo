################################################ CREATION DE CLASSES ############################################################
###################### Pour simplifiez le code, organiser les idées, structurer les programmes ##################################
#################################################################################################################################

# Créer la classe 'Livre’ qui prend en attributs privés un titre, un auteur et un nombre de pages.
# Créer les assesseurs et mutateurs nécessaires afin de pouvoir modifier et afficher les attributs. 
# Pour changer le nombre de pages, le nombre doit être un nombre entier positif sinon la valeur n’est pas changée et un message d’erreur est affiché.

class Livre:                             
    def __init__(self, titre, auteur, pages):                                  
        self.__titre = titre                              
        self.__auteur = auteur
        self.__pages = pages
    
    def get_Titre(self):                                      
        return self.__titre

    def get_Auteur(self):
        return self.__auteur
        
    def get_Pages(self):
        return self.__pages
    
    def set_Titre(self, new_titre):
        self.__titre = new_titre
    
    def set_Auteur(self,new_auteur):
        self.__auteur = new_auteur

    def set_Pages(self,new_pages):
        if new_pages > 0:
            self.__pages = new_pages


livre = Livre("On a pas toujours du caviar" ,"Johannes Mario Simmel", 688)
print(livre.get_Titre())
print(livre.get_Auteur())
print(livre.get_Pages())

livre.set_Titre("La toile d'araignée")
print(livre.get_Titre())

livre.set_Auteur("Agatha Christie")
print(livre.get_Auteur())

livre.set_Pages(235)
print(livre.get_Pages())