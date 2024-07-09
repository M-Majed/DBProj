from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import Variable
from dbfunctions import *
from DBManagement import DBM
from time import sleep
from threading import Timer

class Ui_MusicWindow(object):
    def __init__(self, parent=None, appstate=None, music_row=None):  # * for window trans
        self.parent = parent
        self.appstate = appstate
        # RETURN TEMPLATE FOR "Tracks" ==>>> row=['2', 'Track Title', 'Artist Name', 'Album Name', '00:03:30', 'Genre', 'Ages', 'Lyrics', 'Area', '2021-06-01']
        self.music_row = music_row
    def setupUi(self, MusicWindow):
        self.MusicWindow = MusicWindow
        MusicWindow.setObjectName("MusicWindow")
        MusicWindow.resize(500, 400)
        MusicWindow.setMinimumSize(QtCore.QSize(500, 400))
        MusicWindow.setMaximumSize(QtCore.QSize(500, 400))
        MusicWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.gridLayout = QtWidgets.QGridLayout(MusicWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Title_lbl.setFont(font)
        self.Title_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Title_lbl.setObjectName("Title_lbl")
        self.verticalLayout.addWidget(self.Title_lbl)
        self.Artist_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Artist_lbl.setFont(font)
        self.Artist_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Artist_lbl.setObjectName("Artist_lbl")
        self.verticalLayout.addWidget(self.Artist_lbl)
        self.Genre_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Genre_lbl.setFont(font)
        self.Genre_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Genre_lbl.setObjectName("Genre_lbl")
        self.verticalLayout.addWidget(self.Genre_lbl)
        self.Area_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Area_lbl.setFont(font)
        self.Area_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Area_lbl.setObjectName("Area_lbl")
        self.verticalLayout.addWidget(self.Area_lbl)
        self.Age_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Age_lbl.setFont(font)
        self.Age_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Age_lbl.setObjectName("Age_lbl")
        self.verticalLayout.addWidget(self.Age_lbl)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Text_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Text_lbl.setFont(font)
        self.Text_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.Text_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Text_lbl.setObjectName("Text_lbl")
        self.horizontalLayout.addWidget(self.Text_lbl)
        self.Text_browser = QtWidgets.QTextBrowser(MusicWindow)
        self.Text_browser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Text_browser.setDocumentTitle("")
        self.Text_browser.setPlaceholderText("")
        self.Text_browser.setObjectName("Text_browser")
        self.horizontalLayout.addWidget(self.Text_browser)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.like_checkBox = QtWidgets.QCheckBox(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.like_checkBox.setFont(font)
        self.like_checkBox.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.like_checkBox.setObjectName("like_checkBox")
        self.gridLayout.addWidget(self.like_checkBox, 1, 1, 1, 1)
        self.comments_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comments_btn.setFont(font)
        self.comments_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.comments_btn.setObjectName("comments_btn")
        self.gridLayout.addWidget(self.comments_btn, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sendComment_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sendComment_btn.setFont(font)
        self.sendComment_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.sendComment_btn.setObjectName("sendComment_btn")
        self.horizontalLayout_2.addWidget(self.sendComment_btn)
        self.comment_lineEdit = QtWidgets.QLineEdit(MusicWindow)
        self.comment_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"")
        self.comment_lineEdit.setObjectName("comment_lineEdit")
        self.horizontalLayout_2.addWidget(self.comment_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.Return_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Return_btn.setFont(font)
        self.Return_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Return_btn.setObjectName("Return_btn")
        self.gridLayout.addWidget(self.Return_btn, 4, 0, 1, 1)
        self.Playlist_comboBox = QtWidgets.QComboBox(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Playlist_comboBox.setFont(font)
        self.Playlist_comboBox.setObjectName("Playlist_comboBox")
        self.Playlist_comboBox.addItem("")
        self.gridLayout.addWidget(self.Playlist_comboBox, 4, 2, 1, 1)

        self.retranslateUi(MusicWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicWindow)
        self.sendComment_btn.clicked.connect(self.send_comment)
        self.Return_btn.clicked.connect(self.open_parent_window)
        
        if self.appstate is not None and self.appstate["subscribed"] is not None:
                self.like_checkBox.setCheckable(self.appstate["subscribed"])
        else:
                self.like_checkBox.setCheckable(False)
        self.like_checkBox.stateChanged.connect(self.like_changed)
        # get current like state for userid and trackid
        dbm = DBM()
        dbm.db_connect()
        print(f'--->>>>> {self.appstate=}\n\t{self.music_row=}')
        already_liked = get_like_for_track(dbm, self.appstate["userid"], self.music_row[0])
        if already_liked:
            self.like_checkBox.setChecked(True)
        else:
            self.like_checkBox.setChecked(False)
        dbm.db_disconnect()
        
    def open_parent_window(self):
        self.parent.show()
        self.MusicWindow.close()
    def like_changed(self):
        dbm = DBM()
        dbm.db_connect()
        if self.like_checkBox.isChecked():
                set_like_for_track(dbm, self.appstate["userid"], self.music_row[0])
        else:
                clear_like_for_track(dbm, self.appstate["userid"], self.music_row[0])
        dbm.db_disconnect()
    def get_all_comments(self):
        dbm = DBM()
        dbm.db_connect()
        friendIds = get_friendIds(dbm, self.appstate["userid"])
        if not friendIds:
                friendIds = []
        result = get_comments(dbm, self.music_row[0], friendIds, self.music_row[0])
        if not result:
            return
        # Later: add ui for comments. first comment is result[0]. and its first columns is result[0][0]. ...

        dbm.db_disconnect()
    def send_comment(self):
        comment = self.comment_lineEdit.text()
        if not self.appstate["subscribed"] or comment or comment == "":
            return
        dbm = DBM()
        dbm.db_connect()
        post_comment(dbm, self.appstate["userid"], self.music_row[0], comment)
        dbm.db_disconnect()
        self.comment_lineEdit.setText("SENT!")
        sleep(1)
        self.comment_lineEdit.setText("")
        # Change bg color of send btn to mild green
        self.sendComment_btn.setStyleSheet("background-color: rgb(144, 238, 144);")
        t = Timer(1.0, self.clear_sendComment_btn_Background)
        t.start()
    def clear_sendComment_btn_Background(self):
        # Change bg color to original color
        self.sendComment_btn.setStyleSheet("color: rgb(255, 255, 255);\n")
    def retranslateUi(self, MusicWindow):
        dbm = DBM()
        dbm.db_connect()
        # check_attribute(dbm)
        # RETURN TEMPLATE FOR "Tracks" ==>>> row=['2', 'Track Title', 'Artist Name', 'Album Name', '00:03:30', 'Genre', 'Ages', 'Lyrics', 'Area', '2021-06-01']
        _translate = QtCore.QCoreApplication.translate
        MusicWindow.setWindowTitle(_translate("MusicWindow", "Form"))
        self.Title_lbl.setText(_translate("MusicWindow", f"Title: {self.music_row[1]}"))
        self.Artist_lbl.setText(_translate("MusicWindow", f"Artist: {self.music_row[2]}"))
        self.Genre_lbl.setText(_translate("MusicWindow", f"Genre: {self.music_row[5]}"))
        self.Area_lbl.setText(_translate("MusicWindow", f"Area: {self.music_row[8]}"))
        self.Age_lbl.setText(_translate("MusicWindow", f"Age: {self.music_row[6]}"))
        # self.Text_lbl.setText(_translate("MusicWindow", f"Lyrics: {self.music_row[7]}"))
        self.Text_lbl.setText(_translate("MusicWindow", f"Lyrics"))
        self.Text_browser.setText(self.music_row[7])
        self.like_checkBox.setText(_translate("MusicWindow", f"Like"))
        self.comments_btn.setText(_translate("MusicWindow", f"Comments")) # Later
        self.sendComment_btn.setText(_translate("MusicWindow", f"Comment"))
        self.Return_btn.setText(_translate("MusicWindow", f"Return"))
        self.Playlist_comboBox.setItemText(0, _translate("MusicWindow", f"Add to Playlist")) # Later
