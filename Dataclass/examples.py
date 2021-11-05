from dataclasses import dataclass, field


"""
* Use for store data which can be mutable
* Other possibles to store data are: tuples (and namedtuple), classes, dictionaries but
- tuple is immutable and only can get data by indexes
- class can be to complex
- dictionary has access by string keys

* We don't need implement __init__ method
* You can easily compare it with other 
* Implement methods like __repr__ and __eq__. Thanks to that we can easily compare objects 
* You can add specific methods
* Can be immutable also
"""


@dataclass
class Person:
    name: str
    job: str
    salary: int = field(default=1000)

    def calculate_salary(self):
        return 10_000


person_1 = Person('Marcin', 'programmer')

print(person_1.name)
print(person_1.job)

person_1.job = 'boss'

print(person_1.job)

print(person_1 == Person('Marcin', 'boss'))

person_3 = Person(name="Marcin", job='programmer')
person_3.calculate_salary()


print(person_3)