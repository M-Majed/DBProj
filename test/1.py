from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PyQt5 Tutorial")
        self.initUI()

    def initUI(self): #* things in window
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(100, 100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Button Clicked")
        self.update()

    def update(self):
        self.label.adjustSize() #* adjust size of label


def window():
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

window()