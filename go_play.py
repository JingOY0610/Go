from player import Player, RandomPlayer, GreedyPlayer, ManualPlayer, MyPlayer
from go import GO
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="size of board n*n")
    parser.add_argument("--player1", type=str, help="Player class. Options: manual, random, greedy, my", default='random')
    parser.add_argument("--player2", type=str, help="Player class. Options: manual, random, greedy, my", default='random')
    args = parser.parse_args()

    n = args.n
    players = [args.player1, args.player2]
    player_objs = []
    for player in players:
        if player.lower() == 'random': 
            player_objs.append(RandomPlayer())
        elif player.lower() == 'manual':
            player_objs.append(ManualPlayer())
        elif player.lower() == 'greedy':
            player_objs.append(GreedyPlayer())
        elif player.lower() == 'my':
            player_objs.append(MyPlayer())
        else:
            print('Wrong player type. Options: manual, random, greedy, my')
            sys.exit()

    player1, player2 = player_objs[0], player_objs[1]
    my_go = GO(n)
    result = my_go.play(player1, player2)
    print(result)