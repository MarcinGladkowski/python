"""
Prefer using comprehension than the for, map, filter functions
"""

"""Count a square of number"""
a = [1, 2, 3, 4, 5, 6, 7]

squares = []
for n in a:
    squares.append(n**2)

result = [x**2 for x in a]

assert squares == result

### p.118

