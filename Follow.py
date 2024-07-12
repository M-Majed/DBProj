from PyQt5 import QtCore, QtGui, QtWidgets
from DBManagement import DBM
from dbfunctions import *
import resources


class Ui_FollowWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, FollowWindow):
        self.FollowWindow = FollowWindow
        FollowWindow.setObjectName("FollowWindow")
        FollowWindow.resize(500, 600)
        FollowWindow.setMinimumSize(QtCore.QSize(500, 600))
        FollowWindow.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FollowWindow.setWindowIcon(icon)
        FollowWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout = QtWidgets.QVBoxLayout(FollowWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Sendreq_lineEdit = QtWidgets.QLineEdit(FollowWindow)
        self.Sendreq_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""")
        self.Sendreq_lineEdit.setObjectName("Sendreq_lineEdit")
        self.horizontalLayout_2.addWidget(self.Sendreq_lineEdit)
        self.Sendreq_btn = QtWidgets.QPushButton(FollowWindow)
        self.Sendreq_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Sendreq_btn.setObjectName("Sendreq_btn")
        self.horizontalLayout_2.addWidget(self.Sendreq_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Following_label = QtWidgets.QLabel(FollowWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Following_label.setFont(font)
        self.Following_label.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Following_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Following_label.setObjectName("Following_label")
        self.verticalLayout.addWidget(self.Following_label)
        self.Following_listView = QtWidgets.QListView(FollowWindow)
        self.Following_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);")
        self.Following_listView.setObjectName("Following_listView")
        self.verticalLayout.addWidget(self.Following_listView)
        self.Follower_lbl = QtWidgets.QLabel(FollowWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Follower_lbl.setFont(font)
        self.Follower_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Follower_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Follower_lbl.setObjectName("Follower_lbl")
        self.verticalLayout.addWidget(self.Follower_lbl)
        self.Follower_listView = QtWidgets.QListView(FollowWindow)
        self.Follower_listView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);")
        self.Follower_listView.setObjectName("Follower_listView")
        self.verticalLayout.addWidget(self.Follower_listView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(FollowWindow)
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
        self.retranslateUi(FollowWindow)
        QtCore.QMetaObject.connectSlotsByName(FollowWindow)

        #$ My Part --------------------------------------------
        dbm = DBM()
        dbm.db_connect()
        followers = get_followers(dbm, self.appstate["userid"]) 
        model = QtGui.QStandardItemModel()
        for follower in followers:
            item = QtGui.QStandardItem(follower)
            model.appendRow(item)
        self.Follower_listView.setModel(model)

        followings = get_followings(dbm, self.appstate["userid"])
        model = QtGui.QStandardItemModel()
        for following in followings:
            item = QtGui.QStandardItem(following)
            model.appendRow(item)
        self.Following_listView.setModel(model)

        
        #$ My Part --------------------------------------------
        self.Sendreq_btn.clicked.connect(lambda: add_follower(dbm, get_userid_by_username(dbm, self.Sendreq_lineEdit.text()), self.appstate["userid"]))
        self.back_btn.clicked.connect(self.open_parent_window)
        self.Follower_listView.doubleClicked.connect(self.remove_follower)
        self.Following_listView.doubleClicked.connect(self.remove_following)
    
    def retranslateUi(self, FollowWindow):
        _translate = QtCore.QCoreApplication.translate
        FollowWindow.setWindowTitle(_translate("FollowWindow", "Follow"))
        self.Sendreq_btn.setText(_translate("FollowWindow", "Send request"))
        self.Following_label.setText(_translate("FollowWindow", "Following"))
        self.Follower_lbl.setText(_translate("FollowWindow", "Followers"))
        self.back_btn.setText(_translate("FollowWindow", "Back"))
        
    def open_parent_window(self):
        self.parent.show()
        self.FollowWindow.close()

    def remove_follower(self, index):
        model = self.Follower_listView.model()
        item = model.itemFromIndex(index)
        follower = item.text()
        dbm = DBM()
        dbm.db_connect()
        remove_follower_fromTable(dbm, self.appstate["userid"], get_userid_by_username(dbm, follower))
        model.removeRow(index.row())

    def remove_following(self, index):
        model = self.Following_listView.model()
        item = model.itemFromIndex(index)
        following = item.text()
        dbm = DBM()
        dbm.db_connect()
        remove_following_fromTable(dbm, self.appstate["userid"], get_userid_by_username(dbm, following))
        model.removeRow(index.row())
