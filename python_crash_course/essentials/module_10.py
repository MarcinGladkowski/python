import json
# 10.1
# read file at once
filepath = 'learning_python.txt'

with open(filepath) as file_object:
    contents = file_object.read()

print(contents)

print('\n')
# read file line by line
with open(filepath) as file_object:
    for line in file_object:
        print(line)

print('\n')
# read and store in list
with open(filepath) as file_object:
    lines = file_object.readlines()


for line in lines:
    print(line)


print('\n')
# 10.2
with open(filepath) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C'))


print('\n')
# 10.3
name = input('Write your name:')

with open('guest.txt', 'w') as file_object:
    file_object.write(name)


print('\n')
# 10.4
while True:
    name = input('Write your name, please: ')

    if name == 'q':
        break

    with open('guest_book.txt', 'w+') as file_object:
        file_object.write(f"{name}\n")


print('\n')
# 10.5
while True:
    answer = input('Why do you like programming?: ')

    if name == 'q':
        break

    with open('guest_book.txt', 'a+') as file_object:
        file_object.write(f"{name}\n")


print('\n')
# 10.6
try:
    number_1 = int(input('First number: '))
    number_2 = int(input('Second number: '))
except ValueError:
    print('The number must be a numeric')
else:
    print(f'Result: {number_1 + number_2}')


print('\n')
# 10.7
while True:
    try:
        number_1 = int(input('First number: '))
        number_2 = int(input('Second number: '))
    except ValueError:
        pass
    else:
        print(f'Result: {number_1 + number_2}')


print('\n')
# 10.8/10.9
try:
    with open('cats.txt') as file_object:
        print(file_object.read())

    with open('dogs.txt') as file_object:
        print(file_object.read())

except FileNotFoundError:
    pass


print('\n')
# 10.10
with open('Model_Flying_Machines.txt') as file_object:
    lines = file_object.readlines()

count = [line.lower().count('model') for line in lines]
print(sum(count)) # 86


print('\n')
# 10.11
user_favourite_number = input('What\'s your favourite number? ')
favourite_number_filename = 'favourite_number.json'

with open(favourite_number_filename, 'w') as f:
    json.dump(user_favourite_number, f)


with open(favourite_number_filename) as f:
    print(f'Your favourite number is {json.load(f)}')


print('\n')
# 10.12

favourite_number_filename = 'favourite_number.json'
with open(favourite_number_filename) as f:
    file_data = json.load(f)
    if file_data:
        print(f'Your favourite number is {file_data}')
    else:
        user_favourite_number = input('What\'s your favourite number? ')

        with open(favourite_number_filename, 'w') as f:
            json.dump(user_favourite_number, f)


# print('\n')
# 10.13
def get_stored_username():
    """Get username from json file"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Ask user to input username and write it into a file"""
    username = input("What's your username?: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet a user"""
    username = get_stored_username()
    if username:

        answer = input(f"It's your username {username} ? ")

        if answer == 'no':
            new_username = get_new_username()
            print(f'Welcome to our system {new_username}')

        print(f'Welcome to our system {username}')
    else:
        get_new_username()
        print('Your\'s name has been stored.')


greet_user()