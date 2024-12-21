"""newcalc.py

This module contains functions and implementations to support
add
sub
mul
div
mod

Usage:
* python newcalc.py add 1 2
  3
* python newcalc.py sub 4 2
  2
"""

import argparse


def create_parser():
    """This method creates the parser"""
    parser = argparse.ArgumentParser(
        prog="Calculator",
        description="This is used for basic calculations such as add sub mul div",
    )
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div", "mod"],
        help="Operation to perform: add, sub, mul, div, mod",
    )
    parser.add_argument("value1", type=int, help="First number")
    parser.add_argument("value2", type=int, help="Second number")
    return parser


def operate(args):
    """This function operates on arguments"""
    if args.operation == "add":
        print(args.value1 + args.value2)
    elif args.operation == "sub":
        print(args.value1 - args.value2)
    elif args.operation == "mul":
        print(args.value1 * args.value2)
    elif args.operation == "div":
        print(args.value1 // args.value2)
    elif args.operation == "mod":
        print(args.value1 % args.value2)


def main():
    """
    This function creates a parser and performs operations
    """
    # Create parser
    parser = create_parser()
    # process arguments
    args = parser.parse_args()
    # perform operations
    operate(args)


if __name__ == "__main__":
    main()
