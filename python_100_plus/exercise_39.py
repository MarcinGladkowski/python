"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list.
 Use [n1:n2] to slice a list
"""


def list_squares():
    result = []
    for x in range(21):
        result.append(x ** 2)
    print(result[-5:])


list_squares()
