from ai import get_random_shoot
from model.shoot_state_enum import ShootResult


class Controller:
    def __init__(self, player_game, ai_game):
        self.__player_game = player_game
        self.__ai_game = ai_game

    def shoot(self, cell):
        if self.__ai_game.try_shoot(cell) == ShootResult.MISS:
            while True:
                shoot = get_random_shoot(self.__player_game)
                shoot_result = self.__player_game.try_shoot(shoot)
                if shoot_result == ShootResult.MISS:
                    break
