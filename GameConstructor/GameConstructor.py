from random import Random

import GameParams
from Game.QMWind_GameScene import QMWind_GameScene


class GameConstructor():

    def __init__(self,main_wind, action_back):
        self.main_wind = main_wind
        self.action_back = action_back

    def createGame(self, gameParams: GameParams) -> QMWind_GameScene:
        game_scene = QMWind_GameScene(self.main_wind,self.action_back,gameParams.sett_game_scene_width,gameParams.sett_game_scene_height)
        game_scene.initRectangles(
            gameParams.sett_game_scene_width,
            gameParams.sett_game_scene_height,
            gameParams.sett_rect_size,
            GameConstructor.get_random_colors(gameParams.sett_colors_palette),
            gameParams.sett_apply_labels
        )
        game_scene.initRectanglesLogic(
            gameParams.sett_rectangle_time_to_move,
            gameParams.sett_moving_paths
        )
        game_scene.initConditionsToWin(0)
        game_scene.initTimer()

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
