"""
Level 3

Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints: Consider use yield
"""


class Seven:

    def __init__(self, max: int):
        self.max = max

    def divide(self):
        for x in range(0, self.max):
            if x % 7 == 0:
                yield x


divide_generator = Seven(200)
iterator = divide_generator.divide()

print(next(iterator))
print(next(iterator))
print(next(iterator))
