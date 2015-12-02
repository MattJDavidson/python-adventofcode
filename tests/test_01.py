import pytest
from advent.problem_01 import (get_floor_number)

def test_get_floor_number():
    assert get_floor_number('(())') == 0
    assert get_floor_number('()()') == 0
    assert get_floor_number('(((') == 3
    assert get_floor_number('(()(()(') == 3
    assert get_floor_number('())') == -1
    assert get_floor_number('))(') == -1
    assert get_floor_number(')))') == -3
    assert get_floor_number(')())())') == -3




