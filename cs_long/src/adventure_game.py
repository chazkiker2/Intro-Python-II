import maze
from player import Player
from utils import prompt_and_respond


def play():
    maze.seed()
    player = Player()
    room = maze.get_location_if_valid(player.x_coordinate, player.y_coordinate)
    room.greet()
    while player.is_alive() and not player.has_won:
        room = maze.get_location_if_valid(player.x_coordinate, player.y_coordinate)
        room.on_player_enter(player)
        if player.is_alive() and not player.has_won:
            prompt_and_respond(player=player, available_actions=room.available_actions())


if __name__ == '__main__':
    play()
