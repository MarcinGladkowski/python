'''
Metaclasses allows to modifying attributes of class
'''


class Field:
    """
    Class for descriptor
    """
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        self.name = name
        self.internal_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):
    def __new__(cls, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(cls, name, bases, class_dict)
        return cls


class DatabaseRow(metaclass=Meta):
    pass


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


class FixedCustomer:
    """
    Without inheritance on class with metaclass
    which set data using __new__() from metaclass
    """
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


customer = BetterCustomer()
print(f'Before {customer.first_name!r} {customer.__dict__}')
customer.first_name = 'Marcin'
print(f'After {customer.first_name!r} {customer.__dict__}')


better_customer = FixedCustomer()
print(f'Before {better_customer.first_name!r} {customer.__dict__}')
customer.first_name = 'Marcin'
print(f'After {better_customer.first_name!r} {customer.__dict__}')