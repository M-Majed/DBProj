from PyQt5 import QtCore, QtGui, QtWidgets
import resources


class Ui_PeopleWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate
    def setupUi(self, PeopleWindow):
        self.PeopleWindow = PeopleWindow
        PeopleWindow.setObjectName("PeopleWindow")
        PeopleWindow.resize(500, 600)
        PeopleWindow.setMinimumSize(QtCore.QSize(500, 600))
        PeopleWindow.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PeopleWindow.setWindowIcon(icon)
        PeopleWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout = QtWidgets.QVBoxLayout(PeopleWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Sendreq_lineEdit = QtWidgets.QLineEdit(PeopleWindow)
        self.Sendreq_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"")
        self.Sendreq_lineEdit.setObjectName("Sendreq_lineEdit")
        self.horizontalLayout_2.addWidget(self.Sendreq_lineEdit)
        self.Sendreq_btn = QtWidgets.QPushButton(PeopleWindow)
        self.Sendreq_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Sendreq_btn.setObjectName("Sendreq_btn")
        self.horizontalLayout_2.addWidget(self.Sendreq_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.peopleList_label = QtWidgets.QLabel(PeopleWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.peopleList_label.setFont(font)
        self.peopleList_label.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.peopleList_label.setAlignment(QtCore.Qt.AlignCenter)
        self.peopleList_label.setObjectName("peopleList_label")
        self.verticalLayout.addWidget(self.peopleList_label)
        self.People_listView = QtWidgets.QListView(PeopleWindow)
        self.People_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);")
        self.People_listView.setObjectName("People_listView")
        self.verticalLayout.addWidget(self.People_listView)
        self.Report_lbl = QtWidgets.QLabel(PeopleWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Report_lbl.setFont(font)
        self.Report_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Report_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Report_lbl.setObjectName("Report_lbl")
        self.verticalLayout.addWidget(self.Report_lbl)
        self.report_listView = QtWidgets.QListView(PeopleWindow)
        self.report_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);")
        self.report_listView.setObjectName("report_listView")
        self.verticalLayout.addWidget(self.report_listView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(PeopleWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PeopleWindow)
        QtCore.QMetaObject.connectSlotsByName(PeopleWindow)

        self.back_btn.clicked.connect(self.open_parent_window)
    def open_parent_window(self):
        self.parent.show()
        self.PeopleWindow.close()

    def retranslateUi(self, PeopleWindow):
        _translate = QtCore.QCoreApplication.translate
        PeopleWindow.setWindowTitle(_translate("PeopleWindow", "People"))
        self.Sendreq_btn.setText(_translate("PeopleWindow", "Send request"))
        self.peopleList_label.setText(_translate("PeopleWindow", "People List"))
        self.Report_lbl.setText(_translate("PeopleWindow", "Report"))
        self.back_btn.setText(_translate("PeopleWindow", "Back"))
