def solution():
    first = 1
    second = 2  
    result = 2
    while first + second < 4000000:
        third = first + second
        if third % 2 == 0:
            result += third
        first = second
        second = third
    return result