class Leg():
    def __init__(self):
        health = 65
        light:bool = False
        heavy:bool = False
        fracture:bool = False

    def setHealth(self, val):
        self.health = val

    def setLight(self, val):
        self.light = val

    def setHeavy(self, val):
        self.heavy = val

    def setFracture(self, val):
        self.fracture = val