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
        PlayListsWindow.resize(600, 600)
        PlayListsWindow.setMinimumSize(QtCore.QSize(600, 600))
        PlayListsWindow.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlayListsWindow.setWindowIcon(icon)
        PlayListsWindow.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(PlayListsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.back_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 2, 0, 1, 1)
        self.listView = QtWidgets.QListView(PlayListsWindow)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 2)
        self.public_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.public_btn.setObjectName("public_btn")
        self.gridLayout.addWidget(self.public_btn, 1, 0, 1, 1)
        self.private_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.private_btn.setObjectName("private_btn")
        self.gridLayout.addWidget(self.private_btn, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.AllPlaylists_listView = QtWidgets.QListView(PlayListsWindow)
        self.AllPlaylists_listView.setObjectName("AllPlaylists_listView")
        self.gridLayout_2.addWidget(self.AllPlaylists_listView, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.like_btn = QtWidgets.QPushButton(PlayListsWindow)
        self.like_btn.setObjectName("like_btn")
        self.gridLayout.addWidget(self.like_btn, 1, 2, 1, 1)
        self.retranslateUi(PlayListsWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayListsWindow)

        #$ My Part --------------------------------------------
        dbm=DBM()
        dbm.db_connect()
        playlist_names = get_user_playlists(dbm, self.appstate["userid"])
        playlist_list = QtCore.QStringListModel()
        playlist_list.setStringList([str(id[0]) for id in playlist_names])
        self.listView.setModel(playlist_list)

        allplaylist_names = get_playlists(dbm)
        allplaylist_list = QtCore.QStringListModel()
        allplaylist_list.setStringList([str(id[1]) for id in allplaylist_names])
        self.AllPlaylists_listView.setModel(allplaylist_list)

        self.back_btn.clicked.connect(self.open_parent_window)
        self.private_btn.clicked.connect(self.convert_to_private)
        self.public_btn.clicked.connect(self.convert_to_public)
        self.like_btn.clicked.connect(self.like_playlist)




    def retranslateUi(self, PlayListsWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayListsWindow.setWindowTitle(_translate("PlayListsWindow", "PlayLists"))
        self.public_btn.setText(_translate("PlayListsWindow", "public"))
        self.private_btn.setText(_translate("PlayListsWindow", "private"))
        self.back_btn.setText(_translate("PlayListsWindow", "return"))
        self.like_btn.setText(_translate("PlayListsWindow", "like"))

    def open_parent_window(self):
        self.parent.show()
        self.PlayListsWindow.close()

    def convert_to_private(self):
        dbm = DBM()
        dbm.db_connect()
        playlist_name = self.listView.currentIndex().data()
        make_playlist_private(dbm, playlist_name)

    def convert_to_public(self):
        dbm = DBM()
        dbm.db_connect()
        playlist_name = self.listView.currentIndex().data()
        make_playlist_public(dbm, playlist_name)

    def like_playlist(self):
        dbm = DBM()
        dbm.db_connect()
        playlist_name = self.AllPlaylists_listView.currentIndex().data()
        playlistid=get_playlistid_by_name(dbm, playlist_name)
        like_playlistTable(dbm, self.appstate["userid"], playlistid)
