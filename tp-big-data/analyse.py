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
i = 0

fig, ax = plt.subplots()
lines = []
x = np.arange('2016-01-01', '2016-12-31', dtype='datetime64[D]')
k = 'ES0109429037'
l = []
old = 0
for d in list(x):
    date = str(d).split('-')
    print(date)
    v = data[k].ouvertures[int(date[0])][int(date[1])][int(date[2])-1]
    if v != None:
        old = v
    l.append(old)
print(l)

# # x = np.arange(1, 13, 1)
# for k in data:
#     if i > 10:
#         break
#     i += 1
#     data[k].show_ouverture()
#     y = data[k].data_annee(2016)
ax.plot(x, l, label=data[k].libele)
#
ax.legend()
plt.show()
# print(data)
