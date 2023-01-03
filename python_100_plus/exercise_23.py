"""
level 1

Question: Write a method which can calculate square value of number

Hints: Using the ** operator

Solution:
"""


def square(number):
    return number ** 2


assert 4 == square(2)
assert 64 == square(8)
assert 16 == square(4)