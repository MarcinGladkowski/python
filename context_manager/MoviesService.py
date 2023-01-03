import random
from types import TracebackType
from typing import Optional, Type
from logger import log

class MovieService:

    def connect(self):
        print('connecting ...')

    def get_movie(self):
        number = random.randint(1, 100)
        if number % 10 == 0:
            raise ValueError

        return f"Movie [{number}]"

    def close(self):
        print('closing ...')


class MovieServiceConnection:

    def __init__(self) -> None:
        self.movie_service = MovieService()

    def __enter__(self):
        self.movie_service.connect()
        return self.movie_service

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ):
        if exc_type:
            log('Something went wrong...')
        self.movie_service.close()

