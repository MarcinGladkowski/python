# 6.1
print('\n6.1\n')
racing_driver = {
    'first_name': 'Robert',
    'last_name': 'Kubica',
    'age': 36,
    'city': 'Krakow',
}

print(racing_driver.get('first_name'))
print(racing_driver.get('last_name'))
print(racing_driver.get('age'))
print(racing_driver.get('city'))

# 6.2
print('\n6.2\n')
favourites_numbers = {
    'John': 7,
    'Json': 1,
    'Elon': 10,
}

print(favourites_numbers)

# 6.3
print('\n6.3\n')

programming = {
    'for': 'To iterate on list',
    'list': 'Stores data',
    'tuple': 'Stores immutable data',
    'variable': 'To store simple type of data',
    'python': 'Programming language',
    'dictionary': 'Store data using key - value pair',
    'print': 'function to display data on terminal',
    'PEP': 'Rules to programming in python',
    'lower()': 'function to small letters',
    'upper()': 'function to capital letters',
}


print(f"key: for, and description: {programming.get('for')}")
print(f"key: list, and description: {programming.get('list')}")
print(f"key: tuple, and description: {programming.get('tuple')}")
print(f"key: variable, and description: {programming.get('variable')}")
print(f"key: python, and description: {programming.get('python')}")

# 6.4
print('\n6.4\n')

for key, value in programming.items():
    print(f"key: {key}, and description: {value}")


# 6.5
print('\n6.5\n')
rivers_in_countries = {
    'Nil': 'Egypt',
    'Tamas': 'London',
    'Mississippi': 'USA'
}

for river, country in rivers_in_countries.items():
    print(f'{river} river flows through {country}')


for river in rivers_in_countries.keys():
    print(river)

for country in rivers_in_countries.values():
    print(country)

# 6.6
print('\n6.6\n')

persons_survey = {
    'Marcin': 'PHP',
    'Łukasz': 'Python',
    'Json': 'JavaScript'
}

new_persons = ['Thomas']

for new_person in new_persons:
    if new_person not in persons_survey:
        print(f'Maybe {new_person} you can take an action ?')

    for person in persons_survey:
        print(f'Thanks for your answer {person}')


# 6.7
print('\n6.7\n')
people = {
    'racing_driver': {
        'first_name': 'Robert',
        'last_name': 'Kubica',
        'age': 36,
        'city': 'Krakow',
    },
    'founder': {
        'first_name': 'Elon',
        'last_name': 'Musk',
        'city': 'California',
        'age': 47
    },
    'rally_driver': {
        'first_name': 'Sebastian',
        'last_name': 'Ogier',
        'city': 'Paris',
        'age': 38
    }
}

for person, user_info in people.items():
    print(f'Person data: {person}')
    for key, value in user_info.items():
        print(f'{key}: {value}')