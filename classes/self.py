class Car:
    def __init__(self) -> None:
        self.engine = False

    def start(self, start):
        self.engine = start


example_car = Car()

example_car.start(True)
"""Execute passing instance as self argument"""
Car.start(example_car, False)