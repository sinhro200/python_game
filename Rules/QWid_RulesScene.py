from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QPushButton, QLabel

from MyAction import MyAction

class QWid_RulesScene(QWidget):
    global btn_width
    btn_width = 200
    scene_width = 400
    scene_height = 400
    #ToDO relative path
    # Now it doesnt work, IDK why
    RULES_FILE_NAME = 'PycharmProjects/6_game/Rules/rules.html'

    def __init__(self, main_window: QMainWindow, actionBack: MyAction):
        super().__init__(main_window)
        self.scene = self.createSceneLayout(actionBack)
        self.setLayout(self.scene)
        self.main_win = main_window

    def onShow(self):
        self.main_win.setGeometry(QRect(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)
        )

    def createSceneLayout(self, act_back: MyAction):
        btnBack = QPushButton(act_back.name)
        btnBack.clicked.connect(act_back.action)
        btnBack.setFixedWidth(btn_width)

        text = self.readRulesFromFile()
        label = QLabel(text)
        label.setStyleSheet("QWidget {color: black; background-color: white; font-size: 18px}")
        label.setWordWrap(True)
        label.setMaximumWidth(self.scene_width)
        # label.setGeometry(50, 30, 120, 100)

        vboxScene = QVBoxLayout()
        vboxScene.addStretch(1)
        vboxScene.addWidget(label)
        vboxScene.addWidget(btnBack)
        vboxScene.setAlignment(Qt.AlignHCenter)
        return vboxScene

    def readRulesFromFile(self) -> str:
        with open(self.RULES_FILE_NAME,"r") as file:
            return file.read()

