from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_CommentsWindow(object):
    def setupUi(self, CommentsWindow):
        CommentsWindow.setObjectName("CommentsWindow")
        CommentsWindow.resize(500, 400)
        CommentsWindow.setMinimumSize(QtCore.QSize(500, 400))
        CommentsWindow.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CommentsWindow.setWindowIcon(icon)
        CommentsWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout = QtWidgets.QVBoxLayout(CommentsWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Comments_label = QtWidgets.QLabel(CommentsWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Comments_label.setFont(font)
        self.Comments_label.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Comments_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Comments_label.setObjectName("Comments_label")
        self.verticalLayout.addWidget(self.Comments_label)
        self.Comments_listView = QtWidgets.QListView(CommentsWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Comments_listView.setFont(font)
        self.Comments_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);")
        self.Comments_listView.setObjectName("Comments_listView")
        self.verticalLayout.addWidget(self.Comments_listView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(CommentsWindow)
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

        self.retranslateUi(CommentsWindow)
        QtCore.QMetaObject.connectSlotsByName(CommentsWindow)

    def retranslateUi(self, CommentsWindow):
        _translate = QtCore.QCoreApplication.translate
        CommentsWindow.setWindowTitle(_translate("CommentsWindow", "Comments"))
        self.Comments_label.setText(_translate("CommentsWindow", "Comments"))
        self.back_btn.setText(_translate("CommentsWindow", "Back"))
