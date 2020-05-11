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
        r1.in_animation = True
        animation = QPropertyAnimation(r1, b"pos")
        animation.setDuration(self.duration)
        animation.setStartValue(QPointF(r1.x(), r1.y()))
        animation.setEndValue(QPointF(r2.x(), r2.y()))
        animation.setLoopCount(1)
        self.animations.append(animation)
        animation.start()
