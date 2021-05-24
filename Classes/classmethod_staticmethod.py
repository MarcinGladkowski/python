class MyClass:
    """
    * Instance method *
    Can modify object instance state
    Can modify class state

    self - it's access to specified instance object

    Only access to method when the instance is created
    """

    def method(self):
        return 'instance method called', self

    """
    * Class method *
    Can't modify object instance state
    Can modify class state
    
    cls - it's a class, not specified instance!
    
    Usage with class instance
    """

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    """
    * Static method *
    Can't modify object instance state
    Can't modify class state
    
    Usage without class instance
    """

    @staticmethod
    def staticmethod():
        return 'static method called'


my_object = MyClass()
print(my_object.method())
print(my_object.classmethod())
print(my_object.staticmethod())
# without creating instance of class
print(MyClass.classmethod())
print(MyClass.staticmethod())

'''
Use classmethod as a simple factory method
'''


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self) -> str:
        return f"{self.ingredients}"

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese'])


Pizza.margherita()
Pizza.prosciutto()

'''
static method
'''


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(2, 4))
