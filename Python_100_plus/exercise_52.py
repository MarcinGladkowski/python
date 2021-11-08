"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""
import math


class Circle:
    def __init__(self, radius: int) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


circle = Circle(2)

print(circle.area())