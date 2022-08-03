"""
Examples based on https://bas.codes/posts/python-involuntary-borgs
"""

first = second = []

first.append('one')
first.append('two')
first.append('three')

print(first, second)


class User:
    """
    Class attribute

    Python interpreters these properties once
    and will be changed with reference
    """
    permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)


user1 = User()
user2 = User()

user1.add_permission('admin')
user1.add_permission('user')
"""
Those permissions will be add to each instance of class User
"""
print(user1.permissions, user2.permissions)


class BetterUser:
    """
    Adding properties in __init__ method creates
    instance attributes
    """
    def __init__(self) -> None:
        self.permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)


user3 = BetterUser()
user3.add_permission('super admin')

user4 = BetterUser()

print(user3.permissions, user4.permissions)


def add(element, elements=[]):
    elements.append(element)
    return elements

elements = add('one')
elements = add('two')

second_list = ['three']
second_list = add('four', second_list)

third_list = add('five')

print(elements)
print(second_list)
print(third_list) # has 'one' and 'two'


def better_add(element, better_elements=None):
    if better_elements is None:
        better_elements = []
    better_elements.append(element)
    return better_elements


better_elements = better_add('six')
better_elements = better_add('seven', better_elements)

better_elements_second = better_add('eight')

print(better_elements, better_elements_second)

