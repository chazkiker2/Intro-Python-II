from collections import Counter

import actions
from directions import Direction

NORTH, EAST, SOUTH, WEST = Direction


class Location:
    def __init__(self, items=None):
        self.branches = {
            NORTH: None,
            EAST: None,
            SOUTH: None,
            WEST: None,
        }

        if isinstance(items, dict):
            self.items = items
        else:
            try:
                self.items = Counter(list(items))
            except TypeError:
                self.items = {}

    def on_item_taken(self, item):
        self.items[item] -= 1
        if not self.items[item]:
            del self.items[item]

    def on_item_dropped(self, item, count=1):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += count

    def greet(self):
        raise NotImplementedError()

    def on_player_enter(self, a_player):
        raise NotImplementedError()

    def get_adjacent_rooms(self):
        return [
            actions.directionActions[cardinal_direction]()
            for cardinal_direction, branch in self.branches.items()
            if branch
        ]

    def available_actions(self):
        moves = self.get_adjacent_rooms() + [actions.Exit(), actions.ViewInventory()]
        if self.items:
            moves += [actions.TakeItem(item) for item in self.items]
        return moves


class Room(Location):
    def __init__(self, name, description=None, items=None):
        super(Room, self).__init__(items=items)
        self.name = name
        self.description = description if description else "No description given"

    def __str__(self):
        str_rep = f"You've entered {self.name}\n" \
                  f"{self.description}"
        if self.items:
            str_rep += "\n\tLooks like there are some items!"
            str_rep += "\t" + "\t".join(item.customize_format(indent="\t") for item in self.items)
        return str_rep

    def greet(self):
        print(self)

    def on_player_enter(self, a_player):
        pass

    def __repr__(self):
        return f"Room({self.name})"
