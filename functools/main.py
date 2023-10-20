"""
Cache (memoize)

- useful when we have repetitive results, calculations
- for properties @cached_property
"""
from functools import cache


@cache
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 1)


for i in range(40):
    print(fibonacci(i))

"""
Freeze functions
"""
from functools import partial

print_no_line = partial(print, end=",")

for _ in range(3):
    print('test')

for _ in range(3):
    print_no_line('test')

square = partial(pow, exp=2)
print('\n')
print(square(4))
print(square(5))

"""
Allow multiple implementation
"""
from functools import singledispatch


@singledispatch
def process(data):
    """Default behavior for unrecognized types."""
    print(f"Received data {data}")


@process.register(str)
def _(data):
    """Handle string objects"""
    print(f"Processing a string {data}")


@process.register(int)
def _(data):
    """Handle int objects"""
    print(f"Processing a int {data}")


@process.register(list)
def _(data):
    """Handle list objects"""
    print(f"Processing a int {data}")


process(42)  # Outputs: Processing an integer: 42
process("hello")  # Outputs: Processing a string: hello
process([1, 2, 3])  # Outputs: Processing a list of length: 3
process(2.5)  # Outputs: Received data

"""
Writing decorators
"""
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapped

@my_decorator
def hello(name: str):
    """Print hello message"""
    print(f"Hello {name}")


"""
Aggregating data
"""
from functools import reduce
import operator

numbers = list(range(1, 11))

print(reduce(operator.add, numbers))
