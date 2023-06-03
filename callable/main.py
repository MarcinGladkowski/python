"""
https://realpython.com/python-callable-instances/
Callable - everything we can use with parenthesis ()
"""

print(dir(abs))  # '__call__'


def greet():
    print("hello world")


greet.__call__()

""" Checking whether an Object is Callable """
print(callable(abs))


class Counter:
    def __init__(self) -> None:
        self.count = 0

    def increment(self) -> None:
        self.count += 1

    def __call__(self):
        self.increment()


my_counter = Counter()
my_counter.increment()
my_counter()

print(my_counter.count)


class PowerFactory:

    def __init__(self, exponent: int = 2) -> None:
        self.exponent = exponent

    def __call__(self, base: int) -> int:
        return base ** self.exponent


power_factory = PowerFactory()
print(power_factory(2))
print(power_factory(3))

"""
    __init__() vs __call__()
"""

class Demo:
    def __init__(self, attr):
        print(f"Initialize an instance of {self.__class__.__name__}")
        self.attr = attr
        print(f"{self.attr = }")

    def __call__(self, arg):
        print(f"Call an instance of {self.__class__.__name__} with {arg}")


new_demo = Demo("Some initial value")

new_demo("Hello")