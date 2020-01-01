from Entreprise import Entreprise
import matplotlib.pyplot as plt
import numpy as np

data = dict()
for a in range(1993, 2017):
    for m in range(12):
        for j in range(31):
            nomfichier = str(a)
            if (m + 1) < 10:
                nomfichier += '0' + str(m + 1)
            else:
                nomfichier += str(m + 1)
            if (j + 1) < 10:
                nomfichier += '0' + str(j + 1)
            else:
                nomfichier += str(j + 1)

            try:
                f = open("data/"+ nomfichier +".txt", 'r')
                print("Importation du fichier", nomfichier)
                i = 0
                for l in f:
                    l = l[:-1]
                    l = l.split('\t')
                    key = l[0]
                    if key not in data:
                        data[key] = Entreprise(key, l[1])
                    data[key].add_ouverture(a, m+1, j, l[2])
            except:
                pass

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
x = np.arange('2016-01-01', '2016-12-31', dtype='datetime64[D]')
keys = ['ES0109429037', 'FR0010425595']

lists = [[], []]
olds = [0, 0]
for d in list(x):
    date = str(d).split('-')
    print(date)
    for i in range(2):
        k = keys[i]
        v = data[k].ouvertures[int(date[0])][int(date[1])][int(date[2])-1]
        if v != None:
            olds[i] = v
        lists[i].append(olds[i])

for i in range(2):
    axs[i].plot(x, lists[i], label=data[keys[i]].libele)
    axs[i].legend()

plt.show()
