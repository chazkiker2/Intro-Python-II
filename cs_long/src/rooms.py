import maze
import actions


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def greet(self):
        raise NotImplementedError()

    def on_player_enter(self, a_player):
        raise NotImplementedError()

    def available_directions(self):
        moves = []
        x, y = self.x, self.y
        if maze.get_location_if_valid(x, y - 1):
            moves.append(actions.MoveNorth())
        if maze.get_location_if_valid(x, y + 1):
            moves.append(actions.MoveSouth())
        if maze.get_location_if_valid(x + 1, y):
            moves.append(actions.MoveEast())
        if maze.get_location_if_valid(x - 1, y):
            moves.append(actions.MoveWest())
        return moves

    def available_actions(self):
        moves = self.available_directions()
        moves.append(actions.Exit())
        moves.append(actions.ViewInventory())
        return moves


class Room(Location):
    def __init__(self, x, y, name, description):
        super(Room, self).__init__(x, y)
        self.string_rep = f"""
You've entered {name}...
{description}
"""

    def greet(self):
        print(self.string_rep)

    def on_player_enter(self, a_player):
        pass


class ItemRoom(Location):
    def __init__(self, x, y, name, description=None, items=None):
        self.items = items if items else []
        super(ItemRoom, self).__init__(x, y)
        extra_str = f"\n{description}\n" if description else ""
        items_list = "\t" + "\t".join(item.customize_format(indent="\t") for item in self.items)
        self.string_rep = f"""
You have entered {name}...{extra_str}
Looks like there are some items!{items_list}
"""

    def __str__(self):
        return self.string_rep

    def greet(self):
        print(self.string_rep)

    def on_player_enter(self, a_player):
        pass

    def available_actions(self):
        return super(ItemRoom, self).available_actions() + [actions.TakeItem(item) for item in self.items]
