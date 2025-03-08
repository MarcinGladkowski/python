import typing as t


T = t.TypeVar("T", bound=str | int | float) # tightens the type to str, int or float

# v1, v2 and outcome should all be of type T
def sum(v1: T, v2: T) -> T:
    return v1 + v2

numbers = sum(10, 20)
strs = sum("app", "le")

print(numbers)
print(strs)

import typing as t
from datetime import datetime
from abc import ABC, abstractmethod

T = t.TypeVar("T") # 👈 We still use the TypeVar

# 👇 Now we must also rely on Generic to say the class
# accepts a type
class BaseDatabase(t.Generic[T], ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> T:
        ...

    @abstractmethod
    def list_all(self) -> list[T]:
        ...

    @abstractmethod
    def create(self, entity: T) -> None:
        ...


class Company:  # Model sample for the company DB
    name: str
    phone: str
    address: str


class CompanyDatabase(BaseDatabase[Company]):
    def get_by_id(self, id: int) -> Company:
        return super().get_by_id(id)

    def list_all(self) -> list[Company]:
        return super().list_all()

    def create(self, entity: Company) -> None:
        return super().create(entity)