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


isinstance(Duck(), EatsBread)