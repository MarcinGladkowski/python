"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

Hints:

Use [n1:n2] notation to get a slice from a tuple.
"""


def print_tuple(tuple):
    print(tuple[:5])
    print(tuple[6:])


print_tuple((1,2,3,4,5,6,7,8,9,10))