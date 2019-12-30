from Joueur import Joueur

class Chasseur(Joueur):
    pv = 0
    mana = 0
    def __init__(self):
        self.pv = 200
        self.mana = 75

class Druid(Joueur):
    pv = 0
    mana = 0
    def __init__(self):
        self.pv = 75
        self.mana = 200

    def attack(self, other):
        other.pv -= 10

class Voleur(Joueur):
    pass
