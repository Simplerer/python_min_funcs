from modules import *

import inquirer



def start():
    questions = [
        # inquirer.Text('name', message="Tell me your name please."),
        inquirer.List('program',
                      message="What numbers program would you like to access?",
                      choices=['Pi to 48 digits', 'Prime numbers', 'None'],
                      ),
    ]
    answers = inquirer.prompt(questions)

    for x in answers:
        if answers[x] == 'None':
            print('Thanks for coming out!')
            return
        elif answers[x] == 'Prime numbers':
            n = input('\n How many prime numbers would you like to see?\n')
            if n.isnumeric():
                numbers.prime(int(n))
                start()
            else:
                print('\n Get serious! \n ')
                start()
        elif answers[x] == 'Pi to 48 digits':
            numbers.nth_of_pi()
            start()


start()