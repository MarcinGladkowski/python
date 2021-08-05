"""
Use when to clear which exceptions are cached, but some will be propagate.
"""
import json


def load_json(data, key):
    try:
        print('* Load data JSON')
        result_dict = json.loads(data)  # can throw ValueError
    except ValueError as e:
        print('* Catch ValueError exception')
        raise KeyError(key) from e
    else:
        print('* Search key')
        return result_dict[key]  # can throw KeyError


assert load_json('{"foo": "bar"}', "foo") == "bar"

load_json('{"foo": "test"}', "fasaoo")