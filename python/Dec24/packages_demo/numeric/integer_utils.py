"""
integer_utils.py

This module will contain functions around integers
"""

def is_even(number):
    """Checks if the number is even

    Args:
        number (int): number passed

    Returns:
        bool: True if even, false other wise
    """
    return number % 2 == 0