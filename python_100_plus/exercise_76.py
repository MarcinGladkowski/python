"""
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints: Use random.choice() to a random element from a list.
"""

import random

some_even_number = random.choice([x for x in range(11) if x % 2 == 0])

print(some_even_number)