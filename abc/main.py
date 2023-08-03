"""
@see https://www.youtube.com/watch?v=EVa5Wdcgl94&ab_channel=CodingTech
"""
from abc import ABCMeta, abstractmethod


class EatsBread(metaclass=ABCMeta):
    @abstractmethod
    def eat_bread(self):
        pass


class Duck(EatsBread):
    def eat_bread(self):
        pass


class Pig(EatsBread):

    def eat_bread(self):
        pass



class Lama:
    """
    Can be used as 'virtual subclass'
    """
    def eat_bread(self):
        pass



def feed_bread(animal: EatsBread):
    animal.eat_bread()