"""
Arguments can be injected using positions and keywords


Keyword arguments
- using call with remainder(number=7... its clear which parameter we use
- we can add to these parameters default values
- we can easily extend functions by new parameters

"""


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

"""
How to make arguments to have using it with keyword arguments
- arguments after * have to be used as keyword arguments
"""


def division(number, divisor, *, optional_1, optional_2):
    pass


# cannot call function in this way
# execute with division(1, 2, 3, 4) generate an error!
division(1, 2, optional_1=3, optional_2=4)


"""
/ - make the end of positional arguments
"""
def safe_division(numerator, denominator, /, *, ignore_overflow=False, ignore_zero_division=False):
    pass




