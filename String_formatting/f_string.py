'''
To formating string use Literal String Interpolation

Comes from https://www.python.org/dev/peps/pep-0498/ Python 3.6

Previous formatting functions (historical)

'''

'''
* We cannot change places
* Variables are in strict order
'''

# don't use anymore
# %
print('Binary value is %d, hex value is %d' % (0b10111011, 0xc5f))
# .format()
print(format(1234.5678, ',.2f'))
# order variables
print('{1} - {0}'.format(10, 29))

template = ('Today is {day}')
formatted = template.format(day='monday')
print(formatted)

'''
Newest way f''
'''
key = 'my_var'
value = 1.234
formatted_value = f'{key} {value}'
print(formatted_value)

'''
We can use all options to formatting values. Use after ':' sign.
'''
formatted_text = f'{key!r:<10} = {value:.2f}'
print(formatted_text)

pantry = [
    ('banana', 2.5),
    ('apple', 1)
]


for i, (item, elem) in enumerate(pantry):
    # old style
    old_style = '#%d: %-10s = %d'% (i + 1, item.title(), round(elem))
    # new style
    new_style = '#{}: {:<10s} = {}'.format(i + 1, item.title(), round(elem))
    # using f strings
    f'#{i + 1}: {item.title():<10s} = {round(elem)}'


# define lettlers to display
places = 3
number = 1.123456
print(f'The number is {number:.{places}f}')