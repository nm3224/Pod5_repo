def say_hello(name):
    print('Hello!\n')
    print(f'My name is {name}.\n')
    print('Have a good day!\n')

word = 'Hello'

def cap_this(phrase):
    return phrase.upper()


def interaction():
    is_friendly = input('Would you like to say hello? (yes/no) \n>>>')

    if is_friendly == 'yes':
        name = input('What is your name? \n>>')
        say_hello(name)

    elif is_friendly == 'no':
        print('You are not friendly')

    else:
        print('You are not coherent')


def say_hello_stranger(name='there'):
    print(f'Why, hello {name}!')



