'''
* Private and public attributes
* Protected style _ <- one underscore
* Child class cannot access to private parent attributes!
'''


class MyObject:
    """
    Public: self.attribute
    Private: self.__attribute
    """
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

'''Access to public attribute'''
foo = MyObject()
assert foo.public_field == 5

'''Access to private attribute'''
assert foo.get_private_field() == 10


class ChildClass(MyObject):
    """AttributeError!"""
    def get_private_field(self):
        return self.__private_field


child = ChildClass()
# child.get_private_field()
assert child._MyObject__private_field == 10 # some hack!

print(child.__dict__)

