from PyQt5.QtGui import QColor


class GameParams():

    def __init__(self, colors_palette, moving_paths, apply_labels, apply_timer, remain_time, game_width, game_height, rect_size, rectangle_time_to_move):
        self.sett_colors_palette = colors_palette
        self.sett_moving_paths =moving_paths
        self.sett_apply_labels = apply_labels
        self.sett_apply_timer = apply_timer
        self.sett_remain_time = remain_time
        self.sett_game_scene_width = game_width
        self.sett_game_scene_height = game_height
        self.sett_rect_size = rect_size
        self.sett_rectangle_time_to_move = rectangle_time_to_move


class MovingPath():
    def __init__(self, clickable, movable):
        self.clickable = clickable
        self.movable = movable


class DefaultValues():

    @staticmethod
    def create():
        return GameParams(
            DefaultValues.default_colors_palette(),
            DefaultValues.default_paths(),
            DefaultValues.default_apply_labels(),
            DefaultValues.default_apply_timer(),
            DefaultValues.default_remain_time_msec(),
            DefaultValues.default_width(),
            DefaultValues.default_height(),
            DefaultValues.default_rect_size(),
            DefaultValues.default_rect_time_to_move_msec()
        )

    @staticmethod
    def default_colors_palette():
        return [
            QColor(50, 168, 82),  # green
            QColor(199, 22, 22),  # red
            QColor(22, 57, 199),  # blue
            QColor(215, 230, 9)  # yellow
        ]

    @staticmethod
    def default_paths():
        return [MovingPath([0, 1, 4], [0, 1, 5, 4]),
                MovingPath([2, 3, 7], [2, 3, 7, 6]),
                MovingPath([8, 12, 13], [8, 9, 13, 12]),
                MovingPath([11, 14, 15], [10, 11, 15, 14]),
                MovingPath([5, 6, 9, 10], [5, 6, 10, 9])
                ]

    @staticmethod
    def default_apply_labels():
        return False

    @staticmethod
    def default_apply_timer():
        return False

    @staticmethod
    def default_remain_time_msec():
        return 600000

    @staticmethod
    def default_width():
        return 800

    @staticmethod
    def default_height():
        return 800

    @staticmethod
    def default_rect_size():
        return 120

    @staticmethod
    def default_rect_time_to_move_msec():
        return 1000