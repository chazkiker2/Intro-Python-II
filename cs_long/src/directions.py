from enum import Enum, unique


@unique
class Direction(Enum):
    NORTH = 1,
    EAST = 2,
    SOUTH = 3,
    WEST = 4
