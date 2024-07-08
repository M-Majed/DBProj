from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import sys
from PyQt5.uic import loadUi
from login_signup import Ui_LoginSignupWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginSignupWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginSignupWindow()
    ui.setupUi(LoginSignupWindow)
    LoginSignupWindow.show()
    sys.exit(app.exec_())