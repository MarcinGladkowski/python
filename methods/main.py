"""
Types of methods

- Instance methods
- Class methods
- Static methods
"""


class Car:
    def __init__(self, model):
        self.model = model
        self.started = False

    def start(self):
        """
        self - it's only convention
        The first argument is bound with existing instance
        but 'self' is only convention name.
        It's not a keyword of python

        """
        print("Starting the car")
        self.started = True

    def stop(self):
        print("Stopping the car")
        self.started = False


honda = Car('Civic')
"""
Not only honda.start()
We can pass an instance instead self to class!
"""
Car.start(honda)


class Point:
    """
    Class method

    decorated @classmethod methods are perfect for multiple constructors

    cls argument provide reference to current class
    """
    def __init__(self, x: int, y: int):
        self.y = y
        self.x = x

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)


    @staticmethod
    def show_intro_message(name: str):
        print(f"Hey {name}")



