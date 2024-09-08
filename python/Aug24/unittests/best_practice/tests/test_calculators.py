"""This module tests calculators
"""
import pytest
from src.finance.calculators import is_even, is_prime

def test_is_even_simple():
    """This function tests the basic behavior
    """
    assert is_even(4) is True
    assert is_even(5) is False

def test_is_even_tricky():
    """This function tests the corner cases
    """
    assert is_even(0) is True
    assert is_even(2.1) is False


def test_is_prime_simple():
    """This function tests if the is_prime is working fine with
    simple cases
    """
    assert is_prime(7) is True
    assert is_prime(6) is False


def test_is_prime_tricky():
    """This function tests with tricky stuff
    """
    assert is_prime(0) is False
    assert is_prime(1) is False
    # from test code we are expecting exception
    with pytest.raises(ValueError):
        is_prime(1.1)
