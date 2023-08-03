import logging
from functools import cached_property, cache
from time import sleep


class Point:
    """
    Class implements getters & setters

    Using underscore _ is only convention!

    Python does not have access modifiers like
    public, private, protected
    """

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y


class PythonicPoint:
    """
    Using getters and setters is not
    Pythonic way
    """

    def __init__(self, x, y) -> None:
        self.y = y
        self.x = x


class Circle:

    def __init__(self, radius) -> None:
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, radius):
        print("Set radius")
        self._radius = radius

    def _del_radius(self):
        print("Del radius")
        del self._radius

    radius = property(
        fset=_set_radius,
        fget=_get_radius,
        fdel=_del_radius,
        doc="The radius property"
    )


circle = Circle(10)
print(circle.radius)
circle.radius = 100
print(circle.radius)


class CircleProperty:
    """
    Using property() as a decorator

    We don't need to implement methods
    like get(), set(),

    Using property decorator:
    - @property decorator must decorate the getter method

    - The docstring must go in the getter method

    - The setter and deleter methods must be decorated with the
      name of the getter method plus .setter and .deleter, respectively.

    """

    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        """The radius property"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        print("Set radius")
        self._radius = radius

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius


class PointReadOnly:
    """
    Providing read-only attributes

    Immutable x and y
    """

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class WriteCoordinateError(Exception):
    pass


class PointValidationSetters:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.x

    # @property.setter
    # def x(self, value):
    #     raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self):
        return self.y

    # @property.setter
    # def y(self, value):
    #     raise WriteCoordinateError("y coordinate is read-only")


class CircleReadWrite:
    """

    """

    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


circle_read_write = CircleReadWrite(10)
print(circle_read_write.radius)
circle_read_write.diameter = 100
print(circle_read_write.diameter)
print(circle_read_write.radius)


class ValidatedPoint:
    """
    EAFP style - easier to ask for forgiveness than permission.

    .setter methods with validation are also invoked during initialization
    an object.
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None


validated_point = ValidatedPoint(1, 2)


class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        try:
            instance.__dict__[self._name] = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None


class DescriptorPoint:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


descriptor_point = DescriptorPoint(10, 20)


class Rectangle:
    """
    Providing computed attributes

    - return lazy attribute
    """

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.width * self.height


class Product:
    """
    Providing computed attributes

    - formatting value
    """

    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price

    def price(self):
        return f"${self._price:,.2f}"


class CachedCircle:
    """
    Using caching from standard library

    - allows mutations without modifying
    """

    def __init__(self, radius) -> None:
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(5)
        return self.radius * 2


cached_circle = CachedCircle(10)
print(cached_circle.diameter)
print(cached_circle.diameter)


class CachedNoModifying:
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    @cache
    def diameter(self):
        sleep(5)
        return self.radius * 2


cached_circle_read_only = CachedNoModifying(10)
print(cached_circle_read_only.diameter)
# cached_circle_read_only.diameter = 100 cannot set!
print(cached_circle_read_only.diameter)

logging.basicConfig(
    format="%(asctime)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)


class LoggedCircle:
    def __init__(self, radius) -> None:
        self._msg = '"radius" was %s. Current value: %s'
        self._radius = radius

    @property
    def radius(self):
        """The radius property"""
        logging.info(self._msg % ("accessed", str(self.radius)))
        return self._radius

    @radius.setter
    def radius(self, value):
        """The radius property setter"""
        try:
            self._radius = float(value)
            logging.info(self._msg % ("mutated", str(self.radius)))
        except ValueError:
            logging.info('Validation error while mutating "radius"')

"""
@see https://mathspp.com/blog/pydonts/properties

Here's the main takeaway of this Pydon't, for you, on a silver platter:

“property is the Pythonic interface for adding dynamic behaviour to your interactions with attributes in classes.”

This Pydon't showed you that:

you can add dynamic dependencies between your class attributes;
the decorator property will turn a method into a property attribute of the same name;
there are a couple of rules of thumb to decide when to use a property;
properties can be used to implement read-only attributes;
property attributes can also be set if one makes use of the decorator @xxx.setter;
you can use setters to add some data validation and normalisation to attribute setting;
property attributes can also have deleter methods;
the decorator property isn't really a decorator, but a descriptor (whatever that may mean); and
the standard library has plenty of properties.
"""

class Person:
    def __init__(self, first, last) -> None:
        self._first = first
        self._last = last


    @property
    def first(self):
        return self._first


user = Person('Jan', 'Kowalski')
user._first = 'name' # because property is set to 'first' but we can change _first
print(user.first)