#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an
order for more. They have a list of the dimensions (length l, width w, and
height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which
makes calculating the required wrapping paper for each gift a little easier:
    1. Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    1. The elves also need a little extra paper for each present: the area of
       the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of
wrapping paper plus 6 square feet of slack, for a total of 58 square feet.  A
present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of
wrapping paper plus 1 square foot of slack, for a total of 43 square feet.  All
numbers in the elves' list are in feet. How many total square feet of wrapping
paper should they order?

"""
import sys

import click


def format_lines(text):
    """Returns list of list of ints"""
    return [[int(i) for i in str.split(line, 'x')] for line in str.split(text)]


def calculate_area(length, width, height):
    """Calculates the area + slack based on dimensions"""
    area_of_sides = [length*width,
                     width*height,
                     height*length]
    return sum(2*area_of_sides, min(area_of_sides))


def total_area(text):
    """Returns total area of wrapping paper"""
    return sum(calculate_area(*dimensions) for dimensions in format_lines(text))


@click.command()
@click.option('--source_file', default='data/02.txt',
              help='source data file for problem')
def main(source_file):
    """Simple solution to adventofcode problem 2."""
    data = ''
    with open(source_file) as source:
        data = source.read()
    print('Total required wrapping paper for part 1 is {}'.format(total_area(data)))


if __name__ == "__main__":
    sys.exit(main())
