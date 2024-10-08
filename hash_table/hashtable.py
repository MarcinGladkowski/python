from collections import namedtuple
from typing import NamedTuple, Any

BLANK = object()

# class Pair(NamedTuple):
#     key: Any
#     value: Any

Pair = namedtuple(
    'Pair',
    ['key', 'value']
)


class HashTable:
    """
        For exercise to implement:
        https://realpython.com/python-bitwise-operators/
        https://peps.python.org/pep-0584/
    """
    def __init__(self, capacity: int):
        """
        self.pairs should not be accessed directly


        -- Defensive copying --

        Access to them should return copy to prevent
        modifying original data structure.

        -- Internal implementation --

        leading underscore _property indicates the
        internal implementation

        """
        if (capacity < 1):
            raise ValueError('capacity must be at least 1')

        self._pairs = capacity * [None]

    def __len__(self):
        return len(self.pairs)

    def __setitem__(self, key, value):
        """
        Methods is called every time when we use [key] = value
        """
        self._pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, item):
        """
        Supports in/not in accessing
        """
        try:
            self[item]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        if key in self:
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def __iter__(self):
        """
        Make class iterable to use it in loops

        keyword: yield for using as generator iterator

        for key in instance:
            # ...
        """
        yield from self.keys

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}") # !r cals __repr__ adding single apostrophes
        return "{" + ", ".join(pairs) + "}"

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    @property
    def keys(self):
        return {pair.key for pair in self._pairs if pair}

    @property
    def pairs(self):
        return {pair for pair in self._pairs if pair}

    @property
    def values(self):
        return [pair.value for pair in self._pairs if pair]

    @property
    def capacity(self):
        return len(self._pairs)

    def _index(self, key):
        return hash(key) % self.capacity

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), capacity=self.capacity)

    def clear(self):
        """To implement as exercise"""
        pass

    def update(self):
        """To implement as exercise"""
        pass

