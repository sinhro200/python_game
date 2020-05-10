from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor, QPaintDevice, QPalette
from PyQt5.QtWidgets import QPushButton


class Rectangle(QPushButton):

    def __init__(self,parent,num, pos, size, color: QColor):
        super().__init__(parent)
        self.num = num
        print(num)
        self.size = size
        self.color = color
        self.pos = pos
        self.setFixedSize(size, size)
        self.move(pos[0],pos[1])
        self.setColor(color)
        self.pressed.connect(self.onClick)

    def draw(self, painter: QPainter,qpd : QPaintDevice):
        painter.begin(qpd)
        painter.setBrush(self.color)
        painter.drawRect(QRectF(
            self.pos[0], self.pos[1],
            self.size, self.size
        ))
        painter.end()

    def onClick(self):
        print(self.num)

    def setColor(self,color):
        palette = self.palette()
        palette.setColor(QPalette.Button, color)
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.update()
