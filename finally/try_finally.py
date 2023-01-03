"""
Finally is great using when we want always execute code when error is
throwing like using file handlers. We want to close handler when the error
has occurred.
"""


def try_finally_example(filename):
    print('* File open')

    handle = open(filename, encoding='utf-8')  # possible exception

    try:
        print('* Read file')
        return handle.read()  # possible exception
    finally:
        print('* Close function close()')
        handle.close()


newfile = 'random_data.txt'

with open(newfile, 'wb') as f:
    f.write(b'\xf1')

data = try_finally_example(newfile)