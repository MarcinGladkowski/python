""" From https://realpython.com/python-catch-multiple-exceptions/"""

"""Separate except clause"""
try:
    first = float(input("What is your first number ? "))
    second = float(input("What is your second number ? "))
    print(f"{first} divided by {second} is {first / second}")
except ValueError:
    print("You must enter a number")
except ZeroDivisionError:
    print("You can't divide by zero")

""" catch both types as tuple"""
try:
    first = float(input("What is your first number ? "))
    second = float(input("What is your second number ? "))
    print(f"{first} divided by {second} is {first / second}")
except (ValueError,  ZeroDivisionError):
    print("There was an error")

"""Get error object"""
try:
    first = float(input("What is your first number ? "))
    second = float(input("What is your second number ? "))
    print(f"{first} divided by {second} is {first / second}")
except (ValueError,  ZeroDivisionError) as error:
    print(f"A {type(error).__name__} has occured")

"""
How to get all Error classes ?

# error_codes.py

import os
import errno
from pprint import pprint

pprint({e: os.strerror(e) for e in sorted(errno.errorcode)})
"""

"""Using Exceptions Groups ( > 3.11)"""
exceptions = [ZeroDivisionError(), FileNotFoundError(), NameError()]
zd_errors = fnf_errors = name_errors = 0

try:
    raise ExceptionGroup("Errors occurred", exceptions)
except* ZeroDivisionError:
    zd_errors += 1
except* FileNotFoundError:
    fnf_errors += 1
except* NameError:
    name_errors += 1
finally:
    print("Count errors!")




