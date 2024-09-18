"""
Mappings are iterable and accessible data by keys

Methods:
    .keys()
    .values()
    .items()
"""

elements = {
    "one": 1,
    "two": 2,
}

try:
    elements["three"]
except KeyError:
    print("key not exists")


# another solution for not existing keys
from collections import defaultdict

elements_default = defaultdict(
    lambda: 0,
    elements
)

elements_default['three'] # no error, returns 0

# another type of collection mapping
from collections import Counter

letters = Counter('learning python')
"""Contains methods like key(), values(), items()"""
print('l' in letters)