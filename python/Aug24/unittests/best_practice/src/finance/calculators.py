"""This module will have calculators
"""

def is_even(number:int) -> bool:
    """This function checks if the number is even or odd

    Args:
        number (int): _description_

    Returns:
        bool: True if even False otherwise
    """
    return number%2 == 0


def is_prime(number:int) -> bool:
    """This function checks if the number is prime or not

    Args:
        number (int): number

    Raises:
        ValueError if the number is not int

    Returns: 
        bool: True if prime, False otherwise
    """
    if not isinstance(number, int):
        raise ValueError(number)
    if number < 2:
        return False
    for index in range(2,number):
        if number%index == 0:
            return False
    return True
