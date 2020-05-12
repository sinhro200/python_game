from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QMenuBar, QAction

from Game.Animation import Animator, AnimationCollection_clrColl
from Game.RectangleUtils import RectangleFactory, RectangleController
from MyAction import MyAction


class QMWind_GameScene(QMainWindow):

    def __init__(self, main_window: QMainWindow, action_back: MyAction, width, height):
        super().__init__(main_window)
        self.action_quit = action_back.action
        self.animations = AnimationCollection_clrColl()
        self.createMenu()
        self.main_win = main_window
        self.scene_width = width
        self.scene_height = height
        # self.painter = QPainter(self)

    def onShow(self):
        self.main_win.setGeometry(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)

    def initRectangles(self, scene_width, scene_height, rect_size, colors, apply_labels):
        self.rects = RectangleFactory.createRectangles(
            self, scene_width, scene_height, rect_size, colors, apply_labels
        )

    def initTimer(self, pastTime=0):
        pass

    def initConditionsToWin(self, win_conditions):
        pass

    # should use after @initRectangles
    def initRectanglesLogic(self, rect_time_to_move, movingPaths):
        animator = Animator(self.animations, rect_time_to_move)
        controller = RectangleController(
            self.rects,
            movingPaths,
            animator
        )

    def createMenu(self):
        mainMenu = QMenuBar(self)
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')

        quitAction = QAction('Save', self)
        quitAction.setShortcut("Ctrl+S")
        quitAction.triggered.connect(self.action_save)
        fileMenu.addAction(quitAction)

        quitAction = QAction('Load', self)
        quitAction.setShortcut("Ctrl+L")
        quitAction.triggered.connect(self.action_load)
        fileMenu.addAction(quitAction)

        quitAction = QAction('Quit', self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.triggered.connect(self.action_quit)
        fileMenu.addAction(quitAction)

    # def createBody(self, gameParams: GameParams):
    # self.rects = RectangleFactory.createDefRectangles(
    #     self, self.scene_width, self.scene_height, self.rect_size
    # )

    def mousePressEvent(self, e):
        self.mousePressed = True
        self.startX = e.x()
        self.startY = e.y()

    # def drawRects(self):
    #     for rect in self.rects:
    #         rect.draw(self.painter, self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        pass
        # self.drawRects()

    def action_save(self):
        pass

    def action_load(self):
        pass

    def action_quit(self):
        pass
