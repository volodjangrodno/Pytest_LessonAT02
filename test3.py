import pytest
from main3 import sort_list

def test_sort_list1():
    assert ([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]

def test_sort_list2():
    assert ([5, -3, 8, 1, 0]) == [-3, 0, 1, 5, 8]
