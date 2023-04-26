#############################################################################################################################################################
###################################################################            L’héritage               #####################################################
#############################################################################################################################################################
###################################################################                           #####################################################
#############################################################################################################################################################

# NOTA BENE : L'héritage est un mécanisme qui permet à une classe (appelée classe dérivée ou sous-classe) d'hériter les attributs 
# et les méthodes d'une autre classe (appelée classe de base ou classe mère) :

# Développer votre version du célèbre jeu Blackjack. Le but est de faire le plus de points sans dépasser 21. Chaque carte représente une valeur :
# de 2 à 10 : ces cartes ont pour valeur sa valeur nominale une figure a pour valeur 10 points et un as 1 ou 11 points au choix
# Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le joueur peut choisir de "prendre" (recevoir) une ou plusieurs cartes supplémentaires pour tenter d'améliorer sa main, 
# ou de "passer" et laisser le tour au croupier. Le croupier prend des cartes jusqu'à ce qu'il ait au moins 17 points, puis s'arrête. Si la main du joueur dépasse 21, il perd immédiatement. 
# Si le total de la main du joueur est supérieur à celui du croupier, le joueur gagne. Sinon, c'est le croupier qui gagne.
# Créer au minimum deux classes Carte et Jeu.
# La classe Carte aura au minimum un attribut valeur et couleur. La classe Jeu quant à elle devra gérer l’ensemble des cartes. Les cartes du jeu seront stockées dans un attribut paquet représenté 
# par une liste et contenant 52 cartes.
# Créer toutes les méthodes nécessaires pour jouer une partie.

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def obtenir_valeur_points(self):
        valeurs_points = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Valet": 10,
            "Dame": 10,
            "Roi": 10,
            "As": 1
        }
        return valeurs_points[self.valeur]

class Jeu:
    def __init__(self):
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
    
    def distribuer_cartes(self, nb_cartes):
        cartes = []
        for _ in range(nb_cartes):
            cartes.append(self.paquet.pop())
        return cartes
    
    def ajouter_cartes(self, cartes):
        self.paquet.extend(cartes)
        random.shuffle(self.paquet)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    
    def recevoir_cartes(self, cartes):
        self.main.extend(cartes)
    
    def afficher_main(self):
        print(f"Main de {self.nom}:")
        for carte in self.main:
            print(carte)
    
    def calculer_points(self):
        total_points = 0
        as_count = 0
        for carte in self.main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                total_points += 10
            elif carte.valeur == "As":
                as_count += 1
            else:
                total_points += int(carte.valeur)
        
        for _ in range(as_count):
            if total_points + 11 <= 21:
                total_points += 11
            else:
                total_points += 1
        
        return total_points
    
class Blackjack:
    def __init__(self, joueur, croupier, jeu):
        self.joueur = joueur
        self.croupier = croupier
        self.jeu = jeu

    def passer(self):
        # Logique pour passer (sauter) son tour dans le jeu de blackjack
        pass
    
    def nouvelle_partie(self):
        self.jeu = Jeu()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")
        
        # Distribuer 2 cartes au joueur et au croupier
        self.joueur.recevoir_cartes(self.jeu.distribuer_cartes(2))
        self.croupier.recevoir_cartes(self.jeu.distribuer_cartes(2))
        
        # Afficher la main du joueur (une carte du croupier est cachée)
        self.joueur.afficher_main()
        print(f"Carte cachée du croupier: {self.croupier.main[0]}")
    
    def jouer_tour(self):
        while True:
            choix = input("Voulez-vous prendre une carte (P) ou passer (S) ? ").upper()
            if choix == "P":
                cartes = self.jeu.distribuer_cartes(1)
                self.joueur.recevoir_cartes(cartes)
                self.joueur.afficher_main()
                if self.joueur.calculer_points() > 21:
                    print("Vous avez dépassé 21, vous avez perdu.")
                    return "Croupier"
            elif choix == "S":
            # Logique pour que le croupier joue son tour :
                while self.croupier.calculer_points() < 17:
                    cartes = self.jeu.distribuer_cartes(1)
                    self.croupier.recevoir_cartes(cartes)
            
                self.joueur.afficher_main()
                self.croupier.afficher_main()
            
                points_joueur = self.joueur.calculer_points()
                points_croupier = self.croupier.calculer_points()
            
                if points_joueur > 21:
                    print("Vous avez dépassé 21, vous avez perdu.")
                    return "Croupier"
                elif points_croupier > 21:
                    print("Le croupier a dépassé 21, vous avez gagné.")
                    return "Joueur"
                elif points_joueur > points_croupier:
                    print("Vous avez gagné.")
                    return "Joueur"
                elif points_joueur < points_croupier:
                    print("Le croupier a gagné.")
                    return "Croupier"
                else:
                    print("Égalité.")
                    return "Égalité"
            else:
                print("Choix invalide. Veuillez choisir entre 'P' pour prendre une carte ou 'S' pour passer.")

joueur = Joueur("Joueur")
croupier = Joueur("Croupier")
jeu = Jeu()
blackjack = Blackjack(joueur, croupier, jeu)
blackjack.jouer_tour()