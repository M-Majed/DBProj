from PyQt5 import QtCore, QtGui, QtWidgets
import resources



class Ui_AddMusicWindow(object):
    def setupUi(self, AddMusicWindow):
        AddMusicWindow.setObjectName("AddMusicWindow")
        AddMusicWindow.resize(400, 400)
        AddMusicWindow.setMinimumSize(QtCore.QSize(400, 400))
        AddMusicWindow.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddMusicWindow.setWindowIcon(icon)
        AddMusicWindow.setStyleSheet("background-image: url(:/Background/background/darkgreen.png);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddMusicWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title_lineEdit = QtWidgets.QLineEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Title_lineEdit.setFont(font)
        self.Title_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Title_lineEdit.setObjectName("Title_lineEdit")
        self.verticalLayout.addWidget(self.Title_lineEdit)
        self.Album_lineEdit = QtWidgets.QLineEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Album_lineEdit.setFont(font)
        self.Album_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Album_lineEdit.setObjectName("Album_lineEdit")
        self.verticalLayout.addWidget(self.Album_lineEdit)
        self.Duration_lineEdit = QtWidgets.QLineEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Duration_lineEdit.setFont(font)
        self.Duration_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Duration_lineEdit.setObjectName("Duration_lineEdit")
        self.verticalLayout.addWidget(self.Duration_lineEdit)
        self.Age_lineEdit = QtWidgets.QLineEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Age_lineEdit.setFont(font)
        self.Age_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Age_lineEdit.setObjectName("Age_lineEdit")
        self.verticalLayout.addWidget(self.Age_lineEdit)
        self.Genre_lineEdit = QtWidgets.QLineEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Genre_lineEdit.setFont(font)
        self.Genre_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Genre_lineEdit.setObjectName("Genre_lineEdit")
        self.verticalLayout.addWidget(self.Genre_lineEdit)
        self.Area_lineEdit = QtWidgets.QLineEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Area_lineEdit.setFont(font)
        self.Area_lineEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Area_lineEdit.setObjectName("Area_lineEdit")
        self.verticalLayout.addWidget(self.Area_lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.Text_textEdit = QtWidgets.QTextEdit(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Text_textEdit.setFont(font)
        self.Text_textEdit.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Text_textEdit.setObjectName("Text_textEdit")
        self.verticalLayout_2.addWidget(self.Text_textEdit)
        self.PlayListPermisiion_checkBox = QtWidgets.QCheckBox(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PlayListPermisiion_checkBox.setFont(font)
        self.PlayListPermisiion_checkBox.setStyleSheet("background-image: url(:/Background/background/transparent.png);\n"
"color: rgb(255, 255, 255);")
        self.PlayListPermisiion_checkBox.setObjectName("PlayListPermisiion_checkBox")
        self.verticalLayout_2.addWidget(self.PlayListPermisiion_checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back_btn = QtWidgets.QPushButton(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Back_btn.setFont(font)
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Back_btn.setObjectName("Back_btn")
        self.horizontalLayout_2.addWidget(self.Back_btn)
        self.Add_btn = QtWidgets.QPushButton(AddMusicWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Add_btn.setFont(font)
        self.Add_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Add_btn.setObjectName("Add_btn")
        self.horizontalLayout_2.addWidget(self.Add_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(AddMusicWindow)
        QtCore.QMetaObject.connectSlotsByName(AddMusicWindow)

    def retranslateUi(self, AddMusicWindow):
        _translate = QtCore.QCoreApplication.translate
        AddMusicWindow.setWindowTitle(_translate("AddMusicWindow", "Add music"))
        self.Title_lineEdit.setPlaceholderText(_translate("AddMusicWindow", "Title"))
        self.Album_lineEdit.setPlaceholderText(_translate("AddMusicWindow", "Album"))
        self.Duration_lineEdit.setPlaceholderText(_translate("AddMusicWindow", "Duration"))
        self.Age_lineEdit.setPlaceholderText(_translate("AddMusicWindow", "Age: ex: 18"))
        self.Genre_lineEdit.setPlaceholderText(_translate("AddMusicWindow", "Genre"))
        self.Area_lineEdit.setPlaceholderText(_translate("AddMusicWindow", "Area"))
        self.Text_textEdit.setPlaceholderText(_translate("AddMusicWindow", "Text of music"))
        self.PlayListPermisiion_checkBox.setText(_translate("AddMusicWindow", "Add to playlist permission"))
        self.Back_btn.setText(_translate("AddMusicWindow", "Back"))
        self.Add_btn.setText(_translate("AddMusicWindow", "Add song"))
import main_rc
