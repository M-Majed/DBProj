from PyQt5 import QtCore, QtGui, QtWidgets
from dbfunctions import *
from DBManagement import DBM


class Ui_PlayListsWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, PlayListsWindow):
        self.PlayListsWindow = PlayListsWindow
        PlayListsWindow.setObjectName("PlayListsWindow")
        PlayListsWindow.resize(500, 600)
        PlayListsWindow.setMinimumSize(QtCore.QSize(500, 600))
        PlayListsWindow.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlayListsWindow.setWindowIcon(icon)
        PlayListsWindow.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(PlayListsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.public_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.public_btn.setObjectName("public_btn")
        self.gridLayout.addWidget(self.public_btn, 1, 0, 1, 1)
        self.listView = QtWidgets.QListView(PlayListsWindow)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 2)
        self.private_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.private_btn.setObjectName("private_btn")
        self.gridLayout.addWidget(self.private_btn, 1, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 2, 0, 1, 1)
        self.retranslateUi(PlayListsWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayListsWindow)

        #$ My Part --------------------------------------------
        dbm=DBM()
        dbm.db_connect()
        playlist_names = get_user_playlists(dbm, self.appstate["userid"])
        playlist_list = QtCore.QStringListModel()
        playlist_list.setStringList([str(id) for id in playlist_names])
        self.listView.setModel(playlist_list)

        self.back_btn.clicked.connect(self.open_parent_window)



    def retranslateUi(self, PlayListsWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayListsWindow.setWindowTitle(_translate("PlayListsWindow", "PlayLists"))
        self.public_btn.setText(_translate("PlayListsWindow", "public"))
        self.private_btn.setText(_translate("PlayListsWindow", "private"))
        self.back_btn.setText(_translate("PlayListsWindow", "return"))

    def open_parent_window(self):
        self.parent.show()
        self.PlayListsWindow.close()