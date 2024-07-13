from PyQt5 import QtCore, QtGui, QtWidgets
from dbfunctions import *
from DBManagement import DBM

class Ui_AlbumWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate
    def setupUi(self, AlbumWindow):
        self.AlbumWindow = AlbumWindow
        AlbumWindow.setObjectName("AlbumWindow")
        AlbumWindow.resize(600, 600)
        AlbumWindow.setMinimumSize(QtCore.QSize(600, 600))
        AlbumWindow.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AlbumWindow.setWindowIcon(icon)
        AlbumWindow.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(AlbumWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(AlbumWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.back_btn = QtWidgets.QPushButton(AlbumWindow)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 2, 0, 1, 1)
        self.Myalbums_view = QtWidgets.QListView(AlbumWindow)
        self.Myalbums_view.setObjectName("Myalbums_view")
        self.gridLayout.addWidget(self.Myalbums_view, 1, 0, 1, 2)
        self.like_btn = QtWidgets.QPushButton(AlbumWindow)
        self.like_btn.setObjectName("like_btn")
        self.gridLayout.addWidget(self.like_btn, 2, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.allalbums_view = QtWidgets.QListView(AlbumWindow)
        self.allalbums_view.setObjectName("allalbums_view")
        self.gridLayout_2.addWidget(self.allalbums_view, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 2, 1, 1)
        self.Myalbums_lbl = QtWidgets.QLabel(AlbumWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Myalbums_lbl.setFont(font)
        self.Myalbums_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Myalbums_lbl.setObjectName("Myalbums_lbl")
        self.gridLayout.addWidget(self.Myalbums_lbl, 0, 0, 1, 1)
        self.retranslateUi(AlbumWindow)
        QtCore.QMetaObject.connectSlotsByName(AlbumWindow)
        #$ My Part --------------------------------------------
        dbm=DBM()
        dbm.db_connect()
        playlist_names = get_user_albums(dbm, self.appstate["userid"])
        playlist_list = QtCore.QStringListModel()
        playlist_list.setStringList([str(id[0]) for id in playlist_names])
        self.Myalbums_view.setModel(playlist_list)

        allplaylist_names = get_albums(dbm)
        allplaylist_list = QtCore.QStringListModel()
        allplaylist_list.setStringList([str(id[1]) for id in allplaylist_names])
        self.allalbums_view.setModel(allplaylist_list)


        self.back_btn.clicked.connect(self.open_parent_window)
        self.like_btn.clicked.connect(self.like_album)


    def retranslateUi(self, AlbumWindow):
        _translate = QtCore.QCoreApplication.translate
        AlbumWindow.setWindowTitle(_translate("AlbumWindow", "Albums"))
        self.label_2.setText(_translate("AlbumWindow", "All Albums"))
        self.back_btn.setText(_translate("AlbumWindow", "return"))
        self.like_btn.setText(_translate("AlbumWindow", "Like"))
        self.Myalbums_lbl.setText(_translate("AlbumWindow", "My Albums"))

    def open_parent_window(self):
        self.parent.show()
        self.AlbumWindow.close()

    def like_album(self):
        dbm = DBM()
        dbm.db_connect()
        album_name = self.allalbums_view.currentIndex().data()
        albumid=get_albumid_by_name(dbm, album_name)
        like_albumTable(dbm, self.appstate["userid"], albumid)