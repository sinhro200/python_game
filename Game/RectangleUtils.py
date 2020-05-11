from typing import List

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor

from Game.MyClearedCollection import MyClearedCollection
from Game.Rectangle import Rectangle, ClickHandler
from GameParams import MovingPath


class RectangleController():

    def __init__(self, rects: List[Rectangle], movingPaths: List[MovingPath], animator):
        self.rects = rects
        self.movingPaths = movingPaths
        self.animator = animator
        self.timeoutActions = RectangleController.TimeoutActions_clrColl()
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
        for r in rects:
            if r.in_animation:
                return
        prev = rects[0]
        first_num = prev.num
        for cur in rects[1:]:
            cur.clickHandler.setClickable(False)
            self.swapRects(prev, cur)
            prev.num = cur.num
            prev = cur
        self.swapRects(prev, rects[0])
        prev.num = first_num

    def swapRects(self, r1: Rectangle, r2: Rectangle):
        self.animator.move(r1, r2)

        timeoutAction = RectangleController.AfterTimeoutAction(r1, r2)
        timeoutAction.run(self.animator.duration)
        self.timeoutActions.append(timeoutAction)

    def getCorrectPath(self, num):
        for path in self.movingPaths:
            if path.clickable.__contains__(num):
                return path.movable

    class AfterTimeoutAction():
        def __init__(self, r1: Rectangle, r2: Rectangle):
            self.setRects(r1, r2)
            self.timer = QTimer()
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.action)

        def run(self, time):
            self.timer.start(time * 1.1)

        def setRects(self, r1: Rectangle, r2: Rectangle):
            self.r1 = r1
            self.r2 = r2

        def action(self):
            self.r1.in_animation = False
            self.r2.in_animation = False
            self.r1.clickHandler.setClickable(True)

    class TimeoutActions_clrColl(MyClearedCollection):
        def shouldDelete(self, elem):
            elem.timer.remainingTime() <= 0


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
    def createRectangles(scene_parent, scene_width, scene_height, rect_size, colors_by_nums):
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
                    colors_by_nums[j + i * field_size]
                )
                rects.append(r)
        return rects
