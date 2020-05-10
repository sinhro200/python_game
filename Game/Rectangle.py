from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor, QPaintDevice, QPalette
from PyQt5.QtWidgets import QPushButton


class ClickHandler():
    def __init__(self, on_click):
        self._onClick = on_click
        self.isEnable = True

    def onClick(self, num):
        if self.isEnable:
            self._onClick(num)

    def setClickable(self, isEnable):
        self.isEnable = isEnable


class Rectangle(QPushButton):

    def __init__(self, parent, _num, pos, size, color: QColor):
        super().__init__(parent)
        self._num = _num
        self.setText(_num.__str__())
        self.size = size
        self.color = color
        self.pos = pos
        self.setFixedSize(size, size)
        self.move(pos[0], pos[1])
        self.setColor(color)
        self.clickHandler = None
        self.pressed.connect(self.onClick)

    num=property()

    @num.setter
    def num(self,val):
        self._num=val
        self.setText(self._num.__str__())
        self.update()
        self.updateGeometry()

    @num.getter
    def num(self):
        return self._num


    def draw(self, painter: QPainter, qpd: QPaintDevice):
        painter.begin(qpd)
        painter.setBrush(self.color)
        painter.drawRect(QRectF(
            self.pos[0], self.pos[1],
            self.size, self.size
        ))
        painter.end()

    def onClick(self):
        self.clickHandler.onClick(self._num)

    def setColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.Button, color)
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.update()
