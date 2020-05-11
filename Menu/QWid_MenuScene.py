from typing import List

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QVBoxLayout, QPushButton, QHBoxLayout

from MyAction import MyAction
from MyButton import MyButton


class QWid_MenuScene(QWidget):
    scene_width = 300
    scene_height = 300

    def __init__(self, main_window: QMainWindow, actions: List[MyAction]):
        super().__init__(main_window)
        self.scene = self.createMenu(actions)
        self.setLayout(self.scene)
        self.main_win = main_window

    def onShow(self):
        self.main_win.setGeometry(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)

    def createMenu(self, actions: List[MyAction]):
        vboxMenu = QVBoxLayout()
        vboxMenu.setContentsMargins(5, 40, 5, 0)

        for act in actions:
            vboxMenu.addWidget(
                MyButton(act.name, act.action)
            )
        vboxMenu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        vboxMenu.setSpacing(10)
        return vboxMenu
