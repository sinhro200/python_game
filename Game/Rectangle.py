from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor, QPaintDevice, QPalette
from PyQt5.QtWidgets import QPushButton


class ClickHandler():
    def __init__(self, on_click):
        self.onClick = on_click

    def onClick(self, num):
        self.onClick(num)


class Rectangle(QPushButton):

    def __init__(self, parent, num, pos, size, color: QColor):
        super().__init__(parent)
        self.num = num
        print(num)
        self.size = size
        self.color = color
        self.pos = pos
        self.setFixedSize(size, size)
        self.move(pos[0], pos[1])
        self.setColor(color)
        self._clickHandler = None
        self.pressed.connect(self.onClick)

    clickHandler = property()

    @clickHandler.setter
    def clickHandler(self, click_handler):
        self._clickHandler = click_handler

    def draw(self, painter: QPainter, qpd: QPaintDevice):
        painter.begin(qpd)
        painter.setBrush(self.color)
        painter.drawRect(QRectF(
            self.pos[0], self.pos[1],
            self.size, self.size
        ))
        painter.end()

    def onClick(self):
        self._clickHandler.onClick(self.num)

    def setColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.Button, color)
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.update()
