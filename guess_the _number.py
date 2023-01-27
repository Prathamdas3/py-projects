import random
# asking player about his name and giving him greetings


def player_name():
    player = input('What is your name?')
    print(f'welcome {player} to the game of Guess The Number ')


# basic stuff before we start the game


def basic():
    print('''
  1. Computer decides a random number and you have to guess it  
  2. If your guess it and if your guess is correct than you win other wise you lose 
  3. You would only have 10 lives 
  ''')


# Choosing the random number
unknown_number = random.choice(range(0, 101))

# counter of the live


# Taking the input from the player


def player_choice():
    choice_again = True
    while choice_again:
        choice = (input('Please select a number between 0 to 100: '))
        if choice.isdigit() == False:
            print('Please input a number')
        elif int(choice) not in range(0, 101):
            print('Please select a number between 0 to 100')
        elif int(choice) in range(0, 101):
            choice_again = False
            return int(choice)
# play-game


def play_game():
    play = input('Do you want to play the game [Y/N]: ').upper()
    return play
# game together


def game_together():
    pg = play_game()
    if pg == 'Y':
        player_name()
        basic()
        game = True
        counter = 10
        while game:
            pc = player_choice()
            counter = counter-1
            print(counter)
            if pc != unknown_number:
                player_choice()
                counter = counter-1
                print(counter)
                print('Choose another number')

            else:
                game = False
    elif pg == 'N':
        print('See you later')


game_together()
