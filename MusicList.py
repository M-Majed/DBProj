import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from datatype import *
from Music import Ui_MusicWindow
from Account import Ui_AccountWindow
from Search import Ui_SearchWindow

class Ui_MusicListWindow(object):
    def __init__(self, parent=None , appstate=None):
        self.parent = parent
        self.appstate = appstate

    def setupUi(self, MusicListWindow):
        self.MusicListWindow = MusicListWindow
        MusicListWindow.setObjectName("MusicListWindow")
        MusicListWindow.resize(800, 600)
        MusicListWindow.setMinimumSize(QtCore.QSize(800, 600))
        MusicListWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MusicListWindow.setWindowIcon(icon)
        MusicListWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);\n""color: rgb(255, 255, 255);")
        self.gridLayout_4 = QtWidgets.QGridLayout(MusicListWindow)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Account_btn = QtWidgets.QPushButton(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Account_btn.setFont(font)
        self.Account_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Account_btn.setObjectName("Account_btn")
        self.verticalLayout.addWidget(self.Account_btn)
        self.Back_btn = QtWidgets.QPushButton(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Back_btn.setObjectName("Back_btn")
        self.verticalLayout.addWidget(self.Back_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Search_btn = QtWidgets.QPushButton(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Search_btn.setFont(font)
        self.Search_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Search_btn.setObjectName("Search_btn")
        self.verticalLayout.addWidget(self.Search_btn)
        self.Category_combobox = QtWidgets.QComboBox(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Category_combobox.setFont(font)
        self.Category_combobox.setToolTip("")
        self.Category_combobox.setStatusTip("")
        self.Category_combobox.setWhatsThis("")
        self.Category_combobox.setAccessibleName("")
        self.Category_combobox.setAccessibleDescription("")
        self.Category_combobox.setStyleSheet("color: rgb(0, 0, 0);")
        self.Category_combobox.setEditable(False)
        self.Category_combobox.setObjectName("Category_combobox")
        self.Category_combobox.addItem("")
        self.Category_combobox.addItem("")
        self.Category_combobox.addItem("")
        self.Category_combobox.addItem("")
        self.Category_combobox.addItem("")
        self.Category_combobox.addItem("")
        self.Category_combobox.addItem("")
        self.verticalLayout.addWidget(self.Category_combobox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.Music_list = QtWidgets.QTableView(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Music_list.setFont(font)
        self.Music_list.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Music_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Music_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Music_list.setDragDropOverwriteMode(False)
        self.Music_list.setObjectName("Music_list")
        self.horizontalLayout_3.addWidget(self.Music_list)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.retranslateUi(MusicListWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicListWindow)

        #$ My Part --------------------------------------------
        self.model = QtGui.QStandardItemModel()
        self.Music_list.setModel(self.model)
        connection = sqlite3.connect('my.db')
        cursor = connection.cursor()
        cursor.execute("PRAGMA table_info(tracks)") 
        columns_info = cursor.fetchall()
        column_names = [info[1] for info in columns_info]
        print(f'{column_names=}')
        self.model.setColumnCount(len(column_names))
        self.model.setHorizontalHeaderLabels(column_names)
        columns_to_hide = [elem if "id" in elem else None for elem in column_names]
        for elem in columns_to_hide:
            if elem:
                column_index = column_names.index(elem)
                self.Music_list.setColumnHidden(column_index, True)
        self.Category_combobox.currentIndexChanged.connect(self.category_changed)

        self.Back_btn.clicked.connect(self.open_parent_window)
        self.Music_list.doubleClicked.connect(self.item_clicked)
        self.Account_btn.clicked.connect(self.open_account_window)
        self.Search_btn.clicked.connect(self.open_search_window)
        self.category_changed(0)

    def retranslateUi(self, MusicListWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicListWindow.setWindowTitle(_translate("MusicListWindow", "MusicList"))
        self.Account_btn.setText(_translate("MusicListWindow", "Account"))
        self.Back_btn.setText(_translate("MusicListWindow", "Back"))
        self.Search_btn.setText(_translate("MusicListWindow", "Search"))
        self.Category_combobox.setCurrentText(_translate("MusicListWindow", "Tracks"))
        self.Category_combobox.setItemText(0, _translate("MusicListWindow", "Tracks"))
        self.Category_combobox.setItemText(1, _translate("MusicListWindow", "Albums"))
        self.Category_combobox.setItemText(2, _translate("MusicListWindow", "Followings"))
        self.Category_combobox.setItemText(3, _translate("MusicListWindow", "Suggestions"))
        self.Category_combobox.setItemText(4, _translate("MusicListWindow", "PlayLists"))
        self.Category_combobox.setItemText(5, _translate("MusicListWindow", "Artists"))
        self.Category_combobox.setItemText(6, _translate("MusicListWindow", "Concerts"))

    def open_account_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_AccountWindow(self.MusicListWindow, self.appstate)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MusicListWindow.close()
    def open_parent_window(self):
        self.parent.show()
        self.MusicListWindow.close()
    def open_search_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_SearchWindow(self.MusicListWindow, self.appstate)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MusicListWindow.close()

    def item_clicked(self, index):
        cat = self.Category_combobox.currentIndex()
        item = self.model.itemFromIndex(index)
        row = [self.model.item(index.row(), col).text() for col in range(self.model.columnCount())]
        print(f'{row=}')
        if cat == 0: # Category = "Tracks"
            # RETURN TEMPLATE FOR "Tracks" ==>>> row=['2', 'Track Title', 'Artist Name', 'Album Name', '00:03:30', 'Genre', 'Ages', 'Lyrics', 'Area', '2021-06-01']
            self.window = QtWidgets.QWidget()
            self.ui = Ui_MusicWindow(self.MusicListWindow,self.appstate,row)
            self.ui.setupUi(self.window)
            self.window.show()
            self.MusicListWindow.close()
            
        elif cat == 1:  # Category = "Albums"
            album_name = str(row[0])
            dbm = DBM()
            dbm.db_connect()
            tracks = dbm.db_execute_read_query(
                f'''
                SELECT distinct title FROM albums WHERE album = '{album_name}'
                ''', None
            )
            if tracks is None:
                print(f"Error: No tracks found for album '{album_name}'")
            else:
                self.model.clear()
                self.model.setHorizontalHeaderLabels(['album'])
                for track in tracks:
                    track_data = [str(item) for item in track]
                    self.model.appendRow([QtGui.QStandardItem(data) for data in track_data])
                dbm.db_disconnect()
            # self.model.clear()
        elif cat == 2: # Category = "Followings"
            qq = self.appstate.get("userid")
            if qq is None:
                print("Error: User ID not found in appstate.")
                return None
            
            result = dbm.db_execute_read_query(
                f'''
                select username from user
                where id in (SELECT following_id FROM followorfollowing WHERE follower_id = {qq});
                ''',
                None,
            )
            if result is None:
                return None
            return [row[0] for row in result]
        elif cat == 3: # Category = "Suggestions"
            #suggest that genre likes user likes the tracks
            dbm = DBM()
            dbm.db_connect()
            qq=self.appstate["userid"]
            rows = dbm.db_execute_read_query(
                f'''
                SELECT title FROM tracks,likes WHERE user_id = {qq} &&  likes.user_id = tracks.id
                ''', None
            )
            if rows is None:
                print(f"Error: No genre found for user '{qq}'")
            else:
                self.model.setHorizontalHeaderLabels(['genre'])
                for genre in rows:
                    genre_data = [str(item) for item in genre]
                    self.model.appendRow([QtGui.QStandardItem(data) for data in genre_data])
                dbm.db_disconnect()
                
            
            
            pass
        elif cat == 4: # Category = "PlayLists"
            
            pass
        elif cat == 5: # Category = "Artists"
            pass
        elif cat == 6: # Category = "Concerts"
            pass

    def category_changed(self, index):
        self.model.clear()
        print(f'{index=}\t{self.Category_combobox.currentIndex()=}\t{self.Category_combobox.currentText()=}')
        dbm = DBM()
        dbm.db_connect()
        rows = None
        if index == 0: # Tracks
            rows = dbm.db_execute_read_query(
                f'''
                SELECT * FROM tracks
                ''', None
            )
        elif index == 1: # Albums
            rows = dbm.db_execute_read_query(
                f'''
                SELECT album FROM albums
                ''', None
            )
        elif index == 2: # Followings
            qq = self.appstate.get("userid")
            if qq is None:
                print("Error: User ID not found in appstate.")
                dbm.db_disconnect()
                return
            
            rows = dbm.db_execute_read_query(
                f'''
                SELECT username FROM user
                WHERE id IN (SELECT following_id FROM followorfollowing WHERE follower_id = {qq});
                ''', None
            )
        elif index == 3: # Suggestions
            dbm = DBM()
            dbm.db_connect()
            qq = self.appstate["userid"]
            rows = dbm.db_execute_read_query(
                f'''
                with recursive
                mytable(g , c ) as ( 
                    SELECT genre , count(*) as c FROM tracks, likes
                    WHERE likes.user_id = {qq} AND likes.track_id = tracks.id
                    GROUP BY genre
                    HAVING COUNT(*) > 0
                    ORDER BY COUNT(*) DESC
                    LIMIT 2)
                SELECT * FROM tracks
                WHERE 
                genre IN (
                    SELECT genre FROM mytable
                )
                
                ''', None
            )
        elif index == 4: # PlayLists
            rows = dbm.db_execute_read_query(
                f'''
                SELECT * FROM playlists
                ''', None
            )
        elif index == 5: # Artists
            rows = dbm.db_execute_read_query(
                f'''
                SELECT username FROM user where singerornormal
                ''', None
            )
        elif index == 6: # Concerts
            rows = dbm.db_execute_read_query(
                f'''
                SELECT * FROM concert
                ''', None
            ) 
        if rows:  
            for row in rows:
                items = [QtGui.QStandardItem(str(field)) for field in row]
                for elem in items:
                    elem.setEditable(False)
                
                                                
                self.model.appendRow(items)
        else:
            print(f'No row fetched.')
        dbm.db_disconnect()