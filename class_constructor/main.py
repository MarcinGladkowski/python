""" custom class"""
from random import choice


class SomeClass:
    pass


"""
Initialize object
"""
SomeClass()
print(SomeClass())

"""
Calling a class vs calling a instance
- to call instance you have to implement __call__ magic method
"""

"""
Instantiation process of class
- create a new instance __new__()
- initialize the new instance __init__()
"""


class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point")

        return super().__new__(cls)

    def __init__(self, x, y) -> None:
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"


point = Point(21, 42)

"""
Run steps manually
"""
point2 = Point.__new__(Point)
point2.__init__(22, 23)


class A:
    def __init__(self, a_value) -> None:
        print("Initialize the new instance of A")
        self.a_value = a_value


class B:

    def __new__(cls, *args, **kwargs):
        return A(52)

    def __init__(self, b_value) -> None:
        self.b_value = b_value
        print("Initialize the new instance of B")


b = B(21)
print(isinstance(b, B))


class Rectangle:
    """
    Providing custom object initializers

    __init__() cannot return anything, only None
    """

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height


"""
NOTE: In python functions and methods returns None without explicit return statement!
"""


class ValidateRectangle:
    """
    Add validation of passed arguments
    """

    def __init__(self, width, height) -> None:
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive with expected, got {width}")
        self.width = width
        if not (isinstance(height, (int, float)) and height > 0):
            raise ValueError(f"positive with expected, got {height}")
        self.height = height


class Person:
    def __init__(self, name, birth_date) -> None:
        self.birth_date = birth_date
        self.name = name


class Employee(Person):
    """
    Init and inheritance - call super().__init__() of parent class
    """

    def __init__(self, name, birth_date, position) -> None:
        super().__init__(name, birth_date)
        self.position = position


john = Employee("John Doe", "2000-09-09", "Python developer")
print(john.name)


class Greeter:
    """
    Optional arguments
    """

    def __init__(self, name, formal=False) -> None:
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good morning, {self.name}")
        else:
            print(f"Hello {self.name}")


informal_greeter = Greeter("Pythonista")
informal_greeter.greet()

formal_greeter = Greeter("Pythonista", True)
formal_greeter.greet()

"""
Ideas and example of overwriting __new__() function
"""


class SomeClass:
    """
    The built-in object class is the default base class for all Python classes
    """

    def __new__(cls, *args, **kwargs):
        # object.__new__() can only get one argument! cls
        instance = super().__new__(cls)
        # Customize your instance here
        return instance


""" Subclassing immutable built-in types """


class Distance(float):

    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

    # incorrect!
    # def __init__(self, value, unit) -> None:
    #     super().__init__(value)
    #     self.unit = unit


distance = Distance(23.0, 'cm')
print(dir(distance))


class Pet:
    def __new__(cls):
        other = choice([Dog, Cat, Python])
        instance = super().__new__(other)
        print(f"I'm a {type(instance).__name__}")
        # __init__() of each pet instance won't be run!
        return instance

class Dog:
    def communicate(self):
        print("woof! woof!")


class Cat:
    def communicate(self):
        print("meow! meow!")


class Python:
    def communicate(self):
        print("hiss! hiss!")


pet = Pet()

pet.communicate()


class Singleton(object):
    """
    Example using __new__()
    to implement Singleton design pattern
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance





