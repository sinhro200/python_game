import copy

from PyQt5.QtWidgets import QWidget, QMainWindow, QDesktopWidget

from MyAction import MyAction
from GameParams import GameParams, Restrictions
from Settings import LayoutCreator


class QWid_SettingsScene(QWidget):
    scene_width = 300
    scene_height = 400

    def __init__(self, main_window: QMainWindow, actionBack: MyAction):
        super().__init__(main_window)
        self.scene = self.createSceneLayout()
        self.setLayout(self.scene)
        self.main_win = main_window
        self.actionBack = actionBack.action
        self.backValues = BackValues()

    def createSceneLayout(self):
        scene = LayoutCreator.Scene()

        self.widthModule = LayoutCreator.EditTextModule("width")
        self.heightModule = LayoutCreator.EditTextModule("height")
        self.sizeModule = LayoutCreator.EditTextModule("size")
        self.timeToMoveModule = LayoutCreator.EditTextModule("time to move")
        self.applyTimerModule = LayoutCreator.BooleanModule("apply timer")
        self.applyLabelsModule = LayoutCreator.BooleanModule("apply labels")
        self.colorsModule = LayoutCreator.ColorModule("Colors")

        self.buttonModule = LayoutCreator.ButtonModule(["back", "reset"], [self.onBack, self.reset])

        scene.addLayout(self.widthModule)
        scene.addLayout(self.heightModule)
        scene.addLayout(self.sizeModule)
        scene.addLayout(self.timeToMoveModule)
        scene.addLayout(self.applyTimerModule)
        scene.addLayout(self.applyLabelsModule)
        scene.addLayout(self.colorsModule)

        scene.addLayout(self.buttonModule)

        print(self.widthModule.getValue())

        # vboxMenu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        return scene

    def getWidth(self, width):
        print(width)

    def onShow(self, gameParams: GameParams):
        self.setGameParams(gameParams)
        self.main_win.setGeometry(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)

    def setGameParams(self, gameParams: GameParams):
        self._gameParams = gameParams
        self.gameParams = gameParams
        self.heightModule.setValue(gameParams.sett_game_scene_height)
        self.widthModule.setValue(gameParams.sett_game_scene_width)
        self.sizeModule.setValue(gameParams.sett_rect_size)
        self.timeToMoveModule.setValue(gameParams.sett_rectangle_time_to_move)
        self.applyLabelsModule.setValue(gameParams.sett_apply_labels)
        self.applyTimerModule.setValue(gameParams.sett_apply_timer)
        self.colorsModule.setValue(gameParams.sett_colors_palette)

    def getChangedGameParams(self):
        return self.gameParams

    def onBack(self):
        self.backValues.width(self.widthModule.getValue())
        self.backValues.height(self.heightModule.getValue())
        self.backValues.size(self.sizeModule.getValue())
        self.backValues.applyTimer(self.applyTimerModule.getValue())
        self.backValues.applyLabels(self.applyLabelsModule.getValue())
        self.backValues.timeToMove(self.timeToMoveModule.getValue())
        self.backValues.colors_palette(self.colorsModule.getValue())

        try:
            self.gameParams = self.backValues.convertToGameParams(self._gameParams)
            self.actionBack()
        except:
            pass

    def reset(self):
        self.setGameParams(self._gameParams)


class BackValues():
    def __init__(self):
        self._width = None
        self._height = None
        self._size = None
        self._timeToMove = None
        self._applyTimer = None
        self._colorsPalette = None
        self._applyLabels = None

    def convertToGameParams(self, default_gp) -> GameParams:
        # gp = CopyGameParams(default_gp)
        width = float(self._width)
        height = float(self._height)
        size = float(self._size)
        time_to_move = int(self._timeToMove)
        apply_timer = bool(self._applyTimer)
        apply_labels = bool(self._applyLabels)

        gp = copy.deepcopy(default_gp)
        if self._width != None:
            gp.sett_game_scene_width = width
        if self._height != None:
            gp.sett_game_scene_height = height
        if self._size != None:
            gp.sett_rect_size = size
        if self._timeToMove != None:
            gp.sett_rectangle_time_to_move = time_to_move
        if self._applyTimer != None:
            gp.sett_apply_timer = apply_timer
        if self._applyLabels != None:
            gp.sett_apply_labels = apply_labels
        if self._colorsPalette != None:
            gp.sett_colors_palette = self._colorsPalette

        if not Restrictions.check(gp):
            raise Exception()

        return gp

    def width(self, val):
        print("width " + val)
        self._width = val

    def height(self, val):
        print("height " + val)
        self._height = val

    def size(self, val):
        print("size " + val)
        self._size = val

    def timeToMove(self, val):
        print("time to move " + val)
        self._timeToMove = val

    def applyTimer(self, val):
        print("apply timer " + val.__str__())
        self._applyTimer = val

    def applyLabels(self, val):
        print("apply labels " + val.__str__())
        self._applyLabels = val

    def colors_palette(self, val):
        print("colors :")
        for c in val:
            print(c.__str__())
        self._colorsPalette = val
