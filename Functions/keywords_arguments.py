""" Keyword arguments """


def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6

remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

"""
SyntaxError: (cannot catch it using try-except block)
    remainder(number=20, 7)
"""

"""Arguments as dictionary"""
my_kwargs = {
    'number': 20,
    'divisor': 7
}

remainder(**my_kwargs)

"""Connect kwargs with arguments"""
my_kwargs_2 = {
    'divisor': 7
}

remainder(number=20, **my_kwargs_2)

"""From two dictionaries"""
my_kwargs_number = {
    'number': 20
}

my_kwargs_divisor = {
    'divisor': 7
}

remainder(**my_kwargs_divisor, **my_kwargs_number)


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


print_parameters(alpha=1.4, beta=9, gamma=4)
