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