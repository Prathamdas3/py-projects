
import random

# creating a board for the user to play


def display_board(board):
    print('\n'*100)
    print(board[7] + '|'+board[8] + '|'+board[9])
    print('-----')
    print(board[4] + '|'+board[5] + '|'+board[6])
    print('-----')
    print(board[1] + '|'+board[2] + '|'+board[3])

# function to get player's input


def player_input():
    '''OUTPUT=(player 1 marker,player 2 marker)'''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
    if marker == "X":
        return ('X', 'O')
    else:
        return ('O', 'X')


# function to position the marker of the player
def place_maker(board, marker, position):
    board[position] = marker

# this function will check the if the player wins or not


def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark)

# this function checks which player goes first


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# check for free spaces in the board


def space_check(board, position):
    return board[position] == ' '

# checks the board is it full or empty


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # board is full if it returns true
    return True

# this function ask the player to choose the next position


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
    return position

# asking player if you want to play again or not


def replay():
    choice = input('Play again? Enter Yes or NO :')
    return choice == 'Yes'


# working of the all function together
# using a while loop to keep running the game
print('welcome to Tic Tac Toe')
while True:
    # play the game

    # set up everything (board, who's first, choose markers x or o)
    board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N: ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    # game play
    # player1 turn
    if turn == 'Player 1':
        # show the board
        display_board(board)
        # choose a position
        position = player_choice(board)
        # place the marker on the position
        place_maker(board, player1_marker, position)
        # check if they won
        if win_check(board, player1_marker):
            display_board(board)
            print('Player 1 has won!')
            game_on = False
        else:
            # or check if there is a tie
            if full_board_check(board):
                display_board(board)
                print('Tie game!')
                game_on = False
            else:
                # no tie and no win? Then next player's turn
                turn = 'Player 2'

    # player2 turn
    else:
        # show the board
        display_board(board)
        # choose a position
        position = player_choice(board)
        # place the marker on the position
        place_maker(board, player2_marker, position)
        # check if they won
        if win_check(board, player2_marker):
            display_board(board)
            print('Player 2 has won!')
            game_on = False
        else:
            # or check if there is a tie
            if full_board_check(board):
                display_board(board)
                print('Tie game!')
                game_on = False
            else:
                # no tie and no win? Then next player's turn
                turn = 'Player 1'
    # break out of the while loop on replay()
    if not replay():
        break
