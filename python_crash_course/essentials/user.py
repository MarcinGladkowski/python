class User:
    def __init__(self, first_name, last_name, role, active, email):
        self.email = email
        self.active = active
        self.role = role
        self.last_name = last_name
        self.first_name = first_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name}, {self.last_name}, {self.role}, {self.active}, {self.email}')

    def greet_user(self):
        print(f'Hi! My name is {self.first_name} {self.last_name}')

