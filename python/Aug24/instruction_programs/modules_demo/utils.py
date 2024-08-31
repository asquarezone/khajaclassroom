"""This module will contain reusable(helper) functions
"""

def add(x,y):
    """This function will add two numbers

    Args:
        x (int): x
        y (int): y
    """
    return x + y


def simple_intrest(principle, rate, time):
    """This function will calculate simple intrest

    Args:
        principle (float): principle amount
        rate (float): rate of intrest
        time (float): time period
    """
    return principle + (principle * rate * time)/100


def compound_intrest(principle, rate, time):
    """This function will calculate compound intrest

    Args:
        principle (float): principle amount
        rate (float): rate of intrest
        time (float): time period
    """
    return principle * (1 + rate/100)**time
