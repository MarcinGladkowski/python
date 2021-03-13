import locale

# bytes
a = b'w\x69taj'
print(list(a)) # return ASCI codes
print(a) # witaj

# str use Unicodes

b = 'a\u0300 propos'
print(list(b))
print(b)

'''
encode(), decode() - uses for transforming from binary to text and back
'''


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

'''
Writing bytes data into file requires to add 'b' parameter also
'''
with open('data.bin', 'wb') as f:
    f.write(b'x\f1\xf2\xf3\xf4')


with open('data.bin', 'rb') as f:
    data = f.read()
assert data == b'x\f1\xf2\xf3\xf4' # True


'''
Example of opening file with specific encoding:
with open('data.bin', 'r', encoding='cp1252') as f:
    data = f.read()
'''

'''
How to check locale encoding
'''
print(locale.getpreferredencoding())