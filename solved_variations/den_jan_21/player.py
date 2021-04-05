# Write a class to hold player information, e.g. what rooms_dict they are in
# currently.
class Player:
    def __init__(self, name, location, inventory=None):
        self.name = name
        self.location = location
        self.inventory = []
        # items is also a list

    def add(self, item):
        self.inventory.append(item)
