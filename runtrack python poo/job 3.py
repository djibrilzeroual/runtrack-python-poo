class Operation:
    def __init__(self, nbr, nbr2):
        self.nombre1 = nbr
        self.nombre2 = nbr2
    def addition(self):
        somme = self.nombre1 + self.nombre2
        print(somme)

calcul1 = Operation(12, 3)
calcul1.addition()
calcul2 = Operation(45, 89)
calcul2.addition()