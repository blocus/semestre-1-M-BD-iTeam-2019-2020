from Entreprise import Entreprise
import matplotlib.pyplot as plt
import numpy as np

data = {}

for annee in range(1993, 2020):
    for mois in range(12):
        for jour in range(31):
            nom_fichier = "data/" + str(annee)
            if (mois + 1) < 10 :
                nom_fichier += "0"
            nom_fichier += str(mois + 1)
            if (jour + 1) < 10 :
                nom_fichier += "0"
            nom_fichier += str(jour + 1) + '.txt'
            try:
                f = open(nom_fichier, "r")
                print(nom_fichier)
                for line in f:
                    line = line[:-1]
                    line = line.split("\t")
                    key = line[0]
                    if key not in data:
                        data[key] = {
                            'id' : key,
                            'libele' : line[1],
                            'historique' : {}
                        }

                    if annee not in data[key]['historique']:
                        data[key]['historique'][annee] = {}
                        for m in range(12):
                            data[key]['historique'][annee][m + 1] = []
                            for i in range(31):
                                data[key]['historique'][annee][m + 1].append(None)
                    data[key]['historique'][annee][mois + 1][jour] = float(line[2])
            except:
                pass

for k in data:
    print(k, end='\t')
k = input("Donner une clé :")
ent = data[k]
x = np.arange('2016-01-01', '2016-12-31', dtype='datetime64[D]')
y = []
old = 0
moy = {}
old_m = 1
s = 0
nb = 0
for date in x:
    v = 0
    d = str(date).split('-')
    annee = int(d[0])
    mois  = int(d[1])
    jour  = int(d[2])

    if mois != old_m:
        old_m = mois
        if nb != 0:
            moy[old_m] = s / nb
        else:
            moy[old_m] = 0
        s = 0

    print(annee, mois, jour -1)
    v = ent['historique'][annee][mois][jour - 1]
    if v != None:
        s += v
        old = v
    y.append(v)

fig1, ax1 = plt.subplots()
fig, ax = plt.subplots()
ax.plot(x, y, label=ent['libele'])
ax1.bar(list(moy.keys()),list(moy.values()) )

ax.legend()
plt.show()
