"""
numberutils.py

This module has functions to verify numeric functionality

is_prime
"""


def is_prime(number: int) -> bool:
    """Checks if the number is prime or not

    Args:
        number (int): number to be checked

    Returns:
        bool: True if prime, False otherwise
    """

    is_prime_number = True
    if number <= 1:
        is_prime_number = False
    for index in range(2, number):
        if number % index == 0:
            is_prime_number = False
            break
    return is_prime_number
