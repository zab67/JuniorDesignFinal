import Leg
from Leg import *
class Character():
    def __init__(self):
        #Health values
        self.totalHealth:int = 440
        self.leftLegHealth:int = 65 
        self.rightLegHealth:int = 65
        self.leftArmHealth:int = 60
        self.rightArmHealth:int = 60  
        self.stomachHealth:int = 70
        self.throaxHealth:int = 85
        self.headHealth:int = 35

    #Function to calculate total health
    def calculateTotal(self):
        totalHealth = self.leftLegHealth + self.rightLegHealth + self.leftArmHealth + self.rightArmHealth + self.stomachHealth + self.throaxHealth + self.headHealth

    #Functions to set the health of limbs + correct total
    def setLeftLeg(self, val):
        self.leftLegHealth = val
        calculateTotal()

    def setRightLeg(self, val):
        self.rightLegHealth = val
        calculateTotal()

    def setLeftArm(self, val):
        self.leftArmHealth = val
        calculateTotal()

    def setRightArm(self, val):
        self.rightArmHealth = val
        calculateTotal()
    
    def setStomachHealth(self, val):
        self.stomachHealth = val
        calculateTotal()

    def setThoraxHealth(self, val):
        self.throaxHealth = val
        calculateTotal()

    def setHeadHealth(self, val):
        self.headHealth = val
        calculateTotal()

    #Functions to return health values
    def getTotalHealth(self):
        return self.totalHealth

    def getLeftLeg(self):
        return self.leftLegHealth

    def getRightLeg(self):
        return self.rightLegHealth

    def getLeftArm(self):
        return self.leftArmHealth

    def getRightArm(self):
        return self.rightArmHealth

    def getStomach(self):
        return self.stomachHealth

    def getThorax(self):
        return self.throaxHealth

    def getHead(self):
        return self.headHealth



    
