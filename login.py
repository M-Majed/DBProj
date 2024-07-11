from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from MusicList import Ui_MusicListWindow

class Ui_LoginWindow(object):
    def __init__(self, parent=None, appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, LoginWindow):
        self.LoginWindow = LoginWindow
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(600, 300)
        LoginWindow.setMinimumSize(QtCore.QSize(600, 300))
        LoginWindow.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off,)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.gridLayout = QtWidgets.QGridLayout(LoginWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Username_input = QtWidgets.QLineEdit(LoginWindow)
        self.Username_input.setMinimumSize(QtCore.QSize(400, 40))
        self.Username_input.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Username_input.setFont(font)
        self.Username_input.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n" "")
        self.Username_input.setInputMask("")
        self.Username_input.setObjectName("Username_input")
        self.gridLayout_2.addWidget(self.Username_input, 2, 0, 1, 1)
        self.Password_label = QtWidgets.QLabel(LoginWindow)
        self.Password_label.setMinimumSize(QtCore.QSize(0, 40))
        self.Password_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Password_label.setFont(font)
        self.Password_label.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);\n""background-color: rgb(22, 46, 51);")
        self.Password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_label.setObjectName("Password_label")
        self.gridLayout_2.addWidget(self.Password_label, 3, 0, 1, 1)
        self.Password_input = QtWidgets.QLineEdit(LoginWindow)
        self.Password_input.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password_input.setFont(font)
        self.Password_input.setStyleSheet("background-image: url(:/Background/background/transparent.png);")
        self.Password_input.setObjectName("Password_input")
        self.gridLayout_2.addWidget(self.Password_input, 4, 0, 1, 1)
        self.Username_label = QtWidgets.QLabel(LoginWindow)
        self.Username_label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.Username_label.setFont(font)
        self.Username_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Username_label.setAutoFillBackground(False)
        self.Username_label.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);\n""background-color: rgb(22, 46, 51);")
        self.Username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Username_label.setObjectName("Username_label")
        self.gridLayout_2.addWidget(self.Username_label, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.back_Btn = QtWidgets.QPushButton(LoginWindow)
        self.back_Btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_Btn.setFont(font)
        self.back_Btn.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(0, 0, 0);")
        self.back_Btn.setObjectName("back_Btn")
        self.horizontalLayout.addWidget(self.back_Btn)
        self.Login_Btn = QtWidgets.QPushButton(LoginWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_Btn.sizePolicy().hasHeightForWidth())
        self.Login_Btn.setSizePolicy(sizePolicy)
        self.Login_Btn.setMinimumSize(QtCore.QSize(100, 40))
        self.Login_Btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Login_Btn.setFont(font)
        self.Login_Btn.setAutoFillBackground(False)
        self.Login_Btn.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(0, 0, 0);")
        self.Login_Btn.setObjectName("Login_Btn")
        self.horizontalLayout.addWidget(self.Login_Btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.Login_icon = QtWidgets.QLabel(LoginWindow)
        self.Login_icon.setMinimumSize(QtCore.QSize(50, 52))
        self.Login_icon.setMaximumSize(QtCore.QSize(16777215, 16777214))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Login_icon.setFont(font)
        self.Login_icon.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""image: url(:/Icons/Icons/user.png);")
        self.Login_icon.setText("")
        self.Login_icon.setObjectName("Login_icon")
        self.gridLayout_2.addWidget(self.Login_icon, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        #$ My Part --------------------------------------------
        self.back_Btn.clicked.connect(self.open_parent_window)
        self.Login_Btn.clicked.connect(self.check_login)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.Username_input.setPlaceholderText(_translate("LoginWindow", "Enter your username"))
        self.Password_label.setText(_translate("LoginWindow", "Password"))
        self.Password_input.setPlaceholderText(_translate("LoginWindow", "Enter your password"))
        self.Username_label.setText(_translate("LoginWindow", "UserName"))
        self.back_Btn.setText(_translate("LoginWindow", "Back"))
        self.Login_Btn.setText(_translate("LoginWindow", "Login"))

    def open_parent_window(self):
        self.parent.show()
        self.LoginWindow.close()

    def check_login(self):
        username = self.Username_input.text()
        password = self.Password_input.text()
        dbm = DBM()
        dbm.db_connect()
        if check_login(dbm, username, password):
            print("Login successful")
            self.open_musicListWindow()
            self.appstate["username"] = username
            uid = get_userid_by_username(dbm, username)
            self.appstate["userid"] = uid # uid || None
            sub = is_subscribed(dbm, uid)
            if sub is not None:
                self.appstate["subscribed"] = sub
            else:
                self.appstate["subscribed"] = False
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Login failed")
            msg.setInformativeText("Invalid username or password")
            msg.setWindowTitle("Error")
            msg.exec_()
        dbm.db_disconnect()

    def open_musicListWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_MusicListWindow(
        self.LoginWindow,
        self.appstate
        )
        self.ui.setupUi(self.window)
        self.window.show()
        self.LoginWindow.close()
