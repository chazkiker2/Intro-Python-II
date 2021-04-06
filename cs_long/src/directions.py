from enum import Enum, unique


@unique
class Direction(Enum):
    NORTH = 1,
    EAST = 2,
    SOUTH = 3,
    WEST = 4


if __name__ == '__main__':
    for member in Direction:
        print(member)
        print(dir(member))
        print(member.name)
        print(member.value)
