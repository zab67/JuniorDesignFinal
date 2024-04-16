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
        self.totalHealth:int = 440
        self.LLeg = Leg()
        self.RLeg = Leg()
        self.LArm = Arm()
        self.RArm = Arm()
        self.Stomach = Stomach()
        self.Thorax = Thorax()
        self.Head = Head()

    #Function to calculate total health
    def calculateTotal(self):
        self.totalHealth = self.LLeg.getHealth() + self.RLeg.getHealth() + self.LArm.getHealth() + self.RArm.getHealth() + self.Stomach.getHealth() + self.Thorax.getHealth() + self.Head.getHealth()

    #Functions to set the health of limbs + correct total
    def setLeftLeg(self, val):
        self.LLeg.setHealth(val)
        self.calculateTotal()

    def setRightLeg(self, val):
        self.RLeg.setHealth(val)
        self.calculateTotal()

    def setLeftArm(self, val):
        self.LArm.setHealth(val)
        self.calculateTotal()

    def setRightArm(self, val):
        self.RArm.setHealth(val)
        self.calculateTotal()
    
    def setStomachHealth(self, val):
        self.Stomach.setHealth(val)
        self.calculateTotal()

    def setThoraxHealth(self, val):
        self.Thorax.setHealth(val)
        self.calculateTotal()

    def setHeadHealth(self, val):
        self.Head.setHealth(val)
        self.calculateTotal()

    #Functions to return health values
    def getTotalHealth(self):
        return self.totalHealth

    def getLeftLeg(self):
        return self.LLeg.getHealth()

    def getRightLeg(self):
        return self.RLeg.getHealth()

    def getLeftArm(self):
        return self.LArm.getHealth()

    def getRightArm(self):
        return self.RArm.getHealth()

    def getStomach(self):
        return self.Stomach.getHealth()

    def getThorax(self):
        return self.Thorax.getHealth()

    def getHead(self):
        return self.Head.getHealth()



    
