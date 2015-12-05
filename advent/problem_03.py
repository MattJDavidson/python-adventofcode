#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

However, the elf back at the north pole has had a little too much eggnog, and
so his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

For example:

- > delivers presents to 2 houses: one at the starting location, and one to the
east.
- ^>v< delivers presents to 4 houses in a square, including twice to the
house at his starting/ending location.
- ^v^v^v^v^v delivers a bunch of presents
to some very lucky children at only 2 houses.
"""
import sys

import click


def update_point(move, point):
    """Returns new point representing position after move"""
    moves = {
        '^': (0, -1),
        '<': (-1, 0),
        'v': (0, 1),
        '>': (1, 0),
    }
    return (point[0]+moves.get(move, (0, 0))[0],
            point[1]+moves.get(move, (0, 0))[1])


def map_known_points(text):
    point = (0, 0)
    points = set({point})
    for move in text:
        point = update_point(move, point)
        points.add(point)
    return points


def number_of_houses_covered(text):
    return len(map_known_points(text))


def calculate_solution_1(text):
    return number_of_houses_covered(text)


def calculate_solution_2(text):
    #  TODO
    return 0


@click.command()
@click.option('--source_file', default='data/03.txt',
              help='source data file for problem')
def main(source_file):
    """Simple solution to adventofcode problem 3."""
    data = ''
    with open(source_file) as source:
        data = source.read()
    print('Santa gave at least one present to {} houses.'.format(
        number_of_houses_covered(data)))


if __name__ == "__main__":
    sys.exit(main())
