from kivy.graphics import Rectangle, Color, Line
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

from model.cell import Cell


class Field(Widget):
    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        print(self)

        self.__game = None
        self.cell_size = 50
        self.__set_computer_game = None
        self.__is_enemy = None
        self.__controller = None

    def init(self, game, controller, is_enemy):
        self.__game = game
        self.width = self.__game.width * self.cell_size
        self.height = self.__game.height * self.cell_size
        self.__is_enemy = is_enemy
        self.__controller = controller

    def update(self):
        with self.canvas:
            self.fill()
            self.draw_grid()

        if self.__game.is_finished:
            popup = Popup(title='Battleship',
                          content=Label(text='Game over!'))
            popup.open()

    def fill(self):
        self.canvas.clear()

        for x in range(self.__game.width):
            for y in range(self.__game.height):
                cell = Cell(x, y)

                if cell in self.__game.ships and not self.__is_enemy:
                    Color(1, 1, 0, 1)
                else:
                    Color(0, 1, 1, 1)

                if cell in self.__game.shoots:
                    if cell in self.__game.ships:
                        Color(1, 0, 0, 1)
                    else:
                        Color(0, 1, 0, 1)

                Rectangle(pos=(self.pos[0] + x * self.cell_size, self.pos[1] + y * self.cell_size),
                          size=(self.cell_size, self.cell_size))



    def draw_grid(self):
        Color(0, 0, 0, 1)
        for i in range(1, self.__game.width):
            y = self.pos[1] + i * self.cell_size
            Line(points=[(self.pos[0], y), (self.pos[0] + self.width, y)], width=0.25)

        for i in range(1, self.__game.height):
            x = self.pos[0] + i * self.cell_size
            Line(points=[(x, self.pos[1]), (x, self.pos[1] + self.height)], width=0.25)

    def on_touch_down(self, touch):
        if not self.__is_enemy:
            return

        x = (touch.pos[0] - self.pos[0]) // self.cell_size
        y = (touch.pos[1] - self.pos[1]) // self.cell_size
        cell = Cell(x, y)
        if 0 <= x < self.__game.width and 0 <= y < self.__game.height:
            self.__controller.shoot(cell)
