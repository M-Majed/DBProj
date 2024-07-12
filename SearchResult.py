import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from datatype import *
from Music import Ui_MusicWindow


class Ui_SearchResultWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, SearchResultWindow):
        self.SearchResultWindow = SearchResultWindow
        SearchResultWindow.setObjectName("SearchResultWindow")
        SearchResultWindow.resize(500, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchResultWindow.setWindowIcon(icon)
        SearchResultWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SearchResultWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Music_tableView = QtWidgets.QTableView(SearchResultWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Music_tableView.setFont(font)
        self.Music_tableView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Music_tableView.setObjectName("Music_tableView")
        self.verticalLayout.addWidget(self.Music_tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back_btn = QtWidgets.QPushButton(SearchResultWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout.addWidget(self.Back_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(SearchResultWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchResultWindow)
        
        
        #$ My Part --------------------------------------------
        dbm = DBM()
        dbm.db_connect()
        if self.appstate["searchOrother"] == "Albums":
            msuics_for_list = get_album_tracks(dbm, self.appstate["AlbumName"])
        elif self.appstate["searchOrother"] == "search":
            msuics_for_list = search_track(dbm, self.appstate["Searchtitle"], self.appstate["Searchartist"], self.appstate["Searchgenre"], self.appstate["Searchage"], self.appstate["SearchArea"])
        elif self.appstate["searchOrother"] == "following":
            msuics_for_list = get_artist_musics(dbm, get_userid_by_username(dbm, self.appstate["followingidshow"]))
        elif self.appstate["searchOrother"] == "playlist":
            msuics_for_list = get_playlist_tracks(dbm, self.appstate["playlistname"])
        elif self.appstate["searchOrother"] == "showaristsong":
            msuics_for_list = get_artist_musics(dbm, self.appstate["Artist_id_to_show"])

        music_model = QtGui.QStandardItemModel()
        if msuics_for_list == None:
            msuics_for_list = []
        column_headers = get_column_headers(dbm, "tracks")
        music_model.setHorizontalHeaderLabels(column_headers)
        for music in msuics_for_list:
            music_items = [QtGui.QStandardItem(str(attr)) for attr in music]
            music_model.appendRow(music_items)
        self.Music_tableView.setModel(music_model)

        self.model = music_model





        self.Back_btn.clicked.connect(self.open_parent_window)
        self.Music_tableView.doubleClicked.connect(self.open_music_window)



    def retranslateUi(self, SearchResultWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchResultWindow.setWindowTitle(_translate("SearchResultWindow", "Search Result"))
        self.Back_btn.setText(_translate("SearchResultWindow", "Return"))

    def open_parent_window(self):
        self.parent.show()
        self.SearchResultWindow.close()

    def open_music_window(self, index):
        row = [self.model.item(index.row(), col).text() for col in range(self.model.columnCount())]
        self.window = QtWidgets.QWidget()
        self.ui = Ui_MusicWindow(self.SearchResultWindow,self.appstate,row)
        self.ui.setupUi(self.window)
        self.window.show()
        self.SearchResultWindow.close()