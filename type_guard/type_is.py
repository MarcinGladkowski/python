import sys

if sys.version_info > (3, 13):  # TypeIs is available in Python 3.13+
    from typing import TypeIs
else:
    from typing_extensions import TypeIs


def is_number(value: object) -> TypeIs[int | float | complex]:
    return isinstance(value, (int, float, complex))


def pretty_print(val: str | int | float | complex) -> None:
    if is_number(val):  # assert_type(val, int | float | complex)
        print(val)
    else:  # assert_type(val, str)
        print("Not a number!")