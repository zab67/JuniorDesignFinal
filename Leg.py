class Leg():
    def __init__(self):
        self.health = 65
        self.light:bool = False
        self.heavy:bool = False
        self.fracture:bool = False

    def setHealth(self, val):
        self.health = val

    def setLight(self, val):
        self.light = val

    def setHeavy(self, val):
        self.heavy = val

    def setFracture(self, val):
        self.fracture = val

    def getHealth(self):
        return self.health