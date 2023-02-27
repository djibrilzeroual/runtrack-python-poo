class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


animal = Animal()


animal.nommer("nice")
print("L'animal se nomme : ", animal.prenom)


print("L'age de l'animal  : ", animal.age)


animal.vieillir()


print("L'age de l'animal  : ", animal.age)
