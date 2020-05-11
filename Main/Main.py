import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

import GameParams
from GameConstructor.GameConstructor import GameConstructor
from MyAction import MyAction
from Menu.QWid_MenuScene import QWid_MenuScene
from Rules.QWid_RulesScene import QWid_RulesScene
from Settings.QWid_SettingsScene import QWid_SettingsScene


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.gameConstructor = GameConstructor(self, MyAction("Back", self.action_quit_from_game))
        self.gameParams = GameParams.DefaultValues.create()

        self.initializase_components()
        self.state_menu()
        self.show()

    def initializase_components(self):
        self.stckWidg_scene = QStackedWidget()
        self.setCentralWidget(self.stckWidg_scene)

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
        self.settingsScene = QWid_SettingsScene(self, MyAction("Back", self.action_quit_from_settings))
        self.gameScene = self.createGameScene()

        self.stckWidg_scene.addWidget(self.gameScene)
        self.stckWidg_scene.addWidget(self.settingsScene)
        self.stckWidg_scene.addWidget(self.menuScene)
        self.stckWidg_scene.addWidget(self.rulesScene)

    def createGameScene(self):
        return self.gameConstructor.createGame(self.gameParams)
        #return QMWind_GameScene(self, MyAction("Back", self.action_quit_from_game), self.gamePrefs)


    def action_play(self):
        self.state_game()

    def action_settings(self):
        self.state_settings()

    def action_rules(self):
        self.state_rules()

    def action_quit(self):
        self.close()

    def action_quit_from_game(self):
        self.state_menu()
        self.stckWidg_scene.removeWidget(self.gameScene)

    def action_quit_from_settings(self):
        self.gameParams = self.settingsScene.getChangedGameParams()
        self.state_menu()

    def state_game(self):
        self.gameScene = self.createGameScene()
        self.stckWidg_scene.addWidget(self.gameScene)
        self.gameScene.onShow()
        self.stckWidg_scene.setCurrentWidget(self.gameScene)

    def state_menu(self):
        self.menuScene.onShow()
        self.stckWidg_scene.setCurrentWidget(self.menuScene)

    def state_rules(self):
        self.rulesScene.onShow()
        self.stckWidg_scene.setCurrentWidget(self.rulesScene)

    def state_settings(self):
        self.settingsScene.onShow(self.gameParams)
        self.stckWidg_scene.setCurrentWidget(self.settingsScene)


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
