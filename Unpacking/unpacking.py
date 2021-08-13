"""
examples from: Python Function Argument Unpacking Tutorial (* and ** Operators)
Real Python (youtube channel)
"""


def print_vector(x, y, z):
    print(f'Vector: {x}, {y}, {z}')


# Data comes from Tuple ex.
tuple_data = (1, 2, 3)

print_vector(1, 2, 3)
print_vector(*tuple_data)  # the same as print_vector(tuple[0]....

# form some Generator
gen_expression = (x * x for x in range(3))
print_vector(*gen_expression)

# from dictionary
dictionary_data = {
    'x': 1,
    'y': 2,
    'z': 3
}

"""
** Double asterisk
bc dictionary doesn't have order index as data[0]...
"""
print_vector(**dictionary_data)
