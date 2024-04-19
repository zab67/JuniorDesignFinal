import Leg
from Leg import *
import Arm
from Arm import *
import Stomach
from Stomach import *
import Thorax
from Thorax import *
import Head
from Head import *
class Character():
    def __init__(self):
        #Health values
        self.totalHealth = 440
        self.weight = 6
        self.energy = 100
        self.hydration = 100
        self.LLeg = Leg()
        self.RLeg = Leg()
        self.LArm = Arm()
        self.RArm = Arm()
        self.Stomach = Stomach()
        self.Thorax = Thorax()
        self.Head = Head()
        self.count = 0
        self.painkill = False

    #Function to calculate total health
    def calculateTotal(self):
        self.totalHealth = self.LLeg.getHealth() + self.RLeg.getHealth() + self.LArm.getHealth() + self.RArm.getHealth() + self.Stomach.getHealth() + self.Thorax.getHealth() + self.Head.getHealth()

    #Funtions for additonal details
    def setWeight(self, val):
        self.weight = val
    
    def setEnergy(self, val):
        self.energy = val

    def setHydration(self, val):
        self.hydration = val

    #Functions to set the health of limbs + correct total
    def setLeftLeg(self, val):
        self.LLeg.setHealth(val)
        self.calculateTotal()

    def setLeftLegStatus(self, l, h, f):
        self.LLeg.setStatus(l, h, f)

    def setRightLeg(self, val):
        self.RLeg.setHealth(val)
        self.calculateTotal()

    def setRightLegStatus(self, l, h, f):
        self.RLeg.setStatus(l, h, f)

    def setLeftArm(self, val):
        self.LArm.setHealth(val)
        self.calculateTotal()

    def setLeftArmStatus(self, l, h, f):
        self.LArm.setStatus(l, h, f)

    def setRightArm(self, val):
        self.RArm.setHealth(val)
        self.calculateTotal()

    def setRightArmStatus(self, l, h, f):
        self.RArm.setStatus(l, h, f)
    
    def setStomachHealth(self, val):
        self.Stomach.setHealth(val)
        self.calculateTotal()

    def setStomachStatus(self, l, h):
        self.Stomach.setStatus(l, h)

    def setThoraxHealth(self, val):
        self.Thorax.setHealth(val)
        self.calculateTotal()
    
    def setThoraxStatus(self, l, h):
        self.Thorax.setStatus(l, h)

    def setHeadHealth(self, val):
        self.Head.setHealth(val)
        self.calculateTotal()
    
    def setHeadStatus(self, l, h):
        self.Head.setStatus(l, h)

    #Functions to return health values
    def getTotalHealth(self):
        return round(self.totalHealth)

    def getLeftLeg(self):
        return round(self.LLeg.getHealth())
    
    def getLeftLegStatus(self):
        return self.LLeg.getStatus()

    def getRightLeg(self):
        return round(self.RLeg.getHealth())
    
    def getRightLegStatus(self):
        return self.RLeg.getStatus()

    def getLeftArm(self):
        return round(self.LArm.getHealth())
    
    def getLeftArmStatus(self):
        return self.LArm.getStatus()

    def getRightArm(self):
        return round(self.RArm.getHealth())
    
    def getRightArmStatus(self):
        return self.RArm.getStatus()

    def getStomach(self):
        return round(self.Stomach.getHealth())
    
    def getStomachStatus(self):
        return self.Stomach.getStatus()

    def getThorax(self):
        return round(self.Thorax.getHealth())
    
    def getThoraxStatus(self):
        return self.Thorax.getStatus()

    def getHead(self):
        return round(self.Head.getHealth())
    
    def getHeadStatus(self):
        return self.Head.getStatus()
    
    #Funtions for additonal details
    def getWeight(self):
        return self.weight
    
    def getEnergy(self):
        return self.energy

    def getHydration(self):
        return self.hydration
    
    def getIfFracture(self):
        (hold, hold, frac1) = self.LLeg.getStatus()
        (hold, hold, frac2) = self.RLeg.getStatus()
        (hold, hold, frac3) = self.LArm.getStatus()
        (hold, hold, frac4) = self.RArm.getStatus()
        return(frac1 or frac2 or frac3 or frac4)
    
    def getIfPainKill(self):
        return self.painkill
    
    def timeStep(self):
        self.count += 1
        if((self.count % 15 == 0)):
            self.energy -= 1
        if((self.count % 20 == 0)):
            self.hydration -= 1
        (l1, h1, hold) = self.LLeg.getStatus()
        (l2, h2, hold) = self.RLeg.getStatus()
        (l3, h3, hold) = self.LArm.getStatus()
        (l4, h4, hold) = self.RArm.getStatus()
        (l5, h5) = self.Stomach.getStatus()
        (l6, h6) = self.Thorax.getStatus()
        (l7, h7) = self.Head.getStatus()
        if(l1 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h1 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)
        if(l2 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h2 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)
        if(l3 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h3 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)
        if(l4 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h4 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)
        if(l5 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h5 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)
        if(l6 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h6 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)
        if(l7 and (self.count % 6 == 0)):
            self.LLeg.subHealth(0.8)
            self.RLeg.subHealth(0.8)
            self.LArm.subHealth(0.8)
            self.RArm.subHealth(0.8)
            self.Stomach.subHealth(0.8)
            self.Thorax.subHealth(0.8)
            self.Head.subHealth(0.8)
        if(h7 and (self.count % 4 == 0)):
            self.LLeg.subHealth(0.9)
            self.RLeg.subHealth(0.9)
            self.LArm.subHealth(0.9)
            self.RArm.subHealth(0.9)
            self.Stomach.subHealth(0.9)
            self.Thorax.subHealth(0.9)
            self.Head.subHealth(0.9)

        self.calculateTotal()
        



    
