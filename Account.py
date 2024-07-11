from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from Ticket import Ui_TicketsWindow
from ArtistMusic_Concert import Ui_ArtistMusic_ConcertWindow
from Follow import Ui_FollowWindow
from Friends import Ui_FriendsWindow


class Ui_AccountWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, AccountWindow):
        self.AccountWindow = AccountWindow
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(500, 350)
        AccountWindow.setMinimumSize(QtCore.QSize(500, 350))
        AccountWindow.setMaximumSize(QtCore.QSize(500, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AccountWindow.setWindowIcon(icon)
        AccountWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);\n""")
        self.gridLayout_2 = QtWidgets.QGridLayout(AccountWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.concertList_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.concertList_btn.setFont(font)
        self.concertList_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.concertList_btn.setObjectName("concertList_btn")
        self.gridLayout_2.addWidget(self.concertList_btn, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 1, 1, 1)
        self.MusicList_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MusicList_btn.setFont(font)
        self.MusicList_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.MusicList_btn.setObjectName("MusicList_btn")
        self.gridLayout_2.addWidget(self.MusicList_btn, 7, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.return_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.return_btn.setFont(font)
        self.return_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.return_btn.setObjectName("return_btn")
        self.gridLayout_2.addWidget(self.return_btn, 9, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 4, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.balance_lbl = QtWidgets.QLabel(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.balance_lbl.setFont(font)
        self.balance_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.balance_lbl.setObjectName("balance_lbl")
        self.verticalLayout_2.addWidget(self.balance_lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deposit_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deposit_btn.setFont(font)
        self.deposit_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.deposit_btn.setObjectName("deposit_btn")
        self.horizontalLayout.addWidget(self.deposit_btn)
        self.deposit_lineEdit = QtWidgets.QLineEdit(AccountWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deposit_lineEdit.sizePolicy().hasHeightForWidth())
        self.deposit_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deposit_lineEdit.setFont(font)
        self.deposit_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);")
        self.deposit_lineEdit.setObjectName("deposit_lineEdit")
        self.horizontalLayout.addWidget(self.deposit_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 1)
        self.tickets_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tickets_btn.setFont(font)
        self.tickets_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.tickets_btn.setObjectName("tickets_btn")
        self.gridLayout_2.addWidget(self.tickets_btn, 9, 1, 1, 1)
        self.artist_checkBox = QtWidgets.QCheckBox(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.artist_checkBox.setFont(font)
        self.artist_checkBox.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.artist_checkBox.setObjectName("artist_checkBox")
        self.gridLayout_2.addWidget(self.artist_checkBox, 3, 3, 1, 1)
        self.Friends_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Friends_btn.setFont(font)
        self.Friends_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Friends_btn.setObjectName("Friends_btn")
        self.gridLayout_2.addWidget(self.Friends_btn, 3, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.follow_btn = QtWidgets.QPushButton(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.follow_btn.setFont(font)
        self.follow_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.follow_btn.setObjectName("follow_btn")
        self.gridLayout_2.addWidget(self.follow_btn, 7, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.Subscription_checkBox = QtWidgets.QCheckBox(AccountWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Subscription_checkBox.setFont(font)
        self.Subscription_checkBox.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Subscription_checkBox.setObjectName("Subscription_checkBox")
        self.verticalLayout.addWidget(self.Subscription_checkBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 3, 1, 1)
        self.retranslateUi(AccountWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountWindow)

        #$ My Part --------------------------------------------
        self.changeartist_status()
        self.return_btn.clicked.connect(self.open_parent_window)
        self.follow_btn.clicked.connect(self.open_follow_window)
        self.Friends_btn.clicked.connect(self.open_friends_window)
        self.tickets_btn.clicked.connect(self.open_tickets_window)
        # self.Subscription_checkBox.clicked.connect(self.changeSubscription)
        self.Subscription_checkBox.stateChanged.connect(self.changeSubscription)
        self.deposit_btn.clicked.connect(self.add_balance)
        self.artist_checkBox.clicked.connect(self.changeartist_status)
        self.MusicList_btn.clicked.connect(self.open_musicList_window)
        self.concertList_btn.clicked.connect(self.open_concertList_window)

    def retranslateUi(self, AccountWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountWindow.setWindowTitle(_translate("AccountWindow", "Account"))
        self.concertList_btn.setText(_translate("AccountWindow", "Concert List"))
        self.MusicList_btn.setText(_translate("AccountWindow", "Musics List"))
        self.return_btn.setText(_translate("AccountWindow", "Return"))
        self.deposit_btn.setText(_translate("AccountWindow", "Deposit"))
        self.deposit_lineEdit.setPlaceholderText(_translate("AccountWindow", "Enter desired amount"))
        self.tickets_btn.setText(_translate("AccountWindow", "Tickets"))
        self.artist_checkBox.setText(_translate("AccountWindow", "Artist"))
        self.Friends_btn.setText(_translate("AccountWindow", "Friends"))
        self.follow_btn.setText(_translate("AccountWindow", "follow"))
        self.Subscription_checkBox.setText(_translate("AccountWindow", "subscription"))

        #$ My Part --------------------------------------------
        dbm = DBM()
        dbm.db_connect()
        uid=self.appstate["userid"]
        self.balance_lbl.setText(_translate("AccountWindow", f"balance:{get_one_user(dbm,uid)[0][9]}"))
        if(get_one_user(dbm,uid)[0][7] == 1):
            self.Subscription_checkBox.setChecked(True)
        else:
            self.Subscription_checkBox.setChecked(False)
        if(get_one_user(dbm,uid)[0][8] == 1):
            self.artist_checkBox.setChecked(True)
        else:
            self.artist_checkBox.setChecked(False)

    def open_parent_window(self):
        self.parent.show()
        self.AccountWindow.close()
    def open_follow_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_FollowWindow(
            self.AccountWindow,
            self.appstate
        )
        self.ui.setupUi(self.window)
        self.window.show()
        self.AccountWindow.close()
    def open_friends_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_FriendsWindow(
            self.AccountWindow,
            self.appstate
        )
        self.ui.setupUi(self.window)
        self.window.show()
        self.AccountWindow.close()
    def open_tickets_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_TicketsWindow(
            self.AccountWindow,
            self.appstate
        )
        self.ui.setupUi(self.window)
        self.window.show()
        self.AccountWindow.close()
    def open_musicList_window(self):
        self.appstate["music_or_concert"] = "music"
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ArtistMusic_ConcertWindow(
            self.AccountWindow,
            self.appstate
        )
        self.ui.setupUi(self.window)
        self.window.show()
        self.AccountWindow.close()
    def open_concertList_window(self):
        self.appstate["music_or_concert"] = "concert"
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ArtistMusic_ConcertWindow(
            self.AccountWindow,
            self.appstate
        )
        self.ui.setupUi(self.window)
        self.window.show()
        self.AccountWindow.close()

    def changeSubscription(self):
        dbm = DBM()
        dbm.db_connect()
        uid=self.appstate["userid"]
        if(self.Subscription_checkBox.isChecked()):
            update_user_subscription(dbm, uid, 1)
            self.appstate["subscribed"] = 1
        else:
            update_user_subscription(dbm, uid, 0)
            self.appstate["subscribed"] = 0
        dbm.db_disconnect()

    def add_balance(self):
        dbm = DBM()
        dbm.db_connect()
        uid=self.appstate["userid"]
        balance = get_one_user(dbm, uid)[0][9]
        if balance == None:
            balance = 0
        balance += int(self.deposit_lineEdit.text())
        update_user_balance(dbm, uid, balance)
        self.balance_lbl.setText(f"balance:{get_one_user(dbm, uid)[0][9]}")
        dbm.db_disconnect()

    def changeartist_status(self):
        dbm = DBM()
        dbm.db_connect()
        uid=self.appstate["userid"]
        if(self.artist_checkBox.isChecked()):
            update_user_artist(dbm, uid, 1)
            self.MusicList_btn.show()
            self.concertList_btn.show()
        else:
            update_user_artist(dbm, uid, 0)
            self.MusicList_btn.hide()
            self.concertList_btn.hide()
        dbm.db_disconnect()
