from collections.abc import MutableMapping
'''
Until Python3.5 the dict returns keys and values in random order -
not he order how the dict was filled.

'''
pets_names = {
    'cat': 'Ksy Ksy',
    'dog': 'JSON'
}

print(pets_names)

'''
Display keys of object
'''


class MyClass:
    def __init__(self):
        self.dog = 'JSON'
        self.cat = 'Ksy Ksy'


pets = MyClass()
for key, value in pets.__dict__.items():
    print(f"{key} = {value}")


'''
Working with objects which looks like dicts
ex: module Collections.abc
'''

votes = {
    'pet1': 1281,
    'pet2': 587,
    'pet3': 863
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}

populate_ranks(votes, ranks)
print(ranks)

winner = get_winner(ranks)
print(winner)

'''
Custom class to implement object with behaviour like dict
'''
class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()

populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)

winner = get_winner(sorted_ranks)
print(winner)

'''
- Not write code to believe on ordering of put values
- Add type hinting to dict
- Check is these parameters are dicts and not similar classes
'''
#78