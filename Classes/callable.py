from containers import defaultdict

"""
Functions and methods in Python are higher order. Its mean they are can be uses 
as arguments
"""


class CountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added += 1
        return 0


counter = CountMissing()
counter() == 0
assert callable(counter)

increments = {
    ('product1', 1),
    ('product2', 2)
}

current = {
    ('product3', 10)
}
"""Example of usage"""
result = defaultdict(counter, current) # use and __call__ method from counter
for key, amount in increments:
    result[key] += amount
assert counter.added == 3