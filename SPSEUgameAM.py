from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QGridLayout
from Inventory import Inventory
import json

######## Выбор характеристики?

with open("questions.json", "r") as file:
    questions = json.load(file)

keys = list(questions.keys())


class Game(object):

    font = QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(75)

    # функция изменяющая деньги
    def change_money(self, amount):
        self.moneyL.setText(str(int(self.moneyL.text()) + amount))
        self.moneyL.adjustSize()

    # функция изменяющая зоровье
    def change_health(self, amount):
        self.healthL.setText(str(int(self.healthL.text()) + amount))
        self.healthL.adjustSize()

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
        # self.headerView = QtWidgets.QHeaderView(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.headerView.setObjectName("headerView")
        # Заголовок
        self.label = QtWidgets.QLabel(self.centralwidget)
        Game.font.setPointSize(15)
        self.label.setFont(Game.font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        # Кнопка
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        Game.font.setPointSize(20)
        self.pushButton.setFont(Game.font)
        self.pushButton.setStyleSheet("background-color: rgb(208, 208, 104);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        # jpg
        # self.jpg = QtWidgets.QLabel(self.centralwidget)
        # self.pic = QPixmap('Starting.jpg')
        # self.jpg.setObjectName('jpg')
        # self.jpg.setPixmap(self.pic)
        # self.jpg.adjustSize()
        # self.jpg.show()

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
        self.label.setText(
            _translate("MainWindow", "Симулятор ГЭУ или как выжить студентом")
        )
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
        self.money = QPixmap("icons/money.png")
        self.moneyW.setObjectName("money")
        self.moneyW.setPixmap(self.money)
        self.moneyW.adjustSize()
        self.moneyW.move(0, 0)
        self.moneyW.show()
        # money label
        self.moneyL = QtWidgets.QLabel(self.centralwidget)
        self.font.setPointSize(20)
        self.moneyL.setFont(self.font)
        self.moneyL.setText("0")
        self.moneyL.adjustSize()
        self.moneyL.move(90, 0)
        self.moneyL.show()

        # health icon
        self.health = QtWidgets.QLabel(self.centralwidget)
        self.heart = QPixmap("icons/simple_heart.png")
        self.health.setObjectName("heart")
        self.health.setPixmap(self.heart)
        self.health.adjustSize()
        self.health.move(0, 60)
        self.health.show()
        # health label
        self.healthL = QtWidgets.QLabel(self.centralwidget)
        self.font.setPointSize(20)
        self.healthL.setFont(self.font)
        self.healthL.setText("100")
        self.healthL.adjustSize()
        self.healthL.move(90, 60)
        self.healthL.show()

        # knowledges icon
        self.knowledges = QtWidgets.QLabel(self.centralwidget)
        self.book = QPixmap("icons/knowledge.png")
        self.knowledges.setObjectName("knowledge")
        self.knowledges.setPixmap(self.book)
        self.knowledges.adjustSize()
        self.knowledges.move(245, 0)
        self.knowledges.show()
        # knowledge bar
        self.knwbar = QtWidgets.QProgressBar(self.centralwidget)
        self.knwbar.setObjectName("knwbar")
        self.knwbar.setGeometry(325, 5, 250, 30)
        self.knwbar.show()

        # motivation icon
        self.motivation = QtWidgets.QLabel(self.centralwidget)
        self.mindset = QPixmap("icons/mindset.png")
        self.motivation.setObjectName("motivation")
        self.motivation.setPixmap(self.mindset)
        self.motivation.adjustSize()
        self.motivation.move(245, 60)
        self.motivation.show()
        # motivation bar
        self.motivationbar = QtWidgets.QProgressBar(self.centralwidget)
        self.motivationbar.setObjectName("motivationbar")
        self.motivationbar.setGeometry(325, 75, 250, 30)
        self.motivationbar.show()

        # dialog window
        self.dgrid = QGridLayout()
        self.dialog = QtWidgets.QFrame(self.centralwidget)
        self.dialog.setLayout(self.dgrid)
        self.dialog.setGeometry(75, 200, 600, 400)
        self.dialog.setStyleSheet(
            "background-color: rgb(200, 15, 100);border-radius:60px;"
        )
        self.dialog.show()
        # dialog...
        self.start = QtWidgets.QPushButton(self.dialog)
        self.start.setText("Начать")
        self.start.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.start.setGeometry(100, 100, 100, 100)
        self.start.show()
        self.start.clicked.connect(self.start_game)

        # inventory
        self.inventory = QtWidgets.QFrame(self.centralwidget)
        self.inventory.setGeometry(1600, 100, 300, 600)
        self.inventory.setStyleSheet("background-color: rgb(123, 125, 123);")

        self.grid = QGridLayout()
        self.inventory.setLayout(self.grid)
        myInv = Inventory()

        self.slot1 = QtWidgets.QFrame()
        self.slot1.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot1check = True
        self.slot2 = QtWidgets.QFrame()
        self.slot2.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot2check = True
        self.slot3 = QtWidgets.QFrame()
        self.slot3.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot3check = True
        self.slot4 = QtWidgets.QFrame()
        self.slot4.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot4check = True
        self.slot5 = QtWidgets.QFrame()
        self.slot5.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot5check = True
        self.slot6 = QtWidgets.QFrame()
        self.slot6.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot6check = True
        self.slot7 = QtWidgets.QFrame()
        self.slot7.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot7check = True
        self.slot8 = QtWidgets.QFrame()
        self.slot8.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot8check = True
        self.slot9 = QtWidgets.QFrame()
        self.slot9.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot9check = True
        self.slot10 = QtWidgets.QFrame()
        self.slot10.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot10check = True
        self.slot11 = QtWidgets.QFrame()
        self.slot11.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot11check = True
        self.slot12 = QtWidgets.QFrame()
        self.slot12.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot12check = True
        self.slot13 = QtWidgets.QFrame()
        self.slot13.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot13check = True
        self.slot14 = QtWidgets.QFrame()
        self.slot14.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot14check = True
        self.slot15 = QtWidgets.QFrame()
        self.slot15.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot15check = True
        self.slot16 = QtWidgets.QFrame()
        self.slot16.setStyleSheet("background-color: rgb(200, 15, 100);")
        self.slot16check = True

        self.grid.addWidget(self.slot1, *(0, 0))
        self.grid.addWidget(self.slot2, *(1, 0))
        self.grid.addWidget(self.slot3, *(2, 0))
        self.grid.addWidget(self.slot4, *(3, 0))
        self.grid.addWidget(self.slot5, *(4, 0))
        self.grid.addWidget(self.slot6, *(5, 0))
        self.grid.addWidget(self.slot7, *(6, 0))
        self.grid.addWidget(self.slot8, *(7, 0))
        self.grid.addWidget(self.slot9, *(0, 1))
        self.grid.addWidget(self.slot10, *(1, 1))
        self.grid.addWidget(self.slot11, *(2, 1))
        self.grid.addWidget(self.slot12, *(3, 1))
        self.grid.addWidget(self.slot13, *(4, 1))
        self.grid.addWidget(self.slot14, *(5, 1))
        self.grid.addWidget(self.slot15, *(6, 1))
        self.grid.addWidget(self.slot16, *(7, 1))

        # inventory button
        self.inventory_button = QtWidgets.QPushButton(self.centralwidget)
        self.inventory_bag = QIcon("icons/bag.png")
        self.inventory_button.setIcon(self.inventory_bag)
        self.inventory_button.setIconSize(QSize(64, 64))
        self.inventory_button.adjustSize()
        self.inventory_button.move(1800, 0)
        self.inventory_button.setCheckable(True)
        self.inventory_button.show()
        self.inventory_button.clicked.connect(self.show_inv)
        self.inventory_button.setToolTip("inventory")

    # окно вопросов
    def start_game(self):
        self.start.deleteLater()
        self.question = QtWidgets.QLabel(self.dialog)
        Game.font.setPointSize(20)
        self.question.setFont(Game.font)
        self.question.setText(keys[0])
        self.question.setAlignment(QtCore.Qt.AlignLeft)
        self.question.adjustSize()
        self.option1 = QtWidgets.QPushButton(self.dialog)
        self.option1.setText(questions[keys[0]][0])
        self.option1.setFont(Game.font)
        self.option1.setStyleSheet(
            "text-align: left; background-color: rgb(255, 255, 255); border-radius:60px;}"
        )
        self.option1.clicked.connect(self.answered)
        self.option2 = QtWidgets.QPushButton(self.dialog)
        self.option2.setText(questions[keys[0]][1])
        self.option2.setFont(Game.font)
        self.option2.setStyleSheet(
            "text-align: left; background-color: rgb(255, 255, 255); border-radius:60px;}"
        )
        self.option2.clicked.connect(self.answered)

        self.dgrid.addWidget(self.question, *(0, 0))
        self.dgrid.addWidget(self.option1, *(1, 0))
        self.dgrid.addWidget(self.option2, *(2, 0))

    def answered(self):
        self.question.deleteLater()
        self.option1.deleteLater()
        self.option2.deleteLater()
        try:
            pair = questions.pop(keys[0])
            self.question = QtWidgets.QLabel(self.dialog)
            Game.font.setPointSize(20)
            self.question.setFont(Game.font)
            self.question.setText(keys[1])
            self.question.setAlignment(QtCore.Qt.AlignLeft)
            self.question.adjustSize()
            self.option1 = QtWidgets.QPushButton(self.dialog)
            self.option1.setText(pair[0])
            self.option1.setFont(Game.font)
            self.option1.setStyleSheet(
                "text-align: left; background-color: rgb(255, 255, 255); border-radius:60px;}"
            )
            self.option1.clicked.connect(self.answered)
            self.option2 = QtWidgets.QPushButton(self.dialog)
            self.option2.setText(pair[1])
            self.option2.setFont(Game.font)
            self.option2.setStyleSheet(
                "text-align: left; background-color: rgb(255, 255, 255); border-radius:60px;}"
            )
            self.option2.clicked.connect(self.answered)

            self.dgrid.addWidget(self.question, *(0, 0))
            self.dgrid.addWidget(self.option1, *(1, 0))
            self.dgrid.addWidget(self.option2, *(2, 0))
            del keys[0]
        except:
            self.question = QtWidgets.QLabel(self.dialog)
            Game.font.setPointSize(20)
            self.question.setFont(Game.font)
            self.question.setText("nema voprosov")
            self.question.setAlignment(QtCore.Qt.AlignCenter)
            self.question.adjustSize()
            self.dgrid.addWidget(self.question, *(0, 0))

    def show_inv(self):
        if self.inventory_button.isCheckable():
            self.inventory_button.setCheckable(False)
            self.inventory.show()
        else:
            self.inventory_button.setCheckable(True)
            ### Руина self.myInv.inv[1] = 'str'
            self.inventory.hide()

    def find_slot(self):
        if self.slot1check:
            self.slot1check = False
            return self.slot1
        elif self.slot2check:
            self.slot2check = False
            return self.slot2
        elif self.slot3check:
            self.slot3check = False
            return self.slot3
        elif self.slot4check:
            self.slot4check = False
            return self.slot4
        elif self.slot5check:
            self.slot5check = False
            return self.slot5
        elif self.slot6check:
            self.slot6check = False
            return self.slot6
        elif self.slot7check:
            self.slot7check = False
            return self.slot7
        elif self.slot8check:
            self.slot8check = False
            return self.slot8
        elif self.slot9check:
            self.slot9check = False
            return self.slot9
        elif self.slot10check:
            self.slot10check = False
            return self.slot10
        elif self.slot11check:
            self.slot11check = False
            return self.slot11
        elif self.slot12check:
            self.slot12check = False
            return self.slot12
        elif self.slot13check:
            self.slot13check = False
            return self.slot13
        elif self.slot13check:
            self.slot13check = False
            return self.slot13
        elif self.slot14check:
            self.slot14check = False
            return self.slot14
        elif self.slot15check:
            self.slot15check = False
            return self.slot15
        elif self.slot16check:
            self.slot16check = False
            return self.slot16
        else:
            return None

    def add_item(self, name="asd"):
        # if self.find_slot() == None:
        # РЕЙЗ ОШИБКУ ТУДЫМ СЮДЫМ
        # else:
        self.new_item = QtWidgets.QPushButton(self.find_slot())
        self.new_item.setText(name)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Game()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # ui.add_item('adsasdasd')
    # ui.names[2] = 'ASD'
    # Game.inventory1.add_item()
    sys.exit(app.exec_())
