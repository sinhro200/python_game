from PyQt5.QtGui import QColor


class GameParams():

    def __init__(self, colors_palette, moving_paths, conditions_to_win, apply_labels, apply_timer, game_width,
                 game_height,
                 rect_size, rectangle_time_to_move):
        self.sett_colors_palette = colors_palette
        self.sett_moving_paths = moving_paths
        self.conditions_to_win = conditions_to_win
        self.sett_apply_labels = apply_labels
        self.sett_apply_timer = apply_timer
        self.sett_game_scene_width = game_width
        self.sett_game_scene_height = game_height
        self.sett_rect_size = rect_size
        self.sett_rectangle_time_to_move = rectangle_time_to_move


class Restrictions():
    min_width = 1
    max_width = 1000
    min_height = 1
    max_height = 1000
    min_size = 1
    max_size = 200
    min_time_to_move = 1
    max_time_to_move = 1000000

    @staticmethod
    def check(gp: GameParams):
        return (
                Restrictions.checkWidth(gp.sett_game_scene_width) and
                Restrictions.checkHeight(gp.sett_game_scene_height) and
                Restrictions.checkSize(gp.sett_rect_size) and
                Restrictions.checkTimeToMove(gp.sett_rectangle_time_to_move)
        )

    @staticmethod
    def checkWidth(val):
        return Restrictions.applyToMinMax(
            val,
            Restrictions.min_width, Restrictions.max_width
        )

    @staticmethod
    def checkHeight(val):
        return Restrictions.applyToMinMax(
            val,
            Restrictions.min_height, Restrictions.max_height
        )

    @staticmethod
    def checkSize(val):
        return Restrictions.applyToMinMax(
            val,
            Restrictions.min_size, Restrictions.max_size
        )

    @staticmethod
    def checkTimeToMove(val):
        return Restrictions.applyToMinMax(
            val,
            Restrictions.min_time_to_move, Restrictions.max_time_to_move
        )

    @staticmethod
    def applyToMinMax(val_to_check, min, max):
        return val_to_check > min and val_to_check < max


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
            DefaultValues.default_conditions_to_win(),
            DefaultValues.default_apply_labels(),
            DefaultValues.default_apply_timer(),
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
    def default_conditions_to_win():
        return [
            [0, 1, 4, 5],
            [2, 3, 6, 7],
            [8, 9, 12, 13],
            [10, 11, 14, 15]
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
