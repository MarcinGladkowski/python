"""
source mathspp

More advanced: https://mathspp.com/blog/pydonts/decorators
"""


def function_cache_decorator(func):
    """
    Simple decorator that caches the return value of a function
    Defined as function
    """
    cache = {}
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper


class CacheDecoratorClass:

    def __init__(self, func):
        self.cache = {}
        self.func = func

    def __call__(self, *args, **kwargs):
        if args not in self.cache:
            self.cache[args] = self.func(*args, **kwargs)
        return self.cache[args]


class CacheTrackDecoratorClass:

    def __init__(self, func):
        self.cache = {}
        self.func = func
        self.hits = 0
        self.misses = 0

    def __call__(self, *args, **kwargs):
        if args not in self.cache:
            self.cache[args] = self.func(*args, **kwargs)
            self.misses += 1
            return self.cache[args]

        self.hits += 1
        return self.cache[args]

    def clear(self):
        """
        As a decorator it can be used as fib.clear()
        """
        self.cache = {}
        self.hits = 0
        self.misses = 0


@CacheDecoratorClass
def fib(num):
    """
    Usage of decorators
    @function_cache_decorator
    @CacheDecoratorClass

    Adding Class decorator became function fib() as a class type (object)
    """
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)

print(fib(34))
