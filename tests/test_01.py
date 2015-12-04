import pytest
from advent.problem_01 import (get_first_negative_floor,
    get_floor_number)

def test_get_floor_number():
    assert get_floor_number('(())') == 0
    assert get_floor_number('()()') == 0
    assert get_floor_number('(((') == 3
    assert get_floor_number('(()(()(') == 3
    assert get_floor_number('())') == -1
    assert get_floor_number('))(') == -1
    assert get_floor_number(')))') == -3
    assert get_floor_number(')())())') == -3


def test_get_first_negative_floor():
    assert get_first_negative_floor(')') == 1
    assert get_first_negative_floor('()())') == 5


def test_get_first_negative_floor_empty_string():
    if get_first_negative_floor('') is not None:
        pytest.fail('Empty string should be None')


def test_get_first_negative_floor_dirty():
    """Test against dirty/mixed input"""
    assert get_first_negative_floor('$di(r)t(y))') == 5
