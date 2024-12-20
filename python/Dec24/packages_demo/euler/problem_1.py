def solution():
    """Solution to problem 1 

    Returns:
        _type_: _description_
    """
    sum = 0
    for number in range(1, 1000):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum
