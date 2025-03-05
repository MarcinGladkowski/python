"""
Creating by constructor set(), or literals `{element1, element2, element-n}`

Elements must be hashable objects
Duplicated values will be removed
{} -> it;s not empty set but dictionary
"""
colors = {'green', 'red', 'green', 'yellow'} # the same result as set(['green', 'red', 'green', 'yellow'])
colors.add('black')
print(colors)

"""Create using comprehension"""
print({x for x in ['red', 'yellow', 'black']})
