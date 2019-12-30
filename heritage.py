from Joueur import Joueur
from autreClasses import Chasseur, Druid, Voleur


j = Joueur()
d = Druid()
c = Chasseur()
v = Voleur()

print("Joueur")
print(j)
print("Druide")
print(d)

d.attack(j)

print("Joueur")
print(j)
print("Druide")
print(d)

while (j.isAlive() and d.isAlive()):
    d.attack(j)
    j.attack(d)

    print("Joueur")
    print(j)
    print("Druide")
    print(d)

print(__name__)
