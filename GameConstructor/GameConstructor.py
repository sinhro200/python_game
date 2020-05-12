from random import Random

import GameParams
from Game.QMWind_GameScene import QMWind_GameScene


class GameConstructor():

    def __init__(self, main_wind, action_back):
        self.main_wind = main_wind
        self.action_back = action_back

    def createGame(self, gameParams: GameParams) -> QMWind_GameScene:
        game_scene = QMWind_GameScene(self.main_wind, self.action_back, gameParams.sett_game_scene_width,
                                      gameParams.sett_game_scene_height)
        game_scene.initRectangles(
            gameParams.sett_game_scene_width,
            gameParams.sett_game_scene_height,
            gameParams.sett_rect_size,
            GameConstructor.get_win_colors(gameParams.sett_colors_palette),
            # GameConstructor.get_random_colors(gameParams.sett_colors_palette),
            gameParams.sett_apply_labels
        )
        game_scene.initRectanglesLogic(
            gameParams.sett_rectangle_time_to_move,
            gameParams.sett_moving_paths,
            gameParams.conditions_to_win
        )
        if gameParams.sett_apply_timer:
            game_scene.initTimer(0)

        return game_scene

    @staticmethod
    def get_random_colors(colors_palette):
        colors = []
        cnt = [0, 0, 0, 0]
        for i in range(16):
            while True:
                rnd = Random().randint(0, 3)
                if cnt[rnd] < 4:
                    cnt[rnd] += 1
                    colors.append(colors_palette[rnd])
                    break
        return colors

    @staticmethod
    def get_win_colors(colors_palette):
        colors = []
        cnt = [0, 0, 0, 0]
        GameConstructor.construct_colors(
            colors,
            colors_palette,
            [0, 0, 1, 1,
             0, 1, 3, 1,
             2, 0, 2, 3,
             2, 2, 3, 3]
        )
        return colors

    @staticmethod
    def construct_colors(colors, colors_palette, list):
        for i in list:
            colors.append(colors_palette[i])
