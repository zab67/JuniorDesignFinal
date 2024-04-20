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
    
    def setStatus(self, l, h, f):
        self.light = l
        self.heavy = h
        self.fracture = f

    def getStatus(self):
        return (self.light, self.heavy, self.fracture)
    
    def subHealth(self, val):
        self.health = self.health - val
        if(self.health < 0):
            self.health = 0
    
    def addHealth(self, val):
        self.health = self.health + val
        if(self.health > 65):
            self.health = 65