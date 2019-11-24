from day1 import calculate_mass_fuel
from helpers import prepare_data


def main():    
    input_data = open('input')    
    basic_fuel_mass = calculate_mass_fuel(prepare_data(input_data))
    total_fuel_mass = calculate_mass_fuel(prepare_data(input_data), with_extra_mass=True)
    print(f"{basic_fuel_mass=}")
    print(f"{total_fuel_mass=}")


if __name__ == "__main__":
    main()
