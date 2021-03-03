# Implement a class to hold rooms_dict information.
# This should have name and description attributes.

from item import Item


class Room:
    def __init__(self, name, description, inventory = []):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
        return f'{self.inventory}'

    def add_item(self, item):
        self.inventory.append(item.name)

    def remove_item(self, item):
        self.inventory.remove(item)