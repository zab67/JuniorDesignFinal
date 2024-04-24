class Thorax():
    def __init__(self):
        self.health = 85
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

    def setStatus(self, l, h):
        self.light = l
        self.heavy = h
        
    def getStatus(self):
        return (self.light, self.heavy)
    
    def subHealth(self, val):
        self.health = self.health - val
        if(self.health < 0):
            self.health = 0

    def addHealth(self, val):
        self.health = self.health + val
        if(self.health > 85):
            self.health = 85
        elif(self.health < 0):
            self.health = 0