from PyQt5.QtGui import QColor

from Game.Rectangle import Rectangle


class RectangleFactory():
    def_color = QColor(556677)
    global field_size
    field_size = 4

    @staticmethod
    def createDefRectangles(scene_parent,scene_width,scene_height,rect_size):
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
                        QColor(556677)
                    )
                )