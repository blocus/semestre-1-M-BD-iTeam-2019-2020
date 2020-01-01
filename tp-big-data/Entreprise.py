class Entreprise:
    id = None
    libele = None
    ouvertures = None

    def __init__(self, id, libele):
        self.id = id
        self.libele = libele
        self.ouvertures = {}

    def add_ouverture(self, annee, mois, jour, valeur):
        if annee not in self.ouvertures:
            self.ouvertures[annee] = dict()
            for m in range(12):
                self.ouvertures[annee][m+1] = list()
                for j in range(31):
                    self.ouvertures[annee][m+1].append(None)
        self.ouvertures[annee][mois][jour] = float(valeur)


    def show_ouverture(self):
        print(self.libele,  ' ==>', self.ouvertures[2016][1])

        print()

    def calc_moyenne(self, annee, mois):
        somme = 0
        nb = 0
        if annee in self.ouvertures:
            if mois in self.ouvertures[annee]:
                for val in self.ouvertures[annee][mois]:
                    if val != None:
                        somme += val
                        nb += 1
        if nb == 0:
            return 0
        else:
            return somme / nb

    def data_annee(self, annee):
        tmp = []
        if annee in self.ouvertures:
            for mois in range(12):
                tmp.append(self.calc_moyenne(annee, mois + 1))
        return tmp
