class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return f"A wild {self.name} has appeared..."

    def on_hit_taken(self, damage):
        self.hp -= damage
        if self.is_alive():
            print(f"{self.name} still has {self.hp} left")
        else:
            print(f"You've killed {self.name}")

    def is_alive(self):
        return self.hp > 0
