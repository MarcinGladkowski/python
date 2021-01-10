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
    print(messages)
    while messages:
        sent = messages.pop()
        sent_messages.append(sent)
       # print(f'{sent}')


send_messages(messages_to_show)
print(messages_to_show)
print(sent_messages)


# 8.11
print('\n8.11\n')
print(messages_to_show)
show_messages(messages_to_show[:])
print(messages_to_show)
print(sent_messages)