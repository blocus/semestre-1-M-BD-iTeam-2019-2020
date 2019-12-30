class Entreprise:
    nom = None
    ca_2018 = 0
    ca_2019 = 0
    nb_employee = 0

    def __init__(self, nom, ca_2018, ca_2019, nb_employee):
        self.nom = nom
        self.ca_2018 = int(ca_2018)
        self.ca_2019 = int(ca_2019)
        self.nb_employee = int(nb_employee)

    def __str__(self):
        return self.nom + " (" + str(self.nb_employee) + ")"

    def __lt__(self, other):
        return self.nb_employee < other.nb_employee

    # def __str__(self):
    #     return self.nom
