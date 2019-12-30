class Joueur:
    pv = 0
    mana = 0
    def __init__(self):
        self.pv = 150
        self.mana = 100

    def isDead(self):
        return self.pv < 0

    def isAlive(self):
        return self.pv > 0

    def __lt__(self, other):
        return self.pv < other.pv

    def attack(self, other):
        print(__name__)
        other.pv -= 5

    def __str__(self):
        return "PV : " + str(self.pv) + "\nMana : " + str(self.mana)
