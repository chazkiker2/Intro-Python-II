from typing import Dict, Optional
from item import Item


class Room:
    """Represents a Room that a player can exist in"""

    def __init__(self, name: str,
                 description: Optional[str] = None,
                 items: Optional[Dict[Item, int]] = None
                 ):
        self.name = name
        self.description = description if description is not None else "No description given!"
        self.items = items if items is not None else {}
        self.branches = {
            "north": None,
            "east": None,
            "south": None,
            "west": None,
        }

    def __repr__(self):
        return f"Room({self.name}, {self.description}, {self.items})"

    def __str__(self):
        n = self.branches["north"]
        e = self.branches["east"]
        s = self.branches["south"]
        w = self.branches["west"]
        n_name = n.name if n else "None"
        e_name = e.name if e else "None"
        s_name = s.name if s else "None"
        w_name = w.name if w else "None"

        items_desc = ", ".join([f"{item}" for item in self.items])

        return f"""
----------------------
Room: {self.name}
- Description: {self.description}
- Items: [{items_desc}]
- Branches: 
    north={n_name}, 
    east={e_name}, 
    south={s_name}
    west={w_name}
"""

    # def add_item(self, item: Item):
    #     if item not in self.items:
    #         self.items[item] = 0
    #     self.items[item] += 1
    #
    # def remove_item(self, item: Item):
    #     if item not in self.items:
    #         return
    #     self.items[item] -= 1
    #     if self.items[item] == 0:
    #         del self.items[item]

    def create_branch_map(self,
                          north: Optional["Room"] = None,
                          east: Optional["Room"] = None,
                          south: Optional["Room"] = None,
                          west: Optional["Room"] = None,
                          ):
        self.branches["north"] = north
        self.branches["east"] = east
        self.branches["south"] = south
        self.branches["west"] = west
