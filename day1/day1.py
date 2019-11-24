def resolve_fuel(mass):
    """
    Resolves amount of fuel for given mass.
    """
    return mass // 3 - 2


def resolve_total_fuel(mass):
    """
    Resolves amount of fuel for mass plus extra fuel that is taking
    into consideration fuel mass itself.
    """
    total_fuel = 0

    while (mass := resolve_fuel(mass)) > 0:
        total_fuel += mass

    return total_fuel


def calculate_mass_fuel(elements_mass, with_extra_mass=False):
    fuel_calculation_method = resolve_total_fuel if with_extra_mass else resolve_fuel

    return sum(map(fuel_calculation_method, elements_mass))

