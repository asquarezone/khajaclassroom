"""This module has function to generate password
"""
import random
import string

def generate_password(
        length=12,
        include_digits=True,
        include_special_characters=True):
    """This function generates password

    Args:
        length (int, optional): lenght. Defaults to 12.
        include_digits (bool, optional): 
            digits to be included or not. Defaults to True.
        include_special_characters (bool, optional): 
            special characters to be included or not. Defaults to True.

    Returns:
        str: password
    """
    password=""
    total_characters = string.ascii_letters
    if include_digits :
        total_characters += string.digits
    if include_special_characters:
        total_characters += string.punctuation
    # rule order
    # 1. Uppercase
    password = random.choice(string.ascii_uppercase)
    # 2. lowercase
    password += random.choice(string.ascii_lowercase)
    count = 2
    # 3. digits
    if include_digits:
        password += random.choice(string.digits)
        count += 1
    # 4. special characters
    if include_special_characters:
        password += random.choice(string.punctuation)
        count += 1
    rest = [random.choice(total_characters) for _ in range(length-count)]
    password = password+"".join(rest)
    return password
