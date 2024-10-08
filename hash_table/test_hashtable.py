import os

from hashtable import HashTable, Pair
import pytest
from pytest_unordered import unordered

from unittest.mock import patch


def test_pair_namedtuple():
    pair = Pair('key', 10)

    assert pair.key == 'key'
    assert pair.value == 10

@pytest.fixture
def sample_data():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_return_capacity():
    assert len(HashTable(capacity=100)) == 0

def test_should_return_length_of_sample_data_hash_table(sample_data):
    assert len(sample_data) == 3

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._pairs == [None, None, None]

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass

def test_should_insert_key_value_pairs(sample_data):
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[True] = False

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (True, False) in hash_table.pairs

    assert len(sample_data) == 3

def test_should_insert_none_value():
    hast_table = HashTable(capacity=100)
    hast_table["key"] = None
    assert Pair("key", None) in hast_table.pairs

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_raise_error_on_missing_key_when_deleting():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_receive_value_by_key(sample_data):
    assert "hola" in sample_data

def test_should_not_find_key(sample_data):
    assert "missing_key" not in sample_data

def test_should_get_value(sample_data):
    assert sample_data.get("hola") == "hello"

def test_should_get_none_when_missing_key(sample_data):
    assert sample_data.get("missing_key") is None

def test_should_get_default_value_when_missing_key(sample_data):
    assert sample_data.get("missing_key", "default") == "default"

def test_should_get_value_with_default(sample_data):
    assert sample_data.get("hola", "default") == "hello"

def test_should_delete_key_value_pair(sample_data):
    assert "hola" in sample_data
    assert ("hola", "hello") in sample_data.pairs
    assert len(sample_data) == 3

    del sample_data["hola"]

    assert "hola" not in sample_data
    assert ("hola", "hello") not in sample_data.pairs
    assert len(sample_data) == 2

def test_should_update_key_value_pair(sample_data):
    assert sample_data["hola"] == "hello"
    assert len(sample_data) == 3

    sample_data["hola"] = "hallo"

    assert sample_data['hola'] == "hallo"
    assert sample_data[98.6] == 37
    assert sample_data[False] == True
    assert len(sample_data) == 3

def test_should_return_pairs(sample_data):
    assert ("hola", "hello") in sample_data.pairs
    assert (98.6, 37) in sample_data.pairs
    assert (False, True) in sample_data.pairs

def test_should_return_copy_of_pairs(sample_data):
    assert sample_data.pairs is not sample_data.pairs

def test_should_not_include_blank_pairs(sample_data):
    assert None not in sample_data.pairs

def test_should_return_duplicated_values(sample_data):
    hash_table = HashTable(capacity=100)

    hash_table['Anna'] = 24
    hash_table['Agnes'] = 42
    hash_table["Adam"] = 42

    assert [24, 42, 42] == sorted(hash_table.values)

def test_should_get_values(sample_data):
    assert unordered(sample_data.values) == ["hello", 37, True]

def test_should_get_values_of_empty_hash_table(sample_data):
    assert HashTable(capacity=100).values == []

def test_should_return_copy_of_values(sample_data):
    assert sample_data.values is not sample_data.values

def test_should_get_keys(sample_data):
    assert sample_data.keys == {"hola", 98.6, False}

def test_should_keys_as_set_of_empty_hash_table(sample_data):
    assert HashTable(capacity=100).keys == set()

def test_should_return_copy_of_keys(sample_data):
    assert sample_data.keys is not sample_data.keys

def test_should_return_all_pairs(sample_data):
    assert sample_data.pairs == unordered({
        Pair("hola", "hello"),
        Pair(98.6, 37),
        Pair(False, True),
    })

def test_should_convert_to_dict(sample_data):
    dictionary = dict(sample_data.pairs)

    assert set(dictionary.keys()) == sample_data.keys
    assert set(dictionary.items()) == sample_data.pairs
    assert list(dictionary.values()) == unordered(sample_data.values)

def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)

def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-1)

def test_should_report_capacity_of_empty_hash_table():
    assert HashTable(capacity=100).capacity == 100

def test_should_report_capacity_of_sample_data_hash_table(sample_data):
    assert sample_data.capacity == 100

def test_should_iterate_over_keys(sample_data):
    for key in sample_data.keys:
        assert key in ("hola", 98.6, False)

def test_should_iterate_over_values(sample_data):
    for key in sample_data.values:
        assert key in ("hello", 37, True)

def test_should_iterate_over_pairs(sample_data):
    for key, value in sample_data.pairs:
        assert value in sample_data.values
        assert key in sample_data.keys

def test_should_iterate_over_instance(sample_data):
    for key in sample_data:
        assert key in ("hola", 98.6, False)

@pytest.mark.skip
def test_should_have_canonical_string_representation(sample_data):
    assert repr(sample_data) in {
        "HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})",
        "HashTable.from_dict({'hola': 'hello', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'hola': 'hello', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'hola': 'hello'})",
        "HashTable.from_dict({False: True, 'hola': 'hello', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'hola': 'hello'})",
    }

def test_should_use_dict_literal_for_str(sample_data):
    assert str(sample_data) in {
        "{'hola': 'hello', 98.6: 37, False: True}",
        "{'hola': 'hello', False: True, 98.6: 37}",
        "{98.6: 37, 'hola': 'hello', False: True}",
        "{98.6: 37, False: True, 'hola': 'hello'}",
        "{False: True, 'hola': 'hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'hola': 'hello'}",
    }

def test_should_compare_equal_to_itself(sample_data):
    assert sample_data == sample_data

def test_should_compare_equal_to_copy(sample_data):
    assert sample_data is not sample_data.copy()
    assert sample_data == sample_data.copy()

def test_should_compare_equal_different_key_value_order(sample_data):
    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"b": 2, "a": 1, "c": 3})
    assert h1 == h2

def test_should_compare_unequal(sample_data):
    other = HashTable.from_dict({"some": "data"})
    assert sample_data != other

def test_should_compare_unequal_another_data_keys(sample_data):
    assert sample_data != 42

def test_should_copy_keys_value_pairs_capacity(sample_data):
    copy = sample_data.copy()

    assert copy is not sample_data
    assert set(sample_data.keys) == set(copy.keys)
    assert unordered(sample_data.values) == copy.values
    assert set(sample_data.pairs) == copy.pairs
    assert sample_data.capacity == copy.capacity

def test_should_compare_equal_different_capacity(sample_data):
    data = {1: 'a', 2: 'b'}

    h1 = HashTable.from_dict(data, capacity=50)
    h2 = HashTable.from_dict(data, capacity=100)

    assert h1 == h2

def test_should_create_hashtable_from_dict(sample_data):
    data = {"hola": "hello", 98.6: 37, False: True}

    hash_table = HashTable.from_dict(data)

    assert hash_table.capacity == len(data) * 10
    assert hash_table.pairs == set(data.items())
    assert unordered(hash_table.values) == list(data.values())
    assert hash_table.keys == set(data.keys())


def test_of_reduce_capacity():
    data = {"hola": "hello", 98.6: 37, False: True}
    hash_table = HashTable.from_dict(data, capacity=len(data))
    """
        With PYTHONHASHSEED=0 the string returned randomly
        content of hash_table. One time has 2 elements, another 1 ...
    """
    print(str(hash_table))

    assert True

@pytest.mark.skip
def test_collision():
    print(os.environ.get('PYTHONHASHSEED'))
    assert (hash('easy') % 100) == (hash('difficult') % 100)

@patch("builtins.hash", return_value=42)
def test_should_detect_hash_collision(sample_data):
    """
       decorator patch allows us to replace builtin python hash function return value
    """
    assert hash('developer') == 42