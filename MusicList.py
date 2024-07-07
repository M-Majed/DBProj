import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import resources




class Ui_MusicListWindow(object):
    def __init__(self, parent=None):  # * for window trans
        self.parent = parent
    def setupUi(self, MusicListWindow):
        self.MusicListWindow = MusicListWindow # * Save the MusicListWindow object
        MusicListWindow.setObjectName("MusicListWindow")
        MusicListWindow.resize(800, 600)
        MusicListWindow.setMinimumSize(QtCore.QSize(800, 600))
        MusicListWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MusicListWindow.setWindowIcon(icon)
        MusicListWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);\n"
"color: rgb(255, 255, 255);")
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
        self.Account_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Account_btn.setObjectName("Account_btn")
        self.verticalLayout.addWidget(self.Account_btn)
        self.Back_btn = QtWidgets.QPushButton(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
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
        self.Search_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
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


        #* get data from database and show it in table ***************
        self.model = QtGui.QStandardItemModel()
        self.Music_list = QtWidgets.QTableView(MusicListWindow)
        self.Music_list.setModel(self.model)
        connection = sqlite3.connect('my.db')
        cursor = connection.cursor()
        cursor.execute("PRAGMA table_info(user)")
        columns_info = cursor.fetchall()
        column_names = [info[1] for info in columns_info]
        self.model.setColumnCount(len(column_names))
        self.model.setHorizontalHeaderLabels(column_names)
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        for row in rows:
            items = [QtGui.QStandardItem(str(field)) for field in row]
            self.model.appendRow(items)
        connection.close()




        font = QtGui.QFont()
        font.setPointSize(10)
        self.Music_list.setFont(font)
        self.Music_list.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Music_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Music_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Music_list.setDragDropOverwriteMode(False)
        self.Music_list.setObjectName("Music_list")
        self.horizontalLayout_3.addWidget(self.Music_list)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(MusicListWindow)
        QtCore.QMetaObject.connectSlotsByName(MusicListWindow)

        self.Back_btn.clicked.connect(self.open_parent_window) # * Connect the back button to the open_parent_window method
 
        
    def open_parent_window(self): # * Method to open the parent window
        self.parent.show()
        self.MusicListWindow.close()



    def retranslateUi(self, MusicListWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicListWindow.setWindowTitle(_translate("MusicListWindow", "MusicList"))
        self.Account_btn.setText(_translate("MusicListWindow", "Account"))
        self.Back_btn.setText(_translate("MusicListWindow", "Back"))
        self.Search_btn.setText(_translate("MusicListWindow", "Search"))
        self.Category_combobox.setCurrentText(_translate("MusicListWindow", "Musics"))
        self.Category_combobox.setItemText(0, _translate("MusicListWindow", "Musics"))
        self.Category_combobox.setItemText(1, _translate("MusicListWindow", "Albums"))
        self.Category_combobox.setItemText(2, _translate("MusicListWindow", "Followings"))
        self.Category_combobox.setItemText(3, _translate("MusicListWindow", "Suggestions"))
        self.Category_combobox.setItemText(4, _translate("MusicListWindow", "PlayLists"))
        self.Category_combobox.setItemText(5, _translate("MusicListWindow", "Artists"))
        self.Category_combobox.setItemText(6, _translate("MusicListWindow", "Concerts"))