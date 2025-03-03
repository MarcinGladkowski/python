"""
Literal pattern

Python doc: https://peps.python.org/pep-0635/#literal-patterns

Data Type	Literal Pattern Example	Matched By
bytes	    b"\xf0\x9f\x90\x8d"	    Equality
str	        "admin"	                Equality
int	        -42	                    Equality
float	    4.2	                    Equality
complex	    4.2 + 2.3j	            Equality
bool	    True, False	            Identity
NoneType	None	                Identity
"""


def get_http_status(is_admin):
    """Compare by identity, not value"""
    match is_admin:
        case True:
            return "200 OK"
        case False:
            return "403 Forbidden"
        case None:
            return "302 Found"
        case _:
            return "400 Bad Request"


"""
bool class is a subclass of int

result:
     1: 400 Bad Request
   1.0: 400 Bad Request
(1+0j): 400 Bad Request
  True: 200 OK
"""
for is_admin in 1, 1.0, 1.0 + 0.0j, True:
    print(f"{is_admin!r:>6}:", get_http_status(is_admin))

"""Reverse example"""
age = 21
match age > 18:  # expression is evaluated as a True
    case 1.0:  # value equality
        print("You're an adult.")

"""
Value pattern
"""
HELP_COMMAND = 'help'


class ClassCommand:
    EXIT_COMMAND = 'exit'


def repl_using_variables():
    match input("Type a Python command: "):
        case command if command == HELP_COMMAND:  # called every time, no matter what you wrote
            print('Called help')
        case ClassCommand.EXIT_COMMAND:
            print("Goodbye!")
            exit()


# repl_using_variables()

"""
Capture pattern

Python documentation: https://peps.python.org/pep-0635/#capture-patterns
"""


def capture_pattern():
    match input("Type a Python command: "):
        case command:
            print(f"Captured local variable {command}")

    return command


print(capture_pattern())

"""
Sequence pattern

Python documentation: https://peps.python.org/pep-0635/#sequence-patterns
"""

"""
Mapping pattern

"""

"""
Class pattern
"""

from datetime import UTC, datetime


def parse(value):
    match value:
        case datetime():
            return value.astimezone(UTC)
        case int() | float():
            return datetime.fromtimestamp(value, UTC)
        case str():
            return datetime.fromisoformat(value).astimezone(UTC)
        case _:
            raise TypeError(f"Unsupported type: {type(value)}")


def aoc_status(date):
    match date:
        case datetime.date(year=_, month=12, day=1):
            print("Advent of Code starts today!")
        case datetime.date(year=_, month=12, day=day) if day <= 25:
            print(f"{25 - day} days until the end of AoC.")
        case _:
            print("Sorry, no Advent of Code today.")


from typing import NamedTuple


class Date(NamedTuple):
    year: int
    month: int
    day: int

"""Using wildcard for year"""
match Date(1969, 7, 20):
    case Date(_, 7, 20):
        print("Celebrating another moon landing anniversary!")
