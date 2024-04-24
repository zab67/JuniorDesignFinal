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
        #Rates
        self.energyRate = 0
        self.hydrationRate = 0
        #Limbs
        self.LLeg = Leg()
        self.RLeg = Leg()
        self.LArm = Arm()
        self.RArm = Arm()
        self.Stomach = Stomach()
        self.Thorax = Thorax()
        self.Head = Head()
        #Count timer
        self.count = 0
        #Effect values
        self.painkill = False
        self.stronger = 0
        self.tired = 0
        self.thirst = 0
        self.hp = 0

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
    #Functions to set limb statuses
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

    #Functions to return health values and limb statuses
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
        return round(self.energy)

    def getHydration(self):
        return round(self.hydration)
    
    #Function to tell if there is a break
    def getIfFracture(self):
        (hold, hold, frac1) = self.LLeg.getStatus()
        (hold, hold, frac2) = self.RLeg.getStatus()
        (hold, hold, frac3) = self.LArm.getStatus()
        (hold, hold, frac4) = self.RArm.getStatus()
        return(frac1 or frac2 or frac3 or frac4)
    
    #Return if painkill is true
    def getIfPainKill(self):
        return self.painkill
    
    #Simulates the effects that occur every second
    def timeStep(self):
        self.count += 1
        #Hydration and energy effects
        self.energy += self.tired
        self.energyRate = self.tired - 0.05
        self.tired = 0
        if((self.count % 15 == 0)):
            self.energy -= 1
        if(self.energy < 0):
            self.energy = 0
        if(self.energy > 100):
            self.energy = 100
        self.hydration += self.thirst
        self.hydrationRate = self.thirst - 0.07
        self.thirst = 0
        if((self.count % 20 == 0)):
            self.hydration -= 1
        if(self.hydration < 0):
            self.hydration = 0
        if(self.hydration > 100):
            self.hydration = 100
        #Gets the bleeds of limbs
        (l1, h1, hold) = self.LLeg.getStatus()
        (l2, h2, hold) = self.RLeg.getStatus()
        (l3, h3, hold) = self.LArm.getStatus()
        (l4, h4, hold) = self.RArm.getStatus()
        (l5, h5) = self.Stomach.getStatus()
        (l6, h6) = self.Thorax.getStatus()
        (l7, h7) = self.Head.getStatus()
        #Calculates the new health of limbs given bleeds
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
        #Calculkates the heal per limb
        limbs = 0
        if(self.LLeg.getHealth() < 65):
            limbs += 1
        if(self.RLeg.getHealth() < 65):
            limbs += 1
        if(self.LArm.getHealth() < 60):
            limbs += 1
        if(self.RArm.getHealth() < 60):
            limbs += 1
        if(self.Stomach.getHealth() < 70):
            limbs += 1
        if(self.Thorax.getHealth() < 85):
            limbs += 1
        if(self.Head.getHealth() < 35):
            limbs += 1
        #Heals the limbs
        if(self.hp > 0):
            if(self.LLeg.getHealth() < 65):
                self.LLeg.addHealth(self.hp/limbs)
            if(self.RLeg.getHealth() < 65):
                self.RLeg.addHealth(self.hp/limbs)
            if(self.LArm.getHealth() < 60):
                self.LArm.addHealth(self.hp/limbs)
            if(self.RArm.getHealth() < 60):
                self.RArm.addHealth(self.hp/limbs)
            if(self.Stomach.getHealth() < 70):
                self.Stomach.addHealth(self.hp/limbs)
            if(self.Thorax.getHealth() < 85):
                self.Thorax.addHealth(self.hp/limbs)
            if(self.Head.getHealth() < 35):
                self.Head.addHealth(self.hp/limbs)
            limbs = 0
        elif(self.hp < 0):
            if(self.LLeg.getHealth() > 0):
                limbs += 1
            if(self.RLeg.getHealth() > 0):
                limbs += 1
            if(self.LArm.getHealth() > 0):
                limbs += 1
            if(self.RArm.getHealth() > 0):
                limbs += 1
            if(self.Stomach.getHealth() > 0):
                limbs += 1
            if(self.Thorax.getHealth() > 0):
                limbs += 1
            if(self.Head.getHealth() > 0):
                limbs += 1
            if(self.LLeg.getHealth() > 0):
                self.LLeg.addHealth(self.hp/limbs)
            if(self.RLeg.getHealth() > 0):
                self.RLeg.addHealth(self.hp/limbs)
            if(self.LArm.getHealth() > 0):
                self.LArm.addHealth(self.hp/limbs)
            if(self.RArm.getHealth() > 0):
                self.RArm.addHealth(self.hp/limbs)
            if(self.Stomach.getHealth() > 0):
                self.Stomach.addHealth(self.hp/limbs)
            if(self.Thorax.getHealth() > 0):
                self.Thorax.addHealth(self.hp/limbs)
            if(self.Head.getHealth() > 0):
                self.Head.addHealth(self.hp/limbs)
            limbs = 0
        
        self.hp = 0   
        self.calculateTotal()

    #Acitivates the effect of stimulant injectors
    def effect(self,effects):
        if(effects[0]):
            self.painkill = True 
        if(effects[1] > self.stronger):
            self.stronger = effects[1]
        if(effects[2]):
            self.LLeg.setStatus(False, False, self.LLeg.getStatus()[2])
            self.RLeg.setStatus(False, False, self.RLeg.getStatus()[2])
            self.LArm.setStatus(False, False, self.LArm.getStatus()[2])
            self.RArm.setStatus(False, False, self.RArm.getStatus()[2])
            self.Stomach.setStatus(False, False)
            self.Thorax.setStatus(False, False)
            self.Head.setStatus(False, False)
        self.tired += effects[3]
        self.thirst += effects[4]
        self.hp += effects[5]
        

    #Returns the strength boost
    def getStronger(self):
        return self.stronger
    
    #Returns the rates
    def getRates(self):
        return (self.energyRate, self.hydrationRate)

    #Returns the body data for injector
    def getHealthData(self):
        return (self.getLeftLeg(), self.getRightLeg(), self.getLeftArm(), self.getRightArm(), self.getStomach(), self.getThorax(), self.getHead())
    
    def getBleedData(self):
        countl = 0
        counth = 0
        data = self.getLeftLegStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        data = self.getRightLegStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        data = self.getLeftArmStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        data = self.getRightArmStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        data = self.getStomachStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        data = self.getThoraxStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        data = self.getHeadStatus()
        if(data[0]):
            countl += 1
        if(data[1]):
            counth += 1
        
        return (countl, counth)

        



    
