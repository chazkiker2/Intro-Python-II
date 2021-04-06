import actions


class Location:
    def __init__(self, maze, coords):
        self.maze = maze
        self.coords = coords

    def greet(self):
        raise NotImplementedError()

    def on_player_enter(self, a_player):
        raise NotImplementedError()

    def available_actions(self):
        moves = self.maze.get_adjacent_rooms(self.coords)
        moves.append(actions.Exit())
        moves.append(actions.ViewInventory())
        return moves


class Room(Location):
    def __init__(self, maze, coords, name, description):
        super(Room, self).__init__(maze, coords)
        self.string_rep = f"""
You've entered {name}...
{description}
"""

    def greet(self):
        print(self.string_rep)

    def on_player_enter(self, a_player):
        pass


class ItemRoom(Location):
    def __init__(self, maze, coords, name, description=None, items=None):
        super(ItemRoom, self).__init__(maze, coords)
        self.items = items if items else []
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
