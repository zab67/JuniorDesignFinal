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
        if(random.random() <= self.odds):
            self.strength = val
            self.strength_time = time
            self.strength_delay = delay
    
    #Effect to stop bleeds for injector
    def addNoBleed(self, time, delay):
        self.noBleed_time = time
        self.noBleed_delay = delay

    #Adds the energy, hydration, and health attributes of injectors
    def addEnergyRate(self, val, time, delay):
        if(random.random() <= self.odds):
            if(val > 0):
                self.energyB = val
                self.energyB_time = time
                self.energyB_delay = delay
            else:
                self.energyDB = val
                self.energyDB_time = time
                self.energyDB_delay = delay
    
    def addHydrationRate(self, val, time, delay):
        if(random.random() <= self.odds):
            if(val > 0):
                self.hydrationB = val
                self.hydrationB_time = time
                self.hydrationB_delay = delay
            else:
                self.hydrationDB = val
                self.hydrationDB_time = time
                self.hydrationDB_delay = delay

    def addHealthRate(self, val, time, delay):
        if(random.random() <= self.odds):
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

    #Function to start timer count
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
            return (pk,st,nb,en,hy,he)
        else:
            return (False, 0, False, 0, 0, 0)

    def getScore(self, health, bleeds, fracture):
        score = 0
        
        return score

    