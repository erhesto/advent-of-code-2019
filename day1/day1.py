def resolve_fuel(mass):
    return mass // 3 - 2


def generate_numbers(data):
    yield from (int(num.strip()) for num in data if num)


def main():
    input_data = open('input')
    numbers = generate_numbers(input_data)
    result = sum(map(resolve_fuel, numbers))
    print(result)


if __name__ == "__main__":
    main()

