'''
Higher order functions


* You can store all yours decorators in separated module
* You can use multiple decorators for function (nested)
* You can use decorators with arguments @decorator(argument)
'''


def greet(name):
    print(f'Hello {name}')


def simon(func):
    func('Simon')


simon(greet)

'''
Functions in functions
'''


def respect(maybe):
    def congrats():
        return "Congrats, bro"

    def insult():
        return "You're silly!"

    if maybe == 'Yes':
        return congrats
    else:
        return insult


def start_stop(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")

    return wrapper


def roll():
    print("Rolling on the floor ....")


start_stop(roll)()

'''
Using @
'''


@start_stop
def roll_with_wrapper():
    print('Rolling on the floor with wrapper...')


roll_with_wrapper()