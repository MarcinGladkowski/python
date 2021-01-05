# 4.3
for number in range(21):
    print(number)

# 4.4
billion_numbers = []
for x in range(1_000_001):
    billion_numbers.append(x)

# 4.5
print(max(billion_numbers))
print(min(billion_numbers))
print(sum(billion_numbers))


# 4.6
# using list comprehension, instead of append method on list
odd_numbers = [x for x in range(0, 20, 3)]
print(odd_numbers)

# 4.7
to_cube = [x**3 for x in range(3, 31)]
print(to_cube)

for cube_number in to_cube:
    print(cube_number)

# 4.8
to_cube_first_10 = []
for x in range(11):
    to_cube_first_10.append(x**3)


for x in to_cube_first_10:
    print(x)

# 4.9
to_cube_first_10_comprehension = [x**3 for x in range(11)]
print(to_cube_first_10_comprehension)

# 4.10
print(f'Three first numbers are {to_cube_first_10_comprehension[:3]}')
print(f'Three numbers in the middle are {to_cube_first_10_comprehension[3:6]}')
print(f'Three numbers in the end are {to_cube_first_10_comprehension[-3:]}')

# 4.11
pizzas = ['Neapolitan', 'Sicilian', 'Californian']

friend_pizzas = pizzas[:]

pizzas.append('Hawaii')
friend_pizzas.append('Margarita')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)


print('My friend favourite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)


# 4.12
my_foods = ['pizza', 'falafel', 'pie']
print('My favourite food are:')
for food in my_foods:
    print(food)


# 4.13 Tuple
print('\n4.13\n')
buffet = ('pizza', 'pie', 'falafel', 'breakfast', 'sapper')

for dinner in buffet:
    print(dinner)


# buffet[0] = 'another food' Throws Exception

buffet = ('super dinner', 'supper dinner 2')

for dinner in buffet:
    print(dinner)


# 4.14
# PEP 8 description: https://www.python.org/dev/peps/pep-0008/


