"""
primenumbers.py

This module contains code to print the prime numbers in a range 
of values
"""

start = 10
end = 20

for number in range(start, end+1):
    # need to check if the number is prime or not
    is_prime_number = True
    for index in range(2,number):
        if number % index == 0:
            is_prime_number = False
            break
    if is_prime_number:
        print(number)
