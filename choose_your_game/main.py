# takeing the name of the player
name = input('What is your name: ')
print(f'Welcome {name}! to this game')

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. which way do you want to go left or right?:  "
).lower()
if answer == "left":
    answer = input(
        'You have to come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim to swim across: ').lower()

    if answer == "swim":
        print('You swam across and were eaten by an alligator,you loose')
    elif answer == "walk":
        print('You walk for many miles, ran out of water and you lost the game')
    else:
        print('Not a valid option,You lose.')
elif answer == "right":
    answer = input(
        'You come to a bridge it looks wobbly , do want to cross it or head back? type cross to cross or back to back: ').lower()
    if answer == 'back':
        print(
            'you go back you loose..'
        )
    elif answer == 'cross':
        answer = input(
            'You cross the bridge and meet a stranger.Do you talk to them (y/n): ').lower()
        if answer == 'y':
            print('you win')
        elif answer == 'n':
            print('you loose')
        else:
            print('Not a valid option,You lose.')
    else:
        print('Not a valid option,You lose.')
else:
    print('Not a valid option,You lose.')
