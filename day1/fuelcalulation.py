from typing import List


def resolve_fuel(mass: int) -> int:
    """
    Resolves amount of fuel for given mass.
    """
    return mass // 3 - 2


def resolve_total_fuel(mass: int) -> int:
    """
    Resolves amount of fuel for mass plus extra fuel that is taking
    into consideration fuel mass itself.
    """
    total_fuel = 0

    while (mass := resolve_fuel(mass)) > 0:
        total_fuel += mass

    return total_fuel


def calculate_mass_fuel(elements_mass: List[int], calculation_method) -> int:
    return sum(map(calculation_method, elements_mass))


CALCULATION_METHODS = {'simple': resolve_fuel, 'total': resolve_total_fuel}
