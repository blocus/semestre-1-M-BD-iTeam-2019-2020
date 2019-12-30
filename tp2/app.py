from Entreprise import Entreprise

fichier = open('input.csv', 'r')
fichier.readline()

liste_entreprises = []

for line in fichier:
    line = line[:-1]
    line = line.split(';')
    liste_entreprises.append(Entreprise(line[0], line[1], line[2], line[3]))


liste_entreprises.sort()

for ent in liste_entreprises:
    print(ent)
