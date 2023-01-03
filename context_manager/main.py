"""
Writing own class with context managing is useful when you aware about initialization some process and closing it
 - files
 - network connections
 - resources
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
