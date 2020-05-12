import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QDesktopWidget, QHBoxLayout, QVBoxLayout

from MyAction import MyAction
from GameParams import GameParams, Restrictions
from Settings import LayoutCreator


class QWid_SettingsScene(QWidget):
    scene_width = 600
    scene_left_width = 300
    scene_right_width = 300
    scene_height = 400

    def __init__(self, main_window: QMainWindow, actionBack: MyAction):
        super().__init__(main_window)
        self.scene = self.createSceneLayout()
        self.setLayout(self.scene)
        self.main_win = main_window
        self.actionBack = actionBack.action
        self.backValues = BackValues()

    def createSceneLayout(self):
        scene = QVBoxLayout()
        topLayout = QHBoxLayout()
        left_layout = LayoutCreator.MyVerticalLayout()

        self.widthModule = LayoutCreator.EditTextModule("width")
        self.heightModule = LayoutCreator.EditTextModule("height")
        self.sizeModule = LayoutCreator.EditTextModule("size")
        self.timeToMoveModule = LayoutCreator.EditTextModule("time to move")
        self.applyTimerModule = LayoutCreator.BooleanModule("apply timer")
        self.applyLabelsModule = LayoutCreator.BooleanModule("apply labels")
        self.colorsModule = LayoutCreator.ColorModule("Colors")

        self.buttonModule = LayoutCreator.ButtonModule(["back", "reset"], [self.onBack, self.reset])

        left_layout.addModule(self.widthModule)
        # left_layout.setAlignment(self.widthModule,Qt.AlignTop)
        left_layout.addModule(self.heightModule)
        left_layout.addModule(self.sizeModule)
        left_layout.addModule(self.timeToMoveModule)
        left_layout.addModule(self.applyTimerModule)
        left_layout.addModule(self.applyLabelsModule)
        left_layout.addModule(self.colorsModule)
        # left_layout.addModule(self.buttonModule)
        left_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.winPathsModule = None
        right_layout = LayoutCreator.MyVerticalLayout()

        right_layout.addLayout(LayoutCreator.EditTextModule("test2"))
        right_layout.addLayout(LayoutCreator.EditTextModule("test3"))
        self.right_layout = right_layout
        topLayout.addLayout(left_layout, 1)
        topLayout.addLayout(right_layout)
        scene.addLayout(topLayout)

        downLayout = QHBoxLayout()
        downLayout.addLayout(self.buttonModule)
        scene.addLayout(downLayout)

        # vboxMenu.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        return scene

    def getWidth(self, width):
        print(width)

    def onShow(self, gameParams: GameParams):
        if self.winPathsModule == None:
            self.winPathsModule = LayoutCreator.WinPathsModule("win conditions", gameParams.conditions_to_win)
            self.right_layout.addLayout(self.winPathsModule)
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
        self.winPathsModule.setValue(gameParams.conditions_to_win)

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
        self.backValues.winPaths(self.winPathsModule.getValue())

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

        defCount = 0
        for a in default_gp.conditions_to_win:
            for b in a:
                defCount = defCount+1
        set = []
        for wp in self._winPaths:
            for num in wp:
                int(num)
                if set.__contains__(num):
                    raise Exception()
                set.append(num)
        if len(set) != defCount:
            raise Exception()

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
        if self._winPaths != None:
            gp.conditions_to_win = self._winPaths

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

    def winPaths(self, val):
        print("win paths")
        for wp in val:
            print(wp.__str__())
        self._winPaths = val
