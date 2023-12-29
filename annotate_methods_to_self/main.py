from typing import Any, Self, TypeVar

"""
From https://realpython.com/python-type-self/

Learning returning Self, and some advanced type hinting from 3.11 - https://peps.python.org/pep-0673/

For python < 3.11 use 'from typing_extensions import Self' This is a 3rd party module
"""

class Queue:

    def __init__(self):
        self.items: list[Any] = []

    def push(self, item: Any) -> Self:
        self.items.append(item)
        return self

    def __bool__(self):
        """
        That's fascinating

        Useful for checking statements like: if <object>
        """
        return len(self.items) > 0



some_queue = Queue()
some_queue.push(1).push(2).push(3)