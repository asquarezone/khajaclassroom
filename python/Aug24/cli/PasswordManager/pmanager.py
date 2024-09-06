"""This module will have command line parsing
"""

from argparse import ArgumentParser
from password import generate_password
from store import save_password, retrieve_password


def argument_parser():
    """Argument parser

    Returns:
        _type_: _description_
    """
    global_parser = ArgumentParser(prog="pmanager")

    subparsers = global_parser.add_subparsers(dest='command')
    generate_parser = subparsers.add_parser(
        "generate", help="generate passwords")
    generate_parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="length of password to be generated, default = 12")
    generate_parser.add_argument(
        "-d"
        "--include-digits",
        action="store_true",
        help="include digits"
    )
    generate_parser.add_argument(
        "-c"
        "--include-special-characters",
        action="store_true",
        help="include special characters"
    )
    generate_parser.add_argument(
        "-u",
        "--username",
        help="username"
    )
    generate_parser.add_argument(
        "-s",
        "--service",
        help="service name"
    )
    retrieve_parser = subparsers.add_parser(
        "retrieve", help="retrieve passwords")
    retrieve_parser.add_argument(
        "-s",
        "--service",
        help="service name"
    )
    return global_parser.parse_args()



def main():
    """This function will parse arguments"""
    args = argument_parser()
    # find if the command is generate or retrieve
    if args.command == 'generate':
        # if it is generate
        # call generate_password from password module
        # call save_password from store module
        password = generate_password(
            length=args.length,
            include_digits=args.d__include_digits,
            include_special_characters=args.c__include_special_characters
            )
        save_password(
            service=args.service,
            username=args.username,
            password=password)
        print("Password was succesfully generate, to fetch use retrive command")
    elif args.command == 'retrieve':
        (username, password) = retrieve_password(
        # if it is retrieve
        # call retrieve_password from store module

            service_name=args.service)
        print(f"username is {username}")
        print(f"password is {password}")



if __name__ == "__main__":
    main()
