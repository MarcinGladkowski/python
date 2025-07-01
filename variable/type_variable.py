def do_nothing[T](arg: T) -> T:
    """
    Generic function -> because of that [T]
    [T] - type variable, which can be any type.
    """
    return arg


do_nothing('Hello, world!')  # str




def func1[T](arg1: T, arg2: T) -> str:
    pass

def func2[T](arg1: int, arg2: T) -> T:
    pass

def func3[T](arg1: list[T], arg2: T) -> bool:
    pass

def func4[T, U](arg1: T, arg2: U) -> tuple[T, U]:
    pass


"""
Syntax > 3.12 [T]
Syntax < 3.12 T
"""
from typing import TypeVar

T = TypeVar("T")

def do_nothing(arg: T) -> T:
    return arg

