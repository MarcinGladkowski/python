"""Generally it's syntactic sugar for this"""


def decorator(the_callback):
    def wrapper():
        print('Behavior to add')
        the_callback()

    return wrapper


def func():
    pass


func = decorator(func)


"""
Lets start from @ operator
"""

# usable in numpy
# @ is called "matmul" using to matrix multiplication
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a @ b)

# case with @dataclass
from dataclasses import dataclass

@dataclass
class XMasMovie:
    title: str
    director: str
    xmas_factor: int


### lets start
def expects_callback(the_callback):
    print('The function that expects a callback')

    def dynamically_defined_function():
        print('The dynamically defined function starts')
        the_callback()
        print('The dynamically defined function ends')

    print('The function that expects a callback stops')

    return dynamically_defined_function


def normal_function():
    print('I am a normal function')


mystery = expects_callback(normal_function)

mystery()


### another simple example
def decorator(func):
    def wrapper():
        print('Behavior to add before')
        func()
        print('Behavior to add after')

    return wrapper


@decorator
def decorated_function():
    print('ta da!')


decorated_function()

