from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from AddMusic import Ui_AddMusicWindow
from AddConcert import Ui_AddConcertWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Ui_ArtistMusic_ConcertWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, ArtistMusic_ConcertWindow):
        self.ArtistMusic_ConcertWindow = ArtistMusic_ConcertWindow
        ArtistMusic_ConcertWindow.setObjectName("ArtistMusic_ConcertWindow")
        ArtistMusic_ConcertWindow.resize(559, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ArtistMusic_ConcertWindow.setWindowIcon(icon)
        ArtistMusic_ConcertWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.gridLayout = QtWidgets.QGridLayout(ArtistMusic_ConcertWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.list_lbl = QtWidgets.QLabel(ArtistMusic_ConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_lbl.setFont(font)
        self.list_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.list_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.list_lbl.setObjectName("list_lbl")
        self.gridLayout.addWidget(self.list_lbl, 1, 1, 1, 1)
        self.list_TableView = QtWidgets.QTableView(ArtistMusic_ConcertWindow)
        self.list_TableView.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.list_TableView.setObjectName("list_TableView")
        self.gridLayout.addWidget(self.list_TableView, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Back_btn = QtWidgets.QPushButton(ArtistMusic_ConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Back_btn.setObjectName("Back_btn")
        self.gridLayout_2.addWidget(self.Back_btn, 1, 1, 1, 1)
        self.Add_btn = QtWidgets.QPushButton(ArtistMusic_ConcertWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Add_btn.setFont(font)
        self.Add_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Add_btn.setObjectName("Add_btn")
        self.gridLayout_2.addWidget(self.Add_btn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        self.retranslateUi(ArtistMusic_ConcertWindow)
        QtCore.QMetaObject.connectSlotsByName(ArtistMusic_ConcertWindow)

        #$ My Part --------------------------------------------
        if self.appstate["music_or_concert"] == "music":
            dbm = DBM()
            dbm.db_connect()
            artist_musics = get_artist_musics(dbm, self.appstate["userid"])
            music_model = QtGui.QStandardItemModel()
            if artist_musics == None:
                artist_musics = []
            column_headers = get_column_headers(dbm, "tracks")
            music_model.setHorizontalHeaderLabels(column_headers)
            for music in artist_musics:
                music_items = [QtGui.QStandardItem(str(attr)) for attr in music]
                music_model.appendRow(music_items)
            self.list_TableView.setModel(music_model)
        elif self.appstate["music_or_concert"] == "concert":
            dbm = DBM()
            dbm.db_connect()
            artist_concerts = get_artist_concerts(dbm, self.appstate["userid"])
            concert_model = QtGui.QStandardItemModel()
            if artist_concerts == None:
                artist_concerts = []
            column_headers = get_column_headers(dbm, "concert")
            concert_model.setHorizontalHeaderLabels(column_headers)
            for concert in artist_concerts:
                concert_items = [QtGui.QStandardItem(str(attr)) for attr in concert]
                concert_model.appendRow(concert_items)
            self.list_TableView.setModel(concert_model)




        self.Back_btn.clicked.connect(self.open_parent_window)
        self.Add_btn.clicked.connect(self.open_add_musicConcert_window)
        if self.appstate["music_or_concert"] == "music":
            self.list_TableView.doubleClicked.connect(self.delete_track)
        elif self.appstate["music_or_concert"] == "concert":
            self.list_TableView.doubleClicked.connect(self.delete_concert)
    def retranslateUi(self, ArtistMusic_ConcertWindow):
        _translate = QtCore.QCoreApplication.translate
        ArtistMusic_ConcertWindow.setWindowTitle(_translate("ArtistMusic_ConcertWindow", "List"))
        self.list_lbl.setText(_translate("ArtistMusic_ConcertWindow", "List"))
        self.Back_btn.setText(_translate("ArtistMusic_ConcertWindow", "Back"))
        self.Add_btn.setText(_translate("ArtistMusic_ConcertWindow", "Add"))

    def open_parent_window(self):
        self.parent.show()
        self.ArtistMusic_ConcertWindow.close()
    def open_add_musicConcert_window(self):
        if self.appstate["music_or_concert"] == "music":
            self.window = QtWidgets.QWidget()
            self.ui = Ui_AddMusicWindow(
            self.ArtistMusic_ConcertWindow,
            self.appstate
            )
            self.ui.setupUi(self.window)
            self.window.show()
            self.ArtistMusic_ConcertWindow.close()
        elif self.appstate["music_or_concert"] == "concert":
            self.window = QtWidgets.QWidget()
            self.ui = Ui_AddConcertWindow(
            self.ArtistMusic_ConcertWindow,
            self.appstate
            )
            self.ui.setupUi(self.window)
            self.window.show()
            self.ArtistMusic_ConcertWindow.close()

    def delete_track(self, index):
        row = index.row()
        track_id = self.list_TableView.model().index(row, 0).data()
        dbm = DBM()
        dbm.db_connect()
        delete_from_tracks(dbm, track_id)
        artist_musics = get_artist_musics(dbm, self.appstate["userid"])
        music_model = QtGui.QStandardItemModel()
        column_headers = get_column_headers(dbm, "tracks")
        music_model.setHorizontalHeaderLabels(column_headers)
        for music in artist_musics:
            music_items = [QtGui.QStandardItem(str(attr)) for attr in music]
            music_model.appendRow(music_items)
        self.list_TableView.setModel(music_model)

    def delete_concert(self, index):
        row = index.row()
        concert_id = self.list_TableView.model().index(row, 0).data()
        dbm = DBM()
        dbm.db_connect()
        delete_from_concerts(dbm, concert_id)
        artist_concerts = get_artist_concerts(dbm, self.appstate["userid"])
        concert_model = QtGui.QStandardItemModel()
        column_headers = get_column_headers(dbm, "concerts")
        concert_model.setHorizontalHeaderLabels(column_headers)
        for concert in artist_concerts:
            concert_items = [QtGui.QStandardItem(str(attr)) for attr in concert]
            concert_model.appendRow(concert_items)
        self.list_TableView.setModel(concert_model)