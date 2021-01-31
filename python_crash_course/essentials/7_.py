# 7.1
print('\n7.1\n')

val = input("What kind of car brand would you rent ?: ")
print('Wait a moment, please...')

# 7.2
print('\n7.2\n')

number = input('Table for ? ')
number = int(number)

if number > 8:
    print('Wait for a table, please...')
else:
    print('Table is ready!')


# 7.3
print('\n7.3\n')
input_number = input('Provide a number: ')
input_number = int(input_number)

if input_number % 10 == 0:
    print('Number is multiplication of 10 number')
else:
    print('Number is not multiplication of 10 number')


# 7.4
print('\n7.4\n')
pizza_toppings = []

while True:
    topping = input("Add topping: ")

    if topping == 'finish':
        break

    pizza_toppings.append(topping)
    print(f'Added {topping}')


# 7.5
print('\n7.5\n')

while True:
    age = int(input("Provide your age:"))

    if age < 3:
        print('Free entry')
    elif age < 12:
        print('Ticket price: 10$')
    else:
        print('Ticket price: 15$')


# 7.6
print('\n7.6\n')
# statement
while True:
    age = input("Provide your age: ") # check is numeric

    if age == 'finish':
        break

    if int(age) < 3:
        print('Free entry')
    elif int(age) < 12:
        print('Ticket price: 10$')
    else:
        print('Ticket price: 15$')

# active
active = True
while active:
    age = int(input("Provide your age:"))

    if age < 3:
        print('Free entry')
    elif age < 12:
        print('Ticket price: 10$')
    else:
        print('Ticket price: 15$')

    if age:
        active = False


# # active
while True:
    age = input("Provide your age:")

    if int(age) < 3:
        print('Free entry')
    elif int(age) < 12:
        print('Ticket price: 10$')
    else:
        print('Ticket price: 15$')

    if age == 'finish':
        break


# 7.7
print('\n7.7\n')

while True:
    print('Test')


# 7.8, 7.9
print('\n7.8 7.9\n')

ordered_sandwiches = ['pastrami','double', 'classic', 'pastrami', 'vege', 'italian', 'pastrami']
finished_sandwiches = []

print("We don't have pastrami")

while 'pastrami' in ordered_sandwiches:
    ordered_sandwiches.remove('pastrami')


for sandwich in ordered_sandwiches:
    print(f'prepared sandwich: {sandwich}')
    finished_sandwiches.append(sandwich)

print('\nFull order')
for finished in finished_sandwiches:
    print(f'{finished}')

# 7.10
print('\n7.10\n')

survey = {}

while True:
    name = input('Whats your name ?: ')
    place = input('Where do you love to travel ?: ')

    if place == 'finish' or name == 'finish':
        break

    survey[name] = place


for name, place in survey.items():
    print(f'{name} wants travel to: {place}')
