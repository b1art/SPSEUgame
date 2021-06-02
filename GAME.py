from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
import json
import random
import sys

with open("questions.json", "r") as file:
    questions = json.load(file)

keys = list(questions.keys())
pair = questions.pop(keys[0])

class Game(object):
    font = QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(75)
    def __init__(self, gen = "man"):
        self.gen = gen
    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("Game")
        QMainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0.08, y1:0.0738636, x2:0.766, y2:0.556864, stop:0 rgba(158, 35, 37, 255), stop:1 rgba(38, 38, 38, 255))")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 120, 541, 591))
        self.label.setStyleSheet("background-color: transparent\n"
                                 "")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pics/people.png"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 650, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("Старт")
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border-radius: 40px;\n"
                                        "border: 1.5px solid white;\n"
                                        "color: white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: black;\n"
                                        "border: 1.5px solid black;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.first_start)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-80, 280, 501, 381))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pics/ipad.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(635, 180, 581, 121))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
                                   "color: white;\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Симулятор студента")
        MainWindow.setCentralWidget(self.centralwidget)

    def first_start(self):
        self.label.deleteLater()
        self.label_2.deleteLater()
        self.label_3.deleteLater()
        self.pushButton_2.deleteLater()
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
        self.label.setText("Выберите пол персонажа")
        self.label.show()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 490, 271, 311))
        self.label_2.setStyleSheet("background-color: transparent")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pics/wooman2.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.show()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1140, 460, 291, 331))
        self.label_3.setStyleSheet("background-color: transparent\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pics/man3.png"))
        self.label_3.setObjectName("label_3")
        self.label_3.show()
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
        self.pushButton_3.clicked.connect(self.first_f)
        self.pushButton_3.show()
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
        self.pushButton_4.clicked.connect(self.second_f)
        self.pushButton_4.show()

    def first_f(self):
        self.pushButton_3.deleteLater()
        self.pushButton_4.deleteLater()
        self.label.deleteLater()
        self.label_2.deleteLater()
        self.label_3.deleteLater()
        self.money = random.randrange(10, 50)
        self.healthh = random.randrange(50, 100)
        self.motivation = random.randrange(30, 80)
        self.knowledges = random.randrange(30, 70)
        # dialog window
        Game.font.setPointSize(20)

        self.dgrid = QGridLayout()
        self.dialog = QtWidgets.QFrame(self.centralwidget)
        self.dialog.setLayout(self.dgrid)
        self.dialog.setGeometry(450, 280, 800, 600)
        self.dialog.setStyleSheet(
            "background-color: transparent;border-radius:60px;"
        )
        self.dialog.show()
        # dialog...
        self.start = QtWidgets.QPushButton(self.dialog)
        self.start.setText("Начать")
        self.start.setStyleSheet("QPushButton{\n"
                                 "font-size: 25px;"
                                 "border-radius: 40px;\n"
                                 "border: 1.5px solid white;\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "color: black;\n"
                                 "border: 1.5px solid black;\n"
                                 "}\n"
                                 "")
        self.start.setGeometry(500, 400, 250, 100)
        self.start.show()
        self.start.clicked.connect(self.start_game)

        # Shop labels

        # Energos
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(1300, 130, 141, 101))
        self.pushButton1.setStyleSheet("QPushButton{\n"
                                       "background-color: transparent; \n"
                                       "border: 2px solid white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 2px solid black;\n"
                                       "background-color: rgba(255, 255, 255, 0.2);\n"
                                       "}")
        self.pushButton1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/energos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton1.setIcon(icon)
        self.pushButton1.setIconSize(QtCore.QSize(140, 90))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.show()
        # Book
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(1500, 130, 141, 101))
        self.pushButton2.setStyleSheet("QPushButton{\n"
                                       "background-color: transparent; \n"
                                       "border: 2px solid white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 2px solid black;\n"
                                       "background-color: rgba(255, 255, 255, 0.2);\n"
                                       "}")
        self.pushButton2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setIcon(icon)
        self.pushButton2.setIconSize(QtCore.QSize(140, 90))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.show()
        # Tubls
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(1700, 130, 141, 101))
        self.pushButton3.setStyleSheet("QPushButton{\n"
                                       "background-color: transparent; \n"
                                       "border: 2px solid white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 2px solid black;\n"
                                       "background-color: rgba(255, 255, 255, 0.2);\n"
                                       "}")
        self.pushButton3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/tubls.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton3.setIcon(icon)
        self.pushButton3.setIconSize(QtCore.QSize(140, 90))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.show()
        # Shop label
        self.label_shop = QtWidgets.QLabel(self.centralwidget)
        self.label_shop.setGeometry(QtCore.QRect(1520, 20, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_shop.setFont(font)
        self.label_shop.setStyleSheet("color:white;\nbackground-color: transparent;"
                                      "")
        self.label_shop.setObjectName("label")
        self.label_shop.show()
        # Human label

        self.label_human = QtWidgets.QLabel(self.centralwidget)
        self.label_human.setGeometry(QtCore.QRect(1620, 370, 281, 621))
        self.label_human.setStyleSheet("background-color: transparent;")
        self.label_human.setText("")
        self.label_human.setPixmap(QtGui.QPixmap("pics/wooman-hgh.png"))
        self.label_human.setObjectName("label")
        self.label_human.show()
        # label_Money

        self.moneyL = QtWidgets.QLabel(self.centralwidget)
        self.moneyL.setGeometry(QtCore.QRect(20, 20, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.moneyL.setFont(font)
        self.moneyL.setStyleSheet("color:white;\nbackground-color: transparent;"
                                  "")
        self.moneyL.setObjectName("label")
        self.moneyL.setText("Money: " + str(self.money) + "$")
        self.moneyL.show()
        # health
        self.healthPBtext = QtWidgets.QLabel(self.centralwidget)
        self.healthPBtext.setGeometry(QtCore.QRect(126, 105, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.healthPBtext.setFont(font)
        self.healthPBtext.setStyleSheet("color:white;\nbackground-color: transparent;"
                                        "")
        self.healthPBtext.setObjectName("label")
        self.healthPB = QtWidgets.QProgressBar(self.centralwidget)
        self.healthPB.setGeometry(QtCore.QRect(30, 140, 280, 23))
        self.color_h()
        self.healthPB.setProperty("value", self.healthh)
        self.healthPB.setObjectName("progressBar")
        self.healthPB.show()
        # motivation
        self.motivationPBtext = QtWidgets.QLabel(self.centralwidget)
        self.motivationPBtext.setGeometry(QtCore.QRect(107, 185, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.motivationPBtext.setFont(font)
        self.motivationPBtext.setStyleSheet("color:white;\nbackground-color: transparent;"
                                            "")
        self.motivationPBtext.setObjectName("label")
        self.motivationPB = QtWidgets.QProgressBar(self.centralwidget)
        self.motivationPB.setGeometry(QtCore.QRect(30, 220, 280, 23))
        self.color_mtv()
        self.motivationPB.setProperty("value", self.motivation)
        self.motivationPB.setObjectName("progressBar")
        self.motivationPB.show()
        # knowledges
        self.knowledgesPBtext = QtWidgets.QLabel(self.centralwidget)
        self.knowledgesPBtext.setGeometry(QtCore.QRect(98, 262, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.knowledgesPBtext.setFont(font)
        self.knowledgesPBtext.setStyleSheet("color:white;\nbackground-color: transparent;"
                                            "")
        self.knowledgesPBtext.setObjectName("label")
        self.knowledgesPB = QtWidgets.QProgressBar(self.centralwidget)
        self.knowledgesPB.setGeometry(QtCore.QRect(30, 300, 280, 23))
        self.color_knw()
        self.knowledgesPB.setProperty("value", self.knowledges)
        self.knowledgesPB.setObjectName("progressBar")
        self.knowledgesPB.show()
        self.pushButton1.clicked.connect(self.energos)
        self.pushButton2.clicked.connect(self.book)
        self.pushButton3.clicked.connect(self.puls)
        self.knowledgesPBtext.setText("Knowledge")
        self.healthPBtext.setText("Health")
        self.motivationPBtext.setText("Motivation")
        self.knowledgesPBtext.show()
        self.healthPBtext.show()
        self.motivationPBtext.show()

    def second_f(self):
        self.pushButton_3.deleteLater()
        self.pushButton_4.deleteLater()
        self.label.deleteLater()
        self.label_2.deleteLater()
        self.label_3.deleteLater()
        self.money = random.randrange(10, 50)
        self.healthh = random.randrange(50, 100)
        self.motivation = random.randrange(30, 80)
        self.knowledges = random.randrange(30, 70)
        # dialog window
        Game.font.setPointSize(20)

        self.dgrid = QGridLayout()
        self.dialog = QtWidgets.QFrame(self.centralwidget)
        self.dialog.setLayout(self.dgrid)
        self.dialog.setGeometry(450, 280, 800, 600)
        self.dialog.setStyleSheet(
            "background-color: transparent;border-radius:60px;"
        )
        self.dialog.show()
        # dialog...
        self.start = QtWidgets.QPushButton(self.dialog)
        self.start.setText("Начать")
        self.start.setStyleSheet("QPushButton{\n"
                                 "font-size: 25px;"
                                 "border-radius: 40px;\n"
                                 "border: 1.5px solid white;\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "color: black;\n"
                                 "border: 1.5px solid black;\n"
                                 "}\n"
                                 "")
        self.start.setGeometry(500, 400, 250, 100)
        self.start.show()
        self.start.clicked.connect(self.start_game)

        # Shop labels

        # Energos
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(1300, 130, 141, 101))
        self.pushButton1.setStyleSheet("QPushButton{\n"
                                       "background-color: transparent; \n"
                                       "border: 2px solid white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 2px solid black;\n"
                                       "background-color: rgba(255, 255, 255, 0.2);\n"
                                       "}")
        self.pushButton1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/energos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton1.setIcon(icon)
        self.pushButton1.setIconSize(QtCore.QSize(140, 90))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.show()
        # Book
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(1500, 130, 141, 101))
        self.pushButton2.setStyleSheet("QPushButton{\n"
                                       "background-color: transparent; \n"
                                       "border: 2px solid white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 2px solid black;\n"
                                       "background-color: rgba(255, 255, 255, 0.2);\n"
                                       "}")
        self.pushButton2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setIcon(icon)
        self.pushButton2.setIconSize(QtCore.QSize(140, 90))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.show()
        # Tubls
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(1700, 130, 141, 101))
        self.pushButton3.setStyleSheet("QPushButton{\n"
                                       "background-color: transparent; \n"
                                       "border: 2px solid white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "border: 2px solid black;\n"
                                       "background-color: rgba(255, 255, 255, 0.2);\n"
                                       "}")
        self.pushButton3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/tubls.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton3.setIcon(icon)
        self.pushButton3.setIconSize(QtCore.QSize(140, 90))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.show()
        # Shop label
        self.label_shop = QtWidgets.QLabel(self.centralwidget)
        self.label_shop.setGeometry(QtCore.QRect(1520, 20, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_shop.setFont(font)
        self.label_shop.setStyleSheet("color:white;\nbackground-color: transparent;"
                                      "")
        self.label_shop.setObjectName("label")
        self.label_shop.show()
        # Human label

        self.label_human = QtWidgets.QLabel(self.centralwidget)
        self.label_human.setGeometry(QtCore.QRect(1620, 370, 281, 621))
        self.label_human.setStyleSheet("background-color: transparent;")
        self.label_human.setText("")
        self.label_human.setPixmap(QtGui.QPixmap("pics/man-hgh.png"))
        self.label_human.setObjectName("label")
        self.label_human.show()
        # label_Money

        self.moneyL = QtWidgets.QLabel(self.centralwidget)
        self.moneyL.setGeometry(QtCore.QRect(20, 20, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.moneyL.setFont(font)
        self.moneyL.setStyleSheet("color:white;\nbackground-color: transparent;"
                                  "")
        self.moneyL.setObjectName("label")
        self.moneyL.setText("Money: " + str(self.money) + "$")
        self.moneyL.show()
        # health
        self.healthPBtext = QtWidgets.QLabel(self.centralwidget)
        self.healthPBtext.setGeometry(QtCore.QRect(126, 105, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.healthPBtext.setFont(font)
        self.healthPBtext.setStyleSheet("color:white;\nbackground-color: transparent;"
                                        "")
        self.healthPBtext.setObjectName("label")
        self.healthPB = QtWidgets.QProgressBar(self.centralwidget)
        self.healthPB.setGeometry(QtCore.QRect(30, 140, 280, 23))
        self.color_h()
        self.healthPB.setProperty("value", self.healthh)
        self.healthPB.setObjectName("progressBar")
        self.healthPB.show()
        # motivation
        self.motivationPBtext = QtWidgets.QLabel(self.centralwidget)
        self.motivationPBtext.setGeometry(QtCore.QRect(107, 185, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.motivationPBtext.setFont(font)
        self.motivationPBtext.setStyleSheet("color:white;\nbackground-color: transparent;"
                                            "")
        self.motivationPBtext.setObjectName("label")
        self.motivationPB = QtWidgets.QProgressBar(self.centralwidget)
        self.motivationPB.setGeometry(QtCore.QRect(30, 220, 280, 23))
        self.color_mtv()
        self.motivationPB.setProperty("value", self.motivation)
        self.motivationPB.setObjectName("progressBar")
        self.motivationPB.show()
        # knowledges
        self.knowledgesPBtext = QtWidgets.QLabel(self.centralwidget)
        self.knowledgesPBtext.setGeometry(QtCore.QRect(98, 262, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.knowledgesPBtext.setFont(font)
        self.knowledgesPBtext.setText("Knowledge")
        self.knowledgesPBtext.setStyleSheet("color:white;\nbackground-color: transparent;"
                                            "")
        self.knowledgesPBtext.setObjectName("label")
        self.knowledgesPB = QtWidgets.QProgressBar(self.centralwidget)
        self.knowledgesPB.setGeometry(QtCore.QRect(30, 300, 280, 23))
        self.color_knw()
        self.knowledgesPB.setProperty("value", self.knowledges)
        self.knowledgesPB.setObjectName("progressBar")
        self.knowledgesPB.show()
        self.pushButton1.clicked.connect(self.energos)
        self.pushButton2.clicked.connect(self.book)
        self.pushButton3.clicked.connect(self.puls)
        self.healthPBtext.setText("Health")
        self.motivationPBtext.setText("Motivation")
        self.knowledgesPBtext.show()
        self.healthPBtext.show()
        self.motivationPBtext.show()

    def energos(self):
        if self.money >= 5:
            self.healthh -= 5
            self.motivation += 10
            self.money -= 5
            self.moneyL.setText("Money: " + str(self.money) + "$")
            self.healthPB.setValue(self.healthh)
            self.motivationPB.setValue(self.motivation)
            self.color_mtv()
            self.color_h()
    def book(self):
        if self.money >= 10:
            self.knowledges += 10
            self.money -= 15
            self.moneyL.setText("Money: " + str(self.money) + "$")
            self.knowledgesPB.setValue(self.knowledges)
            self.color_knw()
    def puls(self):
        if self.money >= 18:
            self.healthh += 15
            self.money -= 18
            self.moneyL.setText("Money: " + str(self.money) + "$")
            self.healthPB.setValue(self.healthh)
            self.color_knw()
    def color_h(self):
        if self.healthh < 35:
            self.healthPB.setStyleSheet("QProgressBar {\n"
                                        "color: white;\n"
                                        "background-color: transparent;\n"
                                        "border: 4px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: red;\n"
                                        "}")
        elif self.healthh > 34 and self.healthh < 65:
            self.healthPB.setStyleSheet("QProgressBar {\n"
                                        "color: white;\n"
                                        "background-color: transparent;\n"
                                        "border: 4px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: orange;\n"
                                        "}")
        elif self.healthh > 64:
            self.healthPB.setStyleSheet("QProgressBar {\n"
                                        "color: white;\n"
                                        "background-color: transparent;\n"
                                        "border: 4px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: green;\n"
                                        "}")
    def color_mtv(self):
        if self.motivation < 35:
            self.motivationPB.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: red;\n"
                                            "}")
        elif self.motivation > 34 and self.motivation < 65:
            self.motivationPB.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: orange;\n"
                                            "}")
        elif self.motivation > 64:
            self.motivationPB.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: green;\n"
                                            "}")
    def color_knw(self):
        if self.knowledges < 35:
            self.knowledgesPB.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: red;\n"
                                            "}")
        elif self.knowledges > 34 and self.knowledges < 65:
            self.knowledgesPB.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: orange;\n"
                                            "}")
        elif self.knowledges > 64:
            self.knowledgesPB.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: green;\n"
                                            "}")
    # функция изменяющая деньги
    def change_money(self, amount):
        self.money += amount
        self.moneyL.setText("Money: " + str(self.money) + "$")
        if self.money < 1:
            self.moneyL.setText("Money: 0$")
            self.money = 0

    # функция изменяющая зоровье
    def change_health(self, amount):
        self.healthh += amount
        if self.healthh < 1:
            self.healthh = 0
        if self.healthh > 99:
            self.healthh = 100
        self.healthPB.setValue(self.healthh)
        self.color_h()
    def change_motivation(self, amount):
        self.motivation += amount
        if self.motivation < 1:
            self.motivation = 0
        if self.motivation > 99:
            self.motivation = 100
        self.motivationPB.setValue(self.motivation)
        self.color_mtv()
    def change_knowledge(self, amount):
        self.knowledges += amount
        if self.knowledges < 1:
            self.knowledges = 0
        if self.knowledges > 99:
            self.knowledges = 100
        self.knowledgesPB.setValue(self.knowledges)
        self.color_knw()

    # окно вопросов
    def start_game(self):
        self.start.deleteLater()
        self.question = QtWidgets.QLabel(self.dialog)
        Game.font.setPointSize(20)
        self.question.setFont(Game.font)
        self.question.setWordWrap(True)
        self.question.setText(keys[0])
        self.question.setAlignment(QtCore.Qt.AlignLeft)
        self.question.adjustSize()
        self.question.setStyleSheet(
            "color: white;text-align: center;"
            "}"
        )
        self.option1 = QtWidgets.QPushButton(self.dialog)
        self.option1.setText(pair[0][0])
        self.option1.setFont(Game.font)
        self.option1.setStyleSheet(
            "QPushButton{\n"
"font-size: 25px;font-style: normal;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
        )
        self.option1.clicked.connect(self.answered_u)
        self.option2 = QtWidgets.QPushButton(self.dialog)
        self.option2.setText(pair[1][0])
        self.option2.setFont(Game.font)
        self.option2.setStyleSheet(
            "QPushButton{\n"
"font-size: 25px;font-style: normal;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
        )
        self.option2.clicked.connect(self.answered_l)

        self.dgrid.addWidget(self.question, *(0, 0))
        self.dgrid.addWidget(self.option1, *(1, 0))
        self.dgrid.addWidget(self.option2, *(2, 0))
    # написать ловер pair 1 1 соответсвенно
    def answered_u(self):
        global pair
        del keys[0]
        self.question.deleteLater()
        self.question.setStyleSheet(
            "color: white;text-align: center;"
            "}"
        )
        self.option1.deleteLater()
        self.option2.deleteLater()
        self.effect(pair[0][1])
        try:
            pair = questions.pop(keys[0])
            if "cost" in pair[0][1] and pair[0][1]["cost"] > self.money or "min_mtv" in pair[0][1] and pair[0][1]["min_mtv"] > self.motivation or "min_knw" in pair[0][1] and pair[0][1]["min_knw"] > self.knowledges:
                if self.healthh <= 0 or self.motivation <= 0 or self.knowledges <= 0:

                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("Вы не смогли справиться с учебой и покинули ВУЗ")
                    self.question.setWordWrap(True)
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )

                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.option1 = QtWidgets.QLabel(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))

            else:
                if self.healthh <= 0 or self.motivation <= 0 or self.knowledges <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("Вы не смогли справиться с учебой и покинули ВУЗ")
                    self.question.setWordWrap(True)
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.option1 = QtWidgets.QPushButton(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option1.clicked.connect(self.answered_u)
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))
        except:
            self.question = QtWidgets.QLabel(self.dialog)
            Game.font.setPointSize(20)
            self.question.setFont(Game.font)
            if self.knowledges >= 80:
                self.question.setText("Победа")
            else:
                self.question.setText("Неплохо, но можно было и лучше")
            self.question.setAlignment(QtCore.Qt.AlignCenter)
            self.question.adjustSize()
            self.question.setStyleSheet(
                "color: white;text-align: center;"
                "}"
            )
            self.dgrid.addWidget(self.question, *(0, 0))

    def answered_l(self):
        global pair
        del keys[0]
        self.question.deleteLater()
        self.option1.deleteLater()
        self.option2.deleteLater()
        self.effect(pair[1][1])
        try:
            pair = questions.pop(keys[0])
            if "cost" in pair[0][1] and pair[0][1]["cost"] > self.money or "min_mtv" in pair[0][1] and pair[0][1]["min_mtv"] > self.motivation or "min_knw" in pair[0][1] and pair[0][1]["min_knw"] > self.knowledges:
                if self.healthh <= 0 or self.motivation <= 0 or self.knowledges <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("Вы не смогли справиться с учебой и покинули ВУЗ")
                    self.question.setWordWrap(True)
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.option1 = QtWidgets.QLabel(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))
            else:
                if self.healthh <= 0 or self.motivation <= 0 or self.knowledges <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("Вы не смогли справиться с учебой и покинули ВУЗ")
                    self.question.setWordWrap(True)
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.question.setStyleSheet(
                        "color: white;text-align: center;"
                        "}"
                    )
                    self.option1 = QtWidgets.QPushButton(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option1.clicked.connect(self.answered_u)
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "QPushButton{\n"
"font-size: 25px;"
"border-radius: 20px;\n"
"border: 1.5px solid white;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"color: black;\n"
"border: 1.5px solid black;\n"
"}\n"
""
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))
        except:
            self.question = QtWidgets.QLabel(self.dialog)
            Game.font.setPointSize(20)
            self.question.setFont(Game.font)
            if self.knowledges >= 80:
                self.question.setText("Победа")
            else:
                self.question.setText("Неплохо, но можно было и лучше")
            self.question.setAlignment(QtCore.Qt.AlignCenter)
            self.question.adjustSize()
            self.question.setStyleSheet(
                "color: white;text-align: center;"
                "}"
            )
            self.dgrid.addWidget(self.question, *(0, 0))

    def effect(self, assoc):
        as_keys = list(assoc.keys())
        for i in as_keys:
            if i == "hp":
                self.change_health(assoc[i])
            if i == "money":
                self.change_money(assoc[i])
            if i == "cost":
                self.change_money(-assoc[i])
            if i == "mtv":
                self.change_motivation(assoc[i])
            if i == "knw":
                self.change_knowledge(assoc[i])


    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_shop.setText(_translate("MainWindow", "Shop"))
        self.moneyL.setText(_translate("MainWindow", "Money: " + str(self.money) + "$"))
        self.healthPBtext.setText(_translate("MainWindow", "Health"))
        self.motivationPBtext.setText(_translate("MainWindow", "Motivation"))
        self.knowledgesPBtext.setText(_translate("MainWindow", "Knowledges"))
        if self.money < 1:
            self.money = 0
            #self.moneyL.setText("Money: 0$")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Game("wooman")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
