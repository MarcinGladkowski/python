"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for
 loops. Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""


def print_dict():
    data = dict()
    for i in range(21):
        data[i] = i ** 2

    print(data.keys())


print_dict()
