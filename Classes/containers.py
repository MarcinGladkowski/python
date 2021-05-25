from containers.abc import Sequence

'''
A lot of classes are just bags for data inheritance from list or dict
but remember you can use classes from containers.abc!
'''

'''Example of implementation of class implementing list'''


class Frequency(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


class BadType(Sequence):
    pass


foo = BadType()
