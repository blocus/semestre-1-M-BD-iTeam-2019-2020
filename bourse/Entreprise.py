class Entreprise:
    id = None
    libele = None
    historique = {}

    def __init__(self, id, libele):
        self.id = id
        self.libele = libele

    def add_historique(self, annee, mois, jour, valeur):
        if annee not in self.historique:
            self.historique[annee] = {}
        if mois not in self.historique[annee]:
            self.historique[annee][mois] = []
            for i in range(31):
                self.historique[annee][mois].append(None)
        self.historique[annee][mois][jour - 1] = float(valeur)
        
