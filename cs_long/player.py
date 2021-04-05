from random import choice

from utils import yes_or_no
import maze
import items


class Player:
    def __init__(self):
        self.inventory = [items.Coin(20)]
        self.hp = 100
        self.x_coordinate, self.y_coordinate = maze.starting_coordinates
        self.victory = False
        self.equipped_weapon = items.Fists()
        self.capacity = 50

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.x_coordinate += dx
        self.y_coordinate += dy
        maze.get_location_if_valid(self.x_coordinate, self.y_coordinate).greet()

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def equip_weapon(self, weapon_name):
        for item in self.inventory:
            if isinstance(item, items.Weapon) and item.name.includes(weapon_name):
                self.equipped_weapon = item

    def take_item(self, item):
        if item.weight > self.capacity:
            print(f"{item.name} is too heavy for you... you'll have to drop some stuff if you really want this")
            will_drop = yes_or_no("Would you like to drop something in your inventory? "
                                  "\n(Y) to choose what to drop (N) to forget this item.")
            if will_drop:
                name_weight_list = "\n\t".join(f"Item name: {item.name} --- weight: {item.weight}")


        if isinstance(item, items.Weapon):
            equip_prompt = f"""
Looks like you've picked up a weapon! 
Would you like to equip {item.name} as your new weapon?

Current weapon: {self.equipped_weapon}
New weapon: {item}
"""
            will_equip = yes_or_no(equip_prompt)
            if will_equip:
                print(f"Swapping out {self.equipped_weapon.name} for {item.name}")
                self.equipped_weapon = item

    def attack(self, enemy):
        print(f"You use {self.equipped_weapon.name} against {enemy.name}!")
        enemy.hp -= self.equipped_weapon.damage
        if not enemy.is_alive():
            print(f"You killed {enemy.name}!")
        else:
            print(f"{enemy.name} HP is {enemy.hp}.")

    def flee(self, room):
        """Moves the player randomly to an adjacent room"""

        available_moves = room.adjacent_moves()
        chosen_action = choice(available_moves)
        self.do_action(chosen_action)

    @staticmethod
    def exit_game():
        exit()
