import random
# asking player about his name and giving him greetings


def player_name():
    player = input('What is your name?')
    print(f'welcome {player} to the game of stone-paper-scissor ')


player_name()
# basic stuff before we start the game


def basic():
    print('''
  1. Stone is stronger than scissor so stone wins 
  2. Paper can warp a stone so paper is stronger than stone so paper wins
  3. Scissor can cut a paper so scissor is stronger than paper so scissor wins 
  ''')


basic()
# game element
game_element = ['Stone', 'Paper', 'Scissor']

# player input


def player_choice():
    choice_again = True
    while choice_again:
        print(f'Please select your element from{game_element} as [1,2,3]')
        choice = (input('What is your choice: '))
        if choice.isdigit() == False:
            print('Please input a number')
        elif int(choice) not in range(1, 4):
            print('Please select a number between 1 to 3')
        else:
            choice_again = False
            return game_element[int(choice)-1]


player_choice()
# computers choice


def computer_choice():
    computer_choice = random.choice(range(0, 3))
    return game_element[computer_choice]


computer_choice()
# play game


def play_game():
    play = input('Do you want to play the game [Y/N]: ').upper()
    return play


play_game()
# try game


def try_next():
    if play_game == 'Y':
        pass
    elif play_game == 'N':
        play_again = False


try_next()
# game together


def game_together():
    play_again = True
    pg = play_game()
    if pg == 'Y':
            player_name()
            basic()
            pc = player_choice()
            cc = computer_choice()
            if pc == cc:
                print("The game is draw")
                try_next()
            elif ((pc == game_element[0]) and (cc == game_element[1])) or ((pc == game_element[1]) and (cc == game_element[2])) or ((pc == game_element[2]) and (cc == game_element[0])):
                print("Better luck next time")
                try_next()
            elif ((pc == game_element[1]) and (cc == game_element[0])) or ((pc == game_element[2]) and (cc == game_element[1])) or ((pc == game_element[0]) and (cc == game_element[2])):
                print("You have won the game..")
                try_next()
    elif pg == 'N':
        print("See you later")


game_together()
