import functools

"""
We have to start from understand Stacks

A stack is a data structure that holds a sequence of data and only lets you interact with the topmost item.

FILO (cards exmaple)

Operations: PUSHING, POPPING


Recursion should be using when the problem is like a tree (have many branches)
Python has a limit of 1000 functions on a stack

"""


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


print('Factorial', factorial(5))

"""
Next well known example is Fibonacci!

Why is bad ? Try to execute recursion example for 35 number and bigger! 
It's ok but for very small numbers
"""


def simple_fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1
    return simple_fibonacci(nth - 2) + simple_fibonacci(nth - 1)


print('Simple fibonacci', simple_fibonacci(7))

'''
To improve it we should cache functions results
'''

FIB_CACHE = {}


def cached_fib(n):
    if n in FIB_CACHE:
        return FIB_CACHE[n]

    if n == 1 or n == 2:
        return 1

    FIB_CACHE[n] = cached_fib(n - 2) + cached_fib(n - 1)

    return FIB_CACHE[n]


@functools.lru_cache()
def simple_fibonacci_with_decorator(nth):
    """
        example with specific decorator for it
    """
    if nth == 1 or nth == 2:
        return 1
    return simple_fibonacci_with_decorator(nth - 2) + simple_fibonacci_with_decorator(nth - 1)
