def is_even(number):
    return number%2 == 0

def even_numbers(start=0, end=10):
    numbers = []
    for number in range(start, end):
        if is_even(number):
            numbers.append(number)
    return numbers

print(even_numbers(100,1000))