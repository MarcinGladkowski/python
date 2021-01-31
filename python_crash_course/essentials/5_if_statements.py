# 5.1 5.2
color = 'green'
name = 'Marcin'

print(color == 'green')
print(name.lower() == 'marcin')
print(len(name) == 6)
print(name == 'Marcin')
print(name == 'marcin')
print(len(name) > 6)
print(len(name) >= 6)
print([] is True)
print('test' is True)
print('test ' == 'test')
print('test' == 'test')
print(name in ['Marcin', 'Tomek'])
print('Test' in ['Marcin', 'Tomek'])
print('Test' not in ['Marcin', 'Tomek'])
print(20 > 10)
print(20 <= 21)
print(True or False)

# 5.3
print('\n5.3\n')
alien_color = 'red'
if alien_color == 'green':
    print('You earn 5 points!')

if alien_color == 'red':
    print('Correct color!')


# 5.4
print('\n5.4\n')
if alien_color == 'green':
    print('You earn 5 points!')
else:
    print('You earn 10 points!')


if alien_color == 'red':
    print('You earn 5 points!')
else:
    print('You earn 10 points!')


# 5.5
print('\n5.5\n')

if alien_color == 'green':
    print('You earn 5 points!')
elif alien_color == 'yellow':
    print('You earn 10 points!')
elif alien_color == 'red':
    print('You earn 15 points!')

# 5.6
print('\n5.6\n')
person_age = 20

if person_age < 2:
    print("It's a baby")
elif 4 > person_age >= 2:
    print("Baby who learn walking!")
elif 13 > person_age >= 4:
    print("Child")
elif 20 > person_age >= 13:
    print("Teenager")
elif 65 > person_age >= 20:
    print("Adult")
elif person_age >= 65:
    print("Senior")


# 5.7
print('\n5.7\n')

favorite_fruits = ['oranges', 'apples', 'bananas']

if 'oranges' in favorite_fruits:
    print('You love oranges!')

if 'apples' in favorite_fruits:
    print('You love apples!')

if 'bananas' in favorite_fruits:
    print('You love bananas!')


# 5.8
print('\n5.8\n')
users = ['user1', 'admin', 'user2', 'user3', 'user4']

for user in users:
    if user == 'admin':
        print('Hello admin. Do you want to look at report ?')
    else:
        print(f'Hello {user}. Thanks for log in')


users = []

if not users:
    print('We have to find users!')


# 5.9
print('\n5.9\n')

current_users = ['Bill', 'Json', 'Robert', 'Elon', 'Bill']
new_users = ['Elon', 'Tom', 'Peter']

# 5.10
current_users_lower = [x.lower() for x in current_users]

for new in new_users:
    if new.lower() in current_users_lower:
        print(f'Sorry, you cannot use this name! {new}')
    else:
        print(f'You can use this name! {new}')

# 5.11
print('\n5.11\n')
numbers = [x for x in range(1, 10)]

print(numbers)

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')


# 5.12
print('\n5.12\n')

