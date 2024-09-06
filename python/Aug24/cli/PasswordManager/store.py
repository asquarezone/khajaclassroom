"""This module will store the passwords to a file
"""

PASSWORD_FILE = 'passwords.txt'

def save_password(service, username, password):
    """This function will save passwords to a file

    Args:
        service (str): service name
        username (str): username
        password (str): password
    """
    with open(PASSWORD_FILE,mode='a',encoding='utf8') as file:
        file.write(f"{service}\t{username}\t{password}\n")

def retrieve_password(service_name):
    """This function will retrive the password based on service
    from a file


    Args:
        service_name (str): service name

    Returns:
       tuple: (username, password)
    """
    with open(PASSWORD_FILE,mode='r',encoding='utf8') as file:
        for line in file.readlines():
            service,username,password = line.split("\t")
            if service == service_name:
                return (username,password)
    # asking stuff which is not present
    return None
    