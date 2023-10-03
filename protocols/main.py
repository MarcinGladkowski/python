"""
@see https://www.youtube.com/watch?v=EVa5Wdcgl94&ab_channel=CodingTech
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class EatsBread(Protocol):
    def eat_bread(self):
        pass


def feed_bread(animal: EatsBread):
    animal.eat_bread()


class Duck:
    """
    Duck is implicitly considered to be a subtype of EatsBread
    Duck is not EatsBread instance !
    """

    def eat_bread(self):
        ...


feed_bread(Duck())

print(isinstance(Duck(), EatsBread))

"""
Second explanation
source: https://codebeez.nl/blogs/type-hinting-in-modern-python-the-protocol-class/

- It's perfectly shows what's duck typing mean. It's something
look and behave as a duck it must be a duck. Using protocol we 
based on behaviour!

- Useful to classes from 3th party packages/not our code
- Resolve inherit problem
"""


class DuckLike(Protocol):
    """
    Defined behaviour, but it will be used only as
    type declaration. Not for directly inherit!
    """

    def walk(self, to: str) -> None: ...

    def quack(self) -> str: ...


class Chicken:

    def walk(self, to: str) -> None:
        print("Chicken walk!")

    def quack(self) -> str:
        return "Chicken quack"


def add_to_zoo_duck_like(duck: DuckLike):
    """
    Typing for Protocol class!

    If passed class don't have Ducklike behaviour
    an error will occur
    """
    duck.walk('Zoo')
    duck.quack()


add_to_zoo_duck_like(Chicken())
