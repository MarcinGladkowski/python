'''
- We can use getattr and setattr to dynamically properties
- getattr is called once when the property doesn't exists
- getattribute is calling always
- be careful for recursion problem, use then super() keyword
'''



class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = f'Value for {item}'
        setattr(self, item, value)
        return value


data = LazyRecord()
print('before:', data.__dict__)
print('foo:', data.foo)
print('Po:', data.__dict__)


# When __getattr__ is called?
class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, item):
        print(f'*Called __getattr__({item!r})')
        result = super().__getattr__(item)
        print(f'*Return {result!r}')
        return result


nextData = LoggingLazyRecord();
print('exists:', nextData.exists)
print('First foo:', nextData.foo)
print('Second foo:', nextData.foo)

'''
Using the __getattribute__
* Checks globally the key in dictionary of class
'''


class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print(f'*Called __getattribute({item!r})')
        try:
            value = super().__getattribute__(item)
            print(f'* Found {item!r}, return {value!r}')
            return value
        except AttributeError:
            value = f'Value for {item}'
            print(f'* {item!r} assign a value {value!r}')
            setattr(self, item, value)
            return value


validatingData = ValidatingRecord()
print('exists:', validatingData.__dict__)
print('First foo:', validatingData.foo)
print('Second foo:', validatingData.foo)

'''
Raising exceptions to dynamically properties
'''


class MissingPropertyRecord:
    def __getattr__(self, item):
        if item == 'bad_property':
            raise AttributeError(f'Property {item} don\'t exists')


bad_attribute = MissingPropertyRecord()
# bad_attribute.bad_property - Rasing exception!

has_property = LoggingLazyRecord()
print('Before:', has_property.__dict__)
print('First foo exists: ', hasattr(has_property, 'foo'))
print('After', has_property.__dict__)
print('Second foo exists: ', hasattr(has_property, 'foo'))

'''
setattr is called always when we want to assign value to new dynamically prop
'''


class SavingRecord:
    def __setattr__(self, key, value):
        super().__setattr__(key, value)


class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, key, value):
        print(f'* Called __setattr__({key!r}, {value!r})')
        super().__setattr__(key, value)


saving_property = LoggingSavingRecord()
print('Before', saving_property.__dict__)
saving_property.foo = 5
print('After', saving_property.__dict__)
saving_property.foo = 7
print('Result', saving_property.__dict__)

'''
__getattr__ and __getattribute__ is calling always!
Using it without super() can make a recursion!
'''


class BrokenRecursionRecord:
    """
    This class is invalid!
    Access to property cause a recursion problem!
    We can fix this using super() keyword
    """
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        return self._data[item]


class DictionaryRecord:
    """
    Fixed problem with recursion by using super()
    """
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        print(f'* Called getattributte({item!r})')
        data_dict = super().__getattribute__('_data')
        return data_dict[item]


dict_access = DictionaryRecord({'name': 'Marcin'})
print('dict_access name prop', dict_access.name)