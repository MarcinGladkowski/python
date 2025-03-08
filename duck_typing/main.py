"""
Duck typing
- If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.
- based on public API of an object/methods
- not rely on any inheritance hierarchy
"""
from typing import Protocol


class CalculateBossSalary:
    def calculate(self, employee):
        pass

class CalculateWorkerSalary:
    def calculate(self, employee):
        pass

"""Classes has the same behavior but different implementation"""
def calculate_salary(salary_calculator, employee):
    """we want to eliminate isinstance() check or hasattr() check"""
    salary_calculator.calculate(employee)


"""One of the solution is to use abstract base class"""
from abc import ABC, abstractmethod

class SalaryCalculator(ABC):
    @abstractmethod
    def calculate(self, employee):
        raise NotImplemented("Method must be implemented in subclass")


"""Other solution is to Protocol"""
class ProtocolCalculation(Protocol):
    """
    Protocol is a way to define a set of methods that an object must have to be considered as a certain type

    Protocols allows us to more advanced type checking without using inheritance
    """
    def calculate(self, employee): ...


def protocol_calculate_salary(salary_calculator: ProtocolCalculation, employee):
    salary_calculator.calculate(employee)


from collections.abc import Collection

def mean(grades: list | tuple | set) -> float:
    return sum(grades) / len(grades)

def mean_better(grades: Collection) -> float:
    return sum(grades) / len(grades)