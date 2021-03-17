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

# omit first index for more clear code
assert test[:3] == test[0:3]
# omit last index
assert test[2:] == test[2:len(test)]

'''
negative values - works from end on the list
'''
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a)
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

'''
unpack values from list
'''
b, c = a[:2]

'''
modifying
'''
print('\nModifying\n')
print(f'Start table {a}')

e = a[3:]
e[1] = 'test'
print(e)
print(a)

a[2:7] = ['test1', 'test2', 'test3']
print(a)

'''
without indexes - copy
'''
g = a[:]

print(g)

'''
g = a[:] - copy (shall probably)
g = a - assert a is b # this is the same object - reference to the same place in memory
'''

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