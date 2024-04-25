class Stomach():
    #Initial values
    def __init__(self):
        self.health = 70
        self.light:bool = False
        self.heavy:bool = False

    #Setter Funtions
    def setHealth(self, val):
        self.health = val

    def setLight(self, val):
        self.light = val

    def setHeavy(self, val):
        self.heavy = val
    
    def setStatus(self, l, h):
        self.light = l
        self.heavy = h
        
    #Getter Functions
    def getHealth(self):
        return self.health
    
    def getStatus(self):
        return (self.light, self.heavy)
    
    #Health modifictation
    def subHealth(self, val):
        self.health = self.health - val
        if(self.health < 0):
            self.health = 0

    def addHealth(self, val):
        self.health = self.health + val
        if(self.health > 70):
            self.health = 70
        elif(self.health < 0):
            self.health = 0