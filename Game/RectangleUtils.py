from typing import List

from PyQt5.QtCore import QPropertyAnimation, QPointF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QAction

from Game.GamePrefs import GamePrefs
from Game.Rectangle import Rectangle, ClickHandler


class Animator():

    def __init__(self, parent:QMainWindow, duration):
        self.duration = duration
        self.parent = parent

    def move(self, r1: Rectangle, r2: Rectangle):
        animation = QPropertyAnimation(r1, b"pos")
        # animation.setPropertyName(b"pos")
        animation.setDuration(self.duration)
        animation.setStartValue(QPointF(r1.pos[0], r1.pos[1]))
        animation.setEndValue(QPointF(r2.pos[0], r2.pos[1]))
        animation.setLoopCount(1)
        self.parent.animation = animation
        animation.start()


class RectangleController():

    def __init__(self, rects: List[Rectangle], movingPaths: List[List[int]], animator):
        self.rects = rects
        self.movingPaths = movingPaths
        self.animator = animator
        for r in rects:
            r.clickHandler = ClickHandler(self.onRectPressed)

    def onRectPressed(self, num):
        path = self.getCorrectPath(num)
        rects = []
        for i_in_path in path:
            for rect in self.rects:
                if rect.num == i_in_path:
                    rects.append(rect)
                    break
        prev = rects[0]
        for i in range(len(rects)):
            cur = rects[i]
            self.animator.move(prev, cur)
            prev = cur
        self.animator.move(prev, rects[0])


    def getCorrectPath(self, num):
        for path in self.movingPaths:
            if path.__contains__(num):
                return path


class RectangleFactory():
    global def_color
    def_color = QColor(556677)
    global field_size
    field_size = 4

    @staticmethod
    def createDefRectangles(scene_parent, scene_width, scene_height, rect_size):
        rects = []
        leftRight_padding = (scene_width - 4 * rect_size - 3 * rect_size / 2) / 2
        topDown_padding = (scene_height - 4 * rect_size - 3 * rect_size / 2) / 2
        for i in range(field_size):
            for j in range(field_size):
                rects.append(
                    Rectangle(
                        scene_parent,
                        j + i * field_size,
                        [
                            (float)((j % field_size) * rect_size + j * rect_size / 2 + leftRight_padding),
                            (float)((i % field_size) * rect_size + i * rect_size / 2 + topDown_padding)
                        ],
                        rect_size,
                        def_color
                    )
                )
        return rects

    @staticmethod
    def createRectangles(scene_parent, scene_width, scene_height, rect_size, gamePrefs: GamePrefs):
        rects = []
        leftRight_padding = (scene_width - 4 * rect_size - 3 * rect_size / 2) / 2
        topDown_padding = (scene_height - 4 * rect_size - 3 * rect_size / 2) / 2
        for i in range(field_size):
            for j in range(field_size):
                r = Rectangle(
                    scene_parent,
                    j + i * field_size,
                    [
                        (float)((j % field_size) * rect_size + j * rect_size / 2 + leftRight_padding),
                        (float)((i % field_size) * rect_size + i * rect_size / 2 + topDown_padding)
                    ],
                    rect_size,
                    gamePrefs.colors[j + i * field_size]
                )
                rects.append(r)
        return rects
