# creating a board for the user to play
def display_board(board):
    # print('\n'*100)
    print(board[7] + '|'+board[8] + '|'+board[9])
    print('-----')
    print(board[4] + '|'+board[5] + '|'+board[6])
    print('-----')
    print(board[1] + '|'+board[2] + '|'+board[3])


board = [' ']*10
test_board = ['#', 'X', 'O', "X", "O", "X", "O", "X", "O", "X"]
# print(display_board(test_board))

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
