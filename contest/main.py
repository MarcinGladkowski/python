"""
Variables scope
"""


a = 2


def add():
    b = 5
    c = a + b
    return c


print(add())


"""
Lambda function
"""

f = lambda: [0, 1, 2][[4, 5, 6][-2]]
f()

