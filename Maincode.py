from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow
from MainWindow import Ui_MainWindow  # Assuming MainWindow is your custom QMainWindow subclass
#Character class
import Character
from Character import *
class Setup(Ui_MainWindow):  # Subclass QMainWindow
    def __init__(self):
        super().__init__()

        self.PMC = Character()
        
    def connectFunctions(self):
        #Light bleed enables
        self.LLLB.stateChanged.connect(self.LeftLegLight)
        self.RLLB.stateChanged.connect(self.RightLegLight)
        self.LALB.stateChanged.connect(self.LeftArmLight)
        self.RALB.stateChanged.connect(self.RightArmLight)
        self.SLB.stateChanged.connect(self.StomachLight)
        self.TLB.stateChanged.connect(self.ThoraxLight)
        self.HLB.stateChanged.connect(self.HeadLight)

        #Heavy bleed enables
        self.LLHB.stateChanged.connect(self.LeftLegHeavy)
        self.RLHB.stateChanged.connect(self.RightLegHeavy)
        self.LAHB.stateChanged.connect(self.LeftArmHeavy)
        self.RAHB.stateChanged.connect(self.RightArmHeavy)
        self.SHB.stateChanged.connect(self.StomachHeavy)
        self.THB.stateChanged.connect(self.ThoraxHeavy)
        self.HHB.stateChanged.connect(self.HeadHeavy)

        #Fracture enables
        self.LLFB.stateChanged.connect(self.LeftLegFracture)
        self.RLFB.stateChanged.connect(self.RightLegFracture)
        self.LAFB.stateChanged.connect(self.LeftArmFracture)
        self.RAFB.stateChanged.connect(self.RightArmFracture)

        #Health bar changes
        self.LLHealth.returnPressed.connect(self.ChangeLeftLegHealth)
        self.RLHealth.returnPressed.connect(self.ChangeRightLegHealth)
        self.LAHealth.returnPressed.connect(self.ChangeLeftArmHealth)
        self.RAHealth.returnPressed.connect(self.ChangeRightArmHealth)
        self.SHealth.returnPressed.connect(self.ChangeStomachHealth)
        self.THealth.returnPressed.connect(self.ChangeThoraxHealth)
        self.HHealth.returnPressed.connect(self.ChangeHeadHealth)

        self.MainTimer = QTimer()
        self.timeStep = 500
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.run)


    #Function to run constantly
    def run(self):
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


        

    #Functions for light bleeds
    def LeftLegLight(self):
        if self.LLLB.isChecked():
            self.LLL.show()
        else:
            self.LLL.hide()

    def RightLegLight(self):
        if self.RLLB.isChecked():
            self.RLL.show()
        else:
            self.RLL.hide()

    def LeftArmLight(self):
        if self.LALB.isChecked():
            self.LAL.show()
        else:
            self.LAL.hide()
    
    def RightArmLight(self):
        if self.RALB.isChecked():
            self.RAL.show()
        else:
            self.RAL.hide()
    
    def StomachLight(self):
        if self.SLB.isChecked():
            self.SL.show()
        else:
            self.SL.hide()

    def ThoraxLight(self):
        if self.TLB.isChecked():
            self.TL.show()
        else:
            self.TL.hide()

    def HeadLight(self):
        if self.HLB.isChecked():
            self.HL.show()
        else:
            self.HL.hide()

    #Functions for heavy bleeds
    def LeftLegHeavy(self):
        if self.LLHB.isChecked():
            self.LLH.show()
        else:
            self.LLH.hide()

    def RightLegHeavy(self):
        if self.RLHB.isChecked():
            self.RLH.show()
        else:
            self.RLH.hide()

    def LeftArmHeavy(self):
        if self.LAHB.isChecked():
            self.LAH.show()
        else:
            self.LAH.hide()
    
    def RightArmHeavy(self):
        if self.RAHB.isChecked():
            self.RAH.show()
        else:
            self.RAH.hide()
    
    def StomachHeavy(self):
        if self.SHB.isChecked():
            self.SH.show()
        else:
            self.SH.hide()

    def ThoraxHeavy(self):
        if self.THB.isChecked():
            self.TH.show()
        else:
            self.TH.hide()

    def HeadHeavy(self):
        if self.HHB.isChecked():
            self.HH.show()
        else:
            self.HH.hide()

    #Functions for fractures
    def LeftLegFracture(self):
        if self.LLFB.isChecked():
            self.LLB.show()
        else:
            self.LLB.hide()
    
    def RightLegFracture(self):
        if self.RLFB.isChecked():
            self.RLB.show()
        else:
            self.RLB.hide()

    def LeftArmFracture(self):
        if self.LAFB.isChecked():
            self.LAB.show()
        else:
            self.LAB.hide()

    def RightArmFracture(self):
        if self.RAFB.isChecked():
            self.RAB.show()
        else:
            self.RAB.hide()
  
    #Limb health functions
    def ChangeLeftLegHealth(self):
        try:
            val = int(self.LLHealth.text())
            if(val >= 0 and val < 66):
                self.PMC.setLeftLeg(val)
                
        except:
            return

    def ChangeRightLegHealth(self):
        try:    
            val = int(self.RLHealth.text())
            if(val >= 0 and val < 66):
                self.PMC.setRightLeg(val)
        except:
            return

    def ChangeLeftArmHealth(self):
        try:
            val = int(self.LAHealth.text())
            if(val >= 0 and val < 61):
                self.PMC.setLeftArm(val)
        except:
            return

    def ChangeRightArmHealth(self):
        try:  
            val = int(self.RAHealth.text())
            if(val >= 0 and val < 61):
                self.PMC.setRightArm(val)
        except:
            return      
    
    def ChangeStomachHealth(self):
        try:  
            val = int(self.SHealth.text())
            if(val >= 0 and val < 71):
                self.PMC.setHeadHealth(val)
        except:
            return
        
    def ChangeThoraxHealth(self):
        try:  
            val = int(self.THealth.text())
            if(val >= 0 and val < 86):
                self.PMC.setThoraxHealth(val)
        except:
            return
        
    def ChangeHeadHealth(self):
        try:  
            val = int(self.HHealth.text())
            if(val >= 0 and val < 36):
                self.PMC.setHeadHealth(val)
        except:
            return

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
    #default no status effects
    ui.LLL.hide()
    ui.LLH.hide()
    ui.LLB.hide()
    ui.RLL.hide()
    ui.RLH.hide()
    ui.RLB.hide()
    ui.LAL.hide()
    ui.LAH.hide()
    ui.LAB.hide()
    ui.RAL.hide()
    ui.RAH.hide()
    ui.RAB.hide()
    ui.SL.hide()
    ui.SH.hide()
    ui.TL.hide()
    ui.TH.hide()
    ui.HL.hide()
    ui.HH.hide()
    ui.HP.hide()
    ui.HPK.hide()
    ui.HO.hide()
    sys.exit(app.exec())
    