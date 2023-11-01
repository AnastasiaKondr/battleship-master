from controller import Controller
from model.game import Game
from ships_generator import generate
from view.app import BattleshipApp


def main():
    width = 10
    height = 10

    ships, ships_count = generate(width, height)
    computer_ships, computer_ships_count = generate(width, height)
    player_game = Game(width, height, ships, ships_count)
    computer_game = Game(width, height, computer_ships, computer_ships_count)
    controller = Controller(player_game, computer_game)
    BattleshipApp(player_game, computer_game, controller).run()


if __name__ == '__main__':
    main()
