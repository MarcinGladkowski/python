"""BAD PRACTICE: Do not assign lambda function to variable"""
import operator


f = lambda x: x + 1
"""GOOD PRACTICE"""
def f(x):
    return x + 1


left = [1, 2, 3]
right = [4, 5, 6]

print(*map(lambda x, y: x + y, left, right))  # BAD PRACTICE
print(*map(operator.add, left, right))  # GOOD PRACTICE - wrapping by lambda function is not needed


"""BAD PRACTICE - not needed to using lambda function"""
def some(x: any):
    return True

print(*map(lambda x: some(x), [1, 2, 3]))

"""GOOD PRACTICE"""
print(*map(some, [1, 2, 3]))


"""BAD PRACTICE"""
values = ['Hello', 'World']

print(*map(lambda x: x.upper(), values))

"""GOOD PRACTICE"""
print(*map(str.upper, values))


