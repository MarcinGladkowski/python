"""
Please generate a random float where the value is between 5 and 95 using Python math module.

Hints: Use random.random() to generate a random float in [0,1].
"""
from random import random


def random_number():
    n = random() * 100
    if 5 < n > 95:
        return random_number()
    return n


print(random_number())