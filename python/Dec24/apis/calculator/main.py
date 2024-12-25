"""
main.py

This module is starting point for web api

Here we implement Caclulator api with methods for

add
sub
div
mul
mod
"""

from fastapi import FastAPI

# create a Fast API instance
app = FastAPI()

@app.get("/calculator/add/{number1}/{number2}")
def add(number1: int, number2: int):
    """
    This is add implementation
    """
    return number1 + number2

@app.get("/calculator/sub/{number1}/{number2}")
def sub(number1: int, number2: int):
    """
    This is sub implementation
    """
    return number1 - number2


@app.get("/calculator/mul/{number1}/{number2}")
def mul(number1: int, number2: int):
    """
    This is mul implementation
    """
    return number1 * number2

@app.get("/calculator/div/{number1}/{number2}")
def div(number1: int, number2: int):
    """
    This is div implementation
    """
    return number1 // number2


@app.get("/calculator/mod/{number1}/{number2}")
def mod(number1: int, number2: int):
    """
    This is mod implementation
    """
    return number1 % number2

@app.get("/calculator/prime/{number}")
def is_prime(number:int):
    return True
