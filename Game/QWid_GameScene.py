from typing import List

from PyQt5.QtCore import QPropertyAnimation, QRectF, QRect, Qt, QPointF
from PyQt5.QtGui import QPainter, QPaintEvent, QColor, QPalette
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QVBoxLayout, QPushButton, QMenuBar, QAction, qApp, \
    QLayout, QHBoxLayout

from Game.Rectangle import Rectangle
from MyAction import MyAction
from MyButton import MyButton


class QWid_GameScene(QWidget):
    scene_width = 800
    scene_height = 800

    def __init__(self, main_window: QMainWindow, action_back: MyAction):
        super().__init__(main_window)
        self.action_quit = action_back.action
        self.createMenu()
        self.createBody()
        self.main_win = main_window
        self.painter = QPainter(self)
        self.initRects()

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

    def createBody(self):
        layout = QHBoxLayout(self)
        rect_but = QPushButton()
        rect_but.setFixedSize(50,50)
        palette = rect_but.palette()
        palette.setColor(QPalette.Button,QColor(102030))
        rect_but.setAutoFillBackground(True)
        rect_but.setPalette(palette)
        rect_but.update()
        self.rect_but = rect_but
        layout.addWidget(rect_but,1,Qt.AlignHCenter)
        self.setLayout(layout)

    def initRects(self):
        self.rects = []
        for i in range(4):
            for j in range(4):

                self.rects.append(
                    Rectangle(
                        [(float)((i%4)*100+50),(float)((j%4)*100+50)],
                        50.0,
                        QColor(556677)
                    )
                )

    def mousePressEvent(self, e):
        self.mousePressed = True
        self.startX = e.x()
        self.startY = e.y()

        animation = QPropertyAnimation(self.rect_but, b"geometry");
        animation.setDuration(4000);
        animation.setStartValue(QRectF(200, 200, 100, 0));
        animation.setEndValue(QRectF(600, 600, 100, 300));
        animation.setLoopCount(-1)
        self.animation = animation
        self.animation.start();
        # self.animation = QPropertyAnimation(
        #     self.rect_but,
        #     b"geometry",
        #     duration=4000,
        #     startValue=QRectF(0, 0,50,200),
        #     endValue=QRectF(500, 10,50,200),
        #     loopCount=-1,
        # )
        # self.animation.start()


    def drawRects(self):
        for rect in self.rects:
            rect.draw(self.painter,self)


    def paintEvent(self, a0: QPaintEvent) -> None:
        self.drawRects()

    def action_save(self):
        pass

    def action_load(self):
        pass

    def action_quit(self):
        pass
