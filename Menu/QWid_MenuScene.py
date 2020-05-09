from typing import List

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QVBoxLayout, QPushButton

from MyAction import MyAction


class QWid_MenuScene(QWidget):
    global btn_width
    btn_width = 170
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
        vboxMenu.addStretch(1)

        for act in actions:
            vboxMenu.addWidget(
                self.MyMenuButton(act.name, act.action)
            )
        vboxMenu.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        return vboxMenu

    class MyMenuButton(QPushButton):
        def __init__(self, name, action):
            QPushButton.__init__(self, name)
            self.setFixedWidth(btn_width)
            self.setText(name)
            self.clicked.connect(action)
