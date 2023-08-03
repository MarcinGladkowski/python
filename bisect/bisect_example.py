"""
Use bisect when search value in sorted data.
* For advantage usage help(bisect)
"""
from bisect import bisect_left


# linear search
data = list(range(10**5))
index = data.index(91234)
assert index == 91234


index = bisect_left(data, 91234)
assert index == 91234

index = bisect_left(data, 91234.56)
assert index == 91234


