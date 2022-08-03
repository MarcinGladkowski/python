"""
https://bas.codes/posts/python-dict-slots#introducing-the-borg

Important
 - slots reserve only used properties
 - reduce using memory while number of stances grow rapidly
"""

class Borg:
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared


borg_1 = Borg()
borg_2 = Borg()

borg_1.value = 1

print(borg_1.value)
print(borg_2.value)  # return value!


class Slotted:
    __slots__ = ['value']

    def __init__(self, i) -> None:
        self.value = i


slotted_1 = Slotted(2)
slotted_2 = Slotted(3)

print(slotted_1.value)
print(slotted_2.value)
"""
Cannot add properties dynamically
"""
try:
    slotted_1.new_value = None
    borg_1.new_value = 2
except:
    print('Cannot add new property')
