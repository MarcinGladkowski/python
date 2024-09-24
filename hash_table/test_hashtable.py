from hash_table.hashtable import Pair
from hashtable import HashTable
import pytest
from pytest_unordered import unordered


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
    assert len(HashTable(capacity=100)) == 100

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

    assert len(sample_data) == 100

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
    assert len(sample_data) == 100

    del sample_data["hola"]

    assert "hola" not in sample_data
    assert ("hola", "hello") not in sample_data.pairs
    assert len(sample_data) == 100

def test_should_update_key_value_pair(sample_data):
    assert sample_data["hola"] == "hello"
    assert len(sample_data) == 100

    sample_data["hola"] = "hallo"

    assert sample_data['hola'] == "hallo"
    assert sample_data[98.6] == 37
    assert sample_data[False] == True
    assert len(sample_data) == 100

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