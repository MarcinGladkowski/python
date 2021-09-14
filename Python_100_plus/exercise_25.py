"""
Level 1

Question: Define a class, which have a class parameter and have a same instance parameter.

Hints: Define a instance parameter, need add it in init method You can init a object with construct parameter
or set the value later
"""


class Employee:
    def __init__(self, name) -> None:
        self.name = name


employee = Employee('John')
print(employee.name)
employee.name = 'Marcin'
print(employee.name)