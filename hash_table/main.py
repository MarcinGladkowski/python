"""
One of the most usage data structure

One of implementation in python is dict()

HASH TABLE vs DICTIONARY

Dictionary are also known as maps or associative arrays
"""

"""
Check which python algorithm Python is using 
"""
import sys

print(sys.hash_info.algorithm)

import string
from pprint import pprint

from python_crash_course.alien_invasion import character

text = string.ascii_uppercase * 100_000_000

text[:-1] # fast event there is bilions s of elements

"""
Formula for find element

element_address = offset + (element_size * element_index)
"""

"""HASH"""
pprint(hash(3.14))
pprint(hash(3.141592653589793))
pprint(hash('This is a custom test to be hashed'))

assert hash("Lorem") == hash("Lorem")

"""
vulnerability for hash

* set custom env variable to make hash function more predicable
set PYTHONHASHSEED=1

* -c parameter
* result of hash() can be negative number
"""
pprint(hash(None))

class Person:
    pass

pprint(hash(Person))


"""Trying to predict hash distribution"""
pprint(hash("Lorem"))
pprint(hash("Loren"))

pprint(hash(42)) # still 42

"""
Compare objects with hash functions

built-in function id()
* based on the memory address
* memory addresses are predicable
"""
pprint(id("Lorem"))

"""Make your own hash function"""

def hash_text_function(text: str) -> int:
    return sum(ord(character) for character in text)

pprint(hash_text_function('Lorem')) # 511
pprint(hash_text_function('Lorem')) # 511
pprint(hash_text_function('Loren')) # 512

pprint(hash_text_function('Loner')) # hash collision


def hash_function_to_str(key):
    return sum(ord(character) for character in str(key))


assert hash_function_to_str('3.14') == hash_function_to_str(3.14) # hash collision


def hash_function_based_on_index(key):
    """
    Slow fro larger inputs 'This is very long input' * 1_000_000_000
    """
    return sum(
        index * ord(char)
        for index, char in enumerate(repr(key), start=1)
    )

# from hash_distribution import plot, distribute
# from string import printable
#
# plot(distribute(printable, 6, hash_function_based_on_index))
