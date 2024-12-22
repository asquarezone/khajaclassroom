"""
numberutlils.py

This module has functions to check number functionalities

* is_even
"""


def is_even(number):
    """This checks if the number is even or not

    Args:
        number (int): number to be checked

    Returns:
        bool: True if even, False otherwise
    """
    return number % 2 != 0
