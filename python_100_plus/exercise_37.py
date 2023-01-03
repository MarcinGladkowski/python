"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list.
"""


def list_squares():
    result = []
    for x in range(21):
        result.append(x ** 2)
    print(result)


list_squares()