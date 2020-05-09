import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QVBoxLayout, QWidget


btn_width = 170

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initializase_component()
        self.show()

    #ToDo alignment center for menu
    def initializase_component(self):
        self.setWindowTitle('Game')
        self.setGeometry(
            QDesktopWidget().availableGeometry().center().x(),
            QDesktopWidget().availableGeometry().center().y(),
            300,300)
        vboxMenu = self.createMenu()

        widget = QWidget()
        widget.setLayout(vboxMenu)
        self.setMenuWidget(widget)

    def createMenu(self):
        btnQuit = self.MyMenuButton("Quit", self.action_quit)
        btnSettings = self.MyMenuButton("Settings", self.action_settings)
        btnRules = self.MyMenuButton("Rules", self.action_rules)
        btnPlay = self.MyMenuButton("Play", self.action_play)

        vboxMenu = QVBoxLayout()
        vboxMenu.addStretch(1)
        vboxMenu.addWidget(btnPlay)
        vboxMenu.addWidget(btnRules)
        vboxMenu.addWidget(btnSettings)
        vboxMenu.addWidget(btnQuit)
        vboxMenu.setAlignment(Qt.AlignTop)
        return vboxMenu

    class MyMenuButton(QPushButton):
        def __init__(self,name,action):
            QPushButton.__init__(self,name)
            self.setFixedWidth(btn_width)
            self.setText(name)
            self.clicked.connect(action)

    def action_play(self):
        None

    def action_settings(self):
        None

    def action_rules(self):
        None

    def action_quit(self):
        self.close()


if (__name__=="__main__"):
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
