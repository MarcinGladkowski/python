from typing import List, Tuple, Set, Dict, Union, Any, Optional, Callable
from dataclasses import dataclass


def multiple_string(factor: int, text: str):
    return text * factor


print(multiple_string(4, 'test'))
print(multiple_string('test', 2)) # also works

'''
Basic types
'''
x: str = 'String'
x: int = 1_000_000
x: float = 0.6
x: bool = True

'''
For collections types
Form Python 3.9  for lists is native (without importing from typing)
'''
x: List = [1, 2, 3]
x: Tuple = (1, 2, 3)
x: Set = {1, 2, 3}
x: Dict = {'one': 1, 'two': 2, 'three': 3 }

'''
More specified
'''
l1: List[int] = [1, 2, 3] # only ints
l2: List[Union[int, str]] = ['text', 1, 2] # ints and string types
l3: List[Tuple[Any, Any]] = [('1', 'two'), (1, 3.4)] # tuples with two types of variables


def multiply(a: int, b: int, c: Optional[int] = None) -> int:
    return a * b * c if c else a * b


multiply(2, 2, 2)


def do_something(): pass


fun: Callable = do_something


@dataclass
class Point:
    x: int = 0
    y: int = 0


p: Point = Point()


