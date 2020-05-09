from PyQt5.QtWidgets import QPushButton

btn_width = 170
class MyButton(QPushButton):

    def __init__(self, name, action):
        QPushButton.__init__(self, name)
        self.setFixedWidth(btn_width)
        self.setText(name)
        self.clicked.connect(action)