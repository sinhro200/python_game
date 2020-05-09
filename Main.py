import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QVBoxLayout, QWidget

from Action import MyAction
from MyMenu import MyMenu


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initializase_components()

        self.state_menu()
        self.show()


    def initializase_components(self):
        self.myMenu = MyMenu(
            [
                MyAction("Play", self.action_play),
                MyAction("Rules", self.action_rules),
                MyAction("Settings", self.action_settings),
                MyAction("Quit", self.action_quit)
            ]
        )

    def action_play(self):
        None

    def action_settings(self):
        None

    def action_rules(self):
        None

    def action_quit(self):
        self.close()

    def state_menu(self):
        self.myMenu.show(self)


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
