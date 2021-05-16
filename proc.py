from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 713)
        self.t = 67
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.08, y1:0.0738636, x2:0.766, y2:0.556864, stop:0 rgba(158, 35, 37, 255), stop:1 rgba(38, 38, 38, 255))")
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(350, 360, 361, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"color: white;\n"
"background-color: transparent;\n"
"border: 4px solid black;\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: red;\n"
"}")
        if self.t < 35:
            self.progressBar.setStyleSheet("QProgressBar {\n"
"color: white;\n"
"background-color: transparent;\n"
"border: 4px solid black;\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: red;\n"
"}")
        elif self.t > 34 and self.t < 65:
            self.progressBar.setStyleSheet("QProgressBar {\n"
"color: white;\n"
"background-color: transparent;\n"
"border: 4px solid black;\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: orange;\n"
"}")
        elif self.t > 64:
            self.progressBar.setStyleSheet("QProgressBar {\n"
"color: white;\n"
"background-color: transparent;\n"
"border: 4px solid black;\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: green;\n"
"}")
        self.progressBar.setProperty("value", self.t)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
