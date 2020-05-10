from PyQt5.QtGui import QPainter, QPaintEvent
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QMenuBar, QAction

from Game.Animation import Animator, AnimationCollection_clrColl
from Game.GamePrefs import GamePrefs
from Game.RectangleUtils import RectangleFactory, RectangleController
from MyAction import MyAction


class QMWind_GameScene(QMainWindow):
    scene_width = 800
    scene_height = 800
    rect_size = 120

    def __init__(self, main_window: QMainWindow, action_back: MyAction, gamePrefs: GamePrefs):
        super().__init__(main_window)
        self.action_quit = action_back.action
        self.animations = AnimationCollection_clrColl()
        self.createMenu()
        self.createBody(gamePrefs)
        self.main_win = main_window
        self.painter = QPainter(self)

    def onShow(self):
        self.main_win.setGeometry(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)

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

    def createBody(self,gamePrefs):
        # self.rects = RectangleFactory.createDefRectangles(
        #     self, self.scene_width, self.scene_height, self.rect_size
        # )
        self.rects = RectangleFactory.createRectangles(
            self, self.scene_width, self.scene_height, self.rect_size,gamePrefs.colors
        )
        animator = Animator(self.animations, 1000)
        controller = RectangleController(
            self.rects,
            gamePrefs.movingPaths,
            #[[0, 1, 5, 4], [2, 3, 7, 6], [8, 9, 13, 12], [10, 11, 15, 14]],
            animator
        )

    def mousePressEvent(self, e):
        self.mousePressed = True
        self.startX = e.x()
        self.startY = e.y()

    def drawRects(self):
        for rect in self.rects:
            rect.draw(self.painter, self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        pass
        # self.drawRects()

    def action_save(self):
        pass

    def action_load(self):
        pass

    def action_quit(self):
        pass
