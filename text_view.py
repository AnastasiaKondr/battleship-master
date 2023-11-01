from model.cell import Cell


def update_view(width, height, self_game, enemy_game):
    if self_game.is_finished:
        print('Game over.')
        return
    if enemy_game.is_finished:
        print('You win!')
        return

    print('You:')
    draw_game(width, height, self_game)
    print('Enemy:')
    draw_game(width, height, enemy_game, is_enemy=True)


def draw_game(width, height, game, is_enemy=False):
    print('  abcdefghij')
    for y in range(height):
        print(y, end=' ')
        for x in range(width):
            cell = Cell(x, y)
            already_shoot = cell in game.shoots

            ship = game.ships.get(cell)
            if ship:
                s = 'X' if already_shoot else 'S'
                if is_enemy and s == 'S':
                    s = '#'
                print(s, end='')
                continue
            
            s = '*' if already_shoot else '#'
            print(s, end='')

        print()
