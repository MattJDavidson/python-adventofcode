import pytest
from advent.problem_02 import (calculate_area,
                               calculate_wribbon,
                               format_lines,
                               total_area,
                               total_wribbon)


def test_format_lines():
    assert format_lines('1x2x3\n') == [[1,2,3]]
    assert format_lines('1x2x3\n4x5x6') == \
            [[1,2,3], [4,5,6]]


def test_calculate_area():
    assert calculate_area(0, 0, 0) == 0
    assert calculate_area(2,3,4) == 58
    assert calculate_area(1, 1, 10) == 43


def test_total_area():
    assert total_area('0x0x0\n') == 0
    assert total_area('2x3x4\n') == 58
    assert total_area('2x3x4\n0x0x0\n') == 58
    assert total_area('2x3x4\n1x1x10\n') == 58+43


def test_calculate_wribbon():
    assert calculate_wribbon([0, 0, 0]) == 0
    assert calculate_wribbon([2, 3, 4]) == 34
    assert calculate_wribbon([1, 1, 10]) == 14


def test_total_wribbon():
    assert total_wribbon('0x0x0\n') == 0
    assert total_wribbon('2x3x4\n') == 34
    assert total_wribbon('2x3x4\n0x0x0\n') == 34
    assert total_wribbon('2x3x4\n1x1x10\n') == 34+14
