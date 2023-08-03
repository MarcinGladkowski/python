"""
Dunder methods - (d)ouble (under)score
* calls automatically in specific situations
* Examples of magic methods: __init__, __str__, __repr__
"""
from typing import Any


class Car:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def __str__(self):
        return f"{self.brand}"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(brand={self.brand})"
        )


"""
Protocols: Iterator, Iterable, Descriptor, Context manager 
"""

