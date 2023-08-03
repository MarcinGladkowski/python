"""
IS vs ==

is - check is the object is the same in the memory (you can check it by id())
== - comparison of values od objects
"""
a  = [1, 2, 3]
b = a # reference to exactly the same variable

print(a == b)
print(a is b)

c = list(a) # create a shallow copy
print(a == c)
print(a is c)

assert id(a) == id(b)
assert id(a) == id(c)

