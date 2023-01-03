'''
__new__() of metaclass - is called after class keyword
metaclasses can check structure of class before creation of instance
__init_subclass__() - use to check/validate child classes before initialization

'''
import json

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* Wykonywanie {meta}.__new__() dla {name}')
        print('Bazowe:', bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass


my_class = MyClass()

'''
Example with checking props before initialization (before creating new instance)
'''


class ValidatePolygon(type):
    def __new__(mcs, name, bases, class_dict):
        # no checking for abstract class Polygon
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('The min value is 3!')
        return type.__new__(mcs, name, bases, class_dict)


class Polygon(metaclass=ValidatePolygon):
    sides = None  # will defined by child classes

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9


# IT RAISE AN ERROR! - metaclass check sides prop before initialization!
# class Line(Polygon):
#     print('Before assign sides')
#     sides = 2
#     print('After assign sides')


assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260

'''
From Python 3.6 creating metaclasses is not necessary
We can use: __init_subclass__
'''


class BetterPolygon():
    sides = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('The min value is 3!')

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Hexagon(BetterPolygon):
    sides = 6


assert Hexagon.interior_angles() == 720

'''
Registration of existing classes by using __init_subclass
'''


class Serializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class Deserialize(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class Point2D(Deserialize):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'


point = Point2D(2, 4)
print('Object', point)
print('Serialized', point.serialize())

serialized = point.serialize()

deserialize = Point2D.deserialize(serialized)

print('Object after deserialize', deserialize)