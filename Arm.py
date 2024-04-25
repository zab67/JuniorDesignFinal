class Arm():
    #Initial values
    def __init__(self):
        self.health = 60
        self.light:bool = False
        self.heavy:bool = False
        self.fracture:bool = False

    #Setter Funtions
    def setHealth(self, val):
        self.health = val

    def setLight(self, val):
        self.light = val

    def setHeavy(self, val):
        self.heavy = val

    def setFracture(self, val):
        self.fracture = val
    
    def setStatus(self, l, h, f):
        self.light = l
        self.heavy = h
        self.fracture = f
    
    #Getter Functions
    def getHealth(self):
        return self.health
    
    def getStatus(self):
        return (self.light, self.heavy, self.fracture)
    
    #Health modifictation
    def subHealth(self, val):
        self.health = self.health - val
        if(self.health < 0):
            self.health = 0

    def addHealth(self, val):
        self.health = self.health + val
        if(self.health > 60):
            self.health = 60
        elif(self.health < 0):
            self.health = 0