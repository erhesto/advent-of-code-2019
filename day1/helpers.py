def generate_numbers(data):
    yield from (int(num.strip()) for num in data if num)


def prepare_data(data):    
    data.seek(0)    
    return generate_numbers(data)

