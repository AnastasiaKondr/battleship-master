class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Cell(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Cell(self.x * other, self.y * other)

    def __repr__(self):
        return f'{self.x} {self.y}'
