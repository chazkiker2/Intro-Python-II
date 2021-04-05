import rooms
import items

"""
Overlook    Treasure
   |          |
 Foyer ---  Narrow
   |
CaveEntrance 
"""

# will contain K,V pairs where each key is a (x,y) coordinate and each value is a Room instance
_maze = {}
# start our player off at double zip
starting_coordinates = (0, 0)


def get_location_if_valid(x, y):
    return _maze.get((x, y))


def seed():
    global _maze
    _maze.clear()
    _maze = {
        (0, 0): rooms.ItemRoom(
            x=0,
            y=0,
            name="Outside Cave Entrance",
            description="North of you, the cave mount beckons",
            items=[items.Sword(), items.SuperHeavy(), items.RatherHeavy(), items.SlightlyLessHeavy()]
        ),
        (0, -1): rooms.Room(
            x=0,
            y=-1,
            name="Foyer",
            description="""Dim light filters in from the south. Dusty passages run north and east."""
        ),
        (0, -2): rooms.Room(0, -2, "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
        (1, -1): rooms.Room(1, -1, "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
        (1, -2): rooms.Room(1, -2, "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    }
