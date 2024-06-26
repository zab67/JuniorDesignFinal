from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow
from MainWindow import Ui_MainWindow  # Assuming MainWindow is your custom QMainWindow subclass

#Character class for effect simulatiom
import Character
from Character import *

#Injector class for creating stimulant injectors
import Injector
from Injector import *

class Setup(Ui_MainWindow):  # Subclass QMainWindow
    #Intiliize character and injectors
    def __init__(self):
        super().__init__()
        
        #Create simulated body
        self.PMC = Character()

        #initilize all injectors with their immidiate values 
        self.morphine = Injector()
        self.morphine.addPK(305, 0)
        self.morphine.addEnergyRate(-10,1,0)
        self.morphine.addHydrationRate(-15,1,0)

        self.l1 = Injector()
        self.l1.addPK(120, 0)
        self.l1.addStrength(20 * 0.6,120,1)
        self.l1.addEnergyRate(-0.45,60,1)
        self.l1.addHydrationRate(-0.45,60,1)

        self.trimadol = Injector()
        self.trimadol.addPK(185, 0)
        self.trimadol.addStrength(10 * 0.6,180,1)
        self.trimadol.addEnergyRate(-0.5,180,1)
        self.trimadol.addHydrationRate(-0.5,180,1)

        self.adrenaline = Injector()
        self.adrenaline.addPK(65, 0)
        self.adrenaline.addStrength(10 * 0.6,60,1)
        self.adrenaline.addHealthRate(4,15,1)
        self.adrenaline.addEnergyRate(-0.8,30,50)
        self.adrenaline.addHydrationRate(-1,30,50)

        self.propital = Injector()
        self.propital.addPK(245, 0)
        self.propital.addHealth(20, 0)
        self.propital.addHealthRate(1,300,1)

        self.eTG = Injector()
        self.eTG.addHealthRate(6.5,60,1)
        self.eTG.addEnergyRate(0.5,60,1)
        self.eTG.addHealth(-5, 6.5)
        self.eTG.addEnergyRate(-3,20,65)

        self.perfotora = Injector()
        self.perfotora.addHealthRate(1.5,60,1)
        self.perfotora.addNoBleed(60, 1)
        self.perfotora.addHealth(-15, 60)
        self.perfotora.addEnergyRate(-1.1,60,60)

        self.aHF1 = Injector()
        self.aHF1.addHealth(5,0)
        self.aHF1.addNoBleed(60, 1)
        self.aHF1.addHydrationRate(-0.3,120,1)

        self.zagustin = Injector()
        self.zagustin.addNoBleed(200, 0)
        self.zagustin.addHydrationRate(-1.4,40,170)

        self.pNB = Injector()
        self.pNB.addStrength(20 * 0.6,40,1)
        self.pNB.addHealthRate(3,40,1)
        self.pNB.addHealth(-20, 41)

        self.obdolbos = Injector(0.25)
        self.obdolbos.addStrength(10 * 0.6 + 0.1,600,1)
        self.obdolbos.addHealthRate(1,600,1)
        self.obdolbos.addHydrationRate(-1,600,1)
        self.obdolbos.addEnergyRate(-1,600,1)
        self.obdolbos.addHealthRate(-600,600,1)

        self.obdolbos2 = Injector()
        self.obdolbos2.addStrength(20 * 0.6 + 27,1800,1)
        self.obdolbos2.addEnergyRate(-1,1800,1)
        self.obdolbos2.addHydrationRate(-1,1800,1)

        self.mULE = Injector()
        self.mULE.addStrength(30,900,1)
        self.mULE.addHealthRate(-0.1,900,1)
        
    #Connect Ui to functions
    def connectFunctions(self):
        #Light bleed enables
        self.LLLB.clicked.connect(self.Statuses)
        self.RLLB.clicked.connect(self.Statuses)
        self.LALB.clicked.connect(self.Statuses)
        self.RALB.clicked.connect(self.Statuses)
        self.SLB.clicked.connect(self.Statuses)
        self.TLB.clicked.connect(self.Statuses)
        self.HLB.clicked.connect(self.Statuses)

        #Heavy bleed enables
        self.LLHB.clicked.connect(self.Statuses)
        self.RLHB.clicked.connect(self.Statuses)
        self.LAHB.clicked.connect(self.Statuses)
        self.RAHB.clicked.connect(self.Statuses)
        self.SHB.clicked.connect(self.Statuses)
        self.THB.clicked.connect(self.Statuses)
        self.HHB.clicked.connect(self.Statuses)

        #Fracture enables
        self.LLFB.clicked.connect(self.Statuses)
        self.RLFB.clicked.connect(self.Statuses)
        self.LAFB.clicked.connect(self.Statuses)
        self.RAFB.clicked.connect(self.Statuses)

        #Health bar force sets
        self.LLHealth.returnPressed.connect(self.ChangeHealth)
        self.RLHealth.returnPressed.connect(self.ChangeHealth)
        self.LAHealth.returnPressed.connect(self.ChangeHealth)
        self.RAHealth.returnPressed.connect(self.ChangeHealth)
        self.SHealth.returnPressed.connect(self.ChangeHealth)
        self.THealth.returnPressed.connect(self.ChangeHealth)
        self.HHealth.returnPressed.connect(self.ChangeHealth)

        #Extra stats force sets
        self.Weight.returnPressed.connect(self.ChangeAdditional)
        self.Energy.returnPressed.connect(self.ChangeAdditional)
        self.Hydration.returnPressed.connect(self.ChangeAdditional)

        #Injector activates which start timeline
        self.UMorphine.clicked.connect(self.MorphineSelect)
        self.UL1.clicked.connect(self.L1Select)
        self.UTrimadol.clicked.connect(self.TrimadolSelect)
        self.UAdrenaline.clicked.connect(self.AdrenalineSelect)
        self.UPropital.clicked.connect(self.PropitalSelect)
        self.UETG.clicked.connect(self.ETGSelect)
        self.UPerfotora.clicked.connect(self.PerfotoraSelect)
        self.UAHF1.clicked.connect(self.AHF1Select)
        self.UZagustin.clicked.connect(self.ZagustinSelect)
        self.UPNB.clicked.connect(self.PNBSelect)
        self.UObdolbos.clicked.connect(self.ObdolbosSelect)
        self.UObdolbos2.clicked.connect(self.Obdolbos2Select)
        self.UMULE.clicked.connect(self.MULESelect)
        self.speed.valueChanged.connect(self.timers)
        #Time speed calculation
        self.timers()
    
    #Setup timers for real time setup
    def timers(self):
        #Real time timers to run simulation
        self.SetTimer = QTimer()
        self.timeStep = round(500/(self.speed.value()))
        self.SetTimer.start(self.timeStep)
        self.SetTimer.timeout.connect(self.run) # Runs UI

        self.MainTimer = QTimer()
        self.timeStep = round(1000/(self.speed.value()))
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.step) # runs Interactions

    #Function to activate stimulant effects and run time effects
    def step(self):
        #Check if injector is running
        self.PMC.effect(self.morphine.simulate())
        self.PMC.effect(self.l1.simulate())
        self.PMC.effect(self.trimadol.simulate())
        self.PMC.effect(self.adrenaline.simulate())
        self.PMC.effect(self.propital.simulate())
        self.PMC.effect(self.eTG.simulate())
        self.PMC.effect(self.perfotora.simulate())
        self.PMC.effect(self.aHF1.simulate())
        self.PMC.effect(self.zagustin.simulate())
        self.PMC.effect(self.pNB.simulate())
        self.PMC.effect(self.obdolbos.simulate())
        self.PMC.effect(self.obdolbos2.simulate())
        self.PMC.effect(self.mULE.simulate())
        #PMC time effect
        self.PMC.timeStep()
        #Find best injector
        self.setBest()

    #Function to get values constantly for user interface and set display
    def run(self):
        if(self.PMC.getHead() == 0 or self.PMC.getThorax() == 0):
            self.end.show()

        #Gets the PMC health and displays them
        val = self.PMC.getLeftLeg()
        self.LeftLegHealth.setValue(val)
        self.LeftLegHealthValue.setText(str(val) + "/65")
        val = self.PMC.getRightLeg()
        self.RightLegHealth.setValue(val)
        self.RightLegHealthValue.setText(str(val) + "/65")
        val = self.PMC.getLeftArm()
        self.LeftArmHealth.setValue(val)
        self.LeftArmHealthValue.setText(str(val) + "/60")
        val = self.PMC.getRightArm()
        self.RightArmHealth.setValue(val)
        self.RightArmHealthValue.setText(str(val) + "/60")
        val = self.PMC.getStomach()
        self.StomachHealth.setValue(val)
        self.StomachHealthValue.setText(str(val) + "/70")
        val = self.PMC.getThorax()
        self.ThoraxHealth.setValue(val)
        self.ThoraxHealthValue.setText(str(val) + "/85")
        val = self.PMC.getHead()
        self.HeadHealth.setValue(val)
        self.HeadHealthValue.setText(str(val) + "/35")
        val = self.PMC.getTotalHealth()
        self.OverallHealth.setValue(val)
        self.OverallHealthValue.setText(str(val) + "/440")

        #Gets the PMC statuses and displays them
        val = self.PMC.getWeight()
        buff = self.PMC.getStronger()
        if(val < 30 + buff):
            self.HO.hide()
            self.WeightValue.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:700; color:#d7ffcb;">' + str(val) + '/ 60</span></p><p><br/></p><p><br/></p></body></html>')
        elif(val < 60 + buff):
            self.WeightValue.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:700; color:#ffe357;">' + str(val) + '/ 60</span></p><p><br/></p><p><br/></p></body></html>')
            self.HO.show()
        else:
            self.WeightValue.setText('<html><head/><body><p><span style=" font-size:12pt; font-weight:700; color:#ff2600;">' + str(val) + '/ 60</span></p><p><br/></p><p><br/></p></body></html>')            
            self.HO.show()
        val = self.PMC.getEnergy()
        self.EnergyValue.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:700; color:#fffb7d;">' + str(val) + '/100</span></p><p><br/></p></body></html>')
        val = self.PMC.getHydration()
        self.HydrationValue.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:700; color:#6ef3ff;">' + str(val) + '/100</span></p><p><br/></p></body></html>')
        (light, heavy, fracture) = self.PMC.getLeftLegStatus()

        #Gets the rate of decrease for energy and hydration
        (en, hy) = self.PMC.getRates()
        if(en < 0):
            self.EnergyRate.setText('<html><head/><body><p><span style=" font-weight:700; color:#fffb7d;">\\/ ' + str(abs(en)) + '</span></p></body></html>')
        else:
            self.EnergyRate.setText('<html><head/><body><p><span style=" font-weight:700; color:#fffb7d;">/\\ ' + str(en) + '</span></p></body></html>')
        if(hy < 0):
            self.HydrationRate.setText('<html><head/><body><p><span style=" font-weight:700; color:#6ef3ff;">\\/ ' + str(abs(hy)) + '</span></p></body></html>')
        else:
            self.HydrationRate.setText('<html><head/><body><p><span style=" font-weight:700; color:#6ef3ff;">/\\ ' + str(hy) + '</span></p></body></html>')
        
        #Gets the limb bleeds and fractures and displays them
        if(light):
            self.LLL.show()
        else:
            self.LLL.hide()
            self.LLLB.setChecked(False)
        if(heavy):
            self.LLH.show()
        else:
            self.LLH.hide()
            self.LLHB.setChecked(False)
        if(fracture):
            self.LLB.show()
        else:
            self.LLB.hide()

        (light, heavy, fracture) = self.PMC.getRightLegStatus()
        if(light):
            self.RLL.show()
        else:
            self.RLL.hide()
            self.RLLB.setChecked(False)
        if(heavy):
            self.RLH.show()
        else:
            self.RLH.hide()
            self.RLHB.setChecked(False)
        if(fracture):
            self.RLB.show()
        else:
            self.RLB.hide()

        (light, heavy, fracture) = self.PMC.getLeftArmStatus()
        if(light):
            self.LAL.show()
        else:
            self.LAL.hide()
            self.LALB.setChecked(False)
        if(heavy):
            self.LAH.show()
        else:
            self.LAH.hide()
            self.LAHB.setChecked(False)
        if(fracture):
            self.LAB.show()
        else:
            self.LAB.hide()

        (light, heavy, fracture) = self.PMC.getRightArmStatus()
        if(light):
            self.RAL.show()
        else:
            self.RAL.hide()
            self.RALB.setChecked(False)
        if(heavy):
            self.RAH.show()
        else:
            self.RAH.hide()
            self.RAHB.setChecked(False)
        if(fracture):
            self.RAB.show()
        else:
            self.RAB.hide()

        (light, heavy) = self.PMC.getStomachStatus()
        if(light):
            self.SL.show()
        else:
            self.SL.hide()
            self.SLB.setChecked(False)
        if(heavy):
            self.SH.show()
        else:
            self.SH.hide()
            self.SHB.setChecked(False)

        (light, heavy) = self.PMC.getThoraxStatus()
        if(light):
            self.TL.show()
        else:
            self.TL.hide()
            self.TLB.setChecked(False)
        if(heavy):
            self.TH.show()
        else:
            self.TH.hide()
            self.THB.setChecked(False)

        (light, heavy) = self.PMC.getHeadStatus()
        if(light):
            self.HL.show()
        else:
            self.HL.hide()
            self.HLB.setChecked(False)
        if(heavy):
            self.HH.show()
        else:
            self.HH.hide()
            self.HHB.setChecked(False)
        
        if(self.PMC.getIfFracture() and not(self.PMC.getIfPainKill())):
            self.HP.show()
        else:
            self.HP.hide()

        if(self.PMC.getIfPainKill()):
            self.HPK.show()
        else:
            self.HPK.hide()

    #Function to find the best injector at every moment
    def setBest(self):
        scores = []
        # runs the score function
        #Index1 gets limb health values
        #Index2 gets light and heavy bleed counts
        #Index3 gets if there is a fracture
        #Index4 gest if the painkill is applied
        #Index5 gets current weight
        #Index6 gets strength buff
        #Index7 gets energy of PMC
        #Index8 gets hydration of PMC
        scores.append(self.morphine.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Morphine: " + str(scores[0]))
        scores.append(self.l1.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("L1: " + str(scores[1]))
        scores.append(self.trimadol.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Trimadol: " + str(scores[2]))
        scores.append(self.adrenaline.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Adrenaline: " + str(scores[3]))
        scores.append(self.propital.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Propital: " + str(scores[4]))
        scores.append(self.eTG.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("ETG: " + str(scores[5]))
        scores.append(self.perfotora.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Perfotoran: " + str(scores[6]))
        scores.append(self.aHF1.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("AHF1: " + str(scores[7]))
        scores.append(self.zagustin.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Zafustin: " + str(scores[8]))
        scores.append(self.pNB.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("PNB: " + str(scores[9]))
        scores.append(self.obdolbos.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Obdolbos: " + str(scores[10]))
        scores.append(self.obdolbos2.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("Obdolbos2: " + str(scores[11]))
        scores.append(self.mULE.getScore(self.PMC.getHealthData(), self.PMC.getBleedData(), self.PMC.getIfFracture(), self.PMC.getIfPainKill(), self.PMC.getWeight(), self.PMC.getStronger(), self.PMC.getEnergy(), self.PMC.getHydration()))
        #print("MULE: " + str(scores[12]))
        #print("")
        #Sets the score label
        self.scores.setText("Morphine:     "+ str(scores[0]) +"\nL1:                  "+ str(scores[1]) +"\nTrimadol:       "+ str(scores[2]) +"\nAdrenaline:    "+ str(scores[3]) +"\nPropital:         "+ str(scores[4]) +"\nETG:                "+ str(scores[5]) +"\nPerfotoran:    "+ str(scores[6]) +"\nAHF1:             "+ str(scores[7]) +"\nZagustin:       "+ str(scores[8]) +"\nPNB:               "+ str(scores[9]) +"\nObdolbos:     "+ str(scores[10]) +"\nObdolbos2:   "+ str(scores[11]) +"\nMULE:            "+str(scores[12]))
        #Gets score list and sets list for best injector
        bestInjector = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        for i in range(len(scores)):
            if scores[i] == max(scores):
                bestInjector[i] = True
        #Sets the best injector in user interface
        self.MorphineB.setChecked(bestInjector[0])
        self.L1B.setChecked(bestInjector[1])
        self.TrimadolB.setChecked(bestInjector[2])
        self.AdrenalineB.setChecked(bestInjector[3])
        self.PropitalB.setChecked(bestInjector[4])
        self.ETGB.setChecked(bestInjector[5])
        self.PerfotoraB.setChecked(bestInjector[6])
        self.AHF1B.setChecked(bestInjector[7])
        self.ZagustinB.setChecked(bestInjector[8])
        self.PNBB.setChecked(bestInjector[9])
        self.ObdolbosB.setChecked(bestInjector[10])
        self.Obdolbos2B.setChecked(bestInjector[11])
        self.MULEB.setChecked(bestInjector[12])  

    #Functions for when the user starts an injector
    def MorphineSelect(self):
        self.morphine.start()

    def L1Select(self):
        self.l1.start()

    def TrimadolSelect(self):
        self.trimadol.start()

    def AdrenalineSelect(self):
        self.adrenaline.start()

    def PropitalSelect(self):
        self.propital.start()

    def ETGSelect(self):
        self.eTG.start()

    def PerfotoraSelect(self):
        self.perfotora.start()

    def AHF1Select(self):
        self.aHF1.start()

    def ZagustinSelect(self):
        self.zagustin.start()

    def PNBSelect(self):
        self.pNB.start()

    def ObdolbosSelect(self):
        self.obdolbos.start()
    def Obdolbos2Select(self):
        self.obdolbos2.start()

    def MULESelect(self):
        self.mULE.start()


        

    #Functions for limb statuses for user setup
    def Statuses(self):
        self.PMC.setLeftLegStatus(self.LLLB.isChecked(), self.LLHB.isChecked(), self.LLFB.isChecked())
        self.PMC.setRightLegStatus(self.RLLB.isChecked(), self.RLHB.isChecked(), self.RLFB.isChecked())
        self.PMC.setLeftArmStatus(self.LALB.isChecked(), self.LAHB.isChecked(), self.LAFB.isChecked())
        self.PMC.setRightArmStatus(self.RALB.isChecked(), self.RAHB.isChecked(), self.RAFB.isChecked())
        self.PMC.setStomachStatus(self.SLB.isChecked(), self.SHB.isChecked())
        self.PMC.setThoraxStatus(self.TLB.isChecked(), self.THB.isChecked())
        self.PMC.setHeadStatus(self.HLB.isChecked(), self.HHB.isChecked())

    #User set Limb health functions
    def ChangeHealth(self):
        try:
            val = int(self.LLHealth.text())
            if(val >= 0 and val < 66):
                self.PMC.setLeftLeg(val) 
        except:
            pass
        try:    
            val = int(self.RLHealth.text())
            if(val >= 0 and val < 66):
                self.PMC.setRightLeg(val)
        except:
            pass
        try:
            val = int(self.LAHealth.text())
            if(val >= 0 and val < 61):
                self.PMC.setLeftArm(val)
        except:
            pass
        try:  
            val = int(self.RAHealth.text())
            if(val >= 0 and val < 61):
                self.PMC.setRightArm(val)
        except:
            pass 
        try:  
            val = int(self.SHealth.text())
            if(val >= 0 and val < 71):
                self.PMC.setStomachHealth(val)
        except:
            pass
        try:  
            val = int(self.THealth.text())
            if(val >= 0 and val < 86):
                self.PMC.setThoraxHealth(val)
        except:
            pass
        try:  
            val = int(self.HHealth.text())
            if(val >= 0 and val < 36):
                self.PMC.setHeadHealth(val)
        except:
            return

    #Changes value for additonal body details
    def ChangeAdditional(self):
        #User set weight
        try:
            val = int(self.Weight.text())
            if(val >= 0 and val < 121):
                self.PMC.setWeight(val) 
        except:
            pass
        #User set energy
        try:
            val = int(self.Energy.text())
            if(val >= 0 and val < 101):
                self.PMC.setEnergy(val) 
        except:
            pass
        #user set hydration
        try:
            val = int(self.Hydration.text())
            if(val >= 0 and val < 101):
                self.PMC.setHydration(val) 
        except:
            return
        
#When program is started set the images up and hide nessasary images
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #window = MainWindow()
    window = QMainWindow()
    ui = Setup()
    ui.setupUi(window)
    ui.connectFunctions()
    window.show()
    #Setting the images of User Interface
    pixmap = QPixmap("New folder/body.png")
    ui.Body.setPixmap(pixmap)
    pixmap = QPixmap("New folder/light.webp")
    ui.LLL.setPixmap(pixmap)
    ui.RLL.setPixmap(pixmap)
    ui.LAL.setPixmap(pixmap)
    ui.RAL.setPixmap(pixmap)
    ui.SL.setPixmap(pixmap)
    ui.TL.setPixmap(pixmap)
    ui.HL.setPixmap(pixmap)
    pixmap = QPixmap("New folder/heavy.webp")
    ui.LLH.setPixmap(pixmap)
    ui.RLH.setPixmap(pixmap)
    ui.LAH.setPixmap(pixmap)
    ui.RAH.setPixmap(pixmap)
    ui.SH.setPixmap(pixmap)
    ui.TH.setPixmap(pixmap)
    ui.HH.setPixmap(pixmap)
    pixmap = QPixmap("New folder/fracture.webp")
    ui.LLB.setPixmap(pixmap)
    ui.RLB.setPixmap(pixmap)
    ui.LAB.setPixmap(pixmap)
    ui.RAB.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Pain.webp")
    ui.HP.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Painkill.webp")
    ui.HPK.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Overweight.webp")
    ui.HO.setPixmap(pixmap)
    pixmap = QPixmap("New folder/weight.png")
    ui.weight.setPixmap(pixmap)
    pixmap = QPixmap("New folder/water.png")
    ui.water.setPixmap(pixmap)
    pixmap = QPixmap("New folder/energy.png")
    ui.energy.setPixmap(pixmap)
    #Injectors
    pixmap = QPixmap("New folder/Morphine.webp")
    ui.Morphine.setPixmap(pixmap)
    pixmap = QPixmap("New folder/L1.webp")
    ui.L1.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Trimadol.webp")
    ui.Trimadol.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Adrenaline.webp")
    ui.Adrenaline.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Propital.webp")
    ui.Propital.setPixmap(pixmap)
    pixmap = QPixmap("New folder/ETG.webp")
    ui.ETG.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Perfotoran.webp")
    ui.Perfotora.setPixmap(pixmap)
    pixmap = QPixmap("New folder/AHF1.webp")
    ui.AHF1.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Zagustin.webp")
    ui.Zagustin.setPixmap(pixmap)
    pixmap = QPixmap("New folder/PNB.webp")
    ui.PNB.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Obdolbos.webp")
    ui.Obdolbos.setPixmap(pixmap)
    pixmap = QPixmap("New folder/Obdolbos2.webp")
    ui.Obdolbos2.setPixmap(pixmap)
    pixmap = QPixmap("New folder/M.U.L.E..webp")
    ui.MULE.setPixmap(pixmap)
    pixmap = QPixmap("New folder/End.png")
    ui.end.setPixmap(pixmap)
    ui.end.hide()
    
    sys.exit(app.exec())
    