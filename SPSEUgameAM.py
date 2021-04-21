from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon



class Game(object):

    font = QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(75)

    # функция изменяющая деньги
    def change_money(self, amount):
        self.moneyL.setText(str(int(self.moneyL.text()) + amount))

    # функция изменяющая зоровье
    def change_health(self, amount):
        self.healthL.setText(str(int(self.healthL.text()) + amount))

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

    # Записываем метод кнопки инициализации игры
    def add_functions(self):
        self.pushButton.clicked.connect(self.init_game)

    # Функция обработки кнопки старт
    def init_game(self):
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.deleteLater()
        self.label.deleteLater()

        # money icon
        self.moneyW = QtWidgets.QLabel(self.centralwidget)
        self.money = QPixmap('money.png')
        self.moneyW.setObjectName('money')
        self.moneyW.setPixmap(self.money)
        self.moneyW.adjustSize()
        self.moneyW.move(0, 0)
        self.moneyW.show()
        # money label
        self.moneyL = QtWidgets.QLabel(self.centralwidget)
        self.font.setPointSize(20)
        self.moneyL.setFont(self.font)
        self.moneyL.setText('0')
        self.moneyL.adjustSize()
        self.moneyL.move(90, 0)
        self.moneyL.show()

        # health icon
        self.health = QtWidgets.QLabel(self.centralwidget)
        self.heart = QPixmap('simple_heart.png')
        self.health.setObjectName('heart')
        self.health.setPixmap(self.heart)
        self.health.adjustSize()
        self.health.move(0, 60)
        self.health.show()
        # health label
        self.healthL = QtWidgets.QLabel(self.centralwidget)
        self.font.setPointSize(20)
        self.healthL.setFont(self.font)
        self.healthL.setText('100')
        self.healthL.adjustSize()
        self.healthL.move(90, 60)
        self.healthL.show()

        # knowledges icon
        self.knowledges = QtWidgets.QLabel(self.centralwidget)
        self.book = QPixmap('knowledge.png')
        self.knowledges.setObjectName('knowledge')
        self.knowledges.setPixmap(self.book)
        self.knowledges.adjustSize()
        self.knowledges.move(245, 0)
        self.knowledges.show()
        # knowledge bar
        self.knwbar = QtWidgets.QProgressBar(self.centralwidget)
        self.knwbar.setObjectName('knwbar')
        self.knwbar.setGeometry(325, 5, 250, 30)
        self.knwbar.show()

        # motivation icon
        self.motivation = QtWidgets.QLabel(self.centralwidget)
        self.mindset = QPixmap('mindset.png')
        self.motivation.setObjectName('motivation')
        self.motivation.setPixmap(self.mindset)
        self.motivation.adjustSize()
        self.motivation.move(245, 60)
        self.motivation.show()
        # motivation bar
        self.motivationbar = QtWidgets.QProgressBar(self.centralwidget)
        self.motivationbar.setObjectName('motivationbar')
        self.motivationbar.setGeometry(325, 75, 250, 30)
        self.motivationbar.show()

        # inventory
        self.inventory = QtWidgets.QLabel(self.centralwidget)
        self.inventory.setText('Будущий инвентарь')
        self.inventory.adjustSize()
        self.inventory.move(300, 300)

        # inventory button
        self.inventory_button = QtWidgets.QPushButton(self.centralwidget)
        self.inventory_bag = QIcon('bag.png')
        self.inventory_button.setIcon(self.inventory_bag)
        self.inventory_button.setIconSize(QSize(64, 64))
        self.inventory_button.adjustSize()
        self.inventory_button.move(1800, 0)
        self.inventory_button.show()
        self.inventory_button.clicked.connect(self.show_inv)


    def show_inv(self):
        self.inventory.show()

        print('Game has started')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Game()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
