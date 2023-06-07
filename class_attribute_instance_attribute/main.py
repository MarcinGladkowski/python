"""
Class attributes - will be shared across all instances of this class!
Useful when you need to share sth between instances
"""

class MyClass:
    """
    Class with instance attribute
    """
    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value


instanceAttribute = MyClass('test')
print(instanceAttribute.value)

try:
    instanceAttribute.value = 10
except AttributeError:
    print("Can't access!")


class MyClass2:
    """
    Class with class attributes
    """
    _value = None

    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value


classAttribute2 = MyClass2('test')
print(classAttribute2.value)

try:
    classAttribute2.value = 10
except AttributeError:
    print("Can't access!")


class Example:
    """
    Class attribute
    """
    test = 1
    pass


class SecondExample:
    """
    Instance attribute:
    The 'self' keyword holds a reference to the current instance

    """
    def __init__(self) -> None:
        """
        Cannot access by SecondExample.test
        """
        self.test = 1


example = Example()

second_example = SecondExample()
second_example.second_test = 2 # instance attribute

"""
    Check all attributes by __dict__ method
    Checks instance attributes first and then class attributes
"""

print(example.test)
print(example.__dict__)
print(second_example.__dict__)


class ObjectCounter:
    num_instances = 0

    def __init__(self) -> None:
        type(self).num_instances += 1
        # ObjectCounter.num_instances += 1
        
        
ObjectCounter()        
ObjectCounter()        
ObjectCounter()

print(
    ObjectCounter().num_instances
)




