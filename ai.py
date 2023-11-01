import random

from model.cell import Cell


def get_random_shoot(game):
    while True:
        shoot = Cell(random.randrange(0, game.width), random.randrange(0, game.height))
        if shoot in game.shoots:
            continue

        return shoot
