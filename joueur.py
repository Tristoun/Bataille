from jeucarte import *

class Joueur () :
    def __init__(self, nom, mainJoueur) :
        self.nom = nom
        self.mainJoueur = mainJoueur

    def finCarte(self) :
        if ( self.getNbCartes() > 0 ) :
            return False
        return True

    def getNom (self) :
        return self.nom
    
    def getNbCartes(self) :
        return len(self.mainJoueur)
   
    def jouerCartes (self) :
        """Enlève et renvoie la dernière carte (objet de type Carte) 
        de la main du joueur pour la jouer, ou retourne None s’il n’y a plus de cartes dans la main du joueur""" 
        if self.finCarte() :
            return None
        else : 
            cjouer = self.mainJoueur[0]
            del self.mainJoueur[0]
            return cjouer
     
    
    def insererMain(self, tas) :
        '''Fonction qui insère les cartes de la liste des cartes gagnées(le tas)dans la main du joueur. 
        (Remarque, il est possible qu'il y ait un None dans le tas)'''
        self.mainJoueur.extend (tas)
