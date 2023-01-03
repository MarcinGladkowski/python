"""
Writing own class with context managing is useful when you aware about initialization some process and closing it
(database/source/resource) connection etc.

"""

from MoviesService import MovieServiceConnection

with MovieServiceConnection() as movie_service:
    print(movie_service.get_movie())


