class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

    def describe_restaurant(self):
        print(f'Welcome in {self.restaurant_name}. We cook the best {self.cuisine_type}')

    def open_restaurant(self):
        print('From 9:00 to 22:00 all week')


class Privileges:
    def __init__(self):
        # print('__init__ method') -> initialization without () doesn't run it
        self.privileges = [
            'add post',
            'edit post',
            'remove post'
        ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)