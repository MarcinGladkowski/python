"""
To each object in memory is assigned a counter of callers. When counter
is 0 the object is removing from memory.
"""
import os


class MyObject:
    """
    * Program which wasting a memory
    """

    def __init__(self) -> None:
        self.data = os.urandom(100)


def get_data():
    values = []
    for _ in range(100):
        obj = MyObject()
        values.append(obj)
    return values


def run():
    deep_values = []
    for _ in range(100):
        deep_values.append(get_data())
    return deep_values
