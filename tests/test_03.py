import pytest
from advent.problem_03 import (number_of_houses_covered,
                               map_single_delivery,
                               map_multiple_deliveries,
                               split_directions,
                               update_point)


def test_update_point():
    assert update_point('', (0,0)) == (0,0)
    assert update_point('^', (0,0)) == (0,-1)
    assert update_point('<', (0,0)) == (-1,0)
    assert update_point('v', (0,0)) == (0,1)
    assert update_point('>', (0,0)) == (1,0)
    assert update_point('$', (0,0)) == (0,0)


def test_map_single_delivery():
    assert map_single_delivery('') == {(0,0)}
    assert map_single_delivery('>') == {(0,0), (1,0)}
    assert map_single_delivery('><>') == {(0,0), (1,0)}
    assert map_single_delivery('^v><<>v^') == {(0,0), (1,0), (0,1), (-1,0), (0,-1)}


def test_number_of_houses_covered():
    assert number_of_houses_covered('>') == 2
    assert number_of_houses_covered('^>v<') == 4
    assert number_of_houses_covered('^v^v^v^v') == 2


def test_split_directions():
    assert split_directions('>>') == ('>','>')
    assert split_directions('>>>') == ('>>','>')


def test_map_multiple_deliveries():
    assert map_multiple_deliveries('') == {(0,0)}
    assert map_multiple_deliveries('>>>') == {(0,0), (1,0), (2,0)}
