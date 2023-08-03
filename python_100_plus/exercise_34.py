"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops.
"""


def print_dict():
    data = dict()
    for i in range(11):
        data[i] = i ** 2
    print(data)


print_dict()