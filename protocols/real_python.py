"""
@see https://realpython.com/python-protocol/

Protocols specifies the methods and attributes that a class must implement
bo be considered of a given type

Tools like myPy, Pyright, Pyre are checking nominal subtyping (no structural subtyping)

Internal Python protocols:
- iterator
- context manager
- descriptor


NOMINAL SUBTYPING is strictly based on inheritance. A class that inherits from a parent class
is a subtype of its parent.

STRUCTURAL SUBTYPING is based in the internal structure of classes. Two classes with the same
methods and attributes are structural subtypes of another.

"""


### DUCK TYPING ###
"""
Consider all builtin iteration objects
"""
numbers = [1, 2, 3]
person = ("Jane", 25, "Dev")
letters = 'abc'
ordinals = {"one": "A", "two": "B"}
even_digits = {2, 4, 6, 8}

containers = [numbers, person, letters, ordinals, even_digits]

for container in containers:
    """
    All of them supports iteration
    """
    for element in container:
        print(element, end=" ")
    print()

"""
Conclusion:

Duck typing allows to use object with same methods without inheritance. 
That's allow to build flexible and decoupled code.
"""

def add(a: float | int, b: float | int) -> int:
    """
    Functions still works for str arguments

    Python does not check types at the runtime.
    That's why having static type analysis tool is valuable.
    """
    return a + b

print(add(1, 2))
print(add("1", "2"))


class Duck:
    def duck(self) -> str:
        return "The duck is quacking"


def make_it_quack(duck: Duck):
        return duck.duck()

class Person:
    def duck(self) -> str:
        return "The person is quacking?"


print(make_it_quack(Duck()))
print(make_it_quack(Person())) # code is still running


"""Use inheritance to resolve that problem"""
class QuackingThing:
    """
    Both classes will be coupled by type, but interface can be not clear - fit to all child classes
    """
    def quack(self):
        raise NotImplementedError("Subclasses must implement this method")

class BetterDuck(QuackingThing):
    def quack(self):
        return "The duck is quacking"

class BetterPerson(QuackingThing):
    def quack(self):
        return "The person is quacking"


def make_it_quack(quack: QuackingThing):
    return quack.quack()

print(make_it_quack(BetterDuck()))
print(make_it_quack(BetterPerson()))

"""Structural Subtyping and Protocols"""
from typing import Protocol, Optional


class Adder(Protocol):
    """
    Protocol methods does not have a body

    Adding explicit typing have impact on classes implements this method.
    To support this protocol type hinting have be same or loose type hinted
    """
    def add(self, a, b): ... # ellipsis syntax


class IntAdder:
    """Implements Adder protocol"""
    def add(self, a, b):
        return a + b

class FloatAdder:
    """Implements Adder protocol"""
    def add(self, a, b):
        return a + b


def add(adder: Adder):
    return adder.add(1, 2)

print(add(IntAdder()))
print(add(FloatAdder()))

"""Building generic protocols"""
from typing import Protocol, TypeVar

T = TypeVar("T")

class GenericProtocol(Protocol[T]):
    def method(self, arg: T) -> T:
        ...


T = TypeVar("T", bound=int| float)

class BetterAdder(Protocol[T]):
    """
        Python 3.12 notation - no T declaration beforehand
        def add[T: int | float](self, x: T, y: T) -> T:
    """
    def add(self, x: T, y: T) -> T:
        ...

class BetterIntAdder:
    def add(self, x: int, y: int) -> int:
        """Use generic type as int"""
        return x + y

class BetterFloatAdder:
    def add(self, x: float, y: float) -> float:
        """use generic type as float"""
        return x + y

def better_add(adder: BetterAdder):
    print(adder.add(1, 4))

better_add(BetterIntAdder())
better_add(BetterFloatAdder())

"""Protocol members"""

"""
Class attributes
"""
from typing import Protocol, ClassVar

class ProtocolMemberDemo(Protocol):
    class_attribute: ClassVar[int]

"""
subprotocols
"""
class ContentCreator(Protocol):
    def create_content(self) -> str:
        ...

class Blogger(ContentCreator, Protocol):
    posts: list[str]

    def add_post(self, title: str, content: str) -> None:
        ...

"""
Recursive protocols
"""
class LinkedListNode(Protocol):
    value: int
    next_node: Optional["LinkedListNode"] # referenced as string




