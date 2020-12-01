# Source: https://realpython.com/python-lists-tuples/

# lists:
# - ordered
# - can contain each objects
# - can be nested
# - mutable
# - dynamic
# - elements needn't be unique
# - can be accessed by the index

test = [12, 'foobar', 3.3, False, len, int]
print(test[0]) # first element
print(test[-1]) # last element
print(test[1:2]) # 'foobar', 3.3
print(test[::-1]) # reverse list
print(test[:]) # returns a copy of list (another behaviour on string)

# use 'in' and 'not in'
'foobar' in test
'barbar' not in test

# + and *
test + ['another']
test * 2

# len(), min(), max()

# Nesting lists
x = ['a', 'b', ['c', 'd']]
x[3][1];


# Mutable
# change series of elements in array
test[1:3] = [1, 2, 3]

# delete elements
test[1:3] = []
# or
del test[1:3]

# appending
a = ['foo', 'bar']
a += 20 # Error

a += [20] # singleton list

'''
Example methods on lists:
- append()
- extend()
- insert()
- remove()
- pop()
'''