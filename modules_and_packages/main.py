"""
* https://realpython.com/python-init-py

__init__.py declares a folder as a regular python package
Without this file directory is treated as namespace package
Importing packages is faster

module vs package in python

modules help organize python single files but packages helps organize multiple python modules

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