import pytest
from advent.problem_05 import (forbidden_patterns,
                               has_letter_hop,
                               nice_string,
                               nicer_string,
                               num_vowels,
                               non_overlapping_pair,
                               repeated_chars,
                               total_nice_strings,
                               total_nicer_strings)

def test_num_vowels():
    assert num_vowels('') == 0
    assert num_vowels('a') == 1
    assert num_vowels('ba') == 1
    assert num_vowels('aaa') == 3


def test_repeated_chars():
    assert repeated_chars('') is False
    assert repeated_chars('a') is False
    assert repeated_chars('aba') is False

    assert repeated_chars('aa') is True
    assert repeated_chars('abbc') is True


def test_forbidden_patterns():
    assert forbidden_patterns('ab') is True
    assert forbidden_patterns('cd') is True
    assert forbidden_patterns('pq') is True
    assert forbidden_patterns('xy') is True

    assert forbidden_patterns('') is False
    assert forbidden_patterns('acefg') is False


def test_nice_string():
    assert nice_string('ugknbfddgicrmopn') is True
    assert nice_string('aaa') is True

    assert nice_string('') is False
    assert nice_string('jchzalrnumimnmhp') is False
    assert nice_string('haegwjzuvuyypxyu') is False
    assert nice_string('dvszwmarrgswjxmb') is False


def test_total_nice_strings():
    assert total_nice_strings('') == 0
    assert total_nice_strings('jchzalrnumimnmhp') == 0
    assert total_nice_strings('ab\njchzalrnumimnmhp') == 0

    assert total_nice_strings('aaa\njchzalrnumimnmhp') == 1
    assert total_nice_strings('aaa\nabjchzalrnumimnmhp') == 1
    assert total_nice_strings('aaa\neee\niii') == 3


def test_non_overlapping_pair():
    assert non_overlapping_pair('') is False
    assert non_overlapping_pair('aaa') is False
    assert non_overlapping_pair('aca') is False

    assert non_overlapping_pair('aaaa') is True
    assert non_overlapping_pair('abab') is True
    assert non_overlapping_pair('aaccaa') is True
    assert non_overlapping_pair('xxyxx') is True


def test_has_letter_hop():
    assert has_letter_hop('') is False
    assert has_letter_hop('aa') is False
    assert has_letter_hop('abcdefgh') is False
    assert has_letter_hop('abbaabb') is False

    assert has_letter_hop('xyx') is True
    assert has_letter_hop('xxyxx') is True
    assert has_letter_hop('abcdefeghi') is True
    assert has_letter_hop('aaa') is True


def test_nicer_string():
    assert nicer_string('') is False
    assert nicer_string('xxyxx') is True


def test_total_nicer_strings():
    assert total_nicer_strings('') == 0
    assert total_nicer_strings('aa') == 0
    assert total_nicer_strings('abcdefgh') == 0
    assert total_nicer_strings('abbaabb') == 0
