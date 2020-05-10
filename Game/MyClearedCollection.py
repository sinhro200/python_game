from PyQt5.QtCore import QTimer


class MyClearedCollection():

    def __init__(self):
        self.collection = []
        self.checkingInterval = 2000
        self.startCheckingTimer()

    def append(self, val):
        self.collection.append(val)

    def __len__(self):
        return len(self.collection)

    def shouldDelete(self, elem):
        pass

    def startCheckingTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkAndDelete)
        self.timer.start(self.checkingInterval)

    def checkAndDelete(self):
        for elem in self.collection:
            if self.shouldDelete(elem):
                self.collection.remove(elem)