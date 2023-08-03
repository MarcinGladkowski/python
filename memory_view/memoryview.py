"""
* Zero copy (my translation)
* Much faster processing data
"""

data = b'This is some data will be split to chunks'
view = memoryview(data)
chunk = view[10:24]
print(chunk)
print('Count: ', chunk.nbytes)
print('Data in view: ', chunk.tobytes())
print('Data in background: ', chunk.obj)


"""
* bytearray
"""

my_array = bytearray(b'hello')
my_array[0] = 0x79
print(my_array)