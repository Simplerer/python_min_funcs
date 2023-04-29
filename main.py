from modules import *
# from modules.prompts import *

import inquirer



def start():

    category = inquirer.prompt(prompts.questions)

    if category['program'] == 'Numbers':    
        answers = inquirer.prompt(prompts.math)

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

    elif category['program'] == 'Text':
        answers = inquirer.prompt(prompts.text)

        for x in answers:
            if answers[x] == 'None':
                print('Thanks for coming out!')
                return
            elif answers[x] == 'FizzBuzz':
                text.fizz_buzz()
                start()
            elif answers[x] == 'Reverse String':
                text.reverse_string()
                start()
    else:
        print('Thanks for coming out!')    


start()