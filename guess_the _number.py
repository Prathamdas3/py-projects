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
# # play-game


def play_game():
    play = input('Do you want to play the game [Y/N]: ').upper()
    return play
# game together


def game_together():
    pg = play_game()
    if pg == 'Y':
        player_name()
        basic()
        for i in reversed(range(0, 11)):

            if i == 0:
                print("You don't have anymore chance ")
                break
            if player_choice() != unknown_number:
                print(
                    f'Please select another number, you have only {i-1} chance left to guess the number ')
            elif player_choice() == unknown_number:
                print('You have won the game')
                break

        print(f'The unknown number was {unknown_number}')

    elif pg == 'N':
        print('See you later')


game_together()
