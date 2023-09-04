# asking player about his name and giving him greetings


# basic stuff before we start the game


def basic():
    print("Let's start playing")
# telling about the rules of this show
    print("Here are the rules of the game 🙂")
    print("""1. You will get questions for a fixed amount of money.
2. If you are able to answer it correctly then you will get it.
3. You have two helpline by which you can call anyone you like and ask the answer for your question.""")
    print("Here is your first question on your screen")


# question of the amount
amount = [1000, 2000, 5000, 10000, 15000, 20000, 25000, 50000, 100000, 1000000]

# question sheet
questions = {
    'question0': "What is the Capital of india ?",
    'question1': "Who is the author of 'Manas ka-Hans'?",
    'question2': "Who is the author of the epic 'Meghdoot'?",
    'question3': "The International Literacy Day is observed on?",
    'question4': "The language of Lakhshawdeep. a union territory of India is?",
    'question5': "In which group of places the Kumbha Mela is held every twelve years?",
    'question6': "Bahubali festival is related to? ",
    'question7': "Which day is observed as the World Standards Day?",
    'question8': "Which of the following was the theme of the World Red Cross and Red Crescent Day?",
    'question9': "September 27 is celebrated every year as?"

}

# option sheet
options = {
    'answer0': ('1.Delhi', '2.Bombay', '3.Kolkata', '4.Pune'),
    'answer1': ('1.Khushwant Singh', '2.Prem Chand', '3.Jayashankar Prasad', '4.Amrit Lal Nagar'),
    'answer2': ('1.Vishakadatta', '2.Valmiki', '3.Banabhatta', '4.Kalidas'),
    'answer3': ('1.Sep 8', '2.Nov 28', '3.May 2', '4.Sep 22'),
    'answer4': ('1.Tamil', '2.Hindi', '3.Malayalam', '4.Telugu'),
    'answer5': ('1.Ujjain,purl,Prayag,Haridwar', '2.Prayaga,Haridwar,Ujjain,Nasik', '3.Rameshwaram,Purl,Badrinath,Dwarika', '4.Chittakoot,Ujjain,Prayag,Haridwar'),
    'answer6': ('1.Islam', '2.Hinduism', '3.Buddhism', '4.Jainism'),
    'answer7': ('1.June 26', '2.Oct 14', '3.Nov 15', '4.Dec 2'),
    'answer8': ('1.Dignity for all-focus on women', '2.Dignity for all-focus on children', '3.Focus on health for all', '4.Nourishment for all-focus on children'),
    'answer9': ('1.Teacher\'s Day', '2.National Integration Day', '3.World Tourism Day', '4.International Literacy Day')
}

# correct answers
correct_answer = [options['answer0'][0], options['answer1'][3], options['answer2'][3], options['answer3'][0], options['answer4']
                  [2], options['answer5'][1], options['answer6'][3], options['answer7'][2], options['answer8'][1], options['answer9'][2]]

# balance
balance = []

# main function


def work():
    name = input('What is your name : ')
    print(f'Welcome {name} to our show')
    play = True
    while play:
        value = input("Do you want to play?(Y/N): ")
        if value.capitalize() == 'Y':
            basic()
            sum = 0
            for i in range(0, 10):
                print(f"{i+1} This question is for {amount[i]} rupees ")
                print(questions[f'question{i}'])
                print(options[f'answer{i}'])
                a = int(input("Select the answer: "))
                if options[f'answer{i}'][a-1] == correct_answer[i]:
                    print(
                        f'Your answer was right and you get {amount[i]} rupees')
                    balance.append(amount[i])
                    sum = sum+balance[i]
                    print(f"Now your balance is {sum} rupees")
                else:
                    print(
                        f"Your answer is wrong and the right answer is {correct_answer[i]}")
                    balance.append(0)

                playnext = input("Do you want to play next (Y/N): ")
                if playnext.capitalize() == 'Y':
                    pass
                elif playnext.capitalize() == 'N':
                    print(f"{name} won {sum} rupees")
                    break

        elif value.capitalize() == 'N':
            play = False


work()
