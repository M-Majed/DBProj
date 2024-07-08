from PyQt5 import QtCore, QtGui, QtWidgets
import resources

# * to open another window
from login import Ui_LoginWindow
from Signup import Ui_SignupWindow


class Ui_LoginSignupWindow(object):
    appstate = None
    def setupUi(self, LoginSignupWindow):
        self.appstate = {}
        LoginSignupWindow.setObjectName("LoginSignupWindow")
        LoginSignupWindow.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginSignupWindow.sizePolicy().hasHeightForWidth())
        LoginSignupWindow.setSizePolicy(sizePolicy)
        LoginSignupWindow.setMinimumSize(QtCore.QSize(600, 300))
        LoginSignupWindow.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Icons/Icons/spotify.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        LoginSignupWindow.setWindowIcon(icon)
        LoginSignupWindow.setStyleSheet(
            "background-image: url(:/Background/background/darkgreen.png);\n" ""
        )

        self.centralwidget = QtWidgets.QWidget(LoginSignupWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginBtn.sizePolicy().hasHeightForWidth())
        self.LoginBtn.setSizePolicy(sizePolicy)
        self.LoginBtn.setMinimumSize(QtCore.QSize(0, 70))
        self.LoginBtn.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LoginBtn.setFont(font)
        self.LoginBtn.setStyleSheet("background-color: rgb(32, 64, 62);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/Icons/Icons/login.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.LoginBtn.setIcon(icon1)
        self.LoginBtn.setIconSize(QtCore.QSize(25, 25))
        self.LoginBtn.setObjectName("LoginBtn")
        self.verticalLayout.addWidget(self.LoginBtn)

        self.SignupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SignupBtn.setMinimumSize(QtCore.QSize(0, 70))
        self.SignupBtn.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.SignupBtn.setFont(font)
        self.SignupBtn.setStyleSheet("background-color: rgb(32, 64, 62);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/Icons/Icons/signup.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.SignupBtn.setIcon(icon2)
        self.SignupBtn.setIconSize(QtCore.QSize(25, 25))
        self.SignupBtn.setObjectName("SignupBtn")
        self.verticalLayout.addWidget(self.SignupBtn)

        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        LoginSignupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginSignupWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginSignupWindow)

        # * Connect the LoginBtn to the method that will open another window
        self.LoginBtn.clicked.connect(self.open_login_window)
        self.LoginSignupWindow = LoginSignupWindow
        # * Connect the SignupBtn to the method that will open another window
        self.SignupBtn.clicked.connect(self.open_signup_window)
        self.LoginSignupWindow = LoginSignupWindow

    def retranslateUi(self, LoginSignupWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginSignupWindow.setWindowTitle(
            _translate("LoginSignupWindow", "Login/SignUp")
        )
        self.LoginBtn.setText(_translate("LoginSignupWindow", "Login"))
        self.SignupBtn.setText(_translate("LoginSignupWindow", "Sign Up"))

    # * open the login window
    def open_login_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_LoginWindow(
            self.LoginSignupWindow,
            self.appstate
        )  # * Pass the main window reference here
        self.ui.setupUi(self.window)
        self.window.show()
        self.LoginSignupWindow.close()

    # * open the signup window
    def open_signup_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_SignupWindow(self.LoginSignupWindow, self.appstate)
        self.ui.setupUi(self.window)
        self.window.show()
        self.LoginSignupWindow.close()

# global mystate
if __name__ == "__main__":
    import sys
    # global mystate
    # mystate = {}
    # mystate['test01'] = "yo"
    app = QtWidgets.QApplication(sys.argv)
    LoginSignupWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginSignupWindow()
    ui.setupUi(LoginSignupWindow)
    LoginSignupWindow.show()
    sys.exit(app.exec_())
