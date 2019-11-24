from fuelcalulation import calculate_mass_fuel, CALCULATION_METHODS
from helpers import prepare_data


def main():    
    input_data = open('input')

    basic_fuel_mass = calculate_mass_fuel(prepare_data(input_data), CALCULATION_METHODS['simple'])
    total_fuel_mass = calculate_mass_fuel(prepare_data(input_data), CALCULATION_METHODS['total'])

    print(f"{basic_fuel_mass=}")
    print(f"{total_fuel_mass=}")


if __name__ == "__main__":
    main()
