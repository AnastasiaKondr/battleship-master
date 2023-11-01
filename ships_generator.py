import datetime
import random

from model.cell import Cell
from model.ship import Ship


def has_neighbour(cell, ships):
    result = False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            neighbour = Cell(cell.x + dx, cell.y + dy)
            result = neighbour in ships
            if result:
                break
        if result:
            break

    return result


def generate_ship(deck, width, height, ships_count, ships):
    ship = Ship(deck + 1)
    ship_cells = set()
    start_time = datetime.datetime.now()

    while True:
        if (datetime.datetime.now() - start_time).seconds > 2:
            raise ValueError("can't generate ships, size is too small")

        ship_cells.clear()
        horizontal = random.choice([True, False])

        pos = Cell(random.randrange(0, width - ship.size), random.randrange(0, height))
        if not horizontal:
            pos = Cell(random.randrange(0, width), random.randrange(0, height - ship.size))

        coords_delta = Cell(1, 0) if horizontal else Cell(0, 1)

        break_ship_building = False
        for j in range(ship.size):
            cell = pos + coords_delta * j
            break_ship_building = has_neighbour(cell, ships)

            if break_ship_building:
                break

            ship_cells.add(cell)

        if break_ship_building:
            continue

        ships_count += 1
        for cell in ship_cells:
            ships[cell] = ship

        break
    return ships_count


def generate(width, height):
    ships = {}
    ships_count = 0
    # random.seed()

    for deck in range(4):
        for i in range(4 - deck):
            ships_count = generate_ship(deck, width, height, ships_count, ships)

    return ships, ships_count
