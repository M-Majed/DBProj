from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import Variable
from dbfunctions import *
from DBManagement import DBM

class Ui_MusicWindow(object):
    def __init__(self, parent=None, appstate=None):  # * for window trans
        self.parent = parent
        self.appstate = appstate

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

        self.Return_btn.clicked.connect(self.open_parent_window)
    def open_parent_window(self):
        self.parent.show()
        self.MusicWindow.close()

    def retranslateUi(self, MusicWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicWindow.setWindowTitle(_translate("MusicWindow", "Form"))
        self.Title_lbl.setText(_translate("MusicWindow", "Title:xxxx"))
        self.Title_lbl.setText(_translate("MusicWindow", "Title:zzzz")) 
        self.Artist_lbl.setText(_translate("MusicWindow", "Artist:{MusicList.row[2]}"))
        # self.Artist_lbl.setText(_translate("MusicWindow", "Artist:ssssss"))
        self.Genre_lbl.setText(_translate("MusicWindow", "Genre:xxxx"))
        self.Area_lbl.setText(_translate("MusicWindow", "Area:xxxx"))
        self.Age_lbl.setText(_translate("MusicWindow", "Age:xxxxx"))
        self.Text_lbl.setText(_translate("MusicWindow", "Text:"))
        self.like_checkBox.setText(_translate("MusicWindow", "Like"))
        self.comments_btn.setText(_translate("MusicWindow", "Comments"))
        self.sendComment_btn.setText(_translate("MusicWindow", "Comment"))
        self.Return_btn.setText(_translate("MusicWindow", "Return"))
        self.Playlist_comboBox.setItemText(0, _translate("MusicWindow", "Add to Playlist"))
