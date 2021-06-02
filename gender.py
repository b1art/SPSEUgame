from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenderWindow_gender(object):
    def setupUi(self, GenderWindow):
        GenderWindow.setObjectName("GenderWindow")
        GenderWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(GenderWindow)
        self.centralwidget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.08, y1:0.0738636, x2:0.766, y2:0.556864, stop:0 rgba(158, 35, 37, 255), stop:1 rgba(38, 38, 38, 255))")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 150, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: transparent;\n"
"color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 490, 271, 311))
        self.label_2.setStyleSheet("background-color: transparent")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pics/wooman2.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1140, 460, 291, 331))
        self.label_3.setStyleSheet("background-color: transparent\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pics/man3.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 460, 301, 331))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: transparent;\n"
"border: 5px solid black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 0, 0, 0.2);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setAutoRepeatDelay(300)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1130, 460, 301, 331))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: transparent; \n"
"border: 4px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setAutoRepeatDelay(300)
        self.pushButton_4.setObjectName("pushButton_4")
        GenderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenderWindow)
        QtCore.QMetaObject.connectSlotsByName(GenderWindow)

    def retranslateUi(self, GenderWindow):
        _translate = QtCore.QCoreApplication.translate
        GenderWindow.setWindowTitle(_translate("GenderWindow", "GenderWindow"))
        self.label.setText(_translate("GenderWindow", "Выберите пол персонажа"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenderWindow = QtWidgets.QMainWindow()
    ui = Ui_GenderWindow()
    ui.setupUi(GenderWindow)
    GenderWindow.show()
    sys.exit(app.exec_())
"""
