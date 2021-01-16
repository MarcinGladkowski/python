class Employee:
    def __init__(self, firstname, lastname, salary):
        self.salary = salary
        self.lastname = lastname
        self.firstname = firstname

    def give_raise(self, amount=5000):
        self.salary += amount
