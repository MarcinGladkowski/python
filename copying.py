import copy

a = [1, 2, 3, 4, 5]
b = a

'''
id() = shows the id from memory
a, b has the same memory id
'''
print(id(a) == id(b))

'''
modyfing b table also modify the a table!
'''
b.append(6)
print(a)

'''
Shallow copy using copy.copy and other methods
'''
c = [1, 2, 3]

c1 = copy.copy(c)
c2 = list(c1)
c3 = c1[:]


'''
But these method not copy nested types - they keep reference
'''
d = [[1, 2], [3, 4]]
e = copy.copy(d)

e[0].append(3)

print(d)

'''
Deep copy
'''
f = copy.deepcopy(d)
f[0].append(4)

print(d)
print(f)




