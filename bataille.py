from jeucarte import *
from carte import *
from joueur import *
import math
import random

class Bataille() :

    def __init__(self) :
        """Initialise la classe Bataille en créant le jeu et en distribuant les cartes, créer les 2 joueurs"""
        self.tas = []
        jeucarte = JeuCartes()
        jeucarte.creerJeu()
        lstjeu = jeucarte.distribuerJeu(2,int(math.floor(jeucarte.getTailleJeu()/2)))

        self.j1 = Joueur("Player", lstjeu[0])
        self.j2 = Joueur("bot", lstjeu[1])

    def tour(self) :
        """Execute un tour de jeu en affichant les carte jouer """

        print( "J1 - " + JeuCartes.affiche( self.j1.mainJoueur) ) #affiche la carte jouer du joueur 1
        print( "J2 - " + JeuCartes.affiche( self.j2.mainJoueur) ) #affiche la carte jouer du joueur 2
        print( " " )        

        if self.j1.finCarte() : #regarde combien reste t'il de carte dans le jeu des joueurs 
            if self.j2.finCarte() :
                return "Nul"
            return "j2w"
        if self.j2.finCarte() :
            return "j1w"
    
        carteverso = [self.j1.jouerCartes(), self.j2.jouerCartes()]
        carteplay = [self.j1.jouerCartes(), self.j2.jouerCartes()]
        self.tas.extend (carteverso)
        self.tas.extend (carteplay)
        
        random.shuffle(self.tas) #mélange le tas

        if carteplay[0].estSuperieurA(carteplay[1]) : #compare les résultats des valeurs
            self.j1.insererMain(self.tas)
            self.tas.clear()    
        elif carteplay[0].estInferieurA(carteplay[1]) :
            self.j2.insererMain(self.tas)
            self.tas.clear()
        elif carteplay[0].egalite(carteplay[1]) :
            game.tour()


    def jeu(self) :
       """Execute les tours de jeu et affiche le gagant """
       while True :
            res = self.tour()
            if res == "j2w" :
                return "Le joueur" + " " + self.j2.nom + " " + "a gagné"
            elif res == "j1w" :
                return "Le joueur" + " " + self.j1.nom + " " + "a gagné"
            elif res == "Nul" :
                return "Match Nul"


if __name__ == "__main__" :
    nbgame = int(input("Combien voulez vous de parties  : "))
    for i in range (nbgame) :
        game = Bataille()
        print ( game.jeu() )
    