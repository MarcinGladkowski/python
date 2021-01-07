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