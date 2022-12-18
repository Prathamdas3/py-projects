# creating a board for the user to play
import random


def display_board(board):
    # print('\n'*100)
    print(board[7] + '|'+board[8] + '|'+board[9])
    print('-----')
    print(board[4] + '|'+board[5] + '|'+board[6])
    print('-----')
    print(board[1] + '|'+board[2] + '|'+board[3])


board = [' ']*10
# test_board = ['#', 'X', 'O', "X", "O", "X", "O", "X", "O", "X"]
# taking input from user and assigning a value to them


def player_input():
    '''OUTPUT=(player 1 marker,player 2 marker)'''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
    if marker == "X":
        return ('X', 'O')
    else:
        return ('O', 'X')


print(player_input())
# creating a function that takes the board, marker, desired position and assign it to the board


def place_maker(board, marker, position):
    board[position] = marker


# print(place_maker(board, '@', 4))
# print(display_board(board))

# this function will check the if the player wins or not


def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark)

# this function checks which player goes first


def check_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
