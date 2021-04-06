from maze import Maze
from player import Player
from utils import prompt_and_respond


def main():
    maze = Maze()
    maze.seed()
    player = Player(maze.get((0, 0)))
    player.location.greet()
    while player.is_alive() and not player.has_won:
        room = player.location
        room.on_player_enter(player)
        if player.is_alive() and not player.has_won:
            prompt_and_respond(player=player, available_actions=room.available_actions())


if __name__ == '__main__':
    main()
