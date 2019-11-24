#!/usr/bin/env python
from day1 import resolve_fuel, resolve_total_fuel, calculate_mass_fuel


def test_12_resolves_to_2():
    assert resolve_fuel(12) == 2


def test_14_resolves_to_2():
    assert resolve_fuel(14) == 2


def test_1969_resolves_to_654():
    assert resolve_fuel(1969) == 654


def test_100756_resolves_to_33583():
    assert resolve_fuel(100756) == 33583


def test_resolve_total_fuel_14_to_2():
    assert resolve_total_fuel(14) == 2


def test_resolve_total_fuel_1969_to_966():
    assert resolve_total_fuel(1969) == 966


def test_resolve_total_fuel_100756_to_50346():
    assert resolve_total_fuel(100756) == 50346


def test_correct_result():
    data = open('input')
    assert calculate_mass_fuel(data) == 3282935


if __name__ == "__main__":
    test_12_resolves_to_2()
    test_14_resolves_to_2()
    test_1969_resolves_to_654()
    test_100756_resolves_to_33583()
    test_resolve_total_fuel_14_to_2
    test_resolve_total_fuel_1969_to_966()
    test_resolve_total_fuel_100756_to_50346()

    test_correct_result()

