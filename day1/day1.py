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


def generate_numbers(data):
    yield from (int(num.strip()) for num in data if num)


def calculate_mass_fuel(data, with_extra_mass=False):
    elements_mass = generate_numbers(data)
    fuel_calc = resolve_total_fuel if with_extra_mass else resolve_fuel

    return sum(map(fuel_calc, elements_mass))


def main():
    input_data = open('input')
    basic_fuel_mass = calculate_mass_fuel(input_data)
    input_data.seek(0)
    total_fuel_mass = calculate_mass_fuel(input_data, with_extra_mass=True)
    print(f"{basic_fuel_mass=}")
    print(f"{total_fuel_mass=}")


if __name__ == "__main__":
    main()

