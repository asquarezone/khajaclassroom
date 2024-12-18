def print_factors(number):
    for index in range(2, number):
        if number % index == 0:
            print(index)


print_factors(10)