class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.s_to = None
        self.n_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"Room(name={self.name}, description={self.description}"
