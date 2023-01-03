"""
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints: Use set() and "&=" to do set intersection operation
"""
first_set = set([1,3,6,78,35,55])
second_set = set([12,24,35,24,88,120,155])

first_set &= second_set

print(first_set)