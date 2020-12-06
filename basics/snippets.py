import sys
# * in python ?


def all_unique(list):
    return len(list) == len(set(list))


x = [1, 1, 2, 2, 3, 4]
y = [1, 2, 3, 4, 5]

print(all_unique(x))
print(all_unique(y))

print(set([1, 1, 2, 3]))

# memory
test_var = 30
print(sys.getsizeof(test_var))


# byte size
def byte_size(string):
    return len(string.encode('utf-8'))


print(byte_size('Test'))

# multiplying string
print('test' * 2)


# filter falsy values

to_filter = [0, "", False, None]

to_filter_mixed = [0, 1, "", 2, False, 3, None]

print(list(filter(None, to_filter)))
print(list(filter(None, to_filter_mixed)))

# Transposition
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(list(transposed))

# Capital first letter
print('title'.title())

# Palindrome
name = 'Name'
print(name[::-1]) # emaN


def palindrome(a):
    return a == a[::-1]


# Get default variable is not in dictionary
d = {'a': 1, 'b': 2}
print(d.get('c', 3))

