from typing import assert_never


def pretty_print(val: int | float | str) -> None:
    if isinstance(val, int):  # assert_type(val, int)
        print(f"Integer: {val}")

    elif isinstance(val, float):  # assert_type(val, float)
        print(f"Float: {val}")

    elif isinstance(val, str):  # assert_type(val, str)
        print(f"String: {val}")

    else:
        assert_never(val)


"""
TypeGuard usage example
"""
from typing import TypedDict, TypeGuard


class Person(TypedDict):
    name: str
    age: int


def is_person(val: dict) -> TypeGuard[Person]:
    try:
        name, age = val["name"], val["age"]
    except KeyError:
        return False

    return len(name) > 1 and 0 < age < 150


def print_age(val: dict) -> None:
    if is_person(val):  # assert_type(val, Person)
        print(f"Age: {val['age']}")
    else:
        print("Not a person!")