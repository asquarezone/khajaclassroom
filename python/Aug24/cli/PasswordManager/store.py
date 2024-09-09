"""This module will store the passwords to a file
"""
import os
import json
from cryptography.fernet import Fernet

PASSWORD_FILE = 'passwords.secret'

def load_secrets():
    """load existing secrets
    """
    with open(PASSWORD_FILE, mode='r', encoding='utf16') as file:
        return json.load(file)


secrets_dictionary = load_secrets()


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

def encrypt(plain_text):
    """This method encyrpts text
    """
    key = get_key()
    f = Fernet(key)
    cipher_bytes = f.encrypt(plain_text.encode())
    cipher_text = cipher_bytes.decode('utf16')
    return cipher_text

def decrypt(cipher_text):
    """This method decrypts text
    """
    key = get_key()
    f = Fernet(key)
    cipher_bytes = cipher_text.encode('utf16')
    return f.decrypt(cipher_bytes).decode()


def save_password(service, username, password):
    """This function will save passwords to a file

    Args:
        service (str): service name
        username (str): username
        password (str): password
    """
    secrets_dictionary[service] = {
        'username': encrypt(username), 
        'password': encrypt(password)
    }
    with open(PASSWORD_FILE, mode='w', encoding='utf16') as file:
        json.dump(secrets_dictionary,file, indent=4)

def retrieve_password(service_name):
    """This function will retrive the password based on service
    from a file


    Args:
        service_name (str): service name

    Returns:
       tuple: (username, password)
    """
    if service_name not in secrets_dictionary:
        raise ValueError('Invalid Service Name')
    username = decrypt(secrets_dictionary[service_name]['username'])
    password = decrypt(secrets_dictionary[service_name]['password'])
    return (username, password)
