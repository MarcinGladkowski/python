# source: https://realpython.com/python-lists-tuples/
# elements are in ()
# Tuples are immutable - you cannot modify it!
# can access to elements with brackets []
#

languages = ('PHP', 'Python', 'JavaScript', 'Java')

print(languages[0])
print(languages[-1])

# reverse mechanism works as well
print(languages[::-1])

# languages[0] = 'PHP8' -> throws exception


# Packing and unpacking
# Number of variables must match
(l1, l2, l3, l4) = languages

print(l1)
print(l4)

# Swap the variables in tuple way!
a = 'foo'
b = 'bar'

a, b = b, a

print(a)
print(b)


