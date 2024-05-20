# Builtin data structures that are sequences

""" LIST """
countries = ["USA", "Poland", "Canada"]

for country in countries:
    print(country)

"""TUPLE"""
countries = "USA", "Poland", "Canada"
for country in countries:
    print(country)

""" STRINGS """
country = "Netherlands"
for letter in country:
    print(letter)

""" Range (data types)"""
numbers = range(1, 10)
for number in numbers:
    print(number)

"""
And others like: byte, bytearray
"""

"""User defined Python sequences"""


class ShapePoints:
    """
    Basic methods require to make class be a Sequence
    * get element by index
    * get count of elements
    * allow to iterate over elements

    Usually sequences implemented also methods
    .count(), .index(), .contains()

    """

    def __init__(self, points):
        """Cast for some mutability issues"""
        self.points = list(points)

    def __getitem__(self, index):
        """
        Making the class Indexable
        """
        return self.points[index]

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        """
        Making the class Iterable
        """
        return iter(self.points)


shape_points = ShapePoints([(10, 20), (10, 23)])

print(shape_points.points)

"""
Possible to use sequence (inherit) from
from collections.abc import Sequence
"""
from collections.abc import Sequence


class ImmutableSequence(Sequence):
    def __init__(self, points):
        self.points = list(points)

    def __repr__(self):
        return f"ShapePoints({self.points})"

    def __getitem__(self, index):
        return self.points[index]

    def __len__(self):
        return len(self.points) - 1

    def __iter__(self):
        return iter(self.points)



"""
# NOT ALLOWED - TypeError
# immutable = ImmutableSequence([(10, 20), (10, 23)])
# immutable[0] = (10, 10)

from collections.abc import MutableSequence # allowed mutability

"""