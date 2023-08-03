"""
Amdahl's law (to check)
* Two built in tools for profiling 'profile' and 'cProfile'
* Use cProfile instead profile
"""
from random import randint
from cProfile import Profile
from pstats import Stats
from bisect import bisect_left


def insertion_sort(data):
    result = []
    for value in data:
        better_insert_value(result, value)
    return result


def better_insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

profiler = Profile()
profiler.runcall(test)


stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()


