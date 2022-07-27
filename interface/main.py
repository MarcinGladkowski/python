import abc
"""
Python does not have built in Interface keyword
"""

""" Informal interface
    - based on duck_typing 
"""


class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Override InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


class EmailParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides InfromalParserInterface.extract_text()"""
        pass


print(issubclass(PdfParser, InformalParserInterface))
print(issubclass(EmailParser, InformalParserInterface))

"""MRO - method resolution order"""
print(PdfParser.__mro__)
print(EmailParser.__mro__)

"""Using meta classes"""


class ParserMeta(type):
    """A Parser metaclass that will be used for a parser class creation"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """
    Virtual base class

    This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via.__subclasscheck__()
    """
    pass


class PdfParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        pass


print(issubclass(PdfParserNew, UpdatedInformalParserInterface))  # True
print(PdfParserNew.__mro__)


class EmailParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        pass


print(issubclass(EmailParserNew, UpdatedInformalParserInterface))  # False

""" Virtual Base Class"""


class PersonMeta(type):
    """A person metaclass"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(csl, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))


class PersonSuper:
    """A person superclass"""

    def name(self) -> str:
        pass

    def age(self) -> int:
        pass


# Inherit subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass


class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__"""


# Formal interfaces

class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass


Double.register(float) # Double as virtual class of float
print(issubclass(float, Double))
print(isinstance(1.23, Double))


@Double.register
class Double64:
    """A 64-bit double-precision floating-point number"""
    pass


