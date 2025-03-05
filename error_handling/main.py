"""
Two main styles of error handling:

Look Before You Leap (LBYL) - check conditions beforehand

can_i_do_it():
    validate()
else:
    handle_error()

cons:
- you must know all possible error roots
- race conditions (something can change just after checking)
"""
import os

file_path = 'custom/path'

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"Error: file {file_path} does not exist!")


"""
Easier to Ask Forgiveness than Permission (EAFP)
"""
try:
    os.remove(file_path)
except OSError as error:
    print(f"Error deleting file: {error}")
