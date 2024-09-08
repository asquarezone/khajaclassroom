"""This module tests the utils 
"""
from utils import is_even

def test_is_even_simple():
    """Simple case for is_even
    """
    assert is_even(4) is True
    assert is_even(3) is False