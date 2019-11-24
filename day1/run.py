from fuelcalulation import calculate_mass_fuel, CalculationMethods
from helpers import prepare_data


def main():    
    input_data = open('input')

    basic_fuel_mass = calculate_mass_fuel(prepare_data(input_data), CalculationMethods.SIMPLE)
    total_fuel_mass = calculate_mass_fuel(prepare_data(input_data), CalculationMethods.TOTAL)

    print(f"{basic_fuel_mass=}")
    print(f"{total_fuel_mass=}")


if __name__ == "__main__":
    main()
