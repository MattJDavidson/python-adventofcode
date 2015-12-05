#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use
as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

- If your secret key is abcdef, the answer is 609043, because the MD5 hash of
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
such number to do so.
- If your secret key is pqrstuv, the lowest number it combines with to make an
MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
pqrstuv1048970 looks like 000006136ef....
"""
import hashlib
import sys

import click


def acceptable_hash(hash, check_length=5):
    acceptable = False
    try:
        acceptable = all(char == '0' for char in hash[:check_length])
    except:
        #  We don't really care why it fails. Meh.
        pass
    return acceptable and len(hash) >= check_length


def generate_hash(token, num):
    return hashlib.md5('{}{}'.format(token, str(num)).encode(
        'utf-8')).hexdigest()


def first_acceptable_hash(token, check_length=5, floor=1, ceiling=999999):
    first = None
    for i in range(floor, ceiling):
        hash = generate_hash(token, i)
        if acceptable_hash(hash, check_length):
            first = i
            break
    return first


def calculate_solution_1(text):
    return first_acceptable_hash(text)


def calculate_solution_2(text):
    return first_acceptable_hash(text, check_length=6, ceiling=9999999)


@click.command()
@click.option('--source_file', default='data/04.txt',
              help='source data file for problem')
def main(source_file):
    """Simple solution to adventofcode problem 4."""
    data = ''
    with open(source_file) as source:
        data = source.read()
    print(first_acceptable_hash(data))
    print(first_acceptable_hash(data, check_length=6, ceiling=9999999))


if __name__ == "__main__":
    sys.exit(main())
