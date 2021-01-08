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