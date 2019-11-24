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
    pass


def generate_numbers(data):
    yield from (int(num.strip()) for num in data if num)


def calculate_mass_fuel(data):
    elements_mass = generate_numbers(data)
    return sum(map(resolve_fuel, elements_mass))


def main():
    input_data = open('input')
    basic_fuel_mass = calculate_mass_fuel(input_data)
    print(f"{basic_fuel_mass=}")


if __name__ == "__main__":
    main()

