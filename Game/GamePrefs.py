from random import Random

from PyQt5.QtGui import QColor

def_colors = [
    QColor(50, 168, 82),  # green
    QColor(199, 22, 22),  # red
    QColor(22, 57, 199),  # blue
    QColor(215, 230, 9)  # yellow
]


class GamePrefs():
    def __init__(self, movingPaths, colors):
        self.movingPaths = movingPaths
        self.colors = colors

    @staticmethod
    def get_default():
        return GamePrefs(
            [MovingPath([0, 1, 4], [0, 1, 5, 4]),
             MovingPath([2, 3, 7], [2, 3, 7, 6]),
             MovingPath([8, 12, 13], [8, 9, 13, 12]),
             MovingPath([11, 14, 15], [10, 11, 15, 14]),
             MovingPath([5, 6, 9, 10], [5, 6, 10, 9])
             ],
            GamePrefs.get_default_random_colors()
        )

    @staticmethod
    def get_default_random_colors():
        colors = []
        cnt = [0, 0, 0, 0]
        for i in range(16):
            while True:
                rnd = Random().randint(0, 3)
                if cnt[rnd] < 4:
                    cnt[rnd] += 1
                    colors.append(def_colors[rnd])
                    break
        return colors


class MovingPath():
    def __init__(self, clickable, movable):
        self.clickable = clickable
        self.movable = movable
