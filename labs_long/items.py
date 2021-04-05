"""Contains all of the items that exist this adventure game"""


class Item:
    """Base class for all Items"""
    def __init__(self,
                 name,
                 weight,
                 value,
                 description=None,
                 ):
        self.name = name
        self.weight = weight
        self.value = value
        self.description = description if description is not None else "No description given!"

    def __repr__(self):
        return f"Item({self.name}, {self.weight}, {self.value}, {self.description})"

    def __str__(self):
        return self.customize_format()

    def customize_format(self, extra=None):
        add_on = f"\n{extra}" if extra else ""
        return f"""
{self.name}
-------------
{self.description}{add_on}
Weight: {self.weight}
Value: {self.value}
"""


class Weapon(Item):
    """Base class for all Weapons"""

    def __init__(self, name, weight, value, description, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, weight, value, description)

    def __str__(self):
        return self.customize_format(f"Damage: {self.damage}")


class Fists(Weapon):
    def __init__(self):
        super(Fists, self).__init__(
            name="Fists",
            weight=0,
            value=0,
            damage=2,
            description="Good ole haymakers... they're not much, but they'll do"
        )


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(
            name="Sword",
            weight=10,
            value=12,
            damage=10,
            description="A hefty weapon that will make for some comfortable monster-killing"
        )


class Coin(Item):
    def __init__(self, amount):
        super(Coin, self).__init__(
            name="Coin",
            weight=0,
            value=amount,
            description=f"A round token worth {amount}"
        )
