from random import randint

'''
range() is pretty sure for iterate on integers
'''

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))

# plenty of time we need also index of element in list
users = ['user1', 'user2', 'user3', 'user4']

for user in users:
    print(user)

print("\nusing range:")
# get indexes
for i in range(len(users)):
    print(users[i])

print('\nuse enumerator\n')
'''
how works enumerate ? - pack it to generator
Thats mean, you can use next() function
'''
it = enumerate(users)
print(next(it)) # tuple (0, 'user1')
print(next(it))

for i, user in enumerate(users):
    print(f'{i+1}: {user}')

print('\nNext example\n')
for i, user in enumerate(users, 1):
    print(f'{i}: {user}')