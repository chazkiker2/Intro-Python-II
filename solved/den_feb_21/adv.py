# from rooms_dict import Room
from player import Player
from room import Room

# from item import Item

# Declare all the rooms
room = {
    'outside': Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons"
    ),
    'foyer': Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east."""
    ),
    'overlook': Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. 
        Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
    ),
    'narrow': Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    ),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['pole']),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' rooms_dict.
name = input("Welcome to the game! What is your name?")
player = Player(name, room['outside'])

# Write a loop that:
direction = None
cur_room = None

print("You must go find the treasure because of reasons!")
input("Press any key to begin: ")

# While game is playing
while direction != "q":
    # If player has not moved
    if cur_room == player.location:
        # Current rooms_dict stays stable
        cur_room = cur_room
    else:
        # Current rooms_dict updates to players new location
        cur_room = player.location

    # Print player name & location
    print(f"{player.name} is in {player.location.name}")

    # * Prints the current rooms_dict name
    print(f"{player.location.name}")
    # * Prints the current description (the textwrap module might be useful here).
    print(f"{player.location.description}")

    # Print items in the rooms_dict
    if player.location.item:
        print(f"{player.location.item}")

    # * Waits for user input and decides what to do.
    direction = input("What do you do? (n, s, e, w, (a)ction: ")

    # If the user enters a cardinal direction, attempt to move to the rooms_dict there.
    if direction.lower() in ["n", "s", "e", "w", "q", "a"]:
        if direction == "n":
            # Update current rooms_dict to northern rooms_dict
            cur_room = cur_room.n_to
        elif direction == "s":
            # Update current rooms_dict to southern rooms_dict
            cur_room = cur_room.s_to
        elif direction == "e":
            # Update current rooms_dict to eastern rooms_dict
            cur_room = cur_room.e_to
        elif direction == "w":
            # Update current rooms_dict to western rooms_dict
            cur_room = cur_room.w_to
        elif direction == "a":
            action = input("What would you like to do? (s)earch (i)nventory (b)ack")
            if action.lower() == "s" and player.location.item:
                item = cur_room.item
                print(f"{player.name} sees {item.name}")
                decide = input(f"Do you want {item.name}? (y)/(n)? ")
                if decide.lower() == "y":
                    player.inventory.append(item.name)
                elif decide.lower() == "n":
                    print("You don't want that.")
            elif action == "s" and player.location.item in player.inventory:
                print("There is nothing to see here")

            if action.lower() == "i":
                print(f"{player.inventory}")
        elif direction == "q":
            quit()

        # If current rooms_dict has None, print a message
        if cur_room is None:
            print(f"There is nowhere for {player.name} to go.")
        elif cur_room == player.location:
            # If current rooms_dict has not updated, print a message
            print("Think about your next move...")
        else:
            # If current rooms_dict available to update, update rooms_dict and move on
            print(f"{player.name} moves with vigor to {cur_room.name}")
            player.location = cur_room

    # Print an error message if the movement isn't allowed.
    else:
        print("Direction Not Valid")

#
# If the user enters "q", quit the game.
