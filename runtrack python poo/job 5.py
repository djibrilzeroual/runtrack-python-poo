class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Le point a pour coordonnées ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")

    def changerX(self, nx):
        self.x = nx

    def changerY(self, ny):
        self.y = ny

point1 = Point(14, 7)


point1.afficherLesPoints() 


point1.afficherX() 
point1.afficherY() 


point1.changerX(15)
point1.afficherX() 


point1.changerY(17)
point1.afficherY() 