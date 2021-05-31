from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.08, y1:0.0738636, x2:0.766, y2:0.556864, stop:0 rgba(158, 35, 37, 255), stop:1 rgba(38, 38, 38, 255))")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 440, 491, 151))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"font-size: 90px;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1060, 710, 411, 301))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pics/solder.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 660, 191, 261))
        self.label_3.setStyleSheet("background-color: transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pics/agds.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 660, 191, 261))
        self.label_4.setStyleSheet("background-color: transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("pics/agds.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 550, 191, 261))
        self.label_5.setStyleSheet("background-color: transparent;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("pics/agds.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1300, 420, 171, 261))
        self.label_6.setStyleSheet("background-color: transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1310, 290, 171, 261))
        self.label_7.setStyleSheet("background-color: transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 240, 171, 261))
        self.label_8.setStyleSheet("background-color: transparent;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 180, 171, 261))
        self.label_9.setStyleSheet("background-color: transparent;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1250, 190, 171, 261))
        self.label_10.setStyleSheet("background-color: transparent;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1240, 340, 171, 261))
        self.label_11.setStyleSheet("background-color: transparent;")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1240, 450, 171, 261))
        self.label_12.setStyleSheet("background-color: transparent;")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(510, 320, 171, 261))
        self.label_13.setStyleSheet("background-color: transparent;")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("pics/432.png"))
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Отчислен!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())