#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers
to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.
- toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning
off the ones that were on, and turning on the ones that were off.
- turn off 499,499 through 500,500 would turn off (or leave off) the middle
four lights.

After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize you
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of
those lights by 2.

What is the total brightness of all lights combined after following Santa's
instructions?

For example:

- turn on 0,0 through 0,0 would increase the total brightness by 1.
- toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""
from collections import Counter
import re
import sys

import click

ON = 1
OFF = -1


def count_lit_lights(lights):
    return sum([Counter(row).get(1, 0) for row in lights])


def count_brightness(lights):
    return sum(light for row in lights for light in row)


def empty_grid(x=1000, y=1000, new_commands=False):
    OFF = 0 if new_commands else -1
    return [[OFF] * x for _ in range(y)] if not (x == 0 or y == 0) else [[]]


def modify_light(light, new_commands=False, modification="toggle"):
    return {'turn on': 1 if not new_commands else light + 1,
            'turn off': -1 if not new_commands else (light-1) if light >= 1 else 0,
            'toggle': light * -1 if not new_commands else light + 2,
            }.get(modification)


def parse_instruction(text):
    p = re.compile(r"""(?P<mod>(turn\s(on|off))|(toggle)) # modification
                   \s(?P<x0>\d*),(?P<y0>\d*)              # x0,y0
                   \sthrough
                   \s(?P<x1>\d*),(?P<y1>\d*)              # x1,y1
                   """, re.VERBOSE)
    m = re.search(p, text)
    return (m.group('mod'),
            (int(m.group('x0')), int(m.group('y0'))),
            (int(m.group('x1')), int(m.group('y1'))))


def follow_instruction(instruction, lights, new_commands=False):
    x_coords = range(instruction[1][0], instruction[2][0]+1)
    y_coords = range(instruction[1][1], instruction[2][1]+1)
    for x in x_coords:
        for y in y_coords:
            lights[y][x] = modify_light(
                lights[y][x], new_commands, modification=instruction[0])

    return lights


def calculate_solution_1(text):
    lights = empty_grid()
    for line in text.split('\n'):
        follow_instruction(parse_instruction(line), lights)
    return count_lit_lights(lights)


def calculate_solution_2(text):
    lights = empty_grid(new_commands=True)
    for line in text.split('\n'):
        follow_instruction(parse_instruction(line), lights, new_commands=True)
    return count_brightness(lights)


@click.command()
@click.option('--source_file', default='data/06.txt',
              help='source data file for problem')
def main(source_file):
    """Simple solution to adventofcode problem 6."""
    data = ''
    with open(source_file) as source:
        data = source.read()

    print('Number of lights switched on is: {}'.format(
        calculate_solution_1(data)))
    print('Brightness of lights is: {}'.format(
        calculate_solution_2(data)))


if __name__ == "__main__":
    sys.exit(main())
