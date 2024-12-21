"""calc.py

This module contains functions and implementations to support
add
sub
mul
div
mod

Usage:
* python calc.py add 1 2
  3
* python calc.py sub 4 2
  2
"""

import sys


class InvalidArgs(Exception):
    pass


def main(args):

    if len(args) != 3:
        raise InvalidArgs
    operation = args[0]
    temp_args = args[1:]
    args = [int(arg) for arg in temp_args]
    if operation.lower() == "add":
        print(args[0] + args[1])
    elif operation.lower() == "sub":
        print(args[0] - args[1])
    elif operation.lower() == "mul":
        print(args[0] * args[1])
    elif operation.lower() == "div":
        print(args[0] // args[1])
    elif operation.lower() == "mod":
        print(args[0] % args[1])
    else:
        print("unsupported opearation {operation}")


if __name__ == "__main__":
    args = sys.argv[1::]
    try:
        main(args)
    except InvalidArgs:
        print("############################")
        print("Usage is as shown below")
        print("python calc.py add 1 2")
        print("Supported operations are add sub mul div mod")
