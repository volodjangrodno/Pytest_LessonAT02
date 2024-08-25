import pytest
from main2 import is_palindrom

def test_is_palindrom_true():
    assert is_palindrom('racecar') == True

def test_is_palindrom_false():
    assert is_palindrom('hello') == False

@pytest.mark.parametrize("test_input, expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("ab", False),
    ("race car", False)
])

def test_palindrom(test_input, expected):
    assert is_palindrom(test_input) == expected