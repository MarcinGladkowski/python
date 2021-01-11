# 9.1
print('\n9.1\n')


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Welcome in {self.restaurant_name}. We cook the best {self.cuisine_type}')

    def open_restaurant(self):
        print('From 9:00 to 22:00 all week')


restaurant = Restaurant('Bzik', 'Regional')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9.2
print('\n9.2\n')

restaurant_2 = Restaurant('Pod wiezami', 'Dinners')
restaurant_3 = Restaurant('Hurry Carry', 'Indian')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


# 9.3
print('\n9.3\n')


class User:
    def __init__(self, first_name, last_name, role, active, email):
        self.email = email
        self.active = active
        self.role = role
        self.last_name = last_name
        self.first_name = first_name

    def describe_user(self):
        print(f'{self.first_name}, {self.last_name}, {self.role}, {self.active}, {self.email}')

    def greet_user(self):
        print(f'Hi! My name is {self.first_name} {self.last_name}')


user1 = User('f_user1', 'f_user1', 'admin', True, 'admin@admin.xx')
user2 = User('f_user2', 'f_user2', 'manager', False, 'manager@manager.xx')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
