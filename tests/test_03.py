import pytest
from advent.problem_03 import (map_known_points, update_point)


def test_update_point():
    assert update_point('', (0,0)) == (0,0)
    assert update_point('^', (0,0)) == (0,-1)
    assert update_point('<', (0,0)) == (-1,0)
    assert update_point('v', (0,0)) == (0,1)
    assert update_point('>', (0,0)) == (1,0)
    assert update_point('$', (0,0)) == (0,0)


def test_map_known_points():
    assert map_known_points('') == {(0,0)}
    assert map_known_points('>') == {(0,0), (1,0)}
    assert map_known_points('><>') == {(0,0), (1,0)}
    assert map_known_points('^v><<>v^') == {(0,0), (1,0), (0,1), (-1,0), (0,-1)}
