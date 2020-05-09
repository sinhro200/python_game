import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyWidget(QWidget):
    # кастомный сигнал
    loaded = pyqtSignal()  # from PyQt5.QtCore import pyqtSignal

    def __init__(self, parent):
        super(MyWidget, self).__init__()
        self.setParent(parent)
        self.setGeometry(30, 50, 160, 70)
        self.btn = QtWidgets.QPushButton("load", self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.load)

        self.progBar = QtWidgets.QProgressBar(self)
        self.progBar.setGeometry(10, 40, 150, 20)

        self.show()

    def load(self):
        for value in range(101):
            self.progBar.setValue(value)
        time.sleep(0.01)
        self.loaded.emit()