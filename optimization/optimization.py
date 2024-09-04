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




