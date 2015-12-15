import pytest
from advent.problem_06 import (count_brightness,
                               count_lit_lights,
                               empty_grid,
                               follow_instruction,
                               modify_light,
                               parse_instruction)


def test_empty_grid():
    assert empty_grid(x=0, y=0) == [[]]
    assert empty_grid(x=1, y=1) == [[-1]]
    assert empty_grid(x=2, y=1) == [[-1,-1]]
    assert empty_grid(x=2, y=0) == [[]]


def test_modify_light():
    assert modify_light(-1, modification="turn on") == 1
    assert modify_light(1, modification="turn on") == 1

    assert modify_light(-1, modification="turn off") == -1
    assert modify_light(1, modification="turn off") == -1

    assert modify_light(-1, modification="toggle") == 1
    assert modify_light(1, modification="toggle") == -1


def test_parse_instruction():
    assert parse_instruction("turn on 0,0 through 2,2") == \
            ("turn on", (0,0), (2,2))
    assert parse_instruction("turn on 1,1 through 999,999") == \
            ("turn on", (1,1), (999,999))
    assert parse_instruction("turn on 1,1 through 1,1") == \
            ("turn on", (1,1), (1,1))


def test_follow_instruction():
    lights = [[-1]]
    assert follow_instruction(("turn on", (0,0), (0,0)), lights) == \
            [[1]]

    lights = [[1]]
    assert follow_instruction(("turn off", (0,0), (0,0)), lights) == \
            [[-1]]

    lights = [[1]]
    assert follow_instruction(("toggle", (0,0), (0,0)), lights) == \
            [[-1]]

    lights = [[-1]]
    assert follow_instruction(("toggle", (0,0), (0,0)), lights) == \
            [[1]]

    lights = [[-1,-1],
              [-1,-1]]
    assert follow_instruction(("toggle", (0,0), (1,1)), lights) == \
            [[1, 1],
             [1,1]]

    lights = [[-1, 1,-1],
              [ 1,-1, 1],
              [-1, 1,-1]]
    assert follow_instruction(("toggle", (0,0), (2,2)), lights) == \
            [[ 1,-1, 1],
             [-1, 1,-1],
             [ 1,-1, 1]]

    lights = [[-1,-1,-1],
              [-1,-1,-1],
              [-1,-1,-1]]
    assert follow_instruction(("toggle", (1,1), (2,2)), lights) == \
            [[-1,-1,-1],
             [-1, 1, 1],
             [-1, 1, 1]]


def test_count_lit_lights():

    lights = [[1]]
    assert count_lit_lights(lights) == 1

    lights = [[-1]]
    assert count_lit_lights(lights) == 0

    lights = [[-1,-1],
              [ 1, 1]]
    assert count_lit_lights(lights) == 2

    lights = [[-1,-1,-1],
              [-1, 1, 1],
              [-1, 1, 1]]
    assert count_lit_lights(lights) == 4


def test_new_modify_light():
    assert modify_light(0, new_commands=True, modification="turn on") == 1
    assert modify_light(1, new_commands=True, modification="turn on") == 2

    assert modify_light(1, new_commands=True, modification="turn off") == 0
    assert modify_light(2, new_commands=True, modification="turn off") == 1

    assert modify_light(0, new_commands=True, modification="toggle") == 2
    assert modify_light(1, new_commands=True, modification="toggle") == 3


def test_count_brightness():
    lights = [[1]]
    assert count_brightness(lights) == 1

    lights = [[0]]
    assert count_brightness(lights) == 0

    lights = [[ 0, 1],
              [ 0, 100]]
    assert count_brightness(lights) == 101

    lights = [[ 0, 0, 0],
              [ 0, 1, 1],
              [ 0, 1, 100]]
    assert count_brightness(lights) == 103


