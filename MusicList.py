from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from dbfunctions import *
from DBManagement import DBM
from DBManagement import *
class Ui_MusicList(object):
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
        self.Logout_btn = QtWidgets.QPushButton(MusicListWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Logout_btn.setFont(font)
        self.Logout_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Logout_btn.setObjectName("Logout_btn")
        self.verticalLayout.addWidget(self.Logout_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
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

        self.Logout_btn.clicked.connect(self.open_parent_window)
    def open_parent_window(self):
        self.parent.show()
        self.MusicListWindow.close()

    def retranslateUi(self, MusicListWindow):
        _translate = QtCore.QCoreApplication.translate
        MusicListWindow.setWindowTitle(_translate("MusicListWindow", "MusicListWindow"))
        self.Account_btn.setText(_translate("MusicListWindow", "Account"))
        self.Logout_btn.setText(_translate("MusicListWindow", "Logout"))
        self.Category_combobox.setCurrentText(_translate("MusicListWindow", "Musics"))
        self.Category_combobox.setItemText(0, _translate("MusicListWindow", "Musics"))
        self.Category_combobox.setItemText(1, _translate("MusicListWindow", "Albums"))
        self.Category_combobox.setItemText(2, _translate("MusicListWindow", "Followings"))
        self.Category_combobox.setItemText(3, _translate("MusicListWindow", "Suggestions"))
        self.Category_combobox.setItemText(4, _translate("MusicListWindow", "PlayLists"))
        self.Category_combobox.setItemText(5, _translate("MusicListWindow", "Artists"))
        self.Category_combobox.setItemText(6, _translate("MusicListWindow", "Concerts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusicListWindow = QtWidgets.QWidget()
    ui = Ui_MusicList()
    ui.setupUi(MusicListWindow)
    MusicListWindow.show()
    sys.exit(app.exec_())

   