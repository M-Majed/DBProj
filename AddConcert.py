from PyQt5 import QtCore, QtGui, QtWidgets
import resources


class Ui_AddConcertWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, AddConcertWindow):
        self.AddConcertWindow = AddConcertWindow
        AddConcertWindow.setObjectName("AddConcertWindow")
        AddConcertWindow.resize(400, 200)
        AddConcertWindow.setMinimumSize(QtCore.QSize(400, 200))
        AddConcertWindow.setMaximumSize(QtCore.QSize(400, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddConcertWindow.setWindowIcon(icon)
        AddConcertWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddConcertWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title_lineEdit = QtWidgets.QLineEdit(AddConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Title_lineEdit.setFont(font)
        self.Title_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Title_lineEdit.setObjectName("Title_lineEdit")
        self.verticalLayout.addWidget(self.Title_lineEdit)
        self.Venue_lineEdit = QtWidgets.QLineEdit(AddConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Venue_lineEdit.setFont(font)
        self.Venue_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Venue_lineEdit.setObjectName("Venue_lineEdit")
        self.verticalLayout.addWidget(self.Venue_lineEdit)
        self.Price_lineEdit = QtWidgets.QLineEdit(AddConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Price_lineEdit.setFont(font)
        self.Price_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Price_lineEdit.setObjectName("Price_lineEdit")
        self.verticalLayout.addWidget(self.Price_lineEdit)
        self.dateEdit = QtWidgets.QDateEdit(AddConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back_btn = QtWidgets.QPushButton(AddConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout_2.addWidget(self.Back_btn)
        self.Add_btn = QtWidgets.QPushButton(AddConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Add_btn.setFont(font)
        self.Add_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Add_btn.setObjectName("Add_btn")
        self.horizontalLayout_2.addWidget(self.Add_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.retranslateUi(AddConcertWindow)
        QtCore.QMetaObject.connectSlotsByName(AddConcertWindow)

        #$ My Part --------------------------------------------
        self.Back_btn.clicked.connect(self.open_parent_window)

    def retranslateUi(self, AddConcertWindow):
        _translate = QtCore.QCoreApplication.translate
        AddConcertWindow.setWindowTitle(_translate("AddConcertWindow", "Add Concert"))
        self.Title_lineEdit.setPlaceholderText(_translate("AddConcertWindow", "Title"))
        self.Venue_lineEdit.setPlaceholderText(_translate("AddConcertWindow", "Venue"))
        self.Price_lineEdit.setPlaceholderText(_translate("AddConcertWindow", "Tiket price"))
        self.Back_btn.setText(_translate("AddConcertWindow", "Back"))
        self.Add_btn.setText(_translate("AddConcertWindow", "Add concert"))

    def open_parent_window(self):
        self.parent.show()
        self.AddConcertWindow.close()