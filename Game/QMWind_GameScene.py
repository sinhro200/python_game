from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPaintEvent, QColor
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QMenuBar, QAction, QLabel, QMessageBox

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
        self.gameTimer = None

    def onShow(self):
        self.main_win.setGeometry(
            QDesktopWidget().availableGeometry().center().x() - self.scene_width / 2,
            QDesktopWidget().availableGeometry().center().y() - self.scene_height / 2,
            self.scene_width, self.scene_height)

    def initRectangles(self, scene_width, scene_height, rect_size, colors, apply_labels):
        self.rects = RectangleFactory.createRectangles(
            self, scene_width, scene_height, rect_size, colors, apply_labels
        )

    def initTimer(self, pastTime=None):
        if pastTime == None:
            return
        self.timerLabel = QLabel(self)
        self.timerLabel.setFixedWidth(50)
        self.timerLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.timerLabel.move(self.scene_width - self.timerLabel.width() - 5, self.timerLabel.y() + 5)
        self.timerLabel.setStyleSheet("QWidget {font-size:20px; padding-left:10; background-color: #44000000}")
        self.layout().addWidget(self.timerLabel)
        self.gameTimer = QMWind_GameScene.GameTimer(self.timerLabel, pastTime)

    class GameTimer():
        deltaTimeMs = 1000

        def __init__(self, label: QLabel, pastTime):
            self.gameTimer = QTimer()
            self.label = label
            self.timeMs = pastTime
            self.updateText()

            self.gameTimer.timeout.connect(self.timerTick)
            self.gameTimer.start(self.deltaTimeMs)

        def timerTick(self):
            self.timeMs = self.timeMs + self.deltaTimeMs
            self.updateText()

        def updateText(self):
            self.label.setText(int(self.timeMs / 1000).__str__())

        def getTime(self):
            return self.timeMs

        # should use after @initRectangles

    def initRectanglesLogic(self, rect_time_to_move, movingPaths, conditions_to_win):
        animator = Animator(self.animations, rect_time_to_move)
        controller = RectangleController(
            self.rects,
            movingPaths,
            animator,
            conditions_to_win,
            self.action_win
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

    def mousePressEvent(self, e):
        self.mousePressed = True
        self.startX = e.x()
        self.startY = e.y()

    def action_save(self):
        pass

    def action_load(self):
        pass

    def action_win(self):
        self.qMessageBox = QMessageBox()
        self.qMessageBox.setText("Victory")
        if self.gameTimer != None:
            self.qMessageBox.setInformativeText("You won in " + (self.gameTimer.getTime() / 1000).__str__() + " sec")
        self.qMessageBox.setStandardButtons(QMessageBox.Ok)
        self.qMessageBox.buttonClicked.connect(self.action_quit)
        self.qMessageBox.exec()
