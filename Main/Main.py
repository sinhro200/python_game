import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

from Game.GamePrefs import GamePrefs
from Game.QMWind_GameScene import QMWind_GameScene
from MyAction import MyAction
from Menu.QWid_MenuScene import QWid_MenuScene
from Rules.QWid_RulesScene import QWid_RulesScene
from Settings.QWid_SettingsScene import QWid_SettingsScene


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initializase_components()

        self.state_menu()
        self.show()

    def initializase_components(self):
        self.qStWid_scene = QStackedWidget()
        self.setCentralWidget(self.qStWid_scene)

        self.menuScene = QWid_MenuScene(
            self,
            [
                MyAction("Play", self.action_play),
                MyAction("Rules", self.action_rules),
                MyAction("Settings", self.action_settings),
                MyAction("Quit", self.action_quit)
            ]
        )
        self.rulesScene = QWid_RulesScene(self, MyAction("Back", self.state_menu))
        self.settingsScene = QWid_SettingsScene(self, MyAction("Back", self.state_menu))
        self.gameScene = QMWind_GameScene(self, MyAction("Back", self.state_menu),GamePrefs.get_default())

        self.qStWid_scene.addWidget(self.gameScene)
        self.qStWid_scene.addWidget(self.settingsScene)
        self.qStWid_scene.addWidget(self.menuScene)
        self.qStWid_scene.addWidget(self.rulesScene)

    def action_play(self):
        self.state_game()

    def action_settings(self):
        self.state_settings()

    def action_rules(self):
        self.state_rules()

    def action_quit(self):
        self.close()

    def state_game(self):
        self.gameScene.onShow()
        self.qStWid_scene.setCurrentWidget(self.gameScene)

    def state_menu(self):
        self.menuScene.onShow()
        self.qStWid_scene.setCurrentWidget(self.menuScene)

    def state_rules(self):
        self.rulesScene.onShow()
        self.qStWid_scene.setCurrentWidget(self.rulesScene)

    def state_settings(self):
        self.settingsScene.onShow()
        self.qStWid_scene.setCurrentWidget(self.settingsScene)


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
