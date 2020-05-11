from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QDesktopWidget, QVBoxLayout

from MyAction import MyAction
from MyButton import MyButton
from GameParams import GameParams


class QWid_SettingsScene(QWidget):
    scene_width = 300
    scene_height = 400

    def __init__(self, main_window: QMainWindow, actionBack: MyAction):
        super().__init__(main_window)
        self.scene = self.createSceneLayout(actionBack)
        self.setLayout(self.scene)
        self.main_win = main_window

    def createSceneLayout(self, actionBack: MyAction):
        vboxMenu = QVBoxLayout()
        vboxMenu.addStretch(1)
        vboxMenu.addWidget(MyButton(actionBack.name, actionBack.action))

        vboxMenu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        return vboxMenu

    def onShow(self, gameParams: GameParams):
        self.gameParams = gameParams
        self.main_win.setGeometry(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)

    def getChangedGameParams(self):
        return self.gameParams
