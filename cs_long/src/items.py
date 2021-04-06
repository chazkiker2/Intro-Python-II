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

    def customize_format(self, indent=None, line_break=None, extra=None):
        if not indent:
            indent = ""
        if not line_break:
            line_break = ""
        if not extra:
            extra = ""
        else:
            extra = "\n" + extra

        return self._customize_format(indent, line_break, extra)

    def _customize_format(self, indent, line_break, extra):
        add_on = f"{indent * 2}{extra}" if extra != "" else ""
        # old end line {indent}--------------------------{line_break}
        return f"""
{indent}--------------------------
{indent}{self.name}: {self.description}{add_on}
{indent * 2}Weight: {self.weight}
{indent * 2}Value: {self.value}{line_break}"""


class Weapon(Item):
    """Base class for all Weapons"""

    def __init__(self, name, weight, value, description, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, weight, value, description)

    def __str__(self):
        extra = f"Damage: {self.damage}"
        return super().customize_format(extra=extra)


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

    def customize_format(self, indent=None, line_break=None, extra=None):
        indent = indent if indent else ""
        line_break = line_break if line_break else ""
        extra = extra if extra else ""
        extra_ = f"\n{indent * 2}Damage: {self.damage}{extra}"
        return super()._customize_format(
            indent=indent,
            line_break=line_break,
            extra=extra_
        )


class Coin(Item):
    def __init__(self, amount):
        super(Coin, self).__init__(
            name="Coin",
            weight=0,
            value=amount,
            description=f"A round token worth {amount}"
        )


# for testing
class Heavy(Item):
    def __init__(self, weight, name=None):
        name_to_use = name if name else "A heavy item"
        super().__init__(
            name=name_to_use,
            weight=weight,
            value=1,
            description=f"A {name_to_use} object that weights {weight}"
        )


# for testing
class SuperHeavy(Heavy):
    def __init__(self):
        super().__init__(
            weight=60,
            name="super_heavy"
        )


# for testing
class RatherHeavy(Heavy):
    def __init__(self):
        super().__init__(weight=35, name="rather_heavy")


# for testing
class SlightlyLessHeavy(Heavy):
    def __init__(self):
        super().__init__(weight=30, name="slightly_heavy")
