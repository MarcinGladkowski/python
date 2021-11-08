"""
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""


class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)
print(rectangle.area())