import printing_functions as pt

# 8.15
# import make_car
# import make_car as mk
# from make_car import make_car
# from make_car import make_car as mk
from make_car import *

#
# def name(parameter1, parameter2)
#
# name(argument1, argument2)

# 8.1
def display_messages():
    print("I learn about creating functions in Python")


display_messages()


# 8.2
def favourite_book(book_title):
    print(f"One of my favourite book is '{book_title}'")


favourite_book('The best')


# 8.3
def make_shirt(size, text='I love Python'):
    print(f"You ordered T-shirt with text: {text} and size {size}")


make_shirt('The best', 'M')
make_shirt(text='Just to it', size='XL')

# 8.4
make_shirt(size='XL')
make_shirt(size='XXL')
make_shirt(size='M', text='Other text')


# 8.5
def describe_city(city, country='Poland'):
    print(f"The {city} is in {country}")


describe_city('Warsaw')
describe_city(city='Krakow')
describe_city('New York')


# 8.6
def city_country(city, country):
    print(f'{city}, {country}')


city_country('Warsaw', 'Poland')
city_country(country='Germany', city='Berlin')
city_country('London', country='Great Britain')


# 8.7
def make_album(band, album_name, singles=None):
    result = {
        'band': band,
        'album_name': album_name
    }
    if singles:
        result['singles'] = singles

    return result


print(make_album('Agnieszka Chylińska', 'Modern Rocking'))
print(make_album('Happysad', 'Mów mi dobrze'))
print(make_album('Myslowitz', 'Miec czy byc'))
print(make_album('Myslowitz', 'Zycie to surfing', 18))


# 8.8
while True:
    band = input("Add band name: ")

    if band == 'q':
        break

    album_name = input("Add album name: ")

    if album_name == 'q':
        break

    make_album(band, album_name)


print('\n8.9\n')


# 8.9
def show_messages(messages):
    for message in messages:
        print(f'{message}')


messages_to_show = ['log', 'debug', 'error']

show_messages(messages_to_show)

sent_messages = []



# 8.10
print('\n8.10\n')


def send_messages(messages):
    while messages:
        sent = messages.pop()
        sent_messages.append(sent)
        print(f'added to send messages: {sent}')


send_messages(messages_to_show)
print(messages_to_show)
print(sent_messages)


# 8.11
print('\n8.11\n')
print(messages_to_show)
send_messages(messages_to_show[:])
print(messages_to_show)
print(sent_messages)


# 8.12
print('\n8.12\n')


def make_sandwitch(*toppings):
    """use *args to get all arguments - the number of argumenr is optional"""
    for topping in toppings:
       print(f'{topping} added to sandwitch')


make_sandwitch('cheese', 'ham', 'butter')
print('\n')
make_sandwitch('cheese', 'ham', 'butter', 'tomatoes')
print('\n')
make_sandwitch('cheese', 'ham', 'butter', 'tomatoes', 'cucumber')



# 8.13
print('\n8.13\n')


def build_profile(first, last, **user_info):
    ''' Build profile using **kwar dictionary'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile('Marcin', 'Programmer', main_lang='PHP', second_lang='JS', learning_lang='Python')
print(my_profile)


# 8.14
print('\n8.14\n')

car = make_car('Honda', 'Civic', color='silver', version='TypeR')
print(car)


# 8.15
print('\n8.15\n')
unprinted_models = ['Honda', 'Mercedes']
completed_models = []

pt.print_models(unprinted_models, completed_models)
pt.show_completed_models(completed_models)
