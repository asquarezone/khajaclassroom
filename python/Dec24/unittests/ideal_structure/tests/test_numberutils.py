"""This module tests the numberutils
"""
from learning.numberutils import is_prime

def test_is_prime_basic():
    """This test case will check prime for
    basic values
    """
    assert is_prime(7), "7 is a prime number"
    assert not is_prime(4), "4 is not a prime number"
    assert is_prime(13), "13 is a prime number"

def test_is_prime_corner():
    """
    This test will check the code for corner scenarios
    """
    assert not is_prime(0), "0 is not a prime number"
    assert not is_prime(-7), "negative numbers cannot be prime"
    assert not is_prime(1), "1 is not a prime number"
    assert is_prime(2), "2 is a prime number"
