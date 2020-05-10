from PyQt5.QtCore import QPropertyAnimation, QPointF, QTimer

from Game.MyClearedCollection import MyClearedCollection
from Game.Rectangle import Rectangle


class AnimationCollection_clrColl(MyClearedCollection):

    def shouldDelete(self, elem: QPropertyAnimation):
        return elem.state() == QPropertyAnimation.Stopped


class Animator():

    def __init__(self, animations: AnimationCollection_clrColl, duration):
        self.duration = duration
        self.animations = animations

    def move(self, r1: Rectangle, r2: Rectangle):
        n1 = r1.num
        n2 = r2.num
        animation = QPropertyAnimation(r1, b"pos")
        animation.setDuration(self.duration)
        animation.setStartValue(QPointF(r1.pos[0], r1.pos[1]))
        animation.setEndValue(QPointF(r2.pos[0], r2.pos[1]))
        animation.setLoopCount(1)
        self.animations.append(animation)
        animation.start()
