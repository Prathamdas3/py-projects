def display_board(board):
    print(board[7] + '|'+board[8] + '|'+board[9])
    print('-----')
    print(board[4] + '|'+board[5] + '|'+board[6])
    print('-----')
    print(board[1] + '|'+board[2] + '|'+board[3])


board = [' ']*10
print(display_board(board))
