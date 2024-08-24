import pytest
from main import check

def test_check():
    assert check(6) == True

def test_check2():
    assert check(5) == False

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (56, True),
    (-3, False),
    (0, True)
])

def test_check_with_params(number, expected):
    assert check(number) == expected

