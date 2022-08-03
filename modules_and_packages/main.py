"""
We can use __all__ what is imported when * is using for it.
"""

import sys
import mod

print(mod.a)
print(mod.s)
print(mod.foo('test'))
print(mod.Foo)

print(sys.path)

print(mod.__file__)