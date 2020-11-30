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