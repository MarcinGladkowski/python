"""
From https://dev.to/jamesbright/10-python-programming-optimisation-techniques-5ckf
"""


# Packing data to binary - data processing more efficient
import struct

from dict.missing import open_picture

# packing two integers into binary format
packed_data = struct.pack('ii', 10, 20)

# unpacking
a, b = struct.unpack('ii', packed_data)


# Disc storage vs memory storage
import mmap

# Memory-mapping a file
with open('data.txt', "r+b") as f:
    mmapped_file = mmap.mmap(f.fileno(), 0)
    print(mmapped_file.readline())
    mmapped_file.close()

# Fixed-length vs variable-length variables

"""
Variable length variables required manage dynamically memory allocation
Fixed length variables are stored in blocks making access faster
"""
import array

# fixed length works very effective
fixed_array = array.array('i', [1, 2, 3, 4, 5, 6])

# dynamic list
dynamic_list =  [1, 2, 3, 4, 5, 6]

# Internal vs public functions
def _private_function(data):
    """ Optimized for internal use with minimal error handling"""
    return data ** 2

def public_function(data):
    """Include additional checks"""
    if isinstance(data, int):
        return _private_function(data)
    raise ValueError("Input must be an integer")


# Function modifiers
"""
Decorators serve multiple usage cases
"""
from functools import lru_cache
@lru_cache(maxsize=1000)
def compute_heavy_function(x):
    # expensive operation
    return x ** x

# Special libraries like Numpy
"""
Written in C are created for specialized operations
"""
import numpy as np

matrix_a = np.random.rand(1000, 1000)
matrix_b = np.random.rand(1000, 1000)

result = np.dot(matrix_a, matrix_b)

# Optimize loops

import numpy as np

array = np.array([1, 2, 3, 4])

result = array * 2


