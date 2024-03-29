from player import Player, RandomPlayer, GreedyPlayer, ManualPlayer, MyPlayer
from go import GO
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", "-n", type=int, help="size of board n*n", default=5)
    parser.add_argument("--player1", "-p1", type=str, help="Black player. Options: manual, random, greedy, my", default='random')
    parser.add_argument("--player2", "-p2", type=str, help="White player. Options: manual, random, greedy, my", default='random')
    parser.add_argument("--times", "-t", type=int, help="playing times.", default=1)
    args = parser.parse_args()

    n = args.size
    times = args.times
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

    black_wins = white_wins = 0
    for time in range(times):
        player1, player2 = player_objs[0], player_objs[1]
        my_go = GO(n)
        result = my_go.play(player1, player2)
        if result == 1: black_wins += 1
        elif result == 2: white_wins += 1
    print()
    print('Black player (X) | Wins:{0:.1f}% Loses:{1:.1f}%'.format(100*black_wins/times, 100*white_wins/times))
    print('White player (O) | Wins:{0:.1f}% Loses:{1:.1f}%'.format(100*white_wins/times, 100*black_wins/times))
    print()