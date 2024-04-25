import random

class Injector():
    def __init__(self, odds = 1):
        #obdolbos odds
        self.odds = odds
        #Start values
        self.begin = False
        self.count = 0

        # Postive effects of injector
        self.painkill_time = 0
        self.painkill_delay = 0

        self.strength = 0
        self.strength_time = 0
        self.strength_delay = 0

        self.noBleed_time = 0
        self.noBleed_delay = 0

        self.energyB = 0
        self.energyB_time = 0
        self.energyB_delay = 0

        self.hydrationB = 0
        self.hydrationB_time = 0
        self.hydrationB_delay = 0

        self.healthB = 0
        self.healthB_time = 0
        self.healthB_delay = 0

        self.health = 0
        self.health_delay = 0

        #Negitive effects of injector
        self.energyDB = 0
        self.energyDB_time = 0
        self.energyDB_delay = 0

        self.hydrationDB = 0
        self.hydrationDB_time = 0
        self.hydrationDB_delay = 0

        self.healthDB = 0
        self.healthDB_time = 0
        self.healthDB_delay = 0

    #Painkill effect for injector
    def addPK(self, time, delay):
        self.painkill_time = time
        self.painkill_delay = delay

    #Increase strength effect for injector
    def addStrength(self, val, time, delay):
        rand = random.random()
        if(rand <= self.odds):
            self.strength = val
            self.strength_time = time
            self.strength_delay = delay
    
    #Effect to stop bleeds for injector
    def addNoBleed(self, time, delay):
        self.noBleed_time = time
        self.noBleed_delay = delay

    #Adds the energy, hydration, and health attributes of injectors
    def addEnergyRate(self, val, time, delay):
        rand = random.random()
        if(rand <= self.odds):
            if(val > 0):
                self.energyB = val
                self.energyB_time = time
                self.energyB_delay = delay
            else:
                self.energyDB = val
                self.energyDB_time = time
                self.energyDB_delay = delay
    
    def addHydrationRate(self, val, time, delay):
        rand = random.random()
        if(rand <= self.odds):
            if(val > 0):
                self.hydrationB = val
                self.hydrationB_time = time
                self.hydrationB_delay = delay
            else:
                self.hydrationDB = val
                self.hydrationDB_time = time
                self.hydrationDB_delay = delay

    def addHealthRate(self, val, time, delay):
        rand = random.random()
        if(rand <= self.odds):
            if(val > 0):
                self.healthB = val
                self.healthB_time = time
                self.healthB_delay = delay
            else:
                self.healthDB = val
                self.healthDB_time = time
                self.healthDB_delay = delay
    
    def addHealth(self, val, delay):
        self.health = val
        self.health_delay = delay

    #Function to start timer count for injector
    def start(self):
        self.begin = True
        self.count = 0

    #Funtion to run the stimulant on timer
    def simulate(self):
        if(self.begin and self.count < 1800):
            if(self.count >= self.painkill_delay and self.count < (self.painkill_delay + self.painkill_time)):
                pk = True
            else:
                pk = False
            if(self.count >= self.strength_delay and self.count < (self.strength_delay + self.strength_time)):
                st = self.strength
            else:
                st = 0
            if(self.count >= self.noBleed_delay and self.count < (self.noBleed_delay + self.noBleed_time)):
                nb = True
            else:
                nb = False
            if(self.count >= self.energyB_delay and self.count < (self.energyB_delay + self.energyB_time)):
                en = self.energyB
            else:
                en = 0
            if(self.count >= self.energyDB_delay and self.count < (self.energyDB_delay + self.energyDB_time)):
                en += self.energyDB
            if(self.count >= self.hydrationB_delay and self.count < (self.hydrationB_delay + self.hydrationB_time)):
                hy = self.hydrationB
            else:
                hy = 0
            if(self.count >= self.hydrationDB_delay and self.count < (self.hydrationDB_delay + self.hydrationDB_time)):
                hy += self.hydrationDB
            if(self.count >= self.healthB_delay and self.count < (self.healthB_delay + self.healthB_time)):
                he = self.healthB
            else:
                he = 0
            if(self.count >= self.healthDB_delay and self.count < (self.healthDB_delay + self.healthDB_time)):
                he += self.healthDB
            if(self.count == self.health_delay):
                he += self.health
            self.count += 1
            #Return the effect values for every second
            return (pk,st,nb,en,hy,he)
        else:
            #If not selected default no effect values
            return (False, 0, False, 0, 0, 0)
    
    #Find the score of the injector for best calculation
    def getScore(self, health, bleeds, fracture, painkill, weight, overweight, energy, hydration):
        score = 0
        
        #Doing math that will be helpful for score calculations
        totalHealth = health[0] + health[1] + health[2] + health[3] + health[4] + health[5] + health[6]
        totalHeal = self.healthB * self.healthB_time
        totalBleed = self.healthDB * self.healthDB_time
        totalenergy = self.energyB * self.energyB_time + self.energyDB * self.energyDB_time
        totalhydration = self.hydrationB * self.hydrationB_time + self.hydrationDB * self.hydrationDB_time
        
        #Score for painkill effect
        #If there is a fracture and not under painkill then positive points
        if(fracture and self.painkill_time > 0 and not painkill):
            score += 500
        
        #Score for bleed reduction effect
        #If there is no bleed effect the score is higher for every bleed
        if(self.noBleed_time > 0):
            score += bleeds[0] * 2100 + bleeds[1] * 2100
        
        #Score for strength effect
        #If the character is overweight score increase for amount of helpful strength
        if(weight - 30 - overweight > 0):
            hold  = (weight - 30)
            if(hold > self.strength):
                hold = self.strength
            score += hold * 80
        
        #Score for energy effects
        #If energy is less than 50 the energy score effect is doubled
        if(energy < 50):
            score += totalenergy * 2
        else:
            score += totalenergy
        
        #Score for hydration effects
        #If hydration is less than 50 the hydration score effect is doubled
        if(hydration < 50):
            score += totalhydration * 2
        else:
            score += totalhydration
        
        #Score for health effects
        #For health debuff negitive for all low values and increase negitive for death
        if(self.healthDB_time > 0):
            score += totalBleed * 5
            if(totalHealth + totalBleed < 0):
                score += totalHealth + totalBleed * 10

        #If head and thorax are low then healing is higher score
        if(totalHeal > 100 and (health[5] < 16 or health[6] < 16)):
            score += self.healthB * 50

        #If positive health effect give points for only healing possible to body                
        if(self.healthB_time > 0):
            score += totalHeal * 10
            if(totalHeal + totalHealth> 440):
                score -= (totalHealth + totalHeal - 440) * 10

        #Give positive or negitive points for heal value
        if(self.health > 0):
            if(self.health + totalHealth> 440):
                score -= (totalHealth + totalHeal - 440) * 5
        elif(self.health < 0):
            score += self.health * 5

        #Randomization of obdolbos makes it not good
        if(self.odds == 0.25):
            score = -100

        return score

    