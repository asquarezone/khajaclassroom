"""This program demonstrates the solution of 
project euler problem 3

"""

def is_prime(number):
    """This function will check if the number is prime or not

    Args:
        number (int): number passed

    Returns:
        bool: True if prime, False otherwise      
    """
    for index in range(2, number // 2 + 1):
        if number % index == 0:
            return False
    return True

def factors(number):
    """This function will find the factors of a number

    Args:
        number (int): number passed
    
    Returns:
       Tuple: factors
    """
    factors_list = []
    for index in range(2, number//2 + 1):
        if number % index == 0:
            factors_list.append(number)
    return tuple(factors_list)


# Lets find the largest factor
def largest_prime_factor(number):
    """This function will find the largest prime factor of a number

    Args:
        number (int): number to be checked for

    Returns:
        int: largest prime factor
    """
    for index in range(number//2 , 1, -1):
        if number%index == 0 and is_prime(index):
            return index
    return None


print(largest_prime_factor(13195))
