import pytest
from advent.problem_04 import (acceptable_hash,
                               first_acceptable_hash,
                               generate_hash)


def test_acceptable_hash():
    assert acceptable_hash('00000') == True
    assert acceptable_hash('000001dbbfa') == True
    assert acceptable_hash('000006136ef') == True

    assert acceptable_hash('00001') == False
    assert acceptable_hash('') == False
    assert acceptable_hash('100000') == False


def test_generate_hash():
    assert generate_hash('abcdef', 609043) == '000001dbbfa3a5c83a2d506429c7b00e'
    assert generate_hash('pqrstuv', 1048970) == '000006136ef2ff3b291c85725f17325c'


def test_first_acceptable_hash():
    assert first_acceptable_hash('$', ceiling=2) is None
    assert first_acceptable_hash('abcdef', floor=609042, ceiling=609044) \
            == 609043
    assert first_acceptable_hash('pqrstuv', floor=1048969, ceiling=1048971) \
            == 1048970
