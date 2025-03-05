"""
We can use __all__ what is imported when * is using for it.

__init__.py -> they are optional from Python 3.3
* can be empty files

my_package/
    __init__.py
    some_module.py
will allow you to run:

import my_package.some_module
# or
from my_package import some_module
"""

import sys
import mod

print(mod.a)
print(mod.s)
print(mod.foo('test'))
print(mod.Foo)

print(sys.path)

print(mod.__file__)