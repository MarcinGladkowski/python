'''
magic function __missing__ allows us to add behaviour
when key in dict is missing
'''

def open_picture(file_path):
    try:
        return open(file_path, 'a+b')
    except OSError:
        print('Error when opening a file')
        raise


class Picture(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value