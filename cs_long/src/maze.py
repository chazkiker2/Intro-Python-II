import rooms
import items
import actions

"""
Overlook     Treasure
  |            |
Foyer  ---  Narrow
  |
CaveEntrance 
"""


class Maze:
    def __init__(self):
        self.maze = {}
        self.starting_coords = (0, 0)

    def get_room_at(self, coords):
        return self.maze.get(coords)

    def get_location_if_exists(self, x, y):
        return self.maze.get((x, y))

    def get_adjacent_rooms(self, coords):
        x, y = coords
        moves = []
        if self.get_room_at((x, y - 1)):
            moves.append(actions.MoveNorth())
        if self.get_room_at((x, y + 1)):
            moves.append(actions.MoveSouth())
        if self.get_room_at((x + 1, y)):
            moves.append(actions.MoveEast())
        if self.get_room_at((x - 1, y)):
            moves.append(actions.MoveWest())
        return moves

    def seed(self):
        self.maze.clear()
        self.maze = {
            (0, 0): rooms.ItemRoom(
                maze=self,
                coords=(0, 0),
                name="Outside Cave Entrance",
                description="North of you, the cave mount beckons",
                items=[items.Sword(), items.SuperHeavy(), items.RatherHeavy(), items.SlightlyLessHeavy()]
            ),
            (0, -1): rooms.Room(
                maze=self,
                coords=(0, 1),
                name="Foyer",
                description="""Dim light filters in from the south. Dusty passages run north and east."""
            ),
            (0, -2): rooms.Room(
                maze=self,
                coords=(0, -2),
                name="Grand Overlook",
                description="A steep cliff appears before you, falling into the darkness. Ahead to the north, "
                            "a light flickers in the distance, but there is no way across the chasm."
            ),
            (1, -1): rooms.Room(
                maze=self,
                coords=(1, -1),
                name="Narrow Passage",
                description="The narrow passage bends here from west to north. The smell of gold permeates the air."
            ),
            (1, -2): rooms.Room(
                maze=self,
                coords=(1, -2),
                name="Treasure Chamber",
                description="You've found the long-lost treasure chamber! Sadly, it has already been completely "
                            "emptied by earlier adventurers. The only exit is to the south."
            ),
        }
