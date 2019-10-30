import random
import sys

class Player:
    def __init__(self):
        self.type = None
        self.input_hint = False

    def get_input(self, go, piece_type, previous_died_pieces):
        pass

class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'random'

    def get_input(self, go, piece_type, previous_died_pieces):
        '''
        Get one input.

        :param go: Go instance.
        :param piece_type: 1('X') or 2('O').
        :param previous_died_pieces: the locations of previous died pieces.
        :return: (row, column) coordinate of input.
        '''        
        possible_placements = []
        for i in range(go.size):
            for j in range(go.size):
                if go.valid_place_check(i, j, piece_type, previous_died_pieces, test_check = True):
                    possible_placements.append((i,j))
        return random.choice(possible_placements)        
        
class ManualPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'manual'
        self.input_hint = True

    def get_input(self, go, piece_type, previous_died_pieces):
        '''
        Get one input.

        :param go: Go instance.
        :param piece_type: 1('X') or 2('O').
        :param previous_died_pieces: the locations of previous died pieces.
        :return: (row, column) coordinate of input.
        '''    
        sign = 'X' if piece_type == 1 else 'O'
        print(('Turn for {}. Please make a move.').format(sign))

        # Pass input
        while 1:
            if self.input_hint: 
                print('Input format: row, column. E.g. 2,3')
                self.input_hint = False

            user_input = input('Input:')
            if user_input.lower() == 'exit':
                sys.exit()
            try:
                input_coordinates = user_input.strip().split(',')
                i, j = int(input_coordinates[0]) - 1, int(input_coordinates[1]) - 1
                return i, j
            except:
                print('Invalid input. Input format: row, column. E.g. 2,3\n')
                self.input_hint = True
                continue
        
class GreedyPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'greedy'

    def get_input(self, go, piece_type, previous_died_pieces):
        '''
        Get one input.

        :param go: Go instance.
        :param piece_type: 1('X') or 2('O').
        :param previous_died_pieces: the locations of previous died pieces.
        :return: (row, column) coordinate of input.
        '''    
        largest_died_chess_cnt = 0
        greedy_placements = []
        for i in range(go.size):
            for j in range(go.size):
                if go.valid_place_check(i, j, piece_type, previous_died_pieces, test_check=True):
                    test_go = go.copy_board()
                    test_go.place_chess(i, j, piece_type, previous_died_pieces)
                    died_chess_cnt = len(test_go.find_died_pieces(3 - piece_type))
                    if died_chess_cnt == largest_died_chess_cnt:
                        greedy_placements.append((i,j))
                    elif died_chess_cnt > largest_died_chess_cnt:
                        largest_died_chess_cnt = died_chess_cnt
                        greedy_placements = [(i,j)]
        return random.choice(greedy_placements)        

class MyPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'my'

    def get_input(self, go, piece_type, previous_died_pieces):
        '''
        Get one input.

        :param go: Go instance.
        :param piece_type: 1('X') or 2('O').
        :param previous_died_pieces: the locations of previous died pieces.
        :return: (row, column) coordinate of input.
        '''   
        pass
        # return i,j