"""
Examples from https://realpython.com/python-tuple/#exploring-other-features-of-tuples

* Allows to create immutable data
* Sequences
* Great for heterogeneous data
* Allows to store any kind of data
* Access elements by indexes
* Can be nested
* Iterable
* Allow to slice

Useful when:
    * ensure data integrity: Immutable data
    * reduce memory consumption
    * improve performance
"""

red = (255, 0, 0)

record = ("John", 25, "Python developer")

print(record)
print(record[0])

"""
Creating tuples
"""
tuple_1 = "one", "two"
tuple_2 = ("three", "four")
empty = ()

print(type(empty))

"""
With single element
- needs comma to created!
"""
one_word = ("Hello",)

print(type(one_word))

"""
Tuple constructor
"""
print(type(tuple([1, 2, 3])))
print(tuple("Pythonista"))
print(tuple({
    "manufacturer": "Boeing"
}))

"""
Generator expression
"""
tuple(x ** 2 for x in range(10))

"""Unpacking"""
point = (1, 23, 10)

x, y, z = point

"""elegant swapping variables values"""
a = 200
b = 400

b, a = a, b

print(a, b)

"""
In case while using classical unpacking the number of variables must be correct. 
When not, the exception will be raised

NOT
values = (1, 2, 3)

a, b  = values
"""

"""Unpacking with unpacking operator '*' """
numbers = (1, 2, 3, 4)

*head, last = numbers

"""Merge tuples to create new one"""
name = ("Marcin", "Developer")
contact = ("email@address",)

user = (*name, *contact)

print(head, last)

"""Returning tuples form functions"""


def find_extremes(iterable):
    data = tuple(iterable)
    if len(data) == 0:
        raise ValueError("Empty iterable")
    # returning tuple but without parenthesis
    # we're not expecting mutating data
    return min(data), max(data)


person_one = ("name", "surname")

person_two = person_one[:]

print(id(person_one) == id(person_two)) # True

from copy import deepcopy

two = deepcopy(person_one)

print(id(person_one) == id(two)) # True

"""Concatenation"""

print(
    ("marcin",) + ("developer",)
)

"""Repeating content of tuple"""
print(
    (1, 2, 3) * 2
)

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

print(days[::-1]) # or use tuple(reversed(days))

"""Iterating"""

months = (
    ("January", 1000)
)

# for index, (month, amount) in enumerate(months, start=1):
#     print(index, month, amount)


"""Tuples API"""

cars = (
    "Honda",
    "BMW"
)

print(cars.count("Honda"))
print(cars.index("Honda"))

"""
Named tuples
* Immutable
* Access to named fields by dots
"""

from collections import namedtuple

Person = namedtuple("Person", "name age position")

person = Person("John", 24, "Python developer")

print(
    person.name,
    person.age,
    person.position
)

"""
    Named tuples with typing
    * still immutable
"""
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    age: int
    position: str = "Python developer"

