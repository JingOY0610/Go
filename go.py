import sys

# Initialize board with size of n
def init_board(n):
    '''
    Initialize a board with size n*n.

    :param n: width and height of chess board.
    :return: 2d array of size n*n, representing the board.
    '''
    board = [[0 for x in range(n)] for y in range(n)]  # Empty space marked as 0
    # Black pieces marked as 1
    # White pieces marked as 2
    return board

# Detect neighbor pieces of a single piece
def detect_neighbor(board, i, j):
    '''
    Detect all the neighbors of a given piece.

    :param board: 2d array board.
    :param i: row number of the board.
    :param j: column number of the board.
    :return: a list containing the neighbors row and column (row, column) of position (i, j).
    '''
    neighbors = []
    # Detect borders and add neighbor coordinates
    if i > 0: neighbors.append((i-1, j))
    if i < len(board) - 1: neighbors.append((i+1, j))
    if j > 0: neighbors.append((i, j-1))
    if j < len(board) - 1: neighbors.append((i, j+1))
    return neighbors

def detect_neighbor_ally(board, i, j):
    '''
    Detect the neibored allies of a given piece.

    :param board: 2d array board.
    :param i: row number of the board.
    :param j: column number of the board.
    :return: a list containing the neighbored allies row and column (row, column) of position (i, j).
    '''
    neighbors = detect_neighbor(board, i, j)  # Detect neighbors
    group_allies = []
    # Iterate through neighbors
    for piece in neighbors:
        # Add to allies list if having the same color
        if board[piece[0]][piece[1]] == board[i][j]:
            group_allies.append(piece)
    return group_allies

def ally_dfs(board, i, j):
    '''
    Using DFS to search for all allies of a given piece.

    :param board: 2d array board.
    :param i: row number of the board.
    :param j: column number of the board.
    :return: a list containing the all allies row and column (row, column) of position (i, j).
    '''
    stack = [(i, j)]  # stack for DFS serach
    ally_members = []  # record allies positions during the search
    while stack:
        piece = stack.pop()
        ally_members.append(piece)
        neighbor_allies = detect_neighbor_ally(board, piece[0], piece[1])
        for ally in neighbor_allies:
            if ally not in stack and ally not in ally_members:
                stack.append(ally)
    return ally_members

def find_qi(board, i, j):
    '''
    Find Qi of a given piece. If a group of allied pieces has no Qi, they all die.

    :param board: 2d array board.
    :param i: row number of the board.
    :param j: column number of the board.
    :return: boolean indicating whether the given piece still has Qi.
    '''
    ally_members = ally_dfs(board, i, j)
    for member in ally_members:
        neighbors = detect_neighbor(board, member[0], member[1])
        for piece in neighbors:
            # If there is empty space around a piece, it has Qi
            if board[piece[0]][piece[1]] == 0:
                return True
    # If none of the pieces in a allied group has an empty space, it has no Qi
    return False

def find_died_pieces(board):
    '''
    Find the died pieces that has no Qi in the board.

    :param board: 2d array board.
    :return: a list containing the dead pieces row and column(row, column).
    '''
    died_pieces = []
    for i in range(len(board)):
        for j in range(len(board)):
            # The piece die if it has no Qi
            if not find_qi(board, i, j):
                died_pieces.append((i,j))
    return died_pieces

def remove_died_pieces(board):
    '''
    Remove the dead pieces in the board.

    :param board: 2d array board.
    :return: None.
    '''
    died_pieces = find_died_pieces(board)
    if not died_pieces: return
    for piece in died_pieces:
        board[piece[0]][piece[1]] = 0

def place_chess(board, i, j, player):
    '''
    Place a chess piece in the board. Modify the board in-place.

    :param board: 2d array board.
    :param i: row number of the board.
    :param j: column number of the board.
    :param player: white or black
    :return: boolean indicating whether the placement is valid.
    '''
    if player == 'black':
        piece_type = 1
    elif player == 'white':
        piece_type = 2
    else:
        print('Invalid input.')
        return False
    if not valid_place_check(board, i, j, piece_type):
        return False
    board[i][j] = piece_type
    return True

def valid_place_check(board, i, j, piece_type):
    '''
    Check whether a placement is valid.

    :param board: 2d array board.
    :param i: row number of the board.
    :param j: column number of the board.
    :param piece_type: 1(white piece) or 2(black piece).
    :return: boolean indicating whether the placement is valid.
    '''   
    if not (i >= 0 and i < len(board)):
        print(('Invalid placement. row should be in the range 1 to {}.').format(len(board) - 1))
        return False
    if not (j >= 0 and j < len(board)):
        print(('Invalid placement. column should be in the range 1 to {}.').format(len(board) - 1))
        return False
    if board[i][j] != 0:
        print('Invalid placement. There is already a chess in this position.')
        return False
    test_board = [[row[c] for c in range(len(board))] for row in board]
    test_board[i][j] = piece_type
    if not find_qi(test_board, i, j):
        print('Invalid placement. No Qi found in this position.')
        return False
    return True
    
def visualize_board(board):
    '''
    Visualize the board.

    :param board: 2d array board.
    :return: None
    '''  
    print('-' * len(board) * 2)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                print(' ', end=' ')
            elif board[i][j] == 1:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()
    print('-' * len(board) * 2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python go.py n. Where n is the dimension of the board n*n.')
        sys.exit()
    n = int(sys.argv[1]) # Size of the board
    board = init_board(n) # Initialize the board of size n*n
    black_move = True # Black(X) chess plays first
    input_hint = True # Print hints for input
    print('----------Input "exit" to exit the program----------')
    print('X stands for black chess, O stands for white chess.')
    visualize_board(board)

    while 1:
        player = 'black' if black_move else 'white'
        sign = 'X' if black_move else 'O'
        print(('Turn for {} ({}). Please make a move.').format(player, sign))

        # Hint for user input
        if input_hint: print('Input format: row, column. E.g. 2,3')
        input_hint = False

        user_input = input()
        if user_input.lower() == 'exit':
            sys.exit()
        try:
            input_coordinates = user_input.strip().split(',')
            i, j = int(input_coordinates[0]) - 1, int(input_coordinates[1]) - 1
        except:
            print('Invalid input.')
            input_hint = True
            continue

        # If invalid input, continue the loop. Else it places a chess on the board.
        if not place_chess(board, i, j, player):
            visualize_board(board) 
            continue

        remove_died_pieces(board) # Remove the dead pieces
        visualize_board(board) # Visualize the board again

        black_move = not black_move # Players take turn

