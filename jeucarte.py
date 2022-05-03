from carte import *
import random

class JeuCartes() :
    def __init__ (self, nbCartes =32) :
        assert (nbCartes == 52 or nbCartes == 32)
        self.jeu= []
        self.nbCartes = nbCartes
        #self.jeu est une liste de self.nbCartes … 
        # à compléter en exécutant la méthode creerJeu() qui doit compléter la liste
    
    @staticmethod
    def affiche(main) : 
        s = ""
        if main != [] :
            s = " - " + main[1].toString()
        else : 
            s = "-"
        return s

    def getTailleJeu (self) :
        ''' Fonction qui retourne le nombre de cartes du jeu Valeur retournée: type int'''
        return len(self.jeu)
    
    def creerJeu (self) :
        '''Créée la liste des cartes de l'attribut self.jeu '''
        for i in range (4) :
            if self.nbCartes == 52 :
                for j in range (13) :
                    self.jeu.append ((couleurs[i], noms[j], valeurs[noms[j]]))
            elif self.nbCartes == 32 :
                for j in range (8) :
                    self.jeu.append ((couleurs[i], noms[j+5], valeurs[noms[j+5]]))
        return self.jeu

    def getJeu (self):
        '''Renvoie la liste des cartes correspondant à l'attribut self.jeu'''
        return self.jeu
    
    def melanger (self) :
        random.shuffle(self.jeu)
    
    def distribuerCarte(self):
        ''' Cette fonction permet de distribuer une carte à un joueur. Elle décrémente le 
        nb de cartes du jeu. Valeur retournée: Objet de type Carte '''
        carte = Cartes(self.jeu[0][1], self.jeu[0][0], self.jeu[0][2])
        del self.jeu[0]
        return carte
    
    def distribuerJeu(self, nbJoueurs, nbCartes):
        ''' Cette méthode distribue nbCartes à chacun des nbJoueurs
        Valeur retournée: une liste de listes de cartes (une liste par joueur)'''
        self.melanger()
        listejeux = []
        for n in range (nbJoueurs) :
            listejeux.append([])
        for i in range (nbCartes) :
            for j in range (nbJoueurs) :
                listejeux[j].append(self.distribuerCarte())
        return listejeux



