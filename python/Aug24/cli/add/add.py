"""This module adds two numbers
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong usage python add.py <num1> <num2")
        sys.exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"{num1} + {num2} = {num1+num2}")
