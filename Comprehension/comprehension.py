"""
Prefer using comprehension than the for, map, filter functions
"""

"""Count a square of number"""
a = [1, 2, 3, 4, 5, 6, 7]

squares = []
for n in a:
    squares.append(n**2)

"""Using comprehension"""
result = [x**2 for x in a]

assert squares == result

"""Other solutions is usage of map()"""
result = map(lambda x: x ** 2, a)

"""Comprehension with statement - count only for even numbers"""
even_result = [x**2 for x in a if x % 2 == 0]

"""The same result using map() and filter()"""
even_functional = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))

"""
Using comprehension with dictionaries
"""
even_squares_dict = {x ** 2 for x in a}

"""Nested list"""
matrix = [[1, 2, 4], [5, 6, 7], [8, 9, 10]]

flat = [x for row in matrix for x in row]

"""Square numbers in nested list"""
squares_nested = [[x ** 2 for x in row] for row in matrix]

b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

"""
leaks variable to main scope
- from FOR
- from WALRUS (from Python 3.8)
- but don't from COMPREHENSION
"""
elements = [1, 2, 3, 4, 5, 6]

for el in elements:
    pass

print(f'last element of iteration is {el}')

# [test := x ** 2 for x in elements]
