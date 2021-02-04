class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __repr__(self):
        return f'{self.inventory}'

    def grab(self, item):
        self.inventory.append(item.name)
        print(f'\nYou now have the {item.name} in your inventory.')
        print(f'  * Your current inventory:\n    {self.inventory}')

    def rem_item(self, item):
        self.inventory.remove(item)
        print(f'  * {item} has been removed from your inventory.')
