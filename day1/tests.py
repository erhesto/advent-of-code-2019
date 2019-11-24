#!/usr/bin/env python
from day1 import resolve_fuel


def test_12_resolves_to_2():
    assert resolve_fuel(12) == 2


def test_14_resolves_to_2():
    assert resolve_fuel(14) == 2


def test_1969_resolves_to_654():
    assert resolve_fuel(1969) == 654


def test_100756_resolves_to_33583():
    assert resolve_fuel(100756) == 33583


if __name__ == "__main__":
    test_12_resolves_to_2()
    test_14_resolves_to_2()
    test_1969_resolves_to_654()
    test_100756_resolves_to_33583()
