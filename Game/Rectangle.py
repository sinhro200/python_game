from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor, QPaintDevice


class Rectangle():

    def __init__(self, pos, size, color: QColor):
        self.size = size
        self.color = color
        self.pos = pos

    def draw(self, painter: QPainter,qpd : QPaintDevice):
        painter.begin(qpd)
        painter.setBrush(self.color)
        painter.drawRect(QRectF(
            self.pos[0], self.pos[1],
            self.size, self.size
        ))
        painter.end()
