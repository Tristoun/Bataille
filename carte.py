couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE') 
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi','As'] 
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As':14}

class Cartes :
    def __init__(self, nom, couleur, valeur): #initialise la classe Cartes
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeur

    def toString(self) : 
        """Renvoie le nom et la couleur de la carte"""
        return self.nom + " " + self.couleur
        
    def getNom (self) :
        return self.nom
    
    def getCouleur (self) :
        return self.couleur
    
    def getValeur (self) :
        return self.valeur
    
    def egalite (self, carte) :
        ''' Renvoie True si les cartes ont même valeur, False sinon carte: Objet de type Carte '''
        if self.valeur == carte.valeur :
            return True
        else : 
            return False
    def estSuperieurA (self, carte) :
        ''' Renvoie True si la valeur de self est supérieure à celle de carte, 
        False sinon. :carte: Objet de type Carte '''
        if self.valeur > carte.valeur :
            return True
        else :
            return False
    
    def estInferieurA (self, carte) :
        ''' Renvoie True si la valeur de self est inferieure à celle de carte,
        False sinon :carte: Objet de type Carte '''
        if self.valeur < carte.valeur :
            return True
        else :
            return False

