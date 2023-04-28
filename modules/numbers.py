
import math


# **Find PI to the Nth Digit** - Enter a number and have the program generate &pi; (pi) up to that many decimal places. Keep a limit to how far the program will go.


def nth_of_pi():
    wait = False
    while wait == False:

        answer = input(
            '\n Up to 48, how many decimal places in pi would you like to see?\n')

        if not answer.isnumeric():
            print('\n Number please!')
        elif int(answer) > 48:
            print('\n Hey!\n I said up to 48 places, try again!')
        elif int(answer) < 0:
            print('\n Really... lets get serious.\n Try a non negative number of places.')
        else:
            print('\n')
            print(f'PI to {answer} places')
            print(f'%.{int(answer)}f' % math.pi)
            print('\n')
            wait = True
    return

# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.


def prime(n):
    prime_nums = [2, 3, 5, 7]
    if n < len(prime_nums):
        print('\n')
        print(prime_nums[:n])
        print(f'\n Here are {n} prime numbers!\n')
        return
    else:
        x = 8
        while n > len(prime_nums):
            if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
                prime_nums.append(x)
                x += 1
            else:
                x += 1
                continue
    print('\n')
    print(prime_nums)
    print(f'\n Here are {len(prime_nums)} prime numbers!\n')
    return