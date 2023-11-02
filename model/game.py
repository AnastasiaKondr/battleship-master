from model.shoot_state_enum import ShootResult


class Game:
    def __init__(self, width, height, ships, ships_count):
        self.is_finished = False
        self.shoots = set()
        self.ships = ships
        self.ships_count = ships_count
        self.width = width
        self.height = height

    def try_shoot(self, cell):
        if cell.x < 0 or cell.x >= self.width or cell.y < 0 or cell.y >= self.height:
            return ShootResult.OUT_OF_BOUNDS

        if cell in self.shoots:
            return ShootResult.ALREADY_HIT
        self.shoots.add(cell)

        ship = self.ships.get(cell)
        if ship:
            ship.hp -= 1
            if ship.hp == 0:
                self.ships_count -= 1
            if self.ships_count == 0:
                self.is_finished = True

            return ShootResult.HIT

        return ShootResult.MISS
