from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    pixmap = QPixmap("body.png")
    ui.Body.setPixmap(pixmap)
    sys.exit(app.exec())
    