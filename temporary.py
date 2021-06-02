from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QGridLayout, QMainWindow
from start import Ui_MainWindow_start
from gender import Ui_GenderWindow_gender
from main import Game
import json
import random
import sys

with open("questions.json", "r") as file:
    questions = json.load(file)

keys = list(questions.keys())
pair = questions.pop(keys[0])


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow_start()
ui.setupUi(MainWindow)
MainWindow.show()
def open_main_window_w():
    global GameWindow
    GameWindow = QtWidgets.QMainWindow()
    ui = Game("wooman")
    ui.setupUi(GameWindow)
    GenderWindow.close()
    GameWindow.show()
    ui.start.clicked.connect(ui.start_game)

def open_main_window_m():
    global GameWindow
    GameWindow = QtWidgets.QMainWindow()
    r = Game("man")
    r.setupUi(GameWindow)
    GenderWindow.close()
    GameWindow.show()
#    ui.start.clicked.connect(ui.start_game)
def open_window_gender():
    global GenderWindow
    GenderWindow = QtWidgets.QMainWindow()
    ui = Ui_GenderWindow_gender()
    ui.setupUi(GenderWindow)
    MainWindow.close()
    GenderWindow.show()
    ui.pushButton_3.clicked.connect(open_main_window_w)
    ui.pushButton_4.clicked.connect(open_main_window_m)


ui.pushButton_2.clicked.connect(open_window_gender)
sys.exit(app.exec_())