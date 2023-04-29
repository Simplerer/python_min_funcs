import inquirer

questions = [
        inquirer.List('program',
                      message="What type of project would you like to run?",
                      choices=['Numbers', 'Text', 'None'],
                      ),
    ]

math = [
        inquirer.List('numbers',
                      message="What numbers program would you like to access?",
                      choices=['Pi to 48 digits', 'Prime numbers', 'None'],
                      ),
    ]

text = [
        inquirer.List('text',
                      message="What text program would you like to access?",
                      choices=['FizzBuzz', 'Reverse String','None'],
                      ),
    ]