from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_TicketsWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, TicketsWindow):
        self.TicketsWindow = TicketsWindow
        TicketsWindow.setObjectName("TicketsWindow")
        TicketsWindow.resize(500, 600)
        TicketsWindow.setMinimumSize(QtCore.QSize(500, 600))
        TicketsWindow.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TicketsWindow.setWindowIcon(icon)
        TicketsWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout = QtWidgets.QVBoxLayout(TicketsWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TicketsList_label = QtWidgets.QLabel(TicketsWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TicketsList_label.setFont(font)
        self.TicketsList_label.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.TicketsList_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TicketsList_label.setObjectName("TicketsList_label")
        self.verticalLayout.addWidget(self.TicketsList_label)
        self.Tickets_listView = QtWidgets.QListView(TicketsWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tickets_listView.setFont(font)
        self.Tickets_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);")
        self.Tickets_listView.setObjectName("Tickets_listView")
        self.verticalLayout.addWidget(self.Tickets_listView)
        self.Expired_lbl = QtWidgets.QLabel(TicketsWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Expired_lbl.setFont(font)
        self.Expired_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Expired_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Expired_lbl.setObjectName("Expired_lbl")
        self.verticalLayout.addWidget(self.Expired_lbl)
        self.Expired_listView = QtWidgets.QListView(TicketsWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Expired_listView.setFont(font)
        self.Expired_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);")
        self.Expired_listView.setObjectName("Expired_listView")
        self.verticalLayout.addWidget(self.Expired_listView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(TicketsWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.retranslateUi(TicketsWindow)
        QtCore.QMetaObject.connectSlotsByName(TicketsWindow)

        #$ My Part --------------------------------------------
        self.back_btn.clicked.connect(self.open_parent_window)

    def retranslateUi(self, TicketsWindow):
        _translate = QtCore.QCoreApplication.translate
        TicketsWindow.setWindowTitle(_translate("TicketsWindow", "Tickets"))
        self.TicketsList_label.setText(_translate("TicketsWindow", "Tickets list"))
        self.Expired_lbl.setText(_translate("TicketsWindow", "Expired tickets"))
        self.back_btn.setText(_translate("TicketsWindow", "Back"))
        
    def open_parent_window(self):
        self.parent.show()
        self.TicketsWindow.close()


