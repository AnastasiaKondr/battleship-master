from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder

from ai import get_random_shoot
from view.field import Field

from view.game_view import GameView

Window.size = (1300, 550)

Builder.load_file('./view/design.kv')


class BattleshipApp(App):
    def __init__(self, player_game, computer_game, controller, **kwargs):
        super(BattleshipApp, self).__init__(**kwargs)
        self.__player_game = player_game
        self.__computer_game = computer_game
        self.__game_view = GameView(self.__player_game, self.__computer_game, controller)

    def build(self):
        Clock.schedule_interval(self.__game_view.update, 1.0/60.0)
        return self.__game_view


