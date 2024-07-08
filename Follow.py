from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_FollowWindow(object):
    def setupUi(self, FollowWindow):
        FollowWindow.setObjectName("FollowWindow")
        FollowWindow.resize(500, 360)
        FollowWindow.setMinimumSize(QtCore.QSize(500, 360))
        FollowWindow.setMaximumSize(QtCore.QSize(500, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FollowWindow.setWindowIcon(icon)
        FollowWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout = QtWidgets.QVBoxLayout(FollowWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Follow_listView = QtWidgets.QListView(FollowWindow)
        self.Follow_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);")
        self.Follow_listView.setObjectName("Follow_listView")
        self.verticalLayout.addWidget(self.Follow_listView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(FollowWindow)
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

        self.retranslateUi(FollowWindow)
        QtCore.QMetaObject.connectSlotsByName(FollowWindow)

    def retranslateUi(self, FollowWindow):
        _translate = QtCore.QCoreApplication.translate
        FollowWindow.setWindowTitle(_translate("FollowWindow", "Follow"))
        self.back_btn.setText(_translate("FollowWindow", "Back"))
