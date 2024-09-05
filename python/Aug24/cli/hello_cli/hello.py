#!/usr/bin/python3
"""This module helps us understand how to build 
command line applicatons
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(f"Hello {sys.argv[-1]}")
    else:
        print("Wrong usage: python hello.py <name>")
