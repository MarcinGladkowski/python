# 9.10/9.11
from restaurant import Restaurant
from user import User
from admin import Admin
from random import randint, choice

# 9.1
print('\n9.1\n')

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

user1 = User('f_user1', 'f_user1', 'admin', True, 'admin@admin.xx')
user2 = User('f_user2', 'f_user2', 'manager', False, 'manager@manager.xx')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# 9.4
print('\n9.4\n')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant_2.set_number_served(20)
print(restaurant_2.number_served)

restaurant_3.increment_number_served(30)
print(restaurant_3.number_served)

# 9.5
print('\n9.5\n')
new_user = User('user3', 'user3', 'user', False, 'noemail@xx')
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)

# 9.6
print('\n9.6\n')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        self.flavours = flavours
        super().__init__(restaurant_name, cuisine_type)

    def show_flavours(self):
        for flavour in self.flavours:
            print(flavour)


ice_cream_stand = IceCreamStand('Grycan', 'Italian ice creams', ['chocolate', 'vanilla'])
ice_cream_stand.show_flavours()

# 9.7
print('\n9.7\n')


# 9.8
print('\n9.8\n')

admin_1 = Admin('super', 'user', 'admin', True, 'admin@xx.com')
admin_1.privileges.show_privileges()


# 9.13
print('\n9.13\n')


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die_1 = Die(6)

for x in range(0, 10):
    die_1.roll_die()

die_2 = Die(10)
for x in range(0, 10):
    die_1.roll_die()

die_3 = Die(20)
for x in range(0, 10):
    die_1.roll_die()

# 9.14
print('\n9.14\n')


def lottery():
    elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
    return [choice(elements) for x in range(0, 4)]


print('The coupon code which won:')
print(lottery())
# 9.15
print('\n9.15\n')
my_ticket = ['A', 7, 5, 'C']

# check comparison of lists
print(['A', 1] == ['A', 1]) # True

lottery_inc = 0
while True:
    lottery_inc += 1
    result = lottery()
    if my_ticket == result:
        print(lottery_inc, my_ticket, result)
        break

# 9.16
print('\n9.16\n')
# Python module of week https://pymotw.com/3/ -> great knowledge about Python standard library
