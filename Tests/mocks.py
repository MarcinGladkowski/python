from datetime import datetime
from unittest.mock import Mock

mock = Mock(spec=get_animals)

expected = [
    ('Spot', datetime(2019, 6, 5 ,11, 15)),
    ('Fluffy', datetime(2019, 12, 5 ,11, 15)),
    ('Jojo', datetime(2019, 6, 2 ,11, 15)),
]
mock.return_value = expected

"""
Check other functions help(unittest.mock.Mock)
"""


"""Datetime mock"""
now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2019, 6, 5, 15, 45)