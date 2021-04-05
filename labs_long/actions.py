from player import Player


class Action:
    """The base class for all simple actions"""

    def __init__(self, method, name, hotkeys=None, **kwargs):
        """Creates a new action

        :param method: the function object to execute
        :param name: the name of the action
        :param hotkey: The keyboard key the player should use to initiate this action
        """

        self.method = method
        self.hotkeys = hotkeys if hotkeys else []
        self.name = name
        self.kwargs = kwargs

    def __repr__(self):
        return f"Action({self.method.__name__}, {self.name}, {self.hotkeys}, {self.kwargs})"

    def __str__(self):
        return f"{self.hotkeys[0]}: {self.name}"

    def match_input(self, user_input):
        return user_input in self.hotkeys


class MultiWordAction(Action):
    def __init__(self, method, name, expected_input, **kwargs):
        self.expected_input = expected_input
        super().__init__(method=method, name=name, **kwargs)

    def __str__(self):
        return f"{self.expected_input}: {self.name}"

    def match_input(self, user_input):
        return user_input.lower().strip() == self.expected_input


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkeys=["n", "north"])


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkeys=["s", "south"])


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkeys=["e", "east"])


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkeys=["w", "west"])


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkeys=["i", "inventory", "inv"])


class EquipWeapon(MultiWordAction):
    def __init__(self, weapon):
        super().__init__(
            method=Player.equip_weapon,
            name="Equip Weapon",
            expected_input=f"equip {weapon.name.lower()}",
            weapon=weapon
        )


class TakeItem(MultiWordAction):
    def __init__(self, item):
        super().__init__(
            method=Player.take_item,
            name="Take Item with the given name",
            expected_input=f"take {item.name.lower()}",
            item=item
        )


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey=["a", "attack"], enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkeys=["f", "flee", "fuck"], tile=tile)


class Exit(Action):
    def __init__(self):
        super().__init__(method=Player.exit_game, name="Save and Exit", hotkeys=["x", "exit", "q", "quit"])
