from math import sqrt, isqrt

"""
* Square is a number multiplied by itself x * x
* In Python we can use x**2, the same as x*x
"""

# perfect squares
print(sqrt(25))
print(sqrt(36))

# not perfect squares
print(sqrt(30))


isqrt(25) # 5

print(25 ** (1. / 2)) # native way


"""
Cube x*x*x == x**3

* Not specialized function in math module
"""

print(4 ** 3) # 64
print(64 ** (1. / 3)) # 3.999...
