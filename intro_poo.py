class User:
    nom = "name"
    prenom = "last name"
    age = 21
    email = None

    def __init__(self, nom, prenom, age, mail = None):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = mail

    def __eq__(self, other): # equal
        return self.email == other.email

    def __ne__(self, other): # not equal
        return self.email != other.email

    def __lt__(self, other): # little than
        return self.age < other.age

    def __str__(self):
        return self.nom + " " + self.prenom

    def dict(self):
        return({
            'nom' : self.nom,
            'prenom' : self.prenom,
            'age' : self.age,
            'email' : self.email
        })

    # __gt__  greater than
    # __ge__  greater or equal
    # __le__  little or equal

    def direBonjour(self):
        print("Bonjour", self.nom, self.prenom)

class Animal:
    nom = "name"
    age = 3

    def direBonjour(self):
        print("Miaw")


ahmed = User("Ahmed", "Elouzi", 29, "ahmed@gmail.com")
neila = User("neila", "qsd", 1, "neila@gmail.com")

print(ahmed.dict())
print(neila.dict())

print(neila != ahmed)
ponpon = Animal()
ahmed.direBonjour()
ponpon.direBonjour()
