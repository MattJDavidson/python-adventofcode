#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or
nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or
aeiouaeiouaeiou.  It contains at least one letter that appears twice in a row,
like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).  It does not contain the
strings ab, cd, pq, or xy, even if they are part of one of the other
requirements.

For example:
- ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a
double letter (...dd...), and none of the disallowed substrings.
- aaa is nice because it has at least three vowels and a double letter, even
though the letters used by different rules overlap.
- jchzalrnumimnmhp is naughty because it has no double letter.
- haegwjzuvuyypxyu is naughty because it contains the string xy.
- dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""
import sys

import click

from string import ascii_lowercase as ALPHABET

FORBIDDEN = ['ab', 'cd', 'pq', 'xy']
VOWELS = 'aeiou'


def num_vowels(text):
    return len([char for char in text if char in VOWELS])


def repeated_chars(text, repeats=2):
    return any([char*repeats in text for char in ALPHABET])


def forbidden_patterns(text):
    return any([pattern in text for pattern in FORBIDDEN])


def nice_string(line):
    return all([num_vowels(line) >= 3,
               repeated_chars(line),
               not forbidden_patterns(line)])


def total_nice_strings(text):
    return sum([nice_string(line) for line in text.split()])


def non_overlapping_pair(text):
    found = False
    for i, char0 in enumerate(text[:-2]):
        pair = (char0, text[i+1])
        if found:
            break

        remaining_text = text[i+2:]
        for j, char1 in enumerate(remaining_text[:-1]):
            if (char1, remaining_text[j+1]) == pair:
                found = True
                break
    return found


def has_letter_hop(text):
    return any([text[i+2] == char for i, char in enumerate(text[:-2])])


def nicer_string(text):
    return non_overlapping_pair(text) and has_letter_hop(text)


def total_nicer_strings(text):
    return sum([nicer_string(line) for line in text.split()])


def calculate_solution_1(text):
    return total_nice_strings(text)


def calculate_solution_2(text):
    return total_nicer_strings(text)


@click.command()
@click.option('--source_file', default='data/05.txt',
              help='source data file for problem')
def main(source_file):
    """Simple solution to adventofcode problem 5."""
    data = ''
    with open(source_file) as source:
        data = source.read()
    print('Santa found {} entries on the nice list.'.format(
        calculate_solution_1(data)))
    print('Santa found {} entries on the nicer list.'.format(
        calculate_solution_2(data)))


if __name__ == "__main__":
    sys.exit(main())
