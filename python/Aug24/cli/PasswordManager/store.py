"""This module will store the passwords to a file
"""
import os
from cryptography.fernet import Fernet

PASSWORD_FILE = 'passwords.secret'


def load_key(key_file="passwords.key"):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(key_file, "rb").read()


def get_key(key_file="passwords.key"):
    """This method generates a key if not present and
    returns the key

    Args:
        key_file (str, optional): key path
    """
    # if the key doesnot exist create it
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
    key = load_key(key_file)
    return key


def save_password(service, username, password):
    """This function will save passwords to a file

    Args:
        service (str): service name
        username (str): username
        password (str): password
    """

    with open(PASSWORD_FILE,mode='a',encoding='utf8') as file:
        file.write(f"{service}\t{username}\t{password}\n")
    # add encryption

def retrieve_password(service_name):
    """This function will retrive the password based on service
    from a file


    Args:
        service_name (str): service name

    Returns:
       tuple: (username, password)
    """
    # add decryption
    with open(PASSWORD_FILE,mode='r',encoding='utf8') as file:
        for line in file.readlines():
            service,username,password = line.split("\t")
            if service == service_name:
                return (username,password)
    # asking stuff which is not present
    return None
    