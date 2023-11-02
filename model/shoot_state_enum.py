from enum import Enum


class ShootResult(Enum):
    OUT_OF_BOUNDS = 1,
    HIT = 2,
    MISS = 3,
    ALREADY_HIT = 4
