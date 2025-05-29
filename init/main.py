"""
__init__ method in Python is a special method that is called when an object is created.
__new__ is called to create a new instance
"""


class Person:
    def __init__(self, name):
        self.name = name


john = Person("John")
print(john.name)

# call as method, mutating the object
john.__init__('Steve')

print(john.name)

my_list = [23, 45, 56]
my_list.__init__(range(10))

print(my_list)

f = 0.5
f.__init__(0.6)

print(f) # not mutated


class SubFloat(float):
    def __init(self, value, arg):
        super().__init__(value)

"""This proving that is something called before __init__ is called,"""
# sf = SubFloat(2.0, 'arg') # ERROR


"""Correct implementation"""
class NewSubFloat(float):
    def __new__(cls, value, arg):
        return super().__new__(cls, value)


sf = NewSubFloat(2.0, 'arg')


from math import isclose

class TolerantFloat(float):
    def __new__(cls, value, rel_tol):
        # create float
        instance = super().__new__(cls, value)
        # save relative tolerance
        # saving it by __init__ method will be
        # partially mutable
        instance.rel_tol = rel_tol
        # return
        return instance

    def __eq__(self, other):
        return isclose(self, other, rel_tol=self.rel_tol)


x = TolerantFloat(0.5, rel_tol=0.1)
print(x == 0.51)
print(x == 0.42)




