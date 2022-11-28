from datetime import date
from time import time

date(2022, 11, 27)
date.today()
date.fromtimestamp(1662450780)
date.fromtimestamp(time())
date.fromordinal(738404)
date.fromisoformat("2022-09-06")

"""
Purpose of multiple class constructors
    Arguments of different data types
    Different number of arguments
"""

class Person:
    """
    why is not possible to implement classic method overloading ?
    Methods are store in an Internal Dictionary __dict__ (cannot duplicate keys)
    Holds the class namespace
    """
    # def __new__(cls, **kwargs):
    #     """
    #     Object creation
    #
    #     Rarely needs overriding
    #
    #     Creates new instances
    #     Often called class constructor
    #     More accurately called:
    #         - Instance Creator
    #         - Object Creator
    #     """
    #     return super().__new__(cls)

    def __init__(self, name: str) -> None:
        """
        Object initialization
        """
        self.name = name


john = Person("John Doe")


class CumulativePowerFactory:

    def __init__(self, exponent=2, *, start=0) -> None:
        self._exponent = exponent
        self.total = start


    def __call__(self, base):
        power = base ** self._exponent
        self.total += power
        return power


square = CumulativePowerFactory()
print(square(29))

cube = CumulativePowerFactory(exponent=3)
print(cube(29))