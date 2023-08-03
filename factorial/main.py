from math import factorial

"""
Own implementation of factorial in plain Python
"""


def fac_1(number: int):
    result = 1
    for n in range(1, number+1):
        result *= n

    return result


assert factorial(5) == fac_1(5)
