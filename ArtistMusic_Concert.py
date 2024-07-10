from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM

class Ui_ArtistMusic_ConcertWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, ArtistMusic_ConcertWindow):
        self.ArtistMusic_ConcertWindow = ArtistMusic_ConcertWindow
        ArtistMusic_ConcertWindow.setObjectName("ArtistMusic_ConcertWindow")
        ArtistMusic_ConcertWindow.resize(559, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ArtistMusic_ConcertWindow.setWindowIcon(icon)
        ArtistMusic_ConcertWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.gridLayout = QtWidgets.QGridLayout(ArtistMusic_ConcertWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.list_lbl = QtWidgets.QLabel(ArtistMusic_ConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_lbl.setFont(font)
        self.list_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.list_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.list_lbl.setObjectName("list_lbl")
        self.gridLayout.addWidget(self.list_lbl, 1, 1, 1, 1)
        self.list_listView = QtWidgets.QListView(ArtistMusic_ConcertWindow)
        self.list_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.list_listView.setObjectName("list_listView")
        self.gridLayout.addWidget(self.list_listView, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Back_btn = QtWidgets.QPushButton(ArtistMusic_ConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Back_btn.setObjectName("Back_btn")
        self.gridLayout_2.addWidget(self.Back_btn, 1, 1, 1, 1)
        self.Add_btn = QtWidgets.QPushButton(ArtistMusic_ConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Add_btn.setFont(font)
        self.Add_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Add_btn.setObjectName("Add_btn")
        self.gridLayout_2.addWidget(self.Add_btn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        self.retranslateUi(ArtistMusic_ConcertWindow)
        QtCore.QMetaObject.connectSlotsByName(ArtistMusic_ConcertWindow)

        #$ My Part --------------------------------------------
        self.Back_btn.clicked.connect(self.open_parent_window)

    def retranslateUi(self, ArtistMusic_ConcertWindow):
        _translate = QtCore.QCoreApplication.translate
        ArtistMusic_ConcertWindow.setWindowTitle(_translate("ArtistMusic_ConcertWindow", "List"))
        self.list_lbl.setText(_translate("ArtistMusic_ConcertWindow", "List"))
        self.Back_btn.setText(_translate("ArtistMusic_ConcertWindow", "Back"))
        self.Add_btn.setText(_translate("ArtistMusic_ConcertWindow", "Add"))

    def open_parent_window(self):
        self.parent.show()
        self.ArtistMusic_ConcertWindow.close()
