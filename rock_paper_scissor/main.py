import random
# asking player about his name and giving him greetings


def player_name():
    player = input('What is your name?')
    print(f'welcome {player} to the game of rock-paper-scissor ')


# basic stuff before we start the game


def basic():
    print('''
  1. rock is stronger than scissor so rock wins 
  2. Paper can warp a rock so paper is stronger than rock so paper wins
  3. Scissor can cut a paper so scissor is stronger than paper so scissor wins 
  ''')


# game element
game_element = ['rock', 'Paper', 'Scissor']

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


# computers choice


def computer_choice():
    computer_choice = random.choice(range(0, 3))
    return game_element[computer_choice]


# play game


def play_game():
    play = input('Do you want to play the game [Y/N]: ').upper()
    return play


# game together


def game_together():

    pg = play_game()
    if pg == 'Y':
        player_name()
        basic()
        pc = player_choice()
        cc = computer_choice()
        if pc == cc:
            print("The game is draw")
        elif ((pc == game_element[0]) and (cc == game_element[1])) or ((pc == game_element[1]) and (cc == game_element[2])) or ((pc == game_element[2]) and (cc == game_element[0])):
            print("Better luck next time")
        elif ((pc == game_element[1]) and (cc == game_element[0])) or ((pc == game_element[2]) and (cc == game_element[1])) or ((pc == game_element[0]) and (cc == game_element[2])):
            print("You have won the game..")
    elif pg == 'N':
        print("See you later")


game_together()
