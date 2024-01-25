"""
Main conclusion: numpy is must faster than traditional python list and looping

@see source => https://www.thepythoncodingstack.com/p/python-numpy-ndarray-primer-numpy-for-numpties

* List can contain any type of types
* Lists are mutable, ndarray are also mutable
* Lists are iterable - e.g. by for loops
* Lists are sequences - get element by index
"""
some_list = [(0,), 10, 'name', [], 3.3]

from array import array

"""
Can contains only the same data types
- use less memory than 'list' type
"""
some_numbers = [1, 13, 20, 33]

some_array_numbers = array("i", some_numbers)

print(type(some_array_numbers))
print(some_array_numbers)

some_array_numbers.typecode  # "i" represents integer

some_array_numbers.append(20)

print(some_array_numbers)

"""
ndarray - 'nd' means multidimensional array
"""
import numpy as np

ndarray_numbers = [2, 22, 30, 30]

some_numbers_np = np.array(ndarray_numbers)

print(type(some_numbers_np))

some_names = ["marcin", 'tomek']

some_names_np = np.array(some_names)

print(some_names_np.dtype)

mixed_data = [1, 2.2, True, 'Hello There'] # adding (0, 0) broke np array

mixed_data_np = np.array(mixed_data)

other_numeric_types = [1, 2.2, True]

other_numeric_types_np = np.array(other_numeric_types)

print(other_numeric_types_np) # every converts to float64,

"""
Important: True is a subclass of Integer!
"""
print(isinstance(True, int))


"""multiplying vs vectorisation"""
to_multiply_list = [1, 2, 3] * 3
print(to_multiply_list)
to_multiply_np = np.array([1, 2, 3]) * 3
print(to_multiply_np)

"""filtering with np.array"""
to_filter_np_array = np.array([1, 2, 4, 5])
np_array_filtered = to_filter_np_array[to_filter_np_array > 2]
print(np_array_filtered)