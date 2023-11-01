from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label



class GameView(Widget):
    player_field = ObjectProperty(None)
    enemy_field = ObjectProperty(None)

    def __init__(self, player_game, computer_game, controller, **kwargs):
        super(GameView, self).__init__(**kwargs)
        self.player_field.init(player_game, controller, False)
        self.enemy_field.init(computer_game, controller, True)

    def update(self, dt):
        self.player_field.update()
        self.enemy_field.update()
        #lbl = Label(pos=(self.pos[0] + 50,self.pos[1] + 50), text="12345", color="red" )
        #lbl.ids =
