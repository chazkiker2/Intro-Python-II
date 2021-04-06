from random import choice
from typing import List
from directions import Direction
import actions
import items
import utils


class Player:
    def __init__(self, location):
        self.location = location
        self.hp = 100
        self.equipped_weapon = items.Fists()
        self.inventory = {
            items.Coin(20): 1,
        }
        self.capacity = 50
        self.has_won = False
        self.max_capacity = 50

    def __str__(self):
        formatted_items = "\n\t".join(str(item) for item in self.inventory) if self.inventory else "No items!"
        return f"""
        Player-------------------
            HP: {self.hp}
            
            Capacity: {self.capacity}
            
            Equipped Weapon: {self.equipped_weapon}
            
            Location: {self.location.name}
            
            Inventory:
                {formatted_items}
        """

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        items_list = "\t" + "\t".join(item.customize_format(indent="\t") for item in self.inventory)

        string_repr = f"""
Capacity: {self.capacity} lbs
Inventory: {items_list}
"""
        print(string_repr)

    def _move_to(self, direction):
        """internally used to move from this room to a separate branch"""
        to_travel = self.location.branches[direction]
        if to_travel:
            self.location = to_travel
            self.location.greet()
        else:
            # we shouldn't ever get here, but just in case
            print("Whoops! That's a wall")

    def move_north(self):
        self._move_to(Direction.NORTH)

    def move_south(self):
        self._move_to(Direction.SOUTH)

    def move_east(self):
        self._move_to(Direction.EAST)

    def move_west(self):
        self._move_to(Direction.WEST)

    def equip_weapon(self, weapon_name):
        for item in self.inventory:
            if isinstance(item, items.Weapon) and item.name.includes(weapon_name):
                self.equipped_weapon = item

    def drop_item(self, item):
        """drops an item from player inventory into current location"""
        self.capacity += item.weight
        self.inventory[item] -= 1
        if not self.inventory[item]:
            del self.inventory[item]

        self.location.on_item_dropped(item)

    def _drop_item(self, item):
        still_dropping = True

        def stop_dropping():
            """used as side-effect to allow user to cancel this process"""
            nonlocal still_dropping
            still_dropping = False

        while item.weight > self.capacity and still_dropping:
            name_weight_list = "\n\t" + "\n\t".join(
                f"item name: {item.name} --- weight: {item.weight}" for item in self.inventory)
            print(name_weight_list)

            drop_title_prompt = "type 'drop item_name' to drop the item with the given name " \
                                "(i.e., 'drop sword' would drop the sword)"

            drop_actions: List[actions.Action] = [actions.MultiWordAction(
                method=self.drop_item,
                name="Drop Item",
                expected_input=f"drop {item.name}",
                item=item
            ) for item in self.inventory]

            drop_actions.append(actions.SideEffect(
                side_effect=stop_dropping,
                name="Stop Dropping",
                valid_input=["stop", "stop dropping"]
            ))

            utils.prompt_and_respond(
                player=self,
                available_actions=drop_actions,
                title_prompt=drop_title_prompt
            )

    def _swap_equipped_weapon(self, weapon):
        equip_prompt = f"""
        Looks like you've picked up a weapon! 
        Would you like to equip {weapon.name} as your new weapon?

        Current weapon: {self.equipped_weapon}
        New weapon: {weapon}
        """
        will_equip = utils.yes_or_no(equip_prompt)
        if will_equip:
            print(f"Swapping out {self.equipped_weapon.name} for {weapon.name}")
            self.equipped_weapon = weapon
        else:
            print(
                f"Fair enough! We'll keep {self.equipped_weapon.name} and just toss your"
                f" new weapon in your inventory"
            )

    def take_item(self, item):
        # it the item is too heavy for our player no matter what
        # we'll skip the "drop some items" phase
        if item.weight > self.max_capacity:
            print(
                f"Sorry! {item.name} is too heavy for you to hold (even if you didn't have anything else)!"
                f"Maybe you should go get stronger so you can hold more than {self.max_capacity} pounds"
            )
            return  # return out, we don't want to pick this up

        # otherwise, it the item is too heavy given what the player currently has,
        # we'll give them the opportunity to drop some of their other items
        # in case they would prefer to keep what they just picked up
        elif item.weight > self.capacity:
            print(
                f"{item.name} weighs {item.weight} lbs. but you only have {self.capacity} lbs of weight left"
                f"... you'll have to drop some stuff if you really want this"
            )

            will_drop = utils.yes_or_no(
                "Would you like to drop something in your inventory? "
                "\n(Y) to choose what to drop (N) to forget this item."
            )

            if not will_drop:
                print(f"Fair enough! We'll leave {item.name} right where you found it")
                return  # return out, we don't want to pick this up
            else:
                self._drop_item(item)

        self.location.on_item_taken(item)
        self.capacity -= item.weight
        if item not in self.inventory:
            self.inventory[item] = 0

        self.inventory[item] += 1

        # if the item itself is a weapon, maybe they want to swap their equipped weapon out
        if isinstance(item, items.Weapon):
            self._swap_equipped_weapon(item)

    def attack(self, enemy):
        print(f"You hit {enemy.name} with {self.equipped_weapon.name}")
        enemy.hp -= self.equipped_weapon.damage
        if not enemy.is_alive():
            print(f"You killed {enemy.name}!")
        else:
            print(f"{enemy.name} HP is {enemy.hp}.")

    def run(self):
        self.do_action(choice(self.location.get_adjacent_rooms()))

    @staticmethod
    def exit_game():
        exit()
