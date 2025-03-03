import dataclasses
from typing import TypedDict


class Movie(TypedDict):
    title: str


"""
Usage as type annotations for dictionary

Therefore for this idea we can use `dataclass` or `pydantic`
"""
movie: Movie = { 'title': 'Titanic' }

"""Comparison to dataclass"""
@dataclasses.dataclass
class PatchUser:
    """For dataclasses all properties have to be available all the time"""
    name: str | None = None
    subscription: str | None = None


class PatchUserTypeDict(TypedDict, total=False):
    name: str | None
    subscription: str | None # field not needed


