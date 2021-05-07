import itertools

"""
Python has built in tools to help with iterators and generators
type: help(itertools)
"""

# help(itertools)

"""chain()"""
it = itertools.chain([1, 2], [3, 4])

"""repeat()"""
it = itertools.repeat('Hello world!', 3)

"""cycle()"""
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]

"""zip_longest()"""

