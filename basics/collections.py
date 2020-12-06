

'''
- no duplicates
- iterable
- order doesn't matter
'''

collection = set()

print(dir(collection))

collection.add(2)
collection.add(3)
collection.add(100)

print(collection)

collection.add('Name')
collection.add(False)

print(collection)

collection.add(100)

for x in collection:
    print(x)

collection.remove(3)

print(collection)

# No errors when element not exists
collection.discard('Name')

print(collection)

# sum
a = set([1, 2, 3]) # or using {}
b = {3, 4, 5}

print(type(a))
print(type(b))

c = a.union(b)
d = c|b

print(c)
print(d)

# multiplication
print(a.intersection(b))

# subtraction
print(a.difference(b))

