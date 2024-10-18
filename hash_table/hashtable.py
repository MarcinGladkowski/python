from collections import namedtuple, deque

"""
Python Glossary

Sentinel value
Space-time tradeoff https://en.wikipedia.org/wiki/Space%E2%80%93time_tradeoff
Sweet Spot

Addressing hash collisions:
- Perfect hashing (https://en.wikipedia.org/wiki/Perfect_hash_function)
- Open addressing
- Closed addressing

Open addressing:
- Cuckoo hashing
- Double hashing
- Hopscotch hashing
- Quadratic hashing
- Robin Hood hashing
"""


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
    def __init__(self, capacity: int = 8, load_factor_threshold: float = 0.6):
        """
        self.pairs should not be accessed directly


        -- Defensive copying --

        Access to them should return copy to prevent
        modifying original data structure.

        -- Internal implementation --

        leading underscore _property indicates the
        internal implementation

        """
        if capacity < 1:
            raise ValueError('Capacity must be a positive number')
        if not (0 < load_factor_threshold <= 1):
            raise ValueError('Load factor threshold must be between 0 and 1')

        self._keys = []
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold

    def __len__(self):
        return len(self.keys)

    def __setitem__(self, key, value):
        """
        Methods is called every time when we use [key] = value
        Previous implementation:
        self._pairs[self._index(key)] = Pair(key, value)
        """
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair is None or pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            #self._resize_and_rehash() # ?
            bucket.append(Pair(key, value))
            self._keys.append(key)

    def __getitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for _, pair in enumerate(bucket):
            if pair.key == key:
                return pair.value
        raise KeyError(key)


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
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del self._buckets[index]
                self._keys.remove(key)
                break
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
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    @property
    def keys(self):
        return self._keys.copy()

    @property
    def pairs(self):
        return [(key, self[key]) for key in self.keys]

    @property
    def values(self):
        return [self[key] for key in self._keys]

    @property
    def capacity(self):
        return len(self._buckets)

    @property
    def load_factor(self):
        occupied_or_deleted = [pair for pair in self._buckets if pair]
        return len(occupied_or_deleted) / self.capacity

    def _index(self, key):
        return hash(key) % self.capacity

    def _probe(self, key) -> [int, Pair]:
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._buckets[index] # _slots
            index = (index + 1) % self.capacity

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

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets


