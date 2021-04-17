from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap



class Game(object):

    font = QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(75)

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
        #self.headerView = QtWidgets.QHeaderView(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.headerView.setObjectName("headerView")
        #Заголовок
        self.label = QtWidgets.QLabel(self.centralwidget)
        Game.font.setPointSize(15)
        self.label.setFont(Game.font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        #Кнопка
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        Game.font.setPointSize(20)
        self.pushButton.setFont(Game.font)
        self.pushButton.setStyleSheet("background-color: rgb(208, 208, 104);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        #jpg
        #self.jpg = QtWidgets.QLabel(self.centralwidget)
        #self.pic = QPixmap('Starting.jpg')
        #self.jpg.setObjectName('jpg')
        #self.jpg.setPixmap(self.pic)
        #self.jpg.adjustSize()
        #self.jpg.show()


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
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout.removeWidget(self.pushButton)
        self.pushButton.deleteLater()
        self.verticalLayout.removeWidget(self.label)
        self.label.deleteLater()

        #money label
        self.money = QtWidgets.QLabel(self.centralwidget)
        Game.font.setPointSize(15)
        self.money.setFont(Game.font)
        #self.money.setAlignment(QtCore.Qt.AlignTop)
        self.money.setObjectName("money")
        #self.verticalLayout.addWidget(self.money)
        self.money.setText('money:')
        self.money.move(0, 0)
        self.money.adjustSize()
        self.money.show()

        #health label
        self.health = QtWidgets.QLabel(self.centralwidget)
        Game.font.setPointSize(15)
        self.health.setFont(Game.font)
        #self.health.setAlignment(QtCore.Qt.AlignTop)
        self.health.setObjectName("health")
        #self.verticalLayout.addWidget(self.health)
        self.health.setText('health:')
        self.health.move(0, 50)
        self.health.adjustSize()
        self.health.show()

        #
        #self.btn = QtWidgets.QPushButton(self.centralwidget)
        #Game.font.setPointSize(20)
        #self.btn.setFont(Game.font)
        #self.btn.setStyleSheet("background-color: rgb(123, 123, 123);")
        #self.btn.setObjectName("btn")
        #self.verticalLayout.addWidget(self.btn)

        #knowledges
        self.knwbar = QtWidgets.QProgressBar(self.centralwidget)
        self.knwbar.setObjectName('knwbar')
        self.knwbar.setGeometry(95, 15, 200, 20)
        self.knwbar.show()

        #motivation
        self.motivationbar = QtWidgets.QProgressBar(self.centralwidget)
        self.motivationbar.setObjectName('motivationbar')
        self.motivationbar.setGeometry(95, 65, 200, 20)
        self.motivationbar.show()

        print('Game has started')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Game()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
