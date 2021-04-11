from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Главное окно
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Компановка
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #Заголовок
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        #Кнопка
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(208, 208, 104);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        # ???? ? ??
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # ? ?? ?
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Добавляем методы кнопкам
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPSEUgame"))
        self.label.setText(_translate("MainWindow", "Симулятор ГЭУ или как выжить студентом"))
        self.pushButton.setText(_translate("MainWindow", "Начать"))
    # Записываем методы в кнопки
    def add_functions(self):
        self.pushButton.clicked.connect(self.init_game)

    # Будущая функция обработки кнопки старт
    def init_game(self):
        MainWindow.setStyleSheet("background-color: rgb(175, 248, 111);")
        self.verticalLayout.removeWidget(self.pushButton)
        self.pushButton.deleteLater()
        self.pushButton = None
        self.verticalLayout.removeWidget(self.label)
        self.label.deleteLater()
        self.label = None
        #В попытках создать деньги
        #self.money = QtWidgets.QLabel(self.centralwidget)
        #font = QtGui.QFont()
        #font.setFamily("Segoe Print")
        #font.setPointSize(15)
        #font.setBold(True)
        #font.setWeight(75)
        #self.money.setFont(font)
        #self.money.setAlignment(QtCore.Qt.AlignCenter)
        #self.money.setObjectName("label")
        #self.verticalLayout.addWidget(self.money)


        print('Game has started')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
