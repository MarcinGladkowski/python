"""
Custom sources: Based on: https://bjoernricks.github.io/posts/python/context-manager/

To address these shortcomings, PEP 343 introduced the with statement and the Context Manager Protocol.

Writing own class with context managing is useful when you aware about initialization some process and closing it
 - files
 - network connections
 - resources

Why ?
- developer can forget about closing resources

With syntax is a syntactic sugar for:

manager = (EXPRESSION)
try:
    TARGET = manager.__enter__(manager)
    BLOCK
except:
    if not manager.__exit__(*sys.exc_info()):
        raise
else:
    manager.__exit__(None, None, None)

"""
from typing import Any

file = open("foo.txt")

try:
    # do something with the file
    file.write("Hello World")
finally:
    """Requires manual action"""
    file.close()


class ContextManager:
    def __enter__(self) -> Any:
        """
        Setup and acquire the resource and return it
        """

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """
        Shutdown and release the resource even if an error was raised
        """

"""
    Traditionally for files
    
    In this case you have to remember about closing file handler
"""
handler = open('some.txt')
try:
    handler.write('some content')
except:
    print('Error has occurred')
finally:
    handler.close()


"""
    Using context manager with "with" keyword
"""
with open('some.txt') as f:
    f.write('some content')


"""
    Custom class context manager
    - implement __enter__
    - implement __exit__
"""

from MoviesService import MovieServiceConnection

with MovieServiceConnection() as movie_service:
    print(movie_service.get_movie())












































