from typing import List

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QVBoxLayout, QPushButton

from MyAction import MyAction

btn_width = 170


class MyMenu():
    def __init__(self, actions: List[MyAction] ):
        vboxMenu = self.createMenu(actions)
        self.menuWidget = QWidget()
        self.menuWidget.setLayout(vboxMenu)

    def show(self, window: QMainWindow):
        window.setGeometry(
            QDesktopWidget().availableGeometry().center().x(),
            QDesktopWidget().availableGeometry().center().y(),
            300, 300)

        window.setMenuWidget(self.menuWidget)

    # ToDo alignment center for menu
    def createMenu1(self, act_play, act_quit, act_rules, act_settings):
        btnQuit = self.MyMenuButton("Quit", act_quit)
        btnSettings = self.MyMenuButton("Settings", act_settings)
        btnRules = self.MyMenuButton("Rules", act_rules)
        btnPlay = self.MyMenuButton("Play", act_play)

        vboxMenu = QVBoxLayout()
        vboxMenu.addStretch(1)
        vboxMenu.addWidget(btnPlay)
        vboxMenu.addWidget(btnRules)
        vboxMenu.addWidget(btnSettings)
        vboxMenu.addWidget(btnQuit)
        vboxMenu.setAlignment(QtCore.Qt.AlignTop)
        return vboxMenu

    def createMenu(self, actions: List[MyAction]):
        vboxMenu = QVBoxLayout()
        vboxMenu.addStretch(1)

        for act in actions:
            vboxMenu.addWidget(
                self.MyMenuButton(act.name, act.action)
            )
        vboxMenu.setAlignment(QtCore.Qt.AlignTop)
        return vboxMenu

    class MyMenuButton(QPushButton):
        def __init__(self, name, action):
            QPushButton.__init__(self, name)
            self.setFixedWidth(btn_width)
            self.setText(name)
            self.clicked.connect(action)
