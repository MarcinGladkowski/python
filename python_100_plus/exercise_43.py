"""
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

Hints:

Use "for" to iterate the tuple Use tuple() to generate a tuple from a list.
"""


def even_tuple(value):
    result = []
    for x in value:
        if x % 2 == 0:
            result.append(x)
    print(tuple(result))


even_tuple((0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10))