class Stomach():
    def __init__(self):
        self.health = 70
        self.light:bool = False
        self.heavy:bool = False

    def setHealth(self, val):
        self.health = val

    def setLight(self, val):
        self.light = val

    def setHeavy(self, val):
        self.heavy = val
    
    def getHealth(self):
        return self.health