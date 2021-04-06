import rooms
import items
from directions import Direction

NORTH, EAST, SOUTH, WEST = Direction


class Maze:
    def __init__(self):
        self.maze = {}

    def get(self, coords):
        return self.maze.get(coords)

    def seed(self):
        self.maze.clear()
        room_outside = rooms.Room(
            name="Outside Cave Entrance",
            description="North of you, the cave mount beckons",
            items=[items.Sword(), items.SuperHeavy(), items.RatherHeavy(), items.SlightlyLessHeavy()]
        )
        room_foyer = rooms.Room(
            name="Foyer",
            description="""Dim light filters in from the south. Dusty passages run north and east."""
        )
        room_overlook = rooms.Room(
            name="Grand Overlook",
            description="A steep cliff appears before you, falling into the darkness. Ahead to the north, "
                        "a light flickers in the distance, but there is no way across the chasm."
        )
        room_narrow = rooms.Room(
            name="Narrow Passage",
            description="The narrow passage bends here from west to north. The smell of gold permeates the air."
        )
        room_treasure = rooms.Room(
            name="Treasure Chamber",
            description="You've found the long-lost treasure chamber! Sadly, it has already been completely "
                        "emptied by earlier adventurers. The only exit is to the south."
        )

        """
        Overlook     Treasure
          |            |
        Foyer  ---   Narrow
          |
        CaveEntrance 
        """

        room_outside.branches.update({
            NORTH: room_foyer,
        })
        room_foyer.branches.update({
            NORTH: room_overlook,
            EAST: room_narrow,
            SOUTH: room_outside
        })
        room_overlook.branches.update({
            SOUTH: room_foyer
        })
        room_narrow.branches.update({
            NORTH: room_treasure,
            WEST: room_foyer,
        })
        room_treasure.branches.update({
            SOUTH: room_narrow,
        })

        self.maze = {
            (0, 0): room_outside,
            (0, -1): room_foyer,
            (0, -2): room_overlook,
            (1, -1): room_narrow,
            (1, -2): room_treasure
        }
