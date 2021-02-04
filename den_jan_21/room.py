# Implement a class to hold rooms_dict information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        # item will be a list and there will be a function to add items to the list
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
