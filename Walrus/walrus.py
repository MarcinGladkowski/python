'''
walrus operator :=
* more clear to read
* sometimes needs to add brackets
* In python we don't have while-do loop and switch cases
'''

# standard way
fresh_fruits = {
    'Orange': 0,
    'Apple': 10,
    'Banana': 2
}

count = fresh_fruits.get('Apple', 0)
if count:
    print('Make a juice')
else:
    print('Sorry, we cannot make a juice')

# with walrus operator
if count := fresh_fruits.get('Apple', 0):
    print('Make a juice')
else:
    print('Sorry, we cannot make a juice')


# with walrus operator
if (count := fresh_fruits.get('Apple', 0)) >= 4:
    print('Make a big juice')
else:
    print('Sorry, we cannot make a big juice')