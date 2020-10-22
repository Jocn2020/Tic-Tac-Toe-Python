"""
Tic Tac Toe Player
"""

import math


X = "X"
O = "O"
EMPTY = 0

def initial_state(): #Save
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): #Save
    """
    Returns player who has the next turn on a board.
    """
    counts = 0
    for n in range(3):
        counts += board[n].count(EMPTY)
    if counts%2 == 1:
        return X
    else:
        return O
    raise NotImplementedError


def actions(board): #Save
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    results =[]
    for n in range(3):
        for m in range(3):
            if board[n][m] == EMPTY:
                results.append((n,m))
    return results
    raise NotImplementedError


def result(board, action):#problem
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = [row[:] for row in board]
    board2[action[0]][action[1]] = player(board2)
    return board2
    raise NotImplementedError


def winner(board): #Save
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]


def terminal(board): #Save
    """
    Returns True if game is over, False otherwise.
    """
    if actions(board) == []:
        return True
    elif winner(board) == X or winner(board) == O:
        return True
    else:
        return False
    raise NotImplementerError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == 'X':
             return 1
        elif winner(board) == 'O':
            return -1
        else:
            return 0
    else:
        all_case = []
        for n in actions(board):
            board2 = [row[:] for row in board]
            board2 = result(board2, n)
            all_case.append(utility(board2))
            
        turn = player(board)
        if turn == X:
            return max(all_case)
        else:
            return min(all_case)
                
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestscore = 5
    move = (-1,-1)
    if terminal(board) == False:
        all_case = []
        action = actions(board)
        for n in action:
            board2 = [row[:] for row in board]
            board2 = result(board2,n)
            score = utility(board2)          
            if score < bestscore:
                bestscore = score
                move = n

    return move
    raise NotImplementedError
