from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from time import sleep
from threading import Timer
from Comments import Ui_CommentsWindow

class Ui_MusicWindow(object):
    def __init__(self, parent=None, appstate=None, music_row=None):  # * for window trans
        self.parent = parent
        self.appstate = appstate
        self.music_row = music_row
        print(f"asdasdasdasdasdasdasdasd{music_row}")
    def setupUi(self, MusicWindow):
        self.MusicWindow = MusicWindow
        MusicWindow.setObjectName("MusicWindow")
        MusicWindow.resize(500, 400)
        MusicWindow.setMinimumSize(QtCore.QSize(500, 400))
        MusicWindow.setMaximumSize(QtCore.QSize(500, 400))
        MusicWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.gridLayout = QtWidgets.QGridLayout(MusicWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.Return_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Return_btn.setFont(font)
        self.Return_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Return_btn.setObjectName("Return_btn")
        self.gridLayout.addWidget(self.Return_btn, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sendComment_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sendComment_btn.setFont(font)
        self.sendComment_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.sendComment_btn.setObjectName("sendComment_btn")
        self.horizontalLayout_2.addWidget(self.sendComment_btn)
        self.comment_lineEdit = QtWidgets.QLineEdit(MusicWindow)
        self.comment_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""")
        self.comment_lineEdit.setObjectName("comment_lineEdit")
        self.horizontalLayout_2.addWidget(self.comment_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Title_lbl.setFont(font)
        self.Title_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Title_lbl.setObjectName("Title_lbl")
        self.verticalLayout.addWidget(self.Title_lbl)
        self.Artist_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Artist_lbl.setFont(font)
        self.Artist_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Artist_lbl.setObjectName("Artist_lbl")
        self.verticalLayout.addWidget(self.Artist_lbl)
        self.Genre_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Genre_lbl.setFont(font)
        self.Genre_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Genre_lbl.setObjectName("Genre_lbl")
        self.verticalLayout.addWidget(self.Genre_lbl)
        self.Area_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Area_lbl.setFont(font)
        self.Area_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Area_lbl.setObjectName("Area_lbl")
        self.verticalLayout.addWidget(self.Area_lbl)
        self.Age_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Age_lbl.setFont(font)
        self.Age_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Age_lbl.setObjectName("Age_lbl")
        self.verticalLayout.addWidget(self.Age_lbl)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.like_checkBox = QtWidgets.QCheckBox(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.like_checkBox.setFont(font)
        self.like_checkBox.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.like_checkBox.setObjectName("like_checkBox")
        self.gridLayout.addWidget(self.like_checkBox, 1, 1, 1, 1)
        self.comments_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comments_btn.setFont(font)
        self.comments_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.comments_btn.setObjectName("comments_btn")
        self.gridLayout.addWidget(self.comments_btn, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Text_lbl = QtWidgets.QLabel(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Text_lbl.setFont(font)
        self.Text_lbl.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""color: rgb(255, 255, 255);")
        self.Text_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Text_lbl.setObjectName("Text_lbl")
        self.horizontalLayout.addWidget(self.Text_lbl)
        self.Text_browser = QtWidgets.QTextBrowser(MusicWindow)
        self.Text_browser.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.Text_browser.setDocumentTitle("")
        self.Text_browser.setPlaceholderText("")
        self.Text_browser.setObjectName("Text_browser")
        self.horizontalLayout.addWidget(self.Text_browser)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.addToPlaylist_btn = QtWidgets.QPushButton(MusicWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addToPlaylist_btn.setFont(font)
        self.addToPlaylist_btn.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 0);")
        self.addToPlaylist_btn.setObjectName("addToPlaylist_btn")
        self.gridLayout.addWidget(self.addToPlaylist_btn, 4, 2, 1, 1)
        self.playlist_lineEdit = QtWidgets.QLineEdit(MusicWindow)
        self.playlist_lineEdit.setMaximumSize(QtCore.QSize(200, 22))
        self.playlist_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n""")
        self.playlist_lineEdit.setObjectName("playlist_lineEdit")
        self.gridLayout.addWidget(self.playlist_lineEdit, 4, 1, 1, 1)
        self.retranslateUi(MusicWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicWindow)

        #$ My Part --------------------------------------------

        self.Return_btn.clicked.connect(self.open_parent_window)
        self.comments_btn.clicked.connect(self.open_comments_window)
        self.sendComment_btn.clicked.connect(self.send_comment_handler)
        self.like_checkBox.stateChanged.connect(self.like_change_handler)
        self.addToPlaylist_btn.clicked.connect(self.add_to_playlist)
        self.init_like_state()
        self.like_checkable_handler()

    def retranslateUi(self, MusicWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicWindow.setWindowTitle(_translate("MusicWindow", "Form"))
        self.Text_lbl.setText(_translate("MusicWindow", f"Lyrics"))
        self.Text_browser.setText(self.music_row[5])
        self.like_checkBox.setText(_translate("MusicWindow", f"Like"))
        self.comments_btn.setText(_translate("MusicWindow", f"Comments"))
        self.sendComment_btn.setText(_translate("MusicWindow", f"Comment"))
        self.Return_btn.setText(_translate("MusicWindow", f"Return"))
        self.addToPlaylist_btn.setText(_translate("MusicWindow", "Add to playlist"))
        self.playlist_lineEdit.setPlaceholderText(_translate("MusicWindow", "enter playlist name"))
        dbm=DBM()
        dbm.db_connect()
        #$ My Part --------------------------------------------
        self.Title_lbl.setText(_translate("MusicWindow", f"Title: {self.music_row[1]}"))
        result = get_username_by_userid( dbm, self.music_row[7])
        
        self.Artist_lbl.setText(_translate("MusicWindow", f"Artist: {result}"))
        self.Genre_lbl.setText(_translate("MusicWindow", f"Genre: {self.music_row[3]}"))
        self.Area_lbl.setText(_translate("MusicWindow", f"Area: {self.music_row[6]}"))
        self.Age_lbl.setText(_translate("MusicWindow", f"Age: {self.music_row[4]}"))

    def open_parent_window(self):
        self.parent.show()
        self.MusicWindow.close()
    def open_comments_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_CommentsWindow(self.MusicWindow,self.appstate,self.music_row)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MusicWindow.close()

    def send_comment_handler(self):
        comment = self.comment_lineEdit.text()
        if not self.appstate["subscribed"] or comment == "":
            return
        dbm = DBM()
        dbm.db_connect()
        post_comment(dbm, self.appstate["userid"], self.music_row[0], comment)
        dbm.db_disconnect()
        self.comment_lineEdit.setText("")

    def like_checkable_handler(self):
        # print(f'00000000000000000000000in "like_checkable_handler"\t {self.appstate["subscribed"]=}')
        if self.appstate["subscribed"] == True:
                self.like_checkBox.setCheckable(True)
        else:
                self.like_checkBox.setCheckable(False)

    def init_like_state(self):
        dbm = DBM()
        dbm.db_connect()
        # print(f'--->>>>> {self.appstate=}\n\t{self.music_row=}')
        already_liked = get_like_for_track(dbm, self.appstate["userid"], self.music_row[0])
        if already_liked:
            self.like_checkBox.setChecked(True)
        else:
            self.like_checkBox.setChecked(False)
        dbm.db_disconnect()
        
    def like_change_handler(self):
        dbm = DBM()
        dbm.db_connect()
        if self.like_checkBox.isChecked():
                set_like_for_track(dbm, self.appstate["userid"], self.music_row[0])
        else:
                clear_like_for_track(dbm, self.appstate["userid"], self.music_row[0])
        dbm.db_disconnect()

    def add_to_playlist(self):
        dbm = DBM()
        dbm.db_connect()
        track_id = self.music_row[0]
        add_to_playlist_table(dbm, self.playlist_lineEdit.text(), track_id, self.appstate["userid"])