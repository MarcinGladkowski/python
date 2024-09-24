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
    def __init__(self, capacity):
        """
        self.pairs should not be accessed directly


        -- Defensive copying --

        Access to them should return copy to prevent
        modifying original data structure.

        -- Internal implementation --

        leading underscore _property indicates the
        internal implementation

        """
        self._pairs = capacity * [None]

    def __len__(self):
        return len(self._pairs)

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

    @property
    def keys(self):
        return {pair.key for pair in self._pairs if pair}

    @property
    def pairs(self):
        return [pair for pair in self._pairs if pair]

    @property
    def values(self):
        return [pair.value for pair in self._pairs if pair]

    def _index(self, key):
        return hash(key) % len(self)
