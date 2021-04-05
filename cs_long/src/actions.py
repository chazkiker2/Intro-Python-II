from player import Player


class Action:
    """The base class for all simple available_actions"""

    def __init__(self, method, name, valid_input=None, **kwargs):
        """Creates a new action

        :param method: the function object to execute
        :param name: the name of the action
        :param valid_input: The input that the player should use to initiate this action
        """

        self.method = method
        self.valid_input = valid_input if valid_input else []
        self.name = name
        self.kwargs = kwargs

    def __repr__(self):
        return f"Action({self.method.__name__}, {self.name}, {self.valid_input}, {self.kwargs})"

    def __str__(self):
        return f"{self.valid_input[0]}: {self.name}"

    def match_input(self, user_input):
        return user_input in self.valid_input


class MultiWordAction(Action):
    def __init__(self, method, name, expected_input, **kwargs):
        self.expected_input = expected_input
        super().__init__(method=method, name=name, valid_input=[expected_input], **kwargs)

    def __str__(self):
        return f"{self.expected_input}"

    def match_input(self, user_input):
        return user_input.lower().strip() == self.expected_input


class SideEffect(Action):
    def __init__(self, side_effect, name, valid_input, **kwargs):
        self.side_effect = side_effect
        super().__init__(method=None, name=name, valid_input=valid_input, **kwargs)

    def __str__(self):
        return f"{self.side_effect.__name__}"

    def invoke(self):
        self.side_effect(**self.kwargs)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', valid_input=["n", "north"])


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', valid_input=["s", "south"])


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', valid_input=["e", "east"])


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', valid_input=["w", "west"])


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', valid_input=["i", "inventory", "inv"])


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
        super().__init__(method=Player.attack, name="Attack", valid_input=["a", "attack"], enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", valid_input=["f", "flee", "fuck"], tile=tile)


class Exit(Action):
    def __init__(self):
        super().__init__(method=Player.exit_game, name="Exit/Quit", valid_input=["x", "exit", "q", "quit"])
