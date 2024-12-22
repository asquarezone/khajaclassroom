"""
test_numberutils.py

This is a test module for numberutils.py
"""
from numberutils import is_even

def test_is_even_positive():
    """This function checks if the is_even function 
    works correctly for all positive scenarios
    """
    assert is_even(2) == True, "2 is even number"
    

