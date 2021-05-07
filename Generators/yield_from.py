"""
- For nested generators use the keyword 'yield from' to connect to one generator
"""

def child():
    for i in range(1_000_000):
        yield i


def slow():
    for i in child():
        yield i


"""Using `yield from` is faster"""
def fast():
    yield from child()
