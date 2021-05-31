from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QGridLayout
import json
import random

with open("questions.json", "r") as file:
    questions = json.load(file)

keys = list(questions.keys())
pair = questions.pop(keys[0])

class Game(object):
    font = QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(75)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.t = 45
        self.money = random.randrange(10, 50)
        self.healthh = random.randrange(50, 100)
        self.motivation = random.randrange(30, 80)
        self.knowladges = random.randrange(30, 70)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.08, y1:0.0738636, x2:0.766, y2:0.556864, stop:0 rgba(158, 35, 37, 255), stop:1 rgba(38, 38, 38, 255))")
        self.centralwidget.setObjectName("centralwidget")
        # dialog window
        Game.font.setPointSize(15)
        Game.font.setPointSize(20)

        self.dgrid = QGridLayout()
        self.dialog = QtWidgets.QFrame(self.centralwidget)
        self.dialog.setLayout(self.dgrid)
        self.dialog.setGeometry(350, 380, 800, 600)
        self.dialog.setStyleSheet(
            "background-color: rgb(219, 112, 147);border-radius:60px;"
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
        self.start.setGeometry(100, 100, 250, 100)
        self.start.show()
        self.start.clicked.connect(self.start_game)

#Shop labels

#Energos
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
#Book
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
#Tubls
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
#Shop label
        self.label_shop = QtWidgets.QLabel(self.centralwidget)
        self.label_shop.setGeometry(QtCore.QRect(1520, 20, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_shop.setFont(font)
        self.label_shop.setStyleSheet("color:white;\nbackground-color: transparent;"
                                  "")
        self.label_shop.setObjectName("label")
#Human label
        self.label_human = QtWidgets.QLabel(self.centralwidget)
        self.label_human.setGeometry(QtCore.QRect(1620, 370, 281, 621))
        self.label_human.setStyleSheet("background-color: transparent;")
        self.label_human.setText("")
        self.label_human.setPixmap(QtGui.QPixmap("pics/man-hgh.png"))
        self.label_human.setObjectName("label")
#label_Money

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 20, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:white;\nbackground-color: transparent;"
                                 "")
        self.label1.setObjectName("label")
#label2 + bar2
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(126, 105, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color:white;\nbackground-color: transparent;"
                                  "")
        self.label2.setObjectName("label")
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar2.setGeometry(QtCore.QRect(30, 140, 280, 23))
        self.progressBar2.setStyleSheet("QProgressBar {\n"
                                        "color: white;\n"
                                        "background-color: transparent;\n"
                                        "border: 4px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: red;\n"
                                        "}")
        if self.healthh < 35:
            self.progressBar2.setStyleSheet("QProgressBar {\n"
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
            self.progressBar2.setStyleSheet("QProgressBar {\n"
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
            self.progressBar2.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: green;\n"
                                            "}")
        self.progressBar2.setProperty("value", self.healthh)
        self.progressBar2.setObjectName("progressBar")
#label3 + bar3
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(107, 185, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color:white;\nbackground-color: transparent;"
                                  "")
        self.label3.setObjectName("label")
        self.progressBar3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar3.setGeometry(QtCore.QRect(30, 220, 280, 23))
        self.progressBar3.setStyleSheet("QProgressBar {\n"
                                        "color: white;\n"
                                        "background-color: transparent;\n"
                                        "border: 4px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: red;\n"
                                        "}")
        if self.motivation < 35:
            self.progressBar3.setStyleSheet("QProgressBar {\n"
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
            self.progressBar3.setStyleSheet("QProgressBar {\n"
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
            self.progressBar3.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: green;\n"
                                            "}")
        self.progressBar3.setProperty("value", self.motivation)
        self.progressBar3.setObjectName("progressBar")
#label4 + bar4
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(98, 262, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color:white;\nbackground-color: transparent;"
                                  "")
        self.label4.setObjectName("label")
        self.progressBar4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar4.setGeometry(QtCore.QRect(30, 300, 280, 23))
        self.progressBar4.setStyleSheet("QProgressBar {\n"
                                        "color: white;\n"
                                        "background-color: transparent;\n"
                                        "border: 4px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "background-color: red;\n"
                                        "}")
        if self.knowladges < 35:
            self.progressBar4.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: red;\n"
                                            "}")
        elif self.knowladges > 34 and self.knowladges < 65:
            self.progressBar4.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: orange;\n"
                                            "}")
        elif self.knowladges > 64:
            self.progressBar4.setStyleSheet("QProgressBar {\n"
                                            "color: white;\n"
                                            "background-color: transparent;\n"
                                            "border: 4px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "text-align: center;\n"
                                            "}\n"
                                            "QProgressBar::chunk{\n"
                                            "background-color: green;\n"
                                            "}")
        self.progressBar4.setProperty("value", self.knowladges)
        self.progressBar4.setObjectName("progressBar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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
        self.option1 = QtWidgets.QPushButton(self.dialog)
        self.option1.setText(pair[0][0])
        self.option1.setFont(Game.font)
        self.option1.setStyleSheet(
            "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
        )
        self.option1.clicked.connect(self.answered_u)
        self.option2 = QtWidgets.QPushButton(self.dialog)
        self.option2.setText(pair[1][0])
        self.option2.setFont(Game.font)
        self.option2.setStyleSheet(
            "border-radius:60px;text-align: left;background-color: rgb(255, 192, 203);"
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
        self.option1.deleteLater()
        self.option2.deleteLater()
        self.effect(pair[0][1])
        try:
            pair = questions.pop(keys[0])
            if "cost" in pair[0][1] and pair[0][1]["cost"] > int(self.moneyL.text()):
                if int(self.healthL.text()) <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("x_x")
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.option1 = QtWidgets.QLabel(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))

            else:
                if int(self.healthL.text()) <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("x_x")
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.option1 = QtWidgets.QPushButton(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option1.clicked.connect(self.answered_u)
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))
        except:
            self.question = QtWidgets.QLabel(self.dialog)
            Game.font.setPointSize(20)
            self.question.setFont(Game.font)
            self.question.setText("Вы отчислены")
            self.question.setAlignment(QtCore.Qt.AlignCenter)
            self.question.adjustSize()
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
            if "cost" in pair[0][1] and pair[0][1]["cost"] > int(self.moneyL.text()):
                if int(self.healthL.text()) <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("x_x")
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.option1 = QtWidgets.QLabel(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))
            else:
                if int(self.healthL.text()) <= 0:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setText("x_x")
                    self.question.setAlignment(QtCore.Qt.AlignCenter)
                    self.question.adjustSize()
                    self.dgrid.addWidget(self.question, *(0, 0))
                else:
                    self.question = QtWidgets.QLabel(self.dialog)
                    Game.font.setPointSize(20)
                    self.question.setFont(Game.font)
                    self.question.setWordWrap(True)
                    self.question.setText(keys[0])
                    self.question.setAlignment(QtCore.Qt.AlignLeft)
                    self.question.adjustSize()
                    self.option1 = QtWidgets.QPushButton(self.dialog)
                    self.option1.setText(pair[0][0])
                    self.option1.setFont(Game.font)
                    self.option1.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option1.clicked.connect(self.answered_u)
                    self.option2 = QtWidgets.QPushButton(self.dialog)
                    self.option2.setText(pair[1][0])
                    self.option2.setFont(Game.font)
                    self.option2.setStyleSheet(
                        "text-align: left;background-color: rgb(255, 192, 203);border-radius:60px;"
                    )
                    self.option2.clicked.connect(self.answered_l)

                    self.dgrid.addWidget(self.question, *(0, 0))
                    self.dgrid.addWidget(self.option1, *(1, 0))
                    self.dgrid.addWidget(self.option2, *(2, 0))
        except:
            self.question = QtWidgets.QLabel(self.dialog)
            Game.font.setPointSize(20)
            self.question.setFont(Game.font)
            self.question.setText("Вы отчислены")
            self.question.setAlignment(QtCore.Qt.AlignCenter)
            self.question.adjustSize()
            self.dgrid.addWidget(self.question, *(0, 0))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_shop.setText(_translate("MainWindow", "Shop"))
        s = 345
        self.label1.setText(_translate("MainWindow", "Money: " + str(self.money) + "$"))
        self.label2.setText(_translate("MainWindow", "Health"))
        self.label3.setText(_translate("MainWindow", "Motivation"))
        self.label4.setText(_translate("MainWindow", "Knowledges"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Game()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())