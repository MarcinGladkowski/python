# Source: https://realpython.com/python-dicts/

# Main diff is accessing to elements: by keys
# Can be mutable
# Any duplicates
# Dictionary key must be type that is immutable!

colors = {
    'main': 'red'
}

# other initialization

colors = dict([
    ('main', 'red')
])

colors = dict(
    main='red'
)
print(type(colors)) # dict
print(colors)

# cannot access by numeric index! - but is some trick! c = {1: 'test'} => c[1] works!

print(colors['main'])
# KeyError: print(colors['not_exits'])

# add new key:
colors['default'] = 'blue'
print(colors)

del colors['default']
print(colors)

# other types can also be an key in dictionary
t = {
    1: 'test',
    2.2: 'test2',
    '3': 'test3',
    True: 'test4',
    (1, 1): 'test5',  # tuple
}

# when use list as a key: TypeError: unhashable type: 'list' because:
print(hash(1))
# print(hash([1, 2])) TypeError: unhashable type: 'list'

print(t)

print(1 in t) # True

print(len(t))

'''
methods:
- clear
- get()
- items()
- keys()
- values()
- pop()
- popitem()
- update()

'''

