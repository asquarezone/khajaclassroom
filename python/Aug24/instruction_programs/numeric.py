"""This module contains helper functions 
to solve numeric problems
"""

def is_even(number):
    """This function will check if the number is even or not

    Args:
        number (int): number to be checked

    Returns:
        True if even, False otherwise
    """
    is_even_result = number%2 == 0
    return is_even_result


def factorial(number):
    """This function returns the factorial of a number

    Args:
        number (int): number

    Returns:
        int: factorial

    Examples:
        factorial(5) => 120
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(4))
