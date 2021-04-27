"""
- named as argument with star
- to make code more clear
- the number of arguments isn't known
"""


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('My numbers are', [1, 2])
log('Hello', [])
log('Hello with *')

numbs = [1, 3, 4]

log('My unpacked numebers', *numbs)

"""
downsides:
- operator * changes it into Tuple
- in case of creating Generator make some troubles
- use it when the number of elements to unpack is not big!
- if you want to add new position argument in the future - it can be problematic
"""

