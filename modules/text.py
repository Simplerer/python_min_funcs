
def fizz_buzz():
    n = input('FizzBuzz time!, how far up are we going?\n Give me a number, less than 300!')
    if not n.isnumeric():
        print('\n A Number please, under 300!\n')
        fizz_buzz()
    if int(n)>300:
        print('\nI said under 300!!!\n')
        fizz_buzz()
    for x in range(1,int(n)):
        if x%15==0:
            print('FizzBuzz')
        elif x%3==0:
            print('Fizz')
        elif x%5==0:
            print('Buzz')
        else:
            print(x)
    return

def reverse_string():
    s = input('\n Type a sentance and lets reverse it!\n')
    s = list(s)
    s.reverse()
    print('\n',''.join(s),'\n')
    return 