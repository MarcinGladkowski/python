class Record:
    """Hold a record of data"""


row = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

record = Record()

for field, value in row.items():
    setattr(record, field, value)

print(
    record.name,
    record.__dict__
)

"""Add using dot notation"""


class User:
    pass


user = User
user.name = 'Jan'
user.lastname = 'Kowalski'


def __init__(self, name, lastname):
    self.name = name
    self.lastname = lastname


User.__init__ = __init__

print(user.name)

second_user = User('Justyna', "Kowalska")

print(second_user.name)
